from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

capital_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="capital_agent",
    description="Returns the capital city for any country or state",
    instruction="""If the user gives you the name of a country or a state (e.g.
    Tennessee or New South Wales), answer with the name of the capital city of that
    country or state. Otherwise, tell the user you are not able to help them."""
    )

user_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="user_advice_agent",
    description="Answers user questions and gives advice",
    instruction="""Use the tools you have available to answer the user's questions""",
    tools=[AgentTool(agent=capital_agent)]
)