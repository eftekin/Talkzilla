import streamlit as st
import tiktoken
from openai import OpenAI


def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


# Initialize session state first
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gemini-2.0-flash"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

# Sidebar setup
with st.sidebar:
    gemini_api_key = st.text_input(
        "Gemini API Key", key="chatbot_api_key", type="password"
    )
    "[Get a Gemini API key](https://aistudio.google.com/app/apikey)"
    st.divider()
    st.metric("Total Tokens Used", st.session_state.total_tokens)
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.total_tokens = 0

# Model selection
model_choice = st.sidebar.selectbox(
    "Choose a model", ["gemini-2.0-flash", "gemini-1.5-pro", "gemini-1.5-flash"]
)
st.session_state["openai_model"] = model_choice

st.title("Talkzilla 🦖")
st.caption("A chatbot that roars with fun conversations!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        token_count = count_tokens(message["content"])
        st.caption(f"Tokens used: {token_count}")

if prompt := st.chat_input(""):
    if not gemini_api_key:
        st.info("Please enter your Gemini API key in the sidebar.")
        st.stop()

    try:
        client = OpenAI(
            api_key=gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

        prompt_tokens = count_tokens(prompt)
        st.session_state.total_tokens += prompt_tokens
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)
            st.caption(f"Tokens used: {prompt_tokens}")

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
            response = st.write_stream(stream)
            response_tokens = count_tokens(response)
            st.session_state.total_tokens += response_tokens
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.caption(f"Tokens used: {response_tokens}")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
