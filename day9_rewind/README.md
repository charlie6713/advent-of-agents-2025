## day9

Agents can store their execution history using sessions and invocations.
Instead of restarting everything when an error happens, we can rewind the agent state to a previous step.
The rewind_async() function restores the session to a chosen moment while keeping the full audit log.
After rewinding, the agent can resume execution from that exact point.

I learned how to make agents recover from mistakes without losing progress.