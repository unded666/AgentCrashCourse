from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
import asyncio

research_agent = Agent(
    model="gemini-2.5-flash",
    name="research_agent",
    description="Researches the performance of a given company",
    instruction="""You are a specialised company research agent.
    
    Given the name of a publicly traded company, research its performance over the last
    three years, paying particular attention to dividends paid out, the market cap, the share price and the P/E ratio.
    
    The results are to be returned in a bullet-point summary. No additional commentary is required.""",
    tools=[google_search]
)

limerick_agent = Agent(
    model="gemini-2.5-flash",
    name="limerick_agent",
    description="Writes a limerick about a given topic",
    instruction="""You are a creative limerick writing agent.   
    Given the company research summary, write a limerick that captures the key points in a humorous way.
    The limerick should follow the traditional AABBA rhyme scheme and be light-hearted and fun.""",
)

root_agent = SequentialAgent(
    name="root_agent",
    description="Agent that researches a company and writes a limerick about it",
    sub_agents=[research_agent, limerick_agent],
)

# Create the runner with the root agent (matches the pattern used in the notebooks)
runner = InMemoryRunner(agent=root_agent)

# Run the agent using run_debug (coroutine that returns a list of events) and collect events in a synchronous script
async def _run_and_collect(prompt: str):
    events = await runner.run_debug(prompt)
    return events

if __name__ == "__main__":
    prompt = "Boeing"  # initial prompt
    events = asyncio.run(_run_and_collect(prompt))

    # Gather all text parts produced by the agent and print only the final non-empty text (the limerick)
    text_parts = []
    for event in events:
        if getattr(event, "content", None) and getattr(event.content, "parts", None):
            for part in event.content.parts:
                if getattr(part, "text", None):
                    text = part.text.strip()
                    if text:
                        text_parts.append(text)

    if text_parts:
        # Print only the last text produced (assumed to be the final limerick)
        print(text_parts[-1])
