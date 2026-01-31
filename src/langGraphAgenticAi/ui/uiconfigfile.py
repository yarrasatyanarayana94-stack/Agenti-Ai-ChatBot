''' 
This py file is going to read the data from the uiconfigfile.ini 
''' 

import os
from configparser import ConfigParser

class Config:
    """
   
    """
    # def __init__(self,configfile="./src/uiconfigfile/ui/uiconfigfile.ini"):
    #     self.config=ConfigParser()
    #     self.config.read(configfile)
    def __init__(self, configfile=None):
        self.config = ConfigParser()

        if configfile is None:
            base_dir = os.path.dirname(__file__)
            configfile = os.path.join(base_dir, "uiconfigfile.ini")

        self.config.read(configfile)

    def _get_list(self, key):
        value = self.config["DEFAULT"].get(key, "")
        return [v.strip() for v in value.split(",") if v.strip()]
    
    def get_llm_options(self):
        return self._get_list("LLM_OPTIONS")

    def get_usecase_options(self):
        return self._get_list("USECASE_OPTIONS")

    def get_groq_model_options(self):
        return self._get_list("GROQ_MODEL_OPTIONS")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "My Streamlit App")


c1=Config()
x=c1.get_page_title()
print(x)
    # def get_llm_options(self):
    #     value = self.config["DEFAULT"].get("LLM_OPTIONS")
    #     if not value:
    #         return []
    #     return value.split(", ")
    
    # def get_usecase_options(self):
    #     value= self.config["DEFAULT"].get("USECASE_OPTIONS")
    #     if not value:
    #         return []
    #     return value.split(", ")
       
    # def get_groq_model_options(self):
    #     value= self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS")
    #     if not value:
    #         return []
    #     return value.split(", ")
    
    # def get_page_title(self):
    #     return self.config["DEFAULT"].get("PAGE_TITLE")