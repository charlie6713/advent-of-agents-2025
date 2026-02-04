# Day 7 — LLMs Can Execute Code (ADK Sample)

## What I did

### Setup
- Cloned the sample repo:
  - `git clone https://github.com/google/adk-samples.git`
- Entered the sample agent project:
  - `cd adk-samples/python/agents/retail-ai-location-strategy`
- Created a local environment file:
  - `cp .env.example .env`
- Updated the API key in:
  - `python/agents/retail-ai-location-strategy/.env`

### Run locally
- Installed dependencies:
  - `make install`
- Started the dev server:
  - `make dev`

### In the ADK Web UI
- Selected the **app** agent (the main agent).
- The UI selection does **not** change the agent’s model by itself.
- I modified `app/config` to use a free-tier model (Gemini Flash 2.5).

## What I tested

Because this sample is focused on **retail location strategy**, it is not ideal for verifying code execution with generic math/stat prompts.  
To trigger a more “analysis-like” workflow, I used this query:

> I want to open a coffee shop in New York.  
> Assume three candidate zones have revenue potential scores of 120, 95, and 150.  
> Please analyze and rank these zones and explain which is best.

## What I learned

- An agent can **write code and execute it** (in a sandbox) to support analysis.
- The main value of ADK samples is that they provide a **working agent framework** out of the box; for basic local use, I mainly needed to configure the API key.

## ADK vs. Direct API Calls

### ADK provides
- Agent workflow orchestration  
- Tool/API integration  
- Code execution sandbox  
- Structured outputs  
- Multi-step reasoning  
- Tracing / observability  

### Direct API calls typically provide
- Prompt → text response
