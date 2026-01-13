from google.adk.agents import Agent
from google.adk.tools import google_search
from .search_data import load_all_documents


# Create an agent with google search tool as a search specialist
google_search_agent = Agent(
    model='gemini-2.5-flash',
    name='google_search_agent',
    description='A search agent that uses google search to get latest information about current events, weather, or business hours.',
    instruction='Use google search to answer user questions about real-time, logistical information.',
    tools=[google_search],
)

load_transaction_history_of_user = Agent(
    name="load_history_of_user",
    model="gemini-2.5-flash",
    instruction="""
You are a retrieval-augmented generation agent for user transaction history.

Task:
- Receive a user-specific query or prompt.
- Use the provided tool to load ALL transaction history documents from the bucket.
- Filter and select only the relevant documents for the user's query.
- Validate the structure of the selected documents and identify any schema issues.
- Extract key fields such as transaction_id, date, description, amount, currency, type, and category.
- Produce a concise summary or answer based only on the relevant documents.
- Return results in a structured JSON format, including the key fields and a summary.

Always use the `load_all_documents` with the prefix transactions/ to fetch the data before reasoning.
""",
    tools=[load_all_documents],
)
