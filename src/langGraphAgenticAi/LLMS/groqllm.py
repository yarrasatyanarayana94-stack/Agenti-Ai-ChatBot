import os
import streamlit as st

from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls=user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls.get("GROQ_API_KEY","") 
            selected_groq_model=self.user_controls.get("selected_groq_model")

            env_key = os.getenv("GROQ_API_KEY", "")
            if not groq_api_key and not env_key:
                st.error("Please enter the Groq API Key")
                return None
            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured  with exception as {e}")
        return llm