"""
Polyreasoner Web Interface
Gradio-based chat UI for multi-perspective reasoning
"""

import gradio as gr
from main import Polyreasoner

# Global instance
reasoner = Polyreasoner()


def chat_response(message, history):
    """
    Process user message and return response.
    Gradio ChatInterface handles history automatically.
    """
    if not message.strip():
        return "Please enter a message."
    
    # Handle commands
    if message.lower() == 'clear':
        reasoner.conversation_history = []
        return "✨ Conversation cleared."
    
    try:
        # Process with Polyreasoner
        response = reasoner.process(message)
        return response
    
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease check your model configuration."


def create_ui():
    """Create and configure Gradio interface"""
    
    # Create ChatInterface
    with gr.Blocks(title="Polyreasoner") as demo:
        
        gr.Markdown("""
        # 🧠 Polyreasoner
        ### Multi-Perspective Reasoning System
        
        Ask complex questions or evaluate ideas. I'll automatically activate multi-agent analysis when needed.
        
        **Examples:**
        - "Should I open source my ML project?"
        - "Evaluate: building a mobile app for freelancers"
        - "What are the risks of switching to microservices?"
        """)
        
        chatbot = gr.ChatInterface(
            fn=chat_response,
            chatbot=gr.Chatbot(height=500),
            textbox=gr.Textbox(
                placeholder="Ask a question or describe an idea to evaluate...",
                container=False
            ),
            examples=[
                "Should I build a SaaS or open source first?",
                "Evaluate: AI-powered code review tool",
                "What could go wrong with this startup idea?",
            ]
        )
        
        gr.Markdown("""
        ---
        💡 **Tip:** Type 'clear' to reset conversation history | The system uses local LLMs for complete privacy
        
        **How it works:**
        - Simple questions → Direct response
        - Complex decisions → Automatic multi-agent analysis (business, risk, security, feasibility, impact, ethical, contrarian perspectives)
        """)
    
    return demo


if __name__ == "__main__":
    print("=" * 60)
    print("  🧠 POLYREASONER WEB INTERFACE")
    print("  Multi-Perspective Reasoning System")
    print("=" * 60)
    print()
    print("Starting Gradio server...")
    print("This will load the LLM models (may take a moment)")
    print()
    
    demo = create_ui()
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True
    )
