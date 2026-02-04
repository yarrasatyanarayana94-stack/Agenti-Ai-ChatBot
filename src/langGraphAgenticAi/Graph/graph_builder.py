from langgraph.graph import StateGraph,START,END
from src.langGraphAgenticAi.state.state import State
from src.langGraphAgenticAi.Nodes.basic_chatbot_node import BsicChabotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def Basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.basic_chatbot_node=BsicChabotNode(self.llm)


        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    
    def setup_usecase(self,usecase:str):
        """
        sets up he graph for the selected usecase
        """
        if usecase=="Basic Chatbot":
            self.Basic_chatbot_build_graph()