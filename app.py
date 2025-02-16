# Import necessary libraries
import streamlit as st
import tiktoken
from openai import OpenAI

# Configure the Streamlit page settings
st.set_page_config(
    page_title="Talkzilla",
    page_icon="🦖",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# Talkzilla 🦖\nA chatbot that roars with fun conversations! Built with Streamlit and Gemini API."
    },
)


# Function to count tokens in the text using tiktoken
def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


# Initialize session state variables for the application
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gemini-2.0-flash"

# Initialize chat messages with a welcome message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm Talkzilla 🦖, here to roar with fun conversations! How can I assist you today?",
        }
    ]

# Initialize token counter
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

# Sidebar configuration
with st.sidebar:
    # API key input field
    gemini_api_key = st.text_input(
        "Gemini API Key", key="chatbot_api_key", type="password"
    )
    # Link to get API key
    "[Get a Gemini API key](https://aistudio.google.com/app/apikey)"
    st.divider()
    # Display total tokens used
    st.metric("Total Tokens Used", st.session_state.total_tokens)
    # Clear chat button
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.total_tokens = 0

# Model selection dropdown in sidebar
model_choice = st.sidebar.selectbox(
    "Choose a model", ["gemini-2.0-flash", "gemini-1.5-pro", "gemini-1.5-flash"]
)
st.session_state["openai_model"] = model_choice

# Main chat interface
st.title("Talkzilla 🦖")
st.caption("A chatbot that roars with fun conversations!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if len(st.session_state.messages) != 1:
            token_count = count_tokens(message["content"])
            st.caption(f"Tokens used: {token_count}")

# Chat input and response handling
if prompt := st.chat_input(""):
    # Check if API key is provided
    if not gemini_api_key:
        st.info("Please enter your Gemini API key in the sidebar.")
        st.stop()

    try:
        # Initialize OpenAI client with Gemini API
        client = OpenAI(
            api_key=gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

        # Calculate tokens and update chat history for user message
        prompt_tokens = count_tokens(prompt)
        st.session_state.total_tokens += prompt_tokens
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
            st.caption(f"Tokens used: {prompt_tokens}")

        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Create streaming chat completion
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
            # Display streaming response and update token count
            response = st.write_stream(stream)
            response_tokens = count_tokens(response)
            st.session_state.total_tokens += response_tokens
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.caption(f"Tokens used: {response_tokens}")

    # Error handling
    except Exception as e:
        st.error(f"Something went wrong: {e}")
