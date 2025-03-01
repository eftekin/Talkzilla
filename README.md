# 🦖 Talkzilla

**Talkzilla: A chatbot that roars with fun conversations!**

Talkzilla is a simple yet engaging chatbot built with Streamlit, designed to maintain conversation history and demonstrate basic token usage with Gemini's API using the OpenAI library. It's a fun, interactive project that showcases how to create a memory-powered chatbot with document analysis capabilities.

## 🚀 Features

- 🧠 Conversation memory
- 📄 File upload and analysis support (TXT, PDF, DOCX)
- 🔑 Token usage tracking
- ⚡ Streamlit-powered UI
- 🤖 Gemini API integration via OpenAI library
- 🔄 Multiple model options (gemini-2.0-flash, gemini-1.5-pro, gemini-1.5-flash)

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

- Open your browser at `http://localhost:8501`
- Enter your Gemini API key in the sidebar. [Get an API key here](https://aistudio.google.com/app/apikey)
- Select your preferred Gemini model from the dropdown
- Upload documents (TXT, PDF, or DOCX) for analysis and discussion
- Start chatting with Talkzilla about the uploaded content or any other topic
- Watch how it remembers the conversation context!

## 🧩 Project Structure

```
📂 talkzilla
   └── app.py            # Main Streamlit app with chat and file processing
   └── requirements.txt  # Dependencies
   └── README.md         # Project documentation
```

## 🤖 How It Works

- Uses Streamlit's session state to store conversation history and file content
- Processes various file formats (TXT, PDF, DOCX) for analysis
- Integrates Gemini's API via the OpenAI library to generate responses
- Tracks token usage for both messages and uploaded content
- Supports multiple Gemini model variants
- Provides real-time streaming responses

## 📦 Dependencies

- streamlit
- openai
- tiktoken
- PyPDF2 (for PDF processing)
- python-docx (for DOCX processing)

## ⚠️ Notes

- Ensure you have a valid Gemini API key
- File size limitations may apply based on token limits
- Different models may have varying performance characteristics

## 🐜 License

MIT License

---

Happy chatting with **Talkzilla**! 🦖💬
