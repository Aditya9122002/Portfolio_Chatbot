import ollama
import os
from dotenv import load_dotenv

load_dotenv()

# ── BASIC INFO ────────────────────────────────────────────────
name         = os.getenv('NAME', 'Your Name')
role         = os.getenv('CURRENT_ROLE', 'Developer')
experience   = os.getenv('EXPERIENCE', '7 Months')
location     = os.getenv('LOCATION', 'India')
open_to      = os.getenv('OPEN_TO', 'AI roles')
availability = os.getenv('AVAILABILITY', 'Available')
work_type    = os.getenv('WORK_TYPE', 'Full-time')

# ── SKILLS ───────────────────────────────────────────────────
skill_ai       = os.getenv('SKILL_AI', '')
skill_python   = os.getenv('SKILL_PYTHON', '')
skill_tools    = os.getenv('SKILL_TOOLS', '')
skill_db       = os.getenv('SKILL_DATABASES', '')
skill_learning = os.getenv('SKILL_LEARNING', '')
skill_soft     = os.getenv('SKILL_SOFT', '')

# ── EXPERIENCE ───────────────────────────────────────────────
company      = os.getenv('COMPANY', '')
company_type = os.getenv('COMPANY_TYPE', '')
work_desc    = os.getenv('CURRENT_WORK_DESC', '')
achievement1 = os.getenv('ACHIEVEMENT1', '')
achievement2 = os.getenv('ACHIEVEMENT2', '')
ai_since     = os.getenv('AI_LEARNING_SINCE', '')

# ── PROJECTS ─────────────────────────────────────────────────
p1_name   = os.getenv('PROJECT1_NAME', '')
p1_desc   = os.getenv('PROJECT1_DESC', '')
p1_tech   = os.getenv('PROJECT1_TECH', '')
p1_github = os.getenv('PROJECT1_GITHUB', '')
p1_demo   = os.getenv('PROJECT1_DEMO', 'coming soon')

p2_name   = os.getenv('PROJECT2_NAME', '')
p2_desc   = os.getenv('PROJECT2_DESC', '')
p2_tech   = os.getenv('PROJECT2_TECH', '')
p2_github = os.getenv('PROJECT2_GITHUB', '')
p2_demo   = os.getenv('PROJECT2_DEMO', 'coming soon')

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

# ── RESEARCH PAPERS ──────────────────────────────────────────
paper1 = os.getenv('PAPER1', '')
paper2 = os.getenv('PAPER2', '')

# ── EDUCATION ────────────────────────────────────────────────
degree  = os.getenv('DEGREE', '')
college = os.getenv('COLLEGE', '')
grad_yr = os.getenv('GRAD_YEAR', '')
courses = os.getenv('RELEVANT_COURSES', '')

# ── CERTIFICATIONS ───────────────────────────────────────────
cert1 = os.getenv('CERT1', '')
cert2 = os.getenv('CERT2', '')
cert3 = os.getenv('CERT3', '')

# ── PERSONALITY ──────────────────────────────────────────────
strength1  = os.getenv('STRENGTH1', '')
strength2  = os.getenv('STRENGTH2', '')
strength3  = os.getenv('STRENGTH3', '')
work_style = os.getenv('WORK_STYLE', '')
passion    = os.getenv('PASSION', '')

# ── JOB PREFERENCES ──────────────────────────────────────────
target_role    = os.getenv('TARGET_ROLE', '')
target_company = os.getenv('TARGET_COMPANY', '')
salary         = os.getenv('SALARY', 'Open to discussion')
notice         = os.getenv('NOTICE_PERIOD', '')
relocation     = os.getenv('RELOCATION', '')
remote         = os.getenv('REMOTE', '')

# ── CONTACT ──────────────────────────────────────────────────
email     = os.getenv('EMAIL', '')
linkedin  = os.getenv('LINKEDIN', '')
github    = os.getenv('GITHUB', '')
portfolio = os.getenv('PORTFOLIO', '')

# ── SYSTEM PROMPT ────────────────────────────────────────────
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
   What   : {p3_desc}
   Tech   : {p3_tech}
   GitHub : {p3_github}
   Note   : {p3_highlight}

2. {p4_name}
   What   : {p4_desc}
   Tech   : {p4_tech}
   GitHub : {p4_github}
   Note   : {p4_highlight}

3. {p1_name}
   What   : {p1_desc}
   Tech   : {p1_tech}
   GitHub : {p1_github}
   Demo   : {p1_demo}

4. {p2_name}
   What   : {p2_desc}
   Tech   : {p2_tech}
   GitHub : {p2_github}
   Demo   : {p2_demo}

== RESEARCH PAPERS (Published) ==
- {paper1}
- {paper2}

== EDUCATION ==
Degree  : {degree}
College : {college}
Year    : {grad_yr}
Courses : {courses}

== CERTIFICATIONS ==
- {cert1}
- {cert2}
- {cert3}

== STRENGTHS & PERSONALITY ==
Strength 1 : {strength1}
Strength 2 : {strength2}
Strength 3 : {strength3}
Work style : {work_style}
Passion    : {passion}

== JOB PREFERENCES ==
Target roles     : {target_role}
Target companies : {target_company}
Salary           : {salary}
Notice period    : {notice}
Relocation       : {relocation}
Remote           : {remote}

== CONTACT ==
Email     : {email}
LinkedIn  : {linkedin}
GitHub    : {github}
Portfolio : {portfolio}

== HOW TO BEHAVE ==
- Be friendly, warm and professional
- Keep answers to 3-5 lines — don't overwhelm
- When asked about projects, mention the research papers too — they are impressive
- For salary always say: "{salary}"
- If asked something not listed here say:
  "I don't have that specific detail — reach {name} directly at {email}"
- If a recruiter shows interest, encourage them to connect on LinkedIn
- Never make up information not listed above
- End every response with an offer to help further
"""

# ── CONVERSATION HISTORY ──────────────────────────────────────
conversation_history = [
    {'role': 'system', 'content': SYSTEM_PROMPT}
]


# ── CHAT FUNCTION ─────────────────────────────────────────────
def chat(user_message):
    conversation_history.append({
        'role': 'user',
        'content': user_message
    })
    response = ollama.chat(
        model='llama3.2:3b',
        messages=conversation_history
    )
    ai_reply = response.message.content
    conversation_history.append({
        'role': 'assistant',
        'content': ai_reply
    })
    return ai_reply


# ── MAIN LOOP ─────────────────────────────────────────────────
print("=" * 50)
print(f"  {name} — Portfolio Assistant")
print("  Ask me anything! Type 'quit' to exit.")
print("=" * 50)
print()

opening = chat("Introduce yourself in 2 friendly lines")
print(f"Bot: {opening}\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == 'quit':
        print(f"Thanks for your interest! Reach out to {name} anytime.")
        break
    reply = chat(user_input)
    print(f"\nBot: {reply}\n")