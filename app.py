# ============================================================
#  PORTFOLIO CHATBOT — Professional Upgrade v2
#  Uses RAG on markdown data files instead of .env
#  Concepts: RAG on personal data, behavioral rules,
#            structured knowledge base, lead detection
# ============================================================

import os
import glob
import html
import requests
import streamlit as st
from dotenv import load_dotenv
from github import Github

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="Aditya Agarwal — AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# ── CUSTOM CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    .header-box {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 28px;
        border-radius: 16px;
        margin-bottom: 20px;
        text-align: center;
        color: white;
        border: 1px solid #0f3460;
    }
    .header-name {
        font-size: 26px;
        font-weight: 700;
        margin: 0;
        color: #00d4aa;
    }
    .header-role {
        font-size: 14px;
        opacity: 0.8;
        margin: 6px 0 0;
    }
    .header-tags {
        margin-top: 12px;
        display: flex;
        gap: 8px;
        justify-content: center;
        flex-wrap: wrap;
    }
    .tag {
        background: rgba(0,212,170,0.15);
        color: #00d4aa;
        border: 1px solid rgba(0,212,170,0.3);
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────
st.markdown("""
<div class="header-box">
    <p class="header-name">Aditya Agarwal</p>
    <p class="header-role">Associate Engineer → AI Engineer | Pune, India</p>
    <div class="header-tags">
        <span class="tag">RAG</span>
        <span class="tag">LangChain</span>
        <span class="tag">AI Agents</span>
        <span class="tag">Embedded Systems</span>
        <span class="tag">2x Research Papers</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── QUICK BUTTONS ─────────────────────────────────────────────
st.markdown("**Quick questions:**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛠 Skills"):
        st.session_state.quick_q = "What are Aditya's technical skills?"
with col2:
    if st.button("📁 Projects"):
        st.session_state.quick_q = "Tell me about all of Aditya's projects in detail"
with col3:
    if st.button("📞 Contact"):
        st.session_state.quick_q = "How can I contact Aditya?"

col4, col5, col6 = st.columns(3)
with col4:
    if st.button("💼 Experience"):
        st.session_state.quick_q = "What is Aditya's work experience?"
with col5:
    if st.button("📄 Research"):
        st.session_state.quick_q = "Tell me about Aditya's research papers"
with col6:
    if st.button("🎯 Hire?"):
        st.session_state.quick_q = "Why should we hire Aditya?"

st.divider()

# ── LOAD AND INDEX KNOWLEDGE BASE ────────────────────────────
@st.cache_resource
def build_knowledge_base():
    md_files = glob.glob("data/*.md")
    if not md_files:
        st.error("No markdown files found in data/ folder!")
        st.stop()

    all_docs = []
    for file_path in md_files:
        loader = TextLoader(file_path, encoding="utf-8")
        docs = loader.load()
        for doc in docs:
            doc.metadata["source_file"] = os.path.basename(file_path)
        all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(all_docs)

    embeddings = MistralAIEmbeddings(
        api_key=os.getenv("MISTRAL_API_KEY"),
        model="mistral-embed"
    )

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore.as_retriever(search_kwargs={"k": 10})


def load_rules():
    try:
        with open("data/rules.md", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Be professional, helpful, and only answer about Aditya."


# ── TELEGRAM NOTIFICATION ─────────────────────────────────────
def send_telegram_alert(user_message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    text = f"""
🚨 *HIRING ALERT — Portfolio Chatbot*

A recruiter just showed hiring interest!

💬 *Their message:*
_{user_message}_

⏰ Check your portfolio chatbot now and follow up!
    """

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    })


# ── GITHUB INTEGRATION ────────────────────────────────────────
SHOW_REPOS = [
    "Portfolio_Chatbot",
    "PDF_Chatbot",
    "Research_Agent",
    "Ai_Projects"
]

def fetch_github_projects():
    try:
        g = Github(os.getenv("GITHUB_TOKEN"))
        user = g.get_user(os.getenv("GITHUB_USERNAME"))
        repos = user.get_repos()

        projects = []
        for repo in repos:
            if repo.name in SHOW_REPOS:
                projects.append({
                    "name": repo.name,
                    "description": repo.description or "No description",
                    "url": repo.html_url,
                    "stars": repo.stargazers_count,
                    "language": repo.language or "Not specified",
                    "updated": repo.updated_at.strftime("%B %Y")
                })
        return projects
    except Exception as e:
        return []


# ── HIRING INTENT DETECTION ───────────────────────────────────
HIRING_KEYWORDS = [
    "hire", "hiring", "interview", "opportunity", "opening",
    "position", "job offer", "would you be interested",
    "good fit", "schedule a call", "send resume", "connect",
    "reach out", "notice period", "join our team", "onboard"
]

def detect_hiring_intent(message):
    return any(kw in message.lower() for kw in HIRING_KEYWORDS)


# ── SMART QUERY ───────────────────────────────────────────────
SHORT_REPLY_STARTERS = [
    "yes", "ye", "ok", "okay", "sure", "yep", "yeah",
    "show me", "tell me more", "go on", "continue",
    "please", "do it", "more", "and", "what about",
    "how about", "expand", "elaborate", "give me", "all"
]

def is_followup(text):
    text = text.strip().lower()
    return any(text.startswith(t) for t in SHORT_REPLY_STARTERS)

def get_smart_query(user_input):
    if is_followup(user_input):
        last_q = st.session_state.get("last_question", "")
        if last_q:
            return last_q
    return user_input

def save_last_question(user_input):
    if not is_followup(user_input):
        st.session_state.last_question = user_input


# ── BUILD RAG CHAIN ───────────────────────────────────────────
@st.cache_resource
def build_chain():
    retriever = build_knowledge_base()
    rules = load_rules()

    llm = ChatMistralAI(
        api_key=os.getenv("MISTRAL_API_KEY"),
        model="mistral-small-latest",
        temperature=0
    )

    prompt = PromptTemplate.from_template("""
{rules}

---

ABSOLUTE RULE — NO HALLUCINATION:
You must ONLY use information explicitly written in the
Knowledge Base Context below.

NEVER use your own training knowledge to fill gaps.
NEVER invent paper titles, project names, or any details.
NEVER say something is true if it is not in the context.

IMPORTANT: The context contains Aditya's education, experience,
skills, projects and research. Read it carefully before saying
information is missing. If it IS in the context, always answer
fully and completely.

If information is truly missing from context — say:
"I don't have that specific detail. You can reach Aditya
directly at agarwal.aditya2017@gmail.com for more info."

Knowledge Base Context:
{context}

Conversation History:
{history}

Current Question: {question}

MEMORY RULE: If the question is a short follow-up like "yes",
"show me all", "tell me more" — expand on the LAST topic from
Conversation History. Do NOT reset or change topics.

Answer:""")

    def format_docs(docs):
        return "\n\n".join([
            f"[From {doc.metadata.get('source_file', 'unknown')}]\n{doc.page_content}"
            for doc in docs
        ])

    chain = (
        {
            "context": (lambda x: x["smart_query"]) | retriever | format_docs,
            "question": lambda x: x["question"],
            "rules": lambda x: rules,
            "history": lambda x: st.session_state.get("history_text", "")
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain, retriever


# ── SESSION STATE ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "history_text" not in st.session_state:
    st.session_state.history_text = ""
if "hiring_detected" not in st.session_state:
    st.session_state.hiring_detected = False
if "last_question" not in st.session_state:
    st.session_state.last_question = ""

# ── BUILD CHAIN ───────────────────────────────────────────────
with st.spinner("Loading knowledge base..."):
    chain, retriever = build_chain()

# ── DISPLAY CHAT HISTORY ──────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── HANDLE QUICK BUTTONS ──────────────────────────────────────
if "quick_q" in st.session_state:
    user_input = st.session_state.quick_q
    del st.session_state.quick_q

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            if detect_hiring_intent(user_input):
                st.session_state.hiring_detected = True
                send_telegram_alert(user_input)

            save_last_question(user_input)
            smart_query = get_smart_query(user_input)

            reply = chain.invoke({
                "question": user_input,
                "smart_query": smart_query
            })
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.history_text += f"\nUser: {user_input}\nAssistant: {reply}\n"
    st.rerun()

# ── CHAT INPUT ────────────────────────────────────────────────
user_input = st.chat_input("Ask me anything about Aditya...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            if detect_hiring_intent(user_input):
                st.session_state.hiring_detected = True
                send_telegram_alert(user_input)

            save_last_question(user_input)
            smart_query = get_smart_query(user_input)

            reply = chain.invoke({
                "question": user_input,
                "smart_query": smart_query
            })
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.history_text += f"\nUser: {user_input}\nAssistant: {reply}\n"

# ── HIRING ALERT ──────────────────────────────────────────────
if st.session_state.hiring_detected:
    st.markdown("""
    <style>
        .hiring-alert-banner {
            margin-top: 12px;
            margin-bottom: 10px;
            padding: 18px 20px;
            border-radius: 14px;
            border: 1px solid rgba(34, 197, 94, 0.5);
            background: linear-gradient(135deg, rgba(6, 78, 59, 0.95), rgba(21, 128, 61, 0.95));
            box-shadow: 0 0 0 1px rgba(34, 197, 94, 0.25), 0 10px 30px rgba(16, 185, 129, 0.35);
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .hiring-alert-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #22c55e;
            animation: hiringPulse 1.4s infinite;
            flex-shrink: 0;
        }
        .hiring-alert-text {
            color: #ecfdf5;
            font-size: 16px;
            font-weight: 700;
            margin: 0;
        }
        @keyframes hiringPulse {
            0% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.75); }
            70% { transform: scale(1.08); box-shadow: 0 0 0 12px rgba(34, 197, 94, 0); }
            100% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
        }
    </style>
    <div class="hiring-alert-banner">
        <span class="hiring-alert-dot"></span>
        <p class="hiring-alert-text">🚨 Recruiter Alert Sent! Aditya has been notified via Telegram</p>
    </div>
    """, unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🚀 Live GitHub Projects")
    projects = fetch_github_projects()
    if projects:
        st.markdown("""
        <style>
            .repo-card {
                background: linear-gradient(145deg, #121826, #101523);
                border: 1px solid rgba(148, 163, 184, 0.22);
                border-radius: 14px;
                padding: 14px 14px 12px;
                margin-bottom: 10px;
                box-shadow: 0 6px 18px rgba(2, 6, 23, 0.35);
            }
            .repo-title { margin: 0 0 6px 0; font-size: 15px; font-weight: 700; }
            .repo-title a { color: #e2e8f0; text-decoration: none; }
            .repo-title a:hover { color: #22d3ee; text-decoration: underline; }
            .repo-description { margin: 0 0 10px 0; color: #94a3b8; font-size: 12px; }
            .repo-meta { display: flex; align-items: center; flex-wrap: wrap; gap: 8px; font-size: 12px; }
            .repo-pill { padding: 3px 9px; border-radius: 999px; font-size: 11px; font-weight: 600; color: #e2e8f0; border: 1px solid rgba(255,255,255,0.2); }
        </style>
        """, unsafe_allow_html=True)

        language_colors = {
            "python": "#3776ab", "javascript": "#f1e05a",
            "typescript": "#3178c6", "java": "#b07219",
            "c++": "#f34b7d", "c": "#555555",
            "html": "#e34c26", "css": "#563d7c",
            "go": "#00add8", "shell": "#89e051",
        }

        for p in projects:
            safe_name = html.escape(p["name"])
            safe_url = html.escape(p["url"], quote=True)
            safe_desc = html.escape(p["description"])
            safe_lang = html.escape(p["language"])
            safe_updated = html.escape(p["updated"])
            stars = p["stars"]
            lang_color = language_colors.get(p["language"].lower(), "#475569")

            st.markdown(f"""
            <div class="repo-card">
                <p class="repo-title">
                    <a href="{safe_url}" target="_blank"><strong>{safe_name}</strong></a>
                </p>
                <p class="repo-description">{safe_desc}</p>
                <div class="repo-meta">
                    <span class="repo-pill" style="background:{lang_color}33; border-color:{lang_color}66;">
                        {safe_lang}
                    </span>
                    <span>⭐ {stars}</span>
                    <span>Updated: {safe_updated}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Could not fetch GitHub projects")

    st.divider()
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.history_text = ""
        st.session_state.hiring_detected = False
        st.session_state.last_question = ""
        st.rerun()