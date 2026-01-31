## day 4

In Day 4, I deployed an ADK agent to Google Agent Engine using source-based deployment.

What I did
Created an agent by following the Day 3 instructions.
Enhanced the existing agent with deployment support by running:
uvx agent-starter-pack enhance --adk my_agent
Selected agent_engine as the deployment target.
Ran the deployment command:
make deploy

Opened the Agent Engine Playground using the link provided after deployment:
https://console.cloud.google.com/vertex-ai/agents/locations/us-central1/agent-engines/6969880074774380544/playground?project=767097193836

What this deployment means
The agent is deployed to Google Agent Engine using source-based deployment.
This is similar to AWS Lambda:
The code runs on Google Cloud infrastructure.
The runtime environment is fully managed by Google.

The difference between local execution and deployed execution is:
When running locally, the agent runs on my own device using adk web.
After deployment, the agent runs on Google Cloud.
Even if my local device is shut down, the agent continues running in the cloud.