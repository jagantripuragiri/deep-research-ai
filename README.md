# DeepResearchAI 

An AI Agentic System using LangGraph + Tavily + LangChain to perform deep research and draft answers.

## Features
- Research Agent: Uses Tavily to gather info.
- Drafting Agent: Synthesizes answer using LLM.
- Performance via LangGraph.

## Setup
```bash
pip install -r requirements.txt
```

Set your API keys in `.env`:
```
TAVILY_API_KEY= our_tavily_key
OPENAI_API_KEY= our_openai_key
```

## Run
```bash
python main.py
```

## Output
Final answer based on deep research logged in console.
