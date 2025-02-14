# 🦖 Talkzilla

**Talkzilla: A chatbot that roars with fun conversations!**

Talkzilla is a simple yet engaging chatbot built with Streamlit, designed to maintain conversation history and demonstrate basic token usage with Gemini's API using the OpenAI library. It's a fun, interactive project that showcases how to create a memory-powered chatbot.

## 🚀 Features

- 🧠 Conversation memory
- 🔑 Token usage demonstration
- ⚡ Streamlit-powered UI
- 🤖 Gemini API integration via OpenAI library

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eftekin/talkzilla.git
   cd talkzilla
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 🧪 Usage

- Open your browser at `http://localhost:8501`.
- Enter your Gemini API key in the sidebar. [Get an API key here](https://aistudio.google.com/app/apikey)
- Start chatting with Talkzilla.
- Watch how it remembers the conversation context!

## 🧩 Project Structure

```
📂 talkzilla
   └── app.py            # Main Streamlit app
   └── requirements.txt  # Dependencies
   └── README.md         # Project documentation
```

## 🤖 How It Works

- Uses Streamlit's session state to store conversation history.
- Integrates Gemini's API via the OpenAI library to generate responses.
- Demonstrates efficient token usage and memory retention.

## ⚠️ Notes

- Ensure you have a valid Gemini API key.
- Adjust token limits based on your usage needs.

## 🐜 License

MIT License

---

Happy chatting with **Talkzilla**! 🦖💬
