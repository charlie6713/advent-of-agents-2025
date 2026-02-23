## The Developer Layer: Callbacks & Plugins 
# This Python snippet demonstrates how to inject security logic using the ADK callback system.


from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from .tools import add, subtract, multiply, divide
from .prompt import instruction_prompt
from google.genai import types
from typing import Optional

MODEL = "gemini-2.5-flash"

async def callback_before_agent(callback_context: CallbackContext) -> Optional[types.Content]:
       # Guardrail 1: Do we have the student profile?
       if not callback_context.state.get("student_profile"):
               return types.Content(role='model', parts=[types.Part(text="Error: Cannot find student profile.")])
# Add more guardrails...

       return None # Allow model call to proceed

agent_math = Agent(
       model=MODEL,
       name="agent_math",
       description="This agent performs basic arithmetic operations (addition, subtraction, multiplication, and division) on user-provided numbers, including ranges.",
       instruction=instruction_prompt,
       tools=[add, subtract, multiply, divide],
       before_agent_callback=callback_before_agent,
)