from google.adk import Agent, ApiRegistry

# 1. Connect to the Cloud API Registry
registry = ApiRegistry(project_id="your-project-id")

# 2. Fetch the specific tool (e.g., BigQuery MCP)
# This retrieves the managed tool definition directly from the registry
bq_tool = registry.get_tool("google-bigquery")

# 3. Add the tool to your Agent
# The agent now has governed access to BigQuery capabilities
agent = Agent(
    model="gemini-3-pro",
    tools=[bq_tool]
)

print("Agent configured with governed BigQuery access.")