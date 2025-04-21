from langgraph.graph import StateGraph
from agents.research_agent import research_agent
from agents.drafting_agent import drafting_agent

def build_graph():
    workflow = StateGraph()

    # Define flow
    workflow.add_node("research", research_agent)
    workflow.add_node("draft", drafting_agent)

    # Define edges
    workflow.set_entry_point("research")
    workflow.add_edge("research", "draft")

    return workflow.compile()
