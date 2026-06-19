from agents import Agent, OpenAIChatCompletionsModel

from gemini_client import gemini_client
from config import GEMINI_MODEL


revision_agent = Agent(
    name="Progress Revision Coach",

    instructions="""
You are an expert fitness progress analyst.

Review the user's weekly progress.

If progress is good:
- congratulate them
- encourage consistency

If progress is slow:
- suggest increasing activity

If weight loss is too fast:
- recommend slowing down

Always give practical advice and motivation.
""",

    model=OpenAIChatCompletionsModel(
        model=GEMINI_MODEL,
        openai_client=gemini_client
    )
)