from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        # Enable Interactions API
        use_interactions_api=True,
    ),
    name="interactions_test_agent",
    tools=[
        # Converted Google Search to a function tool
        GoogleSearchTool(bypass_multi_tools_limit=True),
        get_current_weather,
    ],
)
