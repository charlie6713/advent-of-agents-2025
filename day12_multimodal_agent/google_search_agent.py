"""Google Search Agent definition for ADK Bidi-streaming demo."""

import os
from google.adk.agents import Agent
from google.adk.tools import google_search

agent = Agent(
    name="google_search_agent",
    model="gemini-2.5-flash-native-audio-preview-09-2025",
    tools=[google_search],
    instruction="You are a helpful voice assistant that can search the web."
)