from dotenv import load_dotenv
load_dotenv()

from workflows.graph_flow import build_graph
from agents.research_agent import research_agent  # Assuming it's imported

if __name__ == "__main__":
    # Accept user input
    query = input("Enter your research topic: ")

    # Build graph
    graph = build_graph()

    # Get research documents using the query
    research_result = research_agent(query)

    # Structure the input data correctly
    input_data = {"query": query, "documents": research_result["documents"]}

    # Invoke the graph with the correct input data
    final_answer = graph.invoke(input_data)

    # Output the final answer
    print("\n\n[Final Answer]\n", final_answer)
