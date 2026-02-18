from google.adk.agents import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
    # Configure thinking level for Gemini 3
    # Options: "HIGH" (deep reasoning), "LOW" (minimal latency), "MINIMAL" (raw speed)
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            thinking_level="LOW"
        )
    ),
)