from langchain_community.tools.tavily_search import TavilySearchResults  # ✅ still working as of LangChain 0.3.25
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in Chatbot
    """
    tools = [TavilySearchResults(name="tavily_search_results_json", max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)
