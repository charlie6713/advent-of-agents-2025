## day 23

Today I learned that an agent can stop, not lose its memory, and continue later from the same place even after a crash.

#This CLI snippet gets you a local durable environment in seconds.

# 1. Get the Claims Processing sample
git clone https://github.com/restatedev/restate-google-adk-example
cd restate-google-adk-example

# 2. Start the Durable Agent (uses uv)
# The agent will register itself and wait for work
export GOOGLE_API_KEY="YOUR_KEY_HERE"
uv run .

# 3. In a new terminal, start the Restate Server
# This acts as the durable log and orchestrator
docker run --name restate --rm -p 8080:8080 -p 9070:9070   --add-host host.docker.internal:host-gateway   docker.restate.dev/restatedev/restate:latest

# 4. Open the UI to trace execution
# http://localhost:9070