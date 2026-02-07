from google.adk.apps import App, EventsCompactionConfig
from google.adk.agents.context_cache_config import ContextCacheConfig

# Configure your App with both Caching and Compaction
app = App(
    name='long-memory-agent',
    root_agent=my_agent,
    
    # 1. Cache heavy instructions
    context_cache_config=ContextCacheConfig(
        min_tokens=2048,    # Only cache if prompt is heavy
        ttl_seconds=1800,   # Keep cache alive for 30 mins
        cache_intervals=10  # Refresh after 10 uses
    ),

    # 2. Compress history to prevent "Context Rot"
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3, # Summarize every 3 turns
        overlap_size=1         # Keep 1 turn of context overlap
    )
)