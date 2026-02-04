import streamlit as st
from src.langGraphAgenticAi.ui.streamlit.loadui import LoadStreamlitUI
from src.langGraphAgenticAi.LLMS.groqllm import GroqLLM
from src.langGraphAgenticAi.Graph.graph_builder import GraphBuilder
from src.langGraphAgenticAi.ui.streamlit.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    loads and runs the Langgraph AgenticAi Applicaion with streamlit UI.
    This function initializes the UI,Handles user input,configures te LLM model.
    set up the graph based on the selected use case, and displays the output while
    implementing the exception handling for robustness
        
    """

    ## Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error:Failed to load user input  from thr UI.")
        return
    user_message=st.chat_input("Enter your message:")
    if user_message:
        try:
            ## config the llm
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error LLm model is not initialized")
                return
            
            # initialize and setup the Graph based on use case
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Error LLm model is not initialized")
                return
            
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_usecase(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error graph set up is failed {e}")
                return
            
        except Exception as e:
            st.error(f"Error graph set up is failed {e}")
            return  

