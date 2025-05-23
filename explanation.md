# Project Explanation: DeepResearchAI

## Overview
This system uses AI agents to conduct deep web research and draft meaningful answers to user queries. It uses:

- Tavily for real-time web data
- LangGraph for agent orchestration
- LangChain for prompt design & LLM inference

## Architecture
1. **Research Agent** uses Tavily API
2. **Drafting Agent** uses GPT-3.5 to write responses
3. **LangGraph** manages the flow between agents

