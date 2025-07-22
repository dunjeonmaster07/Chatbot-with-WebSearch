#Part 1: adding the streamlit UI Component :
import streamlit as st
from src.langgraphAgenticAI.Gui.streamlitui.loadui import LoadStreamlitUi
from src.langgraphAgenticAI.LLMs.groqllm import GroqLLM
from src.langgraphAgenticAI.Graph.graph_builder import GraphBuilder
from src.langgraphAgenticAI.Gui.streamlitui.display_results import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    #Load UI Streamlit:
    ui = LoadStreamlitUi() #loading class
    user_input = ui.load_streamlit_ui() #loading method
    
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")
    
    
    #Part 2: Create a pipeline from frontend to the backend:
    if user_message:
        try:
            
            ## Configure The LLM's. Called from LLM dir and fetches the streamlit's user_input as defined above
            obj_llm_config=GroqLLM(user_contols_input=user_input)
            model=obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            # Initialize and set up the graph based on use case(Use case is not Streamlit)
            usecase=user_input.get("selected_usecase")
            
            if not usecase:
                    st.error("Error: No use case selected.")
                    return
            
            ## Graph Builder

            graph_builder=GraphBuilder(model)
            try:
                #st.write("Methods available in GraphBuilder:", dir(graph_builder))
                graph=graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                 st.error(f"Error: Graph set up failed- {e}")
                 return

        except Exception as e:
             st.error(f"Error: Graph set up failed- {e}")
             return 
            
    

