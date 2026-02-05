## Day 8

Agents are not prompt stacks. Agents are context management systems.

Do not put everything into the model.
Instead, compile the right context for each turn.

Key ideas:

Separate static vs dynamic instructions

Static = permanent rules, safety, schema, identity
Turn = goal, style, runtime control, corrections
Build a context pipeline
Raw data → filter → compress → format → send to LLM


Give the model only what it needs
Store long-term data outside the prompt
Retrieve memory and tool data only when necessary
Control scope during tool calls
Use caching for stable system headers

Reduce cost
Reduce latency
Increase consistency

Always design layered context
Add a runtime controller
Treat prompts as compiled output, not source data
Optimize for production, not demos