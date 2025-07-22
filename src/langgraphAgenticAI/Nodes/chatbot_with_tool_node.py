from src.langgraphAgenticAI.State.state import State

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self,model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node



'''
This is the actual LangGraph-compatible node function.

bind_tools(tools): Binds tool definitions (like Tavily search, calculator, etc.) to the LLM.

Returns a callable node (function) that:

Takes in a state with chat history (state["messages"])

Calls the tool-bound LLM

Returns the updated message list as a new state

✅ This chatbot_node() function is what you plug into LangGraph like:
'''
'''
The process function is like a standalone inference method — not graph-integrated, possibly for testing/debugging.
Takes a state (conversation history).
Extracts latest user message.
Calls the LLM using .invoke(...) with a single message.
Mocks a tools_response message.
Returns both messages as a dictionary: {"messages": [...]}.

🧠 You can use this outside LangGraph to quickly test what the LLM + mock tools would do.
'''