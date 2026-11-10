from helpers import L, LM, opt, env_names

Q = [
    {"id": "who", "type": "choice", "prompt": "Who’s filling this out?",
     "options": [opt("student", "The student"), opt("parent", "A parent / guardian"), opt("adult", "An adult returning to school"), opt("mentor", "A mentor or counselor")]},
    {"id": "path", "type": "choice", "prompt": "What kind of program?",
     "options": [opt("four", "4-year college / university"), opt("cc", "Community college / transfer"), opt("trade", "Trade / vocational program"), opt("mixed", "Still comparing options")]},
    {"id": "term", "type": "choice", "prompt": "When do you hope to start?",
     "options": [opt("6", "Within 6 months"), opt("12", "6–12 months"), opt("18", "12–18 months"), opt("24", "More than 18 months")]},
    {"id": "count", "type": "choice", "prompt": "How many programs are you applying to?",
     "options": [opt("1_3", "1–3"), opt("4_7", "4–7"), opt("8", "8+"), opt("unsure", "Not sure yet")]},
    {"id": "essay", "type": "choice", "prompt": "Where are you on essays or personal statements?",
     "options": [opt("none", "Haven’t started"), opt("ideas", "Have ideas"), opt("draft", "Have a draft"), opt("na", "Not required for my programs")]},
    {"id": "tests", "type": "choice", "prompt": "Any tests or placement exams in your plan?",
     "options": [opt("yes", "Yes, still to take"), opt("done", "Already done"), opt("optional", "Test-optional / not required"), opt("unsure", "Not sure")]},
    {"id": "aid", "type": "choice", "prompt": "Will you apply for financial aid or scholarships?",
     "options": [opt("yes", "Yes"), opt("maybe", "Maybe"), opt("no", "No")]},
    {"id": "recs", "type": "choice", "prompt": "Do you know who’ll write recommendations (if needed)?",
     "options": [opt("yes", "Yes, already asked"), opt("know", "I know who — haven’t asked"), opt("no", "Not yet"), opt("na", "Not required")]},
    {"id": "hours", "type": "choice", "prompt": "Hours per week available for applications?",
     "options": [opt("1", "1–2"), opt("3", "3–5"), opt("6", "6+")]},
    {"id": "worry", "type": "choice", "prompt": "What worries you most?",
     "options": [opt("deadlines", "Missing deadlines"), opt("essay", "The essay"), opt("money", "Paying for it"), opt("choosing", "Choosing where to apply")]},
]


def plan(a):
    months = int(a.get("term", "12"))
    path = L(Q[1]["options"], a.get("path"))
    tasks = ["Make one deadline sheet: each program, its deadline, required items, and portal login (store passwords safely).",
             "Check each program’s official website for current requirements — they change yearly."]
    if a.get("aid") in ("yes", "maybe"):
        tasks.append("Note the FAFSA/state aid opening dates on studentaid.gov and your state’s aid site; add them to the sheet.")
    if a.get("recs") in ("know", "no"):
        tasks.append("Ask recommenders at least 4–6 weeks before your earliest deadline, with a one-page brag sheet.")
    essay = {"none": "Week 1–2: brainstorm 3 true stories; pick one.", "ideas": "Week 1: outline your strongest idea in 5 bullets.", "draft": "Week 1: get one trusted reader’s feedback; revise for clarity.", "na": "Skip essays; use the time for program research."}[a.get("essay", "none")]
    return {
        "title": f"Applyward timeline — {path}, starting in ~{months} months",
        "summary": f"Applying to {L(Q[3]['options'], a.get('count')).lower()} programs with {L(Q[8]['options'], a.get('hours')).lower()} hours/week. Biggest worry: {L(Q[9]['options'], a.get('worry')).lower()}. Applyward is an organizing tool — it can’t guarantee admission, aid, or scholarships.",
        "preview_sections": [
            {"title": "Start here (unlocked)", "bullets": tasks},
            {"title": "Essay sprint", "bullets": [essay, "Write in your own voice — admissions offices want you, not a ghostwriter.", "Leave 1 week buffer before the first deadline."]},
            {"title": "Official sources first", "body": "Always confirm deadlines and requirements on each school’s official site and studentaid.gov. Applyward isn’t a counselor and doesn’t predict admission chances."},
        ],
        "locked_sections": [
            {"title": "Week-by-week countdown", "teaser": "Every task from now until your last deadline."},
            {"title": "Recommendation ask scripts", "teaser": "Polite emails + brag-sheet template."},
            {"title": "Aid & scholarship tracker", "teaser": "Organizes dates and documents — not financial advice."},
            {"title": "Parent / mentor check-in guide", "teaser": "15-minute weekly check-ins that don’t become nagging."},
        ],
    }


BRAND = {
    "name": "Applyward", "slug": "applyward", "port": 5110,
    "tagline": "A week-by-week application timeline for college and trade-school applicants.",
    "eyebrow": "College · community college · trade school",
    "hero_title": "Every deadline, essay, and form — on one calm timeline.",
    "hero_lede": "Answer 10 questions about your programs, start date, and where you are now. Applyward builds a weekly plan so nothing sneaks up on you.",
    "cta_primary": "Build my application timeline", "cta_short": "Start quiz",
    "cta_band_title": "Less 3 a.m. panic. More steady progress.",
    "cta_band_text": "A weekly plan for students, parents, and returning adults.",
    "honesty_line": "Organizing help only. No admission, aid, or scholarship guarantees.",
    "audience_line": "Students, parents, and adults returning to school who want a clear weekly plan for applications and aid forms.",
    "personas": [
        {"title": "First-gen student", "text": "Nobody at home has done this before — you want the steps."},
        {"title": "Busy parent", "text": "You want to help without hovering."},
        {"title": "Career changer", "text": "Heading to a trade or community college program as an adult."},
    ],
    "journey": [
        {"stage": "Choose", "pain": "Too many options, no shortlist.", "fix": "A simple research sheet per program."},
        {"stage": "Organize", "pain": "Deadlines live in 6 browser tabs.", "fix": "One deadline sheet and weekly tasks."},
        {"stage": "Write", "pain": "The essay feels impossible.", "fix": "A small-steps essay sprint in your own voice."},
        {"stage": "Submit & fund", "pain": "Aid forms and recs come last-minute.", "fix": "Early reminders tied to official dates."},
    ],
    "how_steps": [
        {"title": "Quiz your situation", "text": "Program type, start date, essays, aid, and hours."},
        {"title": "Preview your timeline", "text": "First tasks and essay sprint unlocked."},
        {"title": "Join the founding list", "text": "No charge today — we’ll email when checkout opens."},
    ],
    "features": [
        {"title": "Weekly countdown", "text": "Tasks sized to your available hours."},
        {"title": "Essay sprint", "text": "Brainstorm → outline → draft → revise."},
        {"title": "Rec-letter scripts", "text": "Respectful asks with a brag sheet."},
        {"title": "Term-based plans", "text": "Fixed 12- or 24-week terms during application season."},
    ],
    "sample_peek": ["One deadline sheet", "Recommender ask 4–6 weeks out", "Aid opening dates noted", "1-week buffer before deadline"],
    "trust_points": [
        {"title": "No admission promises", "text": "Nobody can honestly guarantee acceptance — we don’t."},
        {"title": "Your voice, your essay", "text": "We coach process; we don’t write essays for you."},
        {"title": "Official sources", "text": "We point to school sites and studentaid.gov."},
    ],
    "faq": [
        {"q": "Can Applyward get me into my top school?", "a": "No one can guarantee admission. Applyward helps you stay organized and on time."},
        {"q": "Do you write essays?", "a": "No. We give a step-by-step process so the essay stays yours."},
        {"q": "Is this financial-aid advice?", "a": "No. We remind you of official dates and documents; aid offices answer the rest."},
    ],
    "pricing": [
        {"id": "12w", "name": "12-week season", "intro": "$29", "period": "12 weeks", "renewal": "$29 / 12 weeks", "renewal_note": "Ends after the term — no auto-renewal. Continue at $29 / 12 weeks only if you choose to.", "includes": ["Weekly countdown", "Essay sprint", "Rec-letter scripts"]},
        {"id": "24w", "name": "24-week full cycle", "intro": "$49", "period": "24 weeks", "renewal": "$29 / 12 weeks", "renewal_note": "Ends after the term — no auto-renewal. Continue at $29 / 12 weeks only if you choose to.", "featured": True, "includes": ["Everything in 12-week", "Aid & scholarship tracker", "Parent / mentor guide"]},
    ],
    "disclaimer_short": "Organizing help only. Not admissions counseling or financial advice. No admission, aid, or scholarship guarantees.",
    "disclaimer_long": "Applyward provides general application-organizing tools and education. It is not affiliated with any school, testing agency, or government aid program, does not guarantee admission, financial aid, or scholarships, and is not professional admissions counseling, legal, or financial advice. Always confirm requirements and deadlines with official sources. Users under 13 should not use this site. No payments are processed on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&family=Atkinson+Hyperlegible:wght@400;700&display=swap",
    "fonts": ("Lexend", "Atkinson Hyperlegible"),
    "questions": Q, "generate_plan": plan,
    "voice": "Supportive older sibling: clear steps, zero judgment, honest about what nobody can promise.",
    "palette": {"Background": "#F7F7FC", "Alt": "#ECECF8", "Card": "#FFFFFF", "Ink": "#1B1E3C", "Muted": "#5A5E80", "Accent (indigo)": "#4338CA", "Accent hover": "#3730A3", "Highlight (mint)": "#34D399"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="14" fill="#4338CA"/><path d="M16 44 32 18l16 26" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M23 35h18" stroke="#34D399" stroke-width="4.5" stroke-linecap="round"/></svg>',
    "css_vars": """
  --bg:#F7F7FC;--bg-alt:#ECECF8;--card:#FFFFFF;--ink:#1B1E3C;--muted:#5A5E80;--line:#DADBEE;
  --accent:#4338CA;--accent-2:#3730A3;--on-accent:#FFFFFF;--hi:#34D399;--radius:12px;
  --font-display:'Lexend', system-ui, sans-serif;--font-body:'Atkinson Hyperlegible', system-ui, sans-serif;
  --shadow-card:0 14px 34px rgba(67,56,202,.10);--shadow-btn:0 8px 18px rgba(67,56,202,.28);
  --cta-band-bg:#1B1E3C;--cta-band-ink:#F7F7FC;--cta-band-btn:#34D399;--cta-band-btn-ink:#0B2A1F;--tracking:-0.02em;
""",
    "personality": "background:linear-gradient(160deg,#E6E5FB 0%, var(--bg) 55%);",
    "extra_css": ".journey-step{background:var(--hi);color:#0B2A1F}.progress{height:.55rem}",
    "dos": ["Use readable, accessible type (Atkinson Hyperlegible).", "Speak to students and parents with equal respect."],
    "donts": ["Imply admission odds or guarantee acceptance, aid, or scholarships.", "Offer to write essays."],
}
BRAND.update(env_names("applyward"))
