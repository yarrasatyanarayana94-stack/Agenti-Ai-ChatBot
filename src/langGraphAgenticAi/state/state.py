from typing import Annotated,List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Docstring for State
    """
    messages:Annotated[list,add_messages]