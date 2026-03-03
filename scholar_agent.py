import streamlit as st
import fitz
from groq import Groq
import urllib.parse
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter
import plotly.express as px

try:
    from wordcloud import WordCloud
    WC_AVAILABLE = True
except ImportError:
    WC_AVAILABLE = False

st.set_page_config(page_title="Scholar-Agent Pro", page_icon="🔬", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;600;700&display=swap');
:root{--bg-deep:#0a0e1a;--bg-card:#111827;--bg-panel:#1a2235;--border:#1e2d45;--accent:#3b82f6;--accent2:#06b6d4;--text-main:#e2e8f0;--text-muted:#64748b;--success:#10b981;--warning:#f59e0b;--danger:#ef4444;}
html,body,[data-testid="stAppViewContainer"]{background:var(--bg-deep)!important;font-family:'Inter',sans-serif;color:var(--text-main);}
[data-testid="stSidebar"]{background:var(--bg-card)!important;border-right:1px solid var(--border);}
.hero-header{text-align:center;padding:2.5rem 0 1.5rem;border-bottom:1px solid var(--border);margin-bottom:2rem;}
.hero-header h1{font-size:2.8rem;font-weight:700;background:linear-gradient(135deg,#3b82f6,#06b6d4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0;}
.hero-header p{color:var(--text-muted);font-size:1rem;margin-top:0.5rem;}
.agent-card{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem;position:relative;overflow:hidden;}
.agent-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));}
.agent-card h3{color:var(--accent2);font-family:'JetBrains Mono',monospace;font-size:0.85rem;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:1rem;}
.stButton>button{background:linear-gradient(135deg,#1e3a5f,#1e4d7b)!important;color:#93c5fd!important;border:1px solid #2563eb!important;border-radius:8px!important;font-family:'JetBrains Mono',monospace!important;font-size:0.82rem!important;font-weight:600!important;}
.stButton>button:hover{background:linear-gradient(135deg,#2563eb,#0891b2)!important;color:#fff!important;box-shadow:0 0 20px rgba(59,130,246,0.3)!important;}
.stTextInput>div>div>input,.stTextArea>div>div>textarea{background:var(--bg-panel)!important;border:1px solid var(--border)!important;border-radius:8px!important;color:var(--text-main)!important;}
[data-testid="stFileUploader"]{background:var(--bg-panel)!important;border:2px dashed var(--border)!important;border-radius:12px!important;padding:1rem!important;}
.stLatex{background:var(--bg-panel)!important;border:1px solid var(--border)!important;border-radius:8px!important;padding:1rem!important;margin:0.5rem 0!important;}
.chip{display:inline-block;background:var(--bg-panel);border:1px solid var(--border);border-radius:20px;padding:0.2rem 0.75rem;font-size:0.78rem;color:var(--text-muted);margin:0.2rem;font-family:'JetBrains Mono',monospace;}
.chip-accent{border-color:var(--accent);color:var(--accent2);}
.chip-success{border-color:#10b981;color:#10b981;}
.chip-warn{border-color:#f59e0b;color:#f59e0b;}
.chip-danger{border-color:#ef4444;color:#ef4444;}
.sidebar-label{font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--text-muted);letter-spacing:0.08em;text-transform:uppercase;}
.section-header{font-size:1.3rem;font-weight:700;color:var(--accent2);margin:2rem 0 1rem;padding-bottom:0.5rem;border-bottom:1px solid var(--border);font-family:'JetBrains Mono',monospace;}
.highlight-claim{background:rgba(59,130,246,0.12);border-left:3px solid var(--accent);padding:0.5rem 1rem;margin:0.4rem 0;border-radius:0 8px 8px 0;font-size:0.9rem;}
.highlight-limit{background:rgba(239,68,68,0.10);border-left:3px solid #ef4444;padding:0.5rem 1rem;margin:0.4rem 0;border-radius:0 8px 8px 0;font-size:0.9rem;}
.glossary-term{background:var(--bg-panel);border:1px solid var(--border);border-radius:8px;padding:0.75rem 1rem;margin:0.4rem 0;}
.glossary-term b{color:var(--accent2);}
.diff-bar-wrap{background:var(--bg-panel);border-radius:8px;height:18px;overflow:hidden;margin:0.5rem 0;}
.diff-bar{height:18px;border-radius:8px;}
::-webkit-scrollbar{width:6px;}::-webkit-scrollbar-track{background:var(--bg-deep);}::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}
</style>
<div class="hero-header">
  <h1>🔬 Scholar-Agent Pro</h1>
  <p>Your AI research assistant · Powered by Groq · 12 Agents · 100% Free</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="sidebar-label">Groq API Key</p>', unsafe_allow_html=True)
    api_key = st.text_input("api_key", placeholder="gsk_...", type="password", label_visibility="collapsed")
    if api_key:
        st.success("✅ Groq Key Ready")
    else:
        st.info("Free key → [console.groq.com](https://console.groq.com)")
    st.markdown("---")
    st.markdown('<p class="sidebar-label">Model</p>', unsafe_allow_html=True)
    model_name = st.selectbox("model", options=[
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
    ], index=0, label_visibility="collapsed")
    st.markdown("---")
    st.markdown("""<div style='font-size:0.75rem;color:#64748b;'>
    <b style='color:#06b6d4;'>Model Guide:</b><br>
    🧠 <b>llama-3.3-70b</b> — Most accurate<br>
    ⚡ <b>llama-3.1-8b</b> — Fastest<br>
    🔀 <b>mixtral-8x7b</b> — Balanced<br>
    💎 <b>gemma2-9b</b> — Google model
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    max_chars = st.slider("Max chars to AI", 5000, 40000, 15000, 1000)
    st.caption("Scholar-Agent Pro v3.0")

STOPWORDS = set(["the","a","an","and","or","but","in","on","at","to","for","of","with","is","are","was","were","be","been","being","have","has","had","do","does","did","will","would","could","should","may","might","shall","can","this","that","these","those","it","its","we","our","their","they","he","she","i","you","by","as","from","into","about","which","who","what","when","where","how","not","no","so","if","than","then","also","each","such","more","other","all","both","between","through","during","while","paper","study","research","using","used","use","results","based","proposed","show","shows","shown","two","one","new","model","data","method","approach","figure","table","al","et","however","thus","therefore","hence","whereas","although"])

def extract_text_from_pdf(uploaded_file):
    try:
        file_bytes = uploaded_file.read()
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        pages_text = []
        for page in doc:
            try:
                text = page.get_text("text")
                text = text.encode("utf-8", errors="replace").decode("utf-8")
                pages_text.append(text)
            except Exception:
                pages_text.append("")
        doc.close()
        return "\n".join(pages_text).strip()
    except Exception as e:
        st.error(f"PDF read error: {e}")
        return ""

def call_groq(prompt, max_tokens=1024):
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        error_msg = str(e)
        if "invalid_api_key" in error_msg.lower() or "401" in error_msg:
            return "ERROR_APIKEY"
        if "rate_limit" in error_msg.lower() or "429" in error_msg:
            return "ERROR_QUOTA"
        return f"ERROR: {error_msg}"

def handle_error(result):
    if result == "ERROR_APIKEY":
        st.error("❌ Invalid Groq API Key → [console.groq.com](https://console.groq.com)")
        return True
    if result == "ERROR_QUOTA":
        st.warning("⚠️ Rate limit — wait 10 seconds and retry!")
        return True
    if result.startswith("ERROR:"):
        st.error(f"❌ {result}")
        return True
    return False

def extract_title(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    for line in lines[:15]:
        if 10 < len(line) < 200 and not re.match(r'^[\d\s\W]+$', line):
            return line
    return lines[0] if lines else "Unknown Title"

def get_top_keywords(text, n=20):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    filtered = [w for w in words if w not in STOPWORDS]
    return Counter(filtered).most_common(n)

def estimate_reading_time(text):
    words = len(text.split())
    full_min = round(words / 250)
    saved = max(0, full_min - 2)
    return {"words": words, "full_min": full_min, "ai_min": 2, "saved": saved}

uploaded_file = st.file_uploader("📄 Upload a Research Paper (PDF)", type=["pdf"])

if not uploaded_file:
    st.markdown("""
    <div class="agent-card" style="text-align:center;padding:3rem;">
      <h3>12 AGENTS READY</h3>
      <p style="color:#94a3b8;font-size:1rem;">Upload any research PDF — let AI do all the heavy reading</p><br>
      <span class="chip chip-accent">📋 Summary</span><span class="chip chip-accent">📚 Sections</span>
      <span class="chip chip-accent">🧒 ELI15</span><span class="chip chip-accent">🔑 Keywords</span>
      <span class="chip chip-accent">💡 Claims</span><span class="chip chip-accent">📊 Charts</span>
      <span class="chip chip-accent">☁️ WordCloud</span><span class="chip chip-accent">🧠 Difficulty</span>
      <span class="chip chip-accent">∑ Math</span><span class="chip chip-accent">🔍 Audit</span>
      <br><br>
      <p style="color:#64748b;font-size:0.85rem;">⚡ Groq LLaMA 3.3 70B · Responses under 3 seconds</p>
    </div>""", unsafe_allow_html=True)
    st.stop()

if not api_key:
    st.warning("⚠️ Paste your Groq API Key in the sidebar.")
    st.stop()

with st.spinner("📖 Reading PDF..."):
    paper_text = extract_text_from_pdf(uploaded_file)

if not paper_text:
    st.error("❌ Could not extract text. Try a different PDF.")
    st.stop()

paper_title = extract_title(paper_text)
rt = estimate_reading_time(paper_text)
top_kw = get_top_keywords(paper_text, 20)

st.markdown(f"""
<div class="agent-card">
  <h3>📄 Paper Loaded</h3>
  <p style="color:#e2e8f0;font-size:1.05rem;margin-bottom:1rem;"><strong>{paper_title}</strong></p>
  <span class="chip">~{rt['words']:,} words</span>
  <span class="chip">~{rt['full_min']} min to read manually</span>
  <span class="chip chip-success">⚡ We save you ~{rt['saved']} minutes</span>
  <span class="chip chip-accent">Groq Ready</span>
</div>""", unsafe_allow_html=True)

with st.expander("👁️ View raw extracted text"):
    st.text_area("Raw", paper_text[:5000] + ("..." if len(paper_text) > 5000 else ""), height=200)

st.markdown("---")
c1,c2,c3,c4 = st.columns(4)
c1.metric("📄 Total Words", f"{rt['words']:,}")
c2.metric("🕐 Manual Read", f"{rt['full_min']} min")
c3.metric("⚡ With AI", f"{rt['ai_min']} min")
c4.metric("✅ Time Saved", f"{rt['saved']} min", delta=f"-{round(rt['saved']/max(rt['full_min'],1)*100)}%")

st.markdown('<p class="section-header">📊 Visual Intelligence (Instant)</p>', unsafe_allow_html=True)
vc1, vc2 = st.columns(2)

with vc1:
    st.markdown('<div class="agent-card"><h3>📊 Keyword Frequency Chart</h3>', unsafe_allow_html=True)
    if top_kw:
        words_list = [w for w, _ in top_kw[:15]]
        counts_list = [c for _, c in top_kw[:15]]
        fig = px.bar(x=counts_list, y=words_list, orientation='h',
            color=counts_list, color_continuous_scale=["#1e3a5f","#3b82f6","#06b6d4"],
            labels={"x":"Frequency","y":"Keyword"})
        fig.update_layout(paper_bgcolor="#111827", plot_bgcolor="#1a2235",
            font=dict(color="#e2e8f0",family="JetBrains Mono"),
            coloraxis_showscale=False, margin=dict(l=10,r=10,t=10,b=10), height=380,
            yaxis=dict(autorange="reversed"))
        fig.update_xaxes(gridcolor="#1e2d45")
        fig.update_yaxes(gridcolor="#1e2d45")
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with vc2:
    st.markdown('<div class="agent-card"><h3>☁️ Word Cloud</h3>', unsafe_allow_html=True)
    if WC_AVAILABLE:
        try:
            clean_text = " ".join([w for w in re.findall(r'\b[a-zA-Z]{4,}\b', paper_text.lower()) if w not in STOPWORDS])
            wc = WordCloud(width=700, height=380, background_color="#111827",
                colormap="cool", max_words=80, prefer_horizontal=0.8).generate(clean_text)
            fig_wc, ax = plt.subplots(figsize=(7,3.8))
            fig_wc.patch.set_facecolor("#111827")
            ax.set_facecolor("#111827")
            ax.imshow(wc, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig_wc)
            plt.close(fig_wc)
        except Exception as e:
            st.info(f"Word cloud error: {e}")
    else:
        st.info("Run: pip install wordcloud")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<p class="section-header">🧠 Difficulty Score</p>', unsafe_allow_html=True)
st.markdown('<div class="agent-card"><h3>🧠 Difficulty Analysis</h3>', unsafe_allow_html=True)
hard_words = ["furthermore","methodology","hypothesis","algorithm","parameter","optimization","inference","empirical","theoretical","probabilistic","quantitative","qualitative","regression","correlation","variance","neural","gradient","convergence","heterogeneous","stochastic"]
all_words_list = re.findall(r'\b[a-zA-Z]+\b', paper_text.lower())
total_w = max(len(all_words_list), 1)
hard_count = sum(1 for w in all_words_list if w in hard_words)
sents = [s for s in paper_text.split('.') if s.strip()]
avg_sent_len = sum(len(s.split()) for s in sents) / max(len(sents), 1)
score = max(1, min(10, round((hard_count / total_w) * 800 + avg_sent_len * 0.15)))
if score <= 3: level, color, cc = "Beginner Friendly", "#10b981", "chip-success"
elif score <= 6: level, color, cc = "Intermediate", "#f59e0b", "chip-warn"
else: level, color, cc = "Advanced / Expert", "#ef4444", "chip-danger"
dc1, dc2 = st.columns([1,2])
with dc1:
    st.markdown(f'<div style="text-align:center;padding:1rem;"><div style="font-size:4rem;font-weight:900;color:{color};font-family:JetBrains Mono,monospace;">{score}/10</div><span class="chip {cc}">{level}</span></div>', unsafe_allow_html=True)
with dc2:
    st.markdown(f'<p style="color:#64748b;font-size:0.85rem;">Difficulty level</p><div class="diff-bar-wrap"><div class="diff-bar" style="width:{score*10}%;background:linear-gradient(90deg,#3b82f6,{color});"></div></div><p style="color:#94a3b8;font-size:0.85rem;margin-top:0.8rem;">📏 Avg sentence: <b>{avg_sent_len:.1f} words</b><br>🔬 Technical terms: <b>{hard_count}</b><br>📖 {"Start with Abstract + Conclusion first." if score > 6 else "Go section by section." if score > 3 else "Easy read — go straight through!"}</p>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<p class="section-header">🤖 AI Agents</p>', unsafe_allow_html=True)

a1, a2 = st.columns(2)
with a1:
    if st.button("📋 Executive Summary", use_container_width=True):
        with st.spinner("Analyzing..."):
            result = call_groq(f"Give EXACTLY 3 sentences:\nSentence 1 — THE PROBLEM:\nSentence 2 — THE METHODOLOGY:\nSentence 3 — THE KEY RESULT:\nNo bullets.\nPAPER: {paper_text[:max_chars]}")
        if not handle_error(result):
            st.markdown('<div class="agent-card"><h3>📋 Executive Summary</h3>', unsafe_allow_html=True)
            sentences = [s.strip() for s in result.strip().split("\n") if s.strip()]
            labels = ["🔴 THE PROBLEM","🔵 THE METHODOLOGY","🟢 THE KEY RESULT"]
            for i, s in enumerate(sentences[:3]):
                st.markdown(f"**{labels[i] if i<3 else f'#{i+1}'}**")
                st.markdown(f"> {s}")
            st.markdown("</div>", unsafe_allow_html=True)

with a2:
    if st.button("🧒 ELI15 Mode", use_container_width=True):
        with st.spinner("Simplifying..."):
            result = call_groq(f"Explain to a 15-year-old. Simple words.\n1. What problem?\n2. How solved?\n3. What found?\n4. Real life impact?\nPAPER: {paper_text[:max_chars]}", max_tokens=1200)
        if not handle_error(result):
            st.markdown('<div class="agent-card"><h3>🧒 ELI15</h3>', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown("</div>", unsafe_allow_html=True)

if st.button("📚 Section Summarizer", use_container_width=True):
    with st.spinner("Summarizing sections..."):
        result = call_groq(f"Summarize each section 2-3 sentences. Headers:\n**ABSTRACT:**\n**INTRODUCTION:**\n**METHODOLOGY:**\n**RESULTS:**\n**DISCUSSION:**\n**CONCLUSION:**\nPAPER: {paper_text[:max_chars]}", max_tokens=1500)
    if not handle_error(result):
        st.markdown('<div class="agent-card"><h3>📚 Section Summary</h3>', unsafe_allow_html=True)
        st.markdown(result)
        st.markdown("</div>", unsafe_allow_html=True)

if st.button("🔑 Keywords + Glossary", use_container_width=True):
    with st.spinner("Building glossary..."):
        result = call_groq(f"1. TOP 10 KEYWORDS: KEYWORD: why it matters\n2. GLOSSARY 8 terms: TERM | plain English\nSeparate with ---\nPAPER: {paper_text[:max_chars]}", max_tokens=1200)
    if not handle_error(result):
        st.markdown('<div class="agent-card"><h3>🔑 Keywords + Glossary</h3>', unsafe_allow_html=True)
        parts = result.split("---")
        if len(parts) >= 2:
            st.markdown("**🏷️ Keywords**")
            for line in parts[0].strip().split("\n"):
                if line.strip() and ":" in line:
                    term, desc = line.split(":", 1)
                    st.markdown(f'<div class="glossary-term"><b>{term.strip()}</b>: {desc.strip()}</div>', unsafe_allow_html=True)
            st.markdown("**📖 Glossary**")
            for line in parts[1].strip().split("\n"):
                if "|" in line:
                    term, defn = line.split("|", 1)
                    st.markdown(f'<div class="glossary-term"><b>{term.strip()}</b> — {defn.strip()}</div>', unsafe_allow_html=True)
        else:
            st.markdown(result)
        st.markdown("</div>", unsafe_allow_html=True)

if st.button("💡 Claims & Limitations", use_container_width=True):
    with st.spinner("Highlighting..."):
        result = call_groq(f"STRONG CLAIMS: 4-6, start with [CLAIM]\nLIMITATIONS: 3-5, start with [LIMIT]\nPAPER: {paper_text[:max_chars]}", max_tokens=1000)
    if not handle_error(result):
        st.markdown('<div class="agent-card"><h3>💡 Claims & Limitations</h3>', unsafe_allow_html=True)
        for line in result.strip().split("\n"):
            line = line.strip()
            if not line: continue
            if "[CLAIM]" in line:
                st.markdown(f'<div class="highlight-claim">✅ <b>CLAIM:</b> {line.replace("[CLAIM]","").strip()}</div>', unsafe_allow_html=True)
            elif "[LIMIT]" in line:
                st.markdown(f'<div class="highlight-limit">⚠️ <b>LIMIT:</b> {line.replace("[LIMIT]","").strip()}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='color:#94a3b8;font-size:0.9rem;'>{line}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

b1, b2 = st.columns(2)
with b1:
    if st.button("∑ Math Extraction", use_container_width=True):
        with st.spinner("Hunting equations..."):
            result = call_groq(f"Extract ALL math equations. Raw LaTeX only, one per line, no $ delimiters. If none: NO_EQUATIONS_FOUND\nPAPER: {paper_text[:max_chars]}")
        if not handle_error(result):
            st.markdown('<div class="agent-card"><h3>∑ Equations</h3>', unsafe_allow_html=True)
            if "NO_EQUATIONS_FOUND" in result:
                st.info("No equations found.")
            else:
                equations = [l.strip() for l in result.strip().split("\n") if l.strip()]
                for i, eq in enumerate(equations, 1):
                    st.markdown(f"**Eq {i}**")
                    try: st.latex(eq)
                    except: st.code(eq, language="latex")
            st.markdown("</div>", unsafe_allow_html=True)

with b2:
    if st.button("🔍 Critical Audit", use_container_width=True):
        with st.spinner("Peer-reviewing..."):
            result = call_groq(f"Top journal peer reviewer. List 3-5 weaknesses numbered. Be blunt.\nPAPER: {paper_text[:max_chars]}")
        if not handle_error(result):
            st.markdown('<div class="agent-card"><h3>🔍 Critical Audit</h3>', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
cc1, cc2 = st.columns([3,1])
with cc1:
    custom_title = st.text_input("📚 Title for citation search:", value=paper_title)
with cc2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔗 Google Scholar", use_container_width=True):
        url = f"https://scholar.google.com/scholar?q={urllib.parse.quote(custom_title)}"
        st.markdown(f'<a href="{url}" target="_blank" style="display:block;text-align:center;background:linear-gradient(135deg,#1e3a5f,#1e4d7b);color:#93c5fd;border:1px solid #2563eb;border-radius:8px;padding:0.6rem 1rem;font-family:monospace;font-size:0.82rem;text-decoration:none;">🔗 Open Scholar →</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Scholar-Agent Pro v3.0 · Groq Edition · Free forever · No data stored · Built with ❤️")
