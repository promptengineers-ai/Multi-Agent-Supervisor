from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from utils.tools import tavily_tool, python_repl_tool
import functools

from utils.supervisor import llm

# Helper function for agent nodes
def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {
        "messages": [HumanMessage(content=result["messages"][-1].content, name=name)]
    }

research_agent = create_react_agent(llm, tools=[tavily_tool])
research_node = functools.partial(agent_node, agent=research_agent, name="Researcher")

code_agent = create_react_agent(llm, tools=[python_repl_tool])
code_node = functools.partial(agent_node, agent=code_agent, name="Coder")

worker_map = {
    "Researcher": research_node,
    "Coder": code_node,
}