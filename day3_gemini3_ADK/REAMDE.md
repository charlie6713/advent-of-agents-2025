## Day 3

What I did

Initialize the project
uv init

Install dependencies
uv add google-adk
uv add google-genai

Activate virtual environment
Windows (Git Bash):
source .venv/Scripts/activate

macOS / Linux:
source .venv/bin/activate

Create an agent
adk create my_agent

Configure API key
Add the following to agent/.env:
GOOGLE_API_KEY="your_api_key_here"

Run the web UI
adk web

Bugs and notes
Do not use export GOOGLE_API_KEY=...
Using export will override the value in .env.
If GOOGLE_API_KEY was previously exported, clear it first:
unset GOOGLE_API_KEY
After that, keep the API key only in agent/.env.

Models
I currently do not have access to the Gemini 3 model.
The model can be easily changed later once access is available.

What I learned
How to initialize and run an ADK agent with uv.
How environment variables interact with .env files.
How to track agent thinking via events.