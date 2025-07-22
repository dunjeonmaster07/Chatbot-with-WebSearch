from langgraph.graph import StateGraph
from src.langgraphAgenticAI.State.state import State
from langgraph.graph import START,END
from src.langgraphAgenticAI.Nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphAgenticAI.Tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphAgenticAI.Nodes.chatbot_with_tool_node import ChatbotWithToolNode


#Prerequisites: We need a state model for the StateGraph that will be defined in the state directory
#To make a pipeline: we need a model as well to be called within the defined nodes in the Graph.
'''
-- Sequence:
    - State
    - Define the Graph builder
    - Define Nodes
'''
class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        
        #Initialize the node
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        
        #Define Nodes and Edges:
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process) #The second method name process is the node name written in Node folder
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        
        ## Define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools)

        ## Define the LLM
        llm=self.llm

        ## Define the chatbot node

        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        
        ## Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        # Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)
       
       
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            
        if usecase =="Chatbot with Web Search":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()