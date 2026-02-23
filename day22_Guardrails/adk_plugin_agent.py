## This Python snippet demonstrates how to load/apply an ADK plugin to an agent.

from google.adk.runners import InMemoryRunner
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from google.genai import types
import asyncio

# Import the plugin.
from .count_plugin import CountInvocationPlugin

async def hello_world(tool_context: ToolContext, query: str):
 print(f'Hello world: query is [{query}]')
 root_agent = Agent(
   model='gemini-2.0-flash',
   name='hello_world',
   description='Prints hello world with user query.',
   instruction="""Use hello_world tool to print hello world and user query.""",
   tools=[hello_world],
)

async def main():
 """Main entry point for the agent."""
 prompt = 'hello world'
 runner = InMemoryRunner(agent=root_agent, app_name='test_app_with_plugin',
     # Add your plugin here. You can add multiple plugins.
     plugins=[CountInvocationPlugin()],)
 ...