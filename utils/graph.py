import operator
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage

from utils.visualize import visualize_graph

# Define agent state
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str

def build_workflow(supervisor, workers, visualize=True):
    workflow = StateGraph(AgentState)
    node_map = {
        "supervisor": supervisor,
        **workers
    }
    for node_name, node_fn in node_map.items():
        workflow.add_node(node_name, node_fn)
        
    for member in workers.keys():
        workflow.add_edge(member, "supervisor")
    
    conditional_map = {k: k for k in workers.keys()}
    conditional_map["FINISH"] = END    
    workflow.add_conditional_edges(
        "supervisor", 
        lambda x: x["next"], 
        conditional_map
    )
    workflow.add_edge(START, "supervisor")
    graph = workflow.compile()
    if visualize:
        visualize_graph(graph)
    return graph