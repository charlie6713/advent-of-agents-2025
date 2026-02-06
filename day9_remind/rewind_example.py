import asyncio
from adk.api.agents.in_memory_runner import InMemoryRunner

# 1. Initialize the runner
runner = InMemoryRunner(...)

# 2. Something goes wrong? (e.g., hallucination or error at 'invocation_456')
# Instead of clearing the session, we request a rewind.

# 3. Rewind (Time Travel)
# This asynchronously restores session state and artifacts to the target moment.
asyncio.run(
    runner.rewind_async(
        session_id='session_123',
        before_invocation_id='invocation_456'
    )
)

# 4. Resume the conversation from that exact point
asyncio.run(runner.run(query="Let's try that request again with these constraints..."))