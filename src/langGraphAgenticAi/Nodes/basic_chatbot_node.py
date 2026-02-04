from src.langGraphAgenticAi.state.state import State


class BsicChabotNode:
    def __init__(self,model):
        self.llm=model
    
    def process(self,state:State)->dict:
        """
        Represent the structure of the state used in grap
        """
        return {"messages":self.llm.invkoke(state['messages'])}