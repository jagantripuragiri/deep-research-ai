from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")

def drafting_agent(context):
    docs = context["documents"]
    query = context["query"]
    
    prompt = f"""You are an AI assistant. Based on the research below, draft a detailed and well-organized answer to the query: "{query}"

Research:
{''.join(docs)}

Answer:"""

    response = llm([HumanMessage(content=prompt)])
    return response.content
