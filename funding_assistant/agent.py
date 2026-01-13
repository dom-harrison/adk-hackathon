from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.langchain_tool import LangchainTool
from .custom_functions import get_fx_rate, get_transaction_history, get_savings_account

transaction_agent = Agent(
    model='gemini-2.5-flash',
    name='transaction_agent',
    description='A sub-agent to fetch customers transaction data. It should look at the credits and debits to see how much the user can save each month',
    tools=[
        FunctionTool(get_transaction_history),
    ]
)

account_type_agent = Agent(
    model='gemini-2.5-flash',
    name='account_agent',
    description='This sub agent will return all the active savings product offering',
    tools=[
        FunctionTool(get_savings_account),
    ]
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant to help you understand how much you can save and to set up regular savings accounts',
    tools=[
        FunctionTool(get_fx_rate)
    ],
    sub_agents=[transaction_agent, account_type_agent]
)