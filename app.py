# ============================================================
#  PORTFOLIO CHATBOT — Streamlit Web App
#  Uses Groq API (free, fast, cloud-based)
#  Anyone can open this on mobile or laptop via a link!
# ============================================================

import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ── READ PERSONAL INFO FROM .env ──────────────────────────────
name         = os.getenv('NAME', 'Your Name')
role         = os.getenv('CURRENT_ROLE', 'Developer')
experience   = os.getenv('EXPERIENCE', '1 year')
location     = os.getenv('LOCATION', 'India')
open_to      = os.getenv('OPEN_TO', 'AI roles')
availability = os.getenv('AVAILABILITY', 'Available')
work_type    = os.getenv('WORK_TYPE', 'Full-time')
skill_ai       = os.getenv('SKILL_AI', '')
skill_python   = os.getenv('SKILL_PYTHON', '')
skill_tools    = os.getenv('SKILL_TOOLS', '')
skill_db       = os.getenv('SKILL_DATABASES', '')
skill_learning = os.getenv('SKILL_LEARNING', '')
skill_soft     = os.getenv('SKILL_SOFT', '')
company      = os.getenv('COMPANY', '')
company_type = os.getenv('COMPANY_TYPE', '')
work_desc    = os.getenv('CURRENT_WORK_DESC', '')
achievement1 = os.getenv('ACHIEVEMENT1', '')
achievement2 = os.getenv('ACHIEVEMENT2', '')
ai_since     = os.getenv('AI_LEARNING_SINCE', '')
p1_name   = os.getenv('PROJECT1_NAME', '')
p1_desc   = os.getenv('PROJECT1_DESC', '')
p1_tech   = os.getenv('PROJECT1_TECH', '')
p1_github = os.getenv('PROJECT1_GITHUB', '')
p2_name   = os.getenv('PROJECT2_NAME', '')
p2_desc   = os.getenv('PROJECT2_DESC', '')
p2_tech   = os.getenv('PROJECT2_TECH', '')
p2_github = os.getenv('PROJECT2_GITHUB', '')
p3_name      = os.getenv('PROJECT3_NAME', '')
p3_desc      = os.getenv('PROJECT3_DESC', '')
p3_tech      = os.getenv('PROJECT3_TECH', '')
p3_github    = os.getenv('PROJECT3_GITHUB', '')
p3_highlight = os.getenv('PROJECT3_HIGHLIGHT', '')
p4_name      = os.getenv('PROJECT4_NAME', '')
p4_desc      = os.getenv('PROJECT4_DESC', '')
p4_tech      = os.getenv('PROJECT4_TECH', '')
p4_github    = os.getenv('PROJECT4_GITHUB', '')
p4_highlight = os.getenv('PROJECT4_HIGHLIGHT', '')
paper1  = os.getenv('PAPER1', '')
paper2  = os.getenv('PAPER2', '')
degree  = os.getenv('DEGREE', '')
college = os.getenv('COLLEGE', '')
grad_yr = os.getenv('GRAD_YEAR', '')
cert1   = os.getenv('CERT1', '')
cert2   = os.getenv('CERT2', '')
cert3   = os.getenv('CERT3', '')
strength1  = os.getenv('STRENGTH1', '')
strength2  = os.getenv('STRENGTH2', '')
strength3  = os.getenv('STRENGTH3', '')
passion    = os.getenv('PASSION', '')
work_style = os.getenv('WORK_STYLE', '')
target_role    = os.getenv('TARGET_ROLE', '')
target_company = os.getenv('TARGET_COMPANY', '')
salary         = os.getenv('SALARY', 'Open to discussion')
notice         = os.getenv('NOTICE_PERIOD', '')
remote         = os.getenv('REMOTE', '')
email     = os.getenv('EMAIL', '')
linkedin  = os.getenv('LINKEDIN', '')
github    = os.getenv('GITHUB', '')

# ── SYSTEM PROMPT ─────────────────────────────────────────────
SYSTEM_PROMPT = f"""
You are {name}'s personal portfolio assistant.
Help recruiters, clients, and developers learn about {name}
in a friendly and professional way.

== ABOUT ==
Name         : {name}
Role         : {role} | Experience: {experience}
Location     : {location}
Availability : {availability}
Work type    : {work_type}
Open to      : {open_to}

== TECHNICAL SKILLS ==
AI & LLM      : {skill_ai}
Python & ML   : {skill_python}
Tools         : {skill_tools}
Databases     : {skill_db}
Learning now  : {skill_learning}
Soft skills   : {skill_soft}

== WORK EXPERIENCE ==
Company    : {company} ({company_type})
Role       : {role} | {experience}
Daily work : {work_desc}
Key win #1 : {achievement1}
Key win #2 : {achievement2}
AI journey : Started {ai_since}

== PROJECTS ==
1. {p3_name}
   What: {p3_desc}
   Tech: {p3_tech}
   GitHub: {p3_github}
   Note: {p3_highlight}

2. {p4_name}
   What: {p4_desc}
   Tech: {p4_tech}
   GitHub: {p4_github}
   Note: {p4_highlight}

3. {p1_name}
   What: {p1_desc}
   Tech: {p1_tech}
   GitHub: {p1_github}

4. {p2_name}
   What: {p2_desc}
   Tech: {p2_tech}
   GitHub: {p2_github}

== RESEARCH PAPERS (Published) ==
- {paper1}
- {paper2}

== EDUCATION ==
Degree  : {degree}
College : {college}
Year    : {grad_yr}

== CERTIFICATIONS ==
- {cert1}
- {cert2}
- {cert3}

== STRENGTHS ==
- {strength1}
- {strength2}
- {strength3}
Work style : {work_style}
Passion    : {passion}

== JOB PREFERENCES ==
Target roles     : {target_role}
Target companies : {target_company}
Salary           : {salary}
Notice period    : {notice}
Remote           : {remote}

== CONTACT ==
Email    : {email}
LinkedIn : {linkedin}
GitHub   : {github}

== HOW TO BEHAVE ==
- Be friendly, warm and professional
- Keep answers to 3-5 lines
- Mention research papers when relevant — they are impressive
- For salary say: "{salary}"
- If asked something not listed say: "I don't have that detail — reach {name} at {email}"
- Never make up information not listed above
- End every response with an offer to help further
"""

# ── GROQ CLIENT ───────────────────────────────────────────────
# Groq is like Ollama but runs in the cloud — free and fast
# This is what makes the app work on mobile and for everyone
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# ── STREAMLIT PAGE CONFIG ─────────────────────────────────────
# This must be the FIRST streamlit command — sets page title and icon
st.set_page_config(
    page_title=f"{name} — Portfolio Assistant",
    page_icon="🤖",
    layout="centered"
)

# ── CUSTOM CSS — makes it look clean and professional ─────────
st.markdown("""
<style>
    .main { max-width: 750px; }
    .stChatMessage { border-radius: 12px; }
    .header-box {
        background: linear-gradient(135deg, #6C63FF, #4FC3F7);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        text-align: center;
        color: white;
    }
    .quick-btn {
        background: #f0f2f6;
        border: 1px solid #e0e0e0;
        border-radius: 20px;
        padding: 6px 14px;
        font-size: 13px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────
st.markdown(f"""
<div class="header-box">
    <h2 style="margin:0; font-size:24px;">👋 Hi, I'm {name}'s AI Assistant</h2>
    <p style="margin:8px 0 0; opacity:0.9; font-size:14px;">
        Ask me anything about {name}'s skills, projects, experience, or how to contact him
    </p>
</div>
""", unsafe_allow_html=True)

# ── QUICK QUESTION BUTTONS ────────────────────────────────────
# These help mobile users — they can tap instead of type
st.markdown("**Quick questions:**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛠 Skills"):
        st.session_state.quick_question = "What are your technical skills?"
with col2:
    if st.button("📁 Projects"):
        st.session_state.quick_question = "Tell me about your projects"
with col3:
    if st.button("📞 Contact"):
        st.session_state.quick_question = "How can I contact you?"

col4, col5, col6 = st.columns(3)
with col4:
    if st.button("💼 Experience"):
        st.session_state.quick_question = "What is your work experience?"
with col5:
    if st.button("📄 Research"):
        st.session_state.quick_question = "Do you have any research papers?"
with col6:
    if st.button("🎯 Hire?"):
        st.session_state.quick_question = "Why should we hire you?"

st.divider()

# ── SESSION STATE — this is Streamlit's version of memory ─────
# st.session_state persists data between user interactions
# Without this, every button click resets everything

if "messages" not in st.session_state:
    # First time loading — start with system prompt + greeting
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    # Get opening greeting from AI
    opening = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # Groq's free llama3 model
        messages=st.session_state.messages + [
            {"role": "user", "content": "Introduce yourself in 2 friendly lines"}
        ]
    )
    greeting = opening.choices[0].message.content
    st.session_state.messages.append({
        "role": "assistant",
        "content": greeting
    })

# ── DISPLAY CHAT HISTORY ──────────────────────────────────────
# Loop through all messages and display them
# Skip the system prompt (index 0) — user should not see it
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── HANDLE QUICK QUESTION BUTTONS ────────────────────────────
if "quick_question" in st.session_state:
    user_input = st.session_state.quick_question
    del st.session_state.quick_question  # clear it after use

    # Add to chat and get response
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# ── CHAT INPUT BOX ────────────────────────────────────────────
# st.chat_input creates the message box at the bottom of the page
user_input = st.chat_input(f"Ask me anything about {name}...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response from Groq
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",   # free Groq model
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)

    # Save to history
    st.session_state.messages.append({"role": "assistant", "content": reply})