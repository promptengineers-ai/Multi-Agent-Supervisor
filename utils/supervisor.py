from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel
from typing import Literal

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

# Define team members and supervisor prompt
members = ["Researcher", "Coder"]
system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    " following workers: {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH."
)
options = ["FINISH"] + members

class RouteResponse(BaseModel):
    next: Literal[tuple(options)]  # type: ignore # Use tuple() to convert list to tuple for Literal

# Create supervisor prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="messages"),
    (
        "system",
        "Given the conversation above, who should act next?"
        " Or should we FINISH? Select one of: {options}",
    ),
]).partial(options=str(options), members=", ".join(members))

def supervisor_agent(state):
    supervisor_chain = prompt | llm.with_structured_output(RouteResponse)
    return supervisor_chain.invoke(state)