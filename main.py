from workflows.graph_flow import build_graph

if __name__ == "__main__":
    graph = build_graph()
    query = input("Enter your research topic: ")
    final_answer = graph.invoke(query)
    print("\n\n[Final Answer]\n", final_answer)
