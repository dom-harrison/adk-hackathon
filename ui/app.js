const chatEl = document.getElementById("chat");
const formEl = document.getElementById("chatForm");
const inputEl = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");

const statusDot = document.getElementById("statusDot");
const statusText = document.getElementById("statusText");

// You told me your agent app name:
const APP_NAME = "funding_assistant";

// Create stable ids for a "conversation"
const userId = localStorage.getItem("userId") || `user_${crypto.randomUUID()}`;
localStorage.setItem("userId", userId);

const sessionId = localStorage.getItem("sessionId") || crypto.randomUUID();
localStorage.setItem("sessionId", sessionId);

function addMessage(text, who) {
  const div = document.createElement("div");
  div.className = `msg ${who}`;
  div.textContent = text;
  chatEl.appendChild(div);
  chatEl.scrollTop = chatEl.scrollHeight;
  return div;
}

function setStatus(connected, text) {
  statusDot.style.background = connected ? "#2ecc71" : "#e74c3c";
  statusText.textContent = text;
}

async function sendMessageStreaming(message) {
  setStatus(true, "Connected");
  sendBtn.disabled = true;

  addMessage(message, "user");
  const botMsgEl = addMessage("", "bot");

  const payload = {
    app_name: APP_NAME,
    user_id: userId,
    session_id: sessionId,
    new_message: {
      role: "user",
      parts: [{ text: message }]
    }
  };

  // IMPORTANT: We call our own wrapper endpoint (same origin)
  const resp = await fetch("/api/run_sse", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!resp.ok || !resp.body) {
    botMsgEl.textContent = `Error: ${resp.status} ${resp.statusText}`;
    sendBtn.disabled = false;
    return;
  }

  const reader = resp.body.getReader();
  const decoder = new TextDecoder("utf-8");

  let buffer = "";
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });

    // ADK streaming returns event-stream style chunks.
    // We’ll parse lines beginning with "data:" and append text.
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";

    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed) continue;

      // many SSE streams look like: "data: {...json...}"
      if (trimmed.startsWith("data:")) {
        const dataStr = trimmed.slice(5).trim();

        // sometimes it sends [DONE]
        if (dataStr === "[DONE]") continue;

        // Try parse JSON; if fails, just append raw
        try {
          const obj = JSON.parse(dataStr);

          // We don’t know your exact chunk schema,
          // so we’ll try the common fields safely:
          const text =
            obj?.delta?.text ??
            obj?.text ??
            obj?.message?.content ??
            obj?.content ??
            "";

          if (text) botMsgEl.textContent += text;
        } catch (e) {
          // Not JSON? Append raw.
          botMsgEl.textContent += dataStr;
        }

        chatEl.scrollTop = chatEl.scrollHeight;
      }
    }
  }

  sendBtn.disabled = false;
}

formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  const msg = inputEl.value.trim();
  if (!msg) return;
  inputEl.value = "";

  try {
    await sendMessageStreaming(msg);
  } catch (err) {
    addMessage(`Error: ${err.message}`, "bot");
    setStatus(false, "Disconnected");
    sendBtn.disabled = false;
  }
});

// initial status
setStatus(false, "Ready");
