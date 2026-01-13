from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, JSONResponse
import httpx

ADK_BASE = "http://127.0.0.1:8000"

app = FastAPI()

@app.post("/api/run")
async def run(request: Request):
    payload = await request.json()

    async with httpx.AsyncClient(timeout=None) as client:
        r = await client.post(
            f"{ADK_BASE}/run_sse",
            json=payload,
            headers={"Accept": "text/event-stream"},
        )

        if r.status_code != 200:
            try:
                return JSONResponse(status_code=r.status_code, content=r.json())
            except Exception:
                return JSONResponse(status_code=r.status_code, content={"raw": r.text})

        async def stream():
            async for chunk in r.aiter_bytes():
                yield chunk

        return StreamingResponse(stream(), media_type="text/event-stream")

# UI mount MUST be "/" (not blank)
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")
