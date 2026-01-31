from langgraph.graph import StateGraph
from langchain_groq import ChatGroq
from backend.agent.tools import (
    log_interaction,
    analyze_sentiment,
    suggest_followup
)

# Dummy LLM (required by assignment)
llm = ChatGroq(
    model="gemma2-9b-it",
    api_key="DUMMY_KEY_FOR_NOW"
)

# -------- Wrapper nodes (CORRECT WAY) --------

def log_node(state: dict):
    return log_interaction.invoke(state)

def sentiment_node(state: dict):
    return analyze_sentiment.invoke(state)

def followup_node(state: dict):
    return suggest_followup.invoke(state)

# -------- LangGraph setup --------

graph = StateGraph(dict)

graph.add_node("log", log_node)
graph.add_node("sentiment", sentiment_node)
graph.add_node("followup", followup_node)

graph.set_entry_point("log")
graph.add_edge("log", "sentiment")
graph.add_edge("sentiment", "followup")

agent = graph.compile()
