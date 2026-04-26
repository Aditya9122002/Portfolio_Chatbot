# 🤖 Aditya Agarwal — AI Portfolio Assistant

An intelligent portfolio chatbot that answers questions about my background,
skills, projects, and experience using RAG (Retrieval Augmented Generation).

🔗 **Live Demo:** [Click here to chat](your-streamlit-url-here)

---

## ✨ Features

- 🧠 **RAG Pipeline** — Answers from a structured knowledge base, not hallucinations
- 💬 **Conversation Memory** — Remembers context across the conversation
- 🔍 **Smart Query Detection** — Handles follow-up replies like "yes", "tell me more"
- 🚨 **Hiring Intent Detection** — Detects recruiter interest and alerts instantly
- 📱 **Telegram Notifications** — Real-time alerts when a recruiter shows interest
- 🚀 **Live GitHub Integration** — Auto-fetches latest projects from GitHub
- 🎯 **Zero Hallucination** — Strict grounding on knowledge base only

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| LLM | Mistral AI (mistral-small-latest) |
| Embeddings | Mistral AI (mistral-embed) |
| Vector DB | ChromaDB |
| RAG Framework | LangChain |
| Notifications | Telegram Bot API |
| GitHub Data | PyGithub |
| Deployment | Streamlit Cloud |

---

## 🏗 Architecture
User Question
↓
Smart Query Detection
(follow-up or real question?)
↓
RAG Retrieval (ChromaDB)
(fetch top 10 relevant chunks)
↓
Mistral AI LLM
(answer from context only)
↓
Hiring Intent Check
(send Telegram alert if recruiter)
↓
Response to User

---

## 📁 Knowledge Base Structure
data/
├── profile.md       # Basic info, contact details
├── projects.md      # All 5 projects in detail
├── skills.md        # Technical skills
├── experience.md    # Work experience at L&T
├── education.md     # Degree, certifications, research papers
└── rules.md         # Bot behavioral rules

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Aditya9122002/Portfolio_Chatbot.git
cd Portfolio_Chatbot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create `.env` file**
MISTRAL_API_KEY=your_key_here
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
GITHUB_TOKEN=your_token_here
GITHUB_USERNAME=Aditya9122002

**4. Run the app**
```bash
streamlit run app.py
```

---

## 💡 Key Concepts Learned

- **RAG** — Retrieval Augmented Generation for grounded answers
- **Vector Embeddings** — Text to numerical representations for semantic search
- **ChromaDB** — Local vector database with cosine similarity search
- **LangChain** — Chaining LLM components with the `|` pipe operator
- **Streamlit** — Rapid web UI development with session state management
- **Hiring Intent Detection** — Keyword-based recruiter interest detection

---

## 📬 Contact

- 📧 Email: agarwal.aditya2017@gmail.com
- 💼 LinkedIn: [Aditya Agarwal](https://www.linkedin.com/in/aditya-agarwal-782461221/)
- 🐙 GitHub: [Aditya9122002](https://github.com/Aditya9122002)

---

⭐ If you found this useful, give it a star!