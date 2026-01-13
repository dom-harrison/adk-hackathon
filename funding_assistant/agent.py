from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.tools.agent_tool import AgentTool
# from google.adk.tools.langchain_tool import LangchainTool
from .custom_functions import get_fx_rate, get_savings_account
from .custom_agents import load_transaction_history_of_user

transaction_agent = Agent(
    model='gemini-2.5-flash',
    name='transaction_agent',
    description="""
        A sub-agent to fetch customers transaction data. 
        It shoudl summarise their spending over the transaction data.
        It should look at the credits and debits to see how much the user can save each month
        """,
    tools=[
        AgentTool(load_transaction_history_of_user),
        # FunctionTool(get_transaction_history)
    ]
)

account_type_agent = Agent(
    model='gemini-2.5-flash',
    name='account_agent',
    description="""
        It should understand from the customer if they want a fixed or non-fixed product, the term they would like to save for, and if the account is for a child.
        This sub agent will fetch savings product a customer is elgible for and show them the most sutible option as well as the other options available.
    """,
    tools=[
        FunctionTool(get_savings_account),
    ]
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description=
    """
        A helpful assistant to help you understand how much you can save and to project how much you could have in your account if you save consistently.
        First it should greet the user and then start a converstion.
        It should conversationaly lead the customer through the following steps one after another:
         - look at their transactions to understand how much they have spare to save each month
         - show them available savings products for them and help them choose one that fits their needs
         - calculate how much they could have in their account if they save consistently over the term of the product

         After each step it should check the customer wants to proceed.
    """,
    sub_agents=[transaction_agent, account_type_agent]
)