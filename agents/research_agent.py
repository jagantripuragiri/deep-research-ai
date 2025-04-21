# research_agent.py
from utils.tavily_wrapper import search_tavily

def research_agent(input_query):
    print(f"[Research Agent] Searching for: {input_query}")
    documents = search_tavily(input_query)
    return {"documents": documents, "query": input_query}
