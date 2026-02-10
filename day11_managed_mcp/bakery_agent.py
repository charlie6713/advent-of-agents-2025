import os
from google.genai import types
from google.genai.adk import Agent
from google.genai.mcp import RemoteMCPServer

# 1. Define the Fully-Managed Remote MCP Servers
#    These endpoints are now natively supported by Google's infrastructure
bigquery_mcp = RemoteMCPServer(
    url="https://mcp.googleapis.com/bigquery",
    capabilities=["schema_read", "query_execute"],
    auth_token=os.getenv("GOOGLE_CLOUD_TOKEN") # Uses standard IAM
)

maps_mcp = RemoteMCPServer(
    url="https://mcp.googleapis.com/maps",
    capabilities=["places_search", "routing", "elevation"],
    auth_token=os.getenv("GOOGLE_MAPS_API_KEY")
)

# 2. Initialize the ADK Agent with MCP Tools
#    The agent can now "see" your enterprise data and the real world
bakery_agent = Agent(
    model="gemini-3-pro",
    tools=[bigquery_mcp, maps_mcp],
    system_instruction="""
    You are a retail expansion scout.
    1. Query BigQuery to find high-revenue demographics.
    2. Use Google Maps to find available locations near competitors.
    3. Synthesize a recommendation for a new bakery location.
    """
)

# 3. Run the Agent
#    Gemini 3 plans the multi-step execution automatically
response = bakery_agent.run(
    "Find a location in Austin, TX with high disposable income and low competition."
)
print(response.text)
