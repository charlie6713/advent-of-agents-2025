# Clone the streaming sample for this deep dive and install
git clone https://github.com/google/adk-samples
cd adk-samples/python/agents/bidi-demo
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venvScriptsactivate
pip install -e .
export SSL_CERT_FILE=$(python -m certifi)

# Create app/.env file with your GOOGLE_API_KEY.

cd app
export SSL_CERT_FILE=$(uv run --project .. python -m certifi)
uv run --project .. uvicorn main:app --port 8000

# Open http://localhost:8000