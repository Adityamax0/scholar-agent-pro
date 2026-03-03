<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Scholar-Agent%20Pro&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=AI-Powered%20Research%20Paper%20Analysis&descAlignY=55&descSize=18" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=22&duration=3000&pause=1000&color=06B6D4&center=true&vCenter=true&multiline=true&width=600&height=80&lines=Stop+reading+papers.+Start+understanding+them.;12+AI+Agents.+1+Upload.+Instant+Insights.)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3b82f6?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-06b6d4?style=for-the-badge&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.24+-10b981?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)
![Cost](https://img.shields.io/badge/Cost-100%25_Free-ef4444?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live_&_Active-10b981?style=for-the-badge)

<br/>

### 🌐 [**→ Open Live App ←**]([https://your-app.streamlit.app](https://scholar-agent-pro-fzwaxyhzrsr5hmumbfynd3.streamlit.app/))

*Works on any device — phone, tablet, laptop. No installation needed.*

<br/>

</div>

---

## 🧠 The Problem I Solved

> Every engineering and science student wastes **3-5 hours** per research paper — reading dense jargon, hunting for equations, trying to understand methodology. Multiply that by 10 papers per semester. That's **50 hours wasted** per student per year.

**Scholar-Agent Pro eliminates that.**

Upload any academic PDF. In under **10 seconds**, 12 specialized AI agents break it down completely — from a 3-sentence executive brief to adversarial peer review, LaTeX equation extraction, keyword glossaries, and visual word maps.

This isn't just a summarizer. It's a **full research intelligence pipeline** built by a 2nd-year engineering student using production-grade tools.

---

## ✨ Feature Showcase

<div align="center">

### ⚡ Instant Features (Zero AI calls — pure computation)

</div>

| Feature | What it does | Tech used |
|---------|-------------|-----------|
| 📊 **Keyword Frequency Chart** | Interactive horizontal bar chart of top 15 terms | Plotly |
| ☁️ **Word Cloud** | Visual frequency map of the entire paper | WordCloud + Matplotlib |
| 🧠 **Difficulty Score** | Rates paper complexity 1-10 using sentence length + technical term density | Custom algorithm |
| ⏱️ **Reading Time Estimator** | Calculates exact minutes saved vs manual reading | Word count analysis |

<div align="center">

### 🤖 AI Agents (Powered by Groq LLaMA 3.3 70B)

</div>

| # | Agent | What it delivers |
|---|-------|-----------------|
| 1 | 📋 **Executive Summary** | Exactly 3 sentences: The Problem → The Method → The Key Result |
| 2 | 📚 **Section Summarizer** | Abstract, Introduction, Methodology, Results, Discussion, Conclusion — each in 2-3 sentences |
| 3 | 🧒 **ELI15 Mode** | Entire paper explained like you're 15 — zero jargon, real-world analogies |
| 4 | 🔑 **Keyword Extractor** | Top 10 critical terms + auto-generated plain-English glossary |
| 5 | 💡 **Claims Highlighter** | Color-coded: strong claims (blue) vs admitted limitations (red) |
| 6 | ∑ **Math Extractor** | Finds every equation and renders it in beautiful LaTeX |
| 7 | 🔍 **Critical Audit** | Adversarial peer review — 3-5 specific methodology weaknesses |
| 8 | 🔗 **Citation Linker** | One-click pre-filled Google Scholar search |

---

## 🏗️ Architecture & Technical Depth

```
┌─────────────────────────────────────────────────────────┐
│                    Scholar-Agent Pro                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   PDF Upload                                             │
│       │                                                  │
│       ▼                                                  │
│   PyMuPDF Engine ──► Text Extraction (UTF-8 safe)        │
│       │                                                  │
│       ├──► Instant Pipeline (no API)                     │
│       │         ├── Keyword Counter (Counter + regex)    │
│       │         ├── Plotly Bar Chart                     │
│       │         ├── WordCloud Generator                  │
│       │         ├── Difficulty Scorer (custom algo)      │
│       │         └── Reading Time Estimator               │
│       │                                                  │
│       └──► AI Pipeline (Groq API)                        │
│                 ├── Executive Summary Agent              │
│                 ├── Section Summarizer Agent             │
│                 ├── ELI15 Agent                          │
│                 ├── Keyword + Glossary Agent             │
│                 ├── Claims Highlighter Agent             │
│                 ├── Math Extractor Agent                 │
│                 └── Critical Audit Agent                 │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Why Groq over OpenAI/Gemini?**
- ⚡ **10x faster** inference than standard APIs
- 🆓 **Completely free** tier — 14,400 requests/day
- 🧠 **LLaMA 3.3 70B** — same accuracy as GPT-4 class models
- 🚫 **Zero rate limit issues** that plagued earlier versions

---

## 🛠️ Tech Stack Deep Dive

| Layer | Technology | Why I chose it |
|-------|-----------|----------------|
| **Frontend** | Streamlit 1.32+ | Rapid prototyping with Python-native UI |
| **AI Inference** | Groq API (LLaMA 3.3 70B) | Fastest free LLM inference available |
| **PDF Engine** | PyMuPDF (fitz) | Most robust PDF parser — handles encoding errors gracefully |
| **Charts** | Plotly Express | Interactive, dark-theme compatible |
| **Word Cloud** | WordCloud + Matplotlib | Visual term frequency mapping |
| **Styling** | Custom CSS (via st.markdown) | Full dark theme — midnight blue + slate grey palette |
| **Fonts** | JetBrains Mono + Inter | Professional monospace/sans-serif pairing |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Free Groq API key → [console.groq.com](https://console.groq.com) *(no credit card)*

### One-Command Setup

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/scholar-agent-pro.git
cd scholar-agent-pro

# Install
pip install -r requirements.txt

# Run
streamlit run scholar_agent.py
```

Open `http://localhost:8501` → paste Groq key in sidebar → upload any PDF → done.

### Requirements

```
streamlit>=1.32.0
groq>=0.9.0
PyMuPDF>=1.24.0
plotly>=5.18.0
matplotlib>=3.8.0
wordcloud>=1.9.0
```

---

## 📁 Project Structure

```
scholar-agent-pro/
│
├── 📄 scholar_agent.py        # Complete app — single file architecture
├── 📦 requirements.txt        # All dependencies
├── 📖 README.md               # This file
└── ⚙️  .streamlit/
    └── config.toml            # Dark theme configuration
```

> **Single-file architecture** — the entire 500+ line application lives in one clean, modular Python file. Every function is independently testable and clearly documented.

---

## 🔑 How to Get Your Free Groq API Key

```
1. Go to  →  console.groq.com
2. Sign in with Google (30 seconds)
3. Click "Create API Key"
4. Copy the  gsk_...  key
5. Paste it in the app sidebar
```

**Free tier limits:** 14,400 requests/day · 30 requests/minute · No credit card ever needed

---

## 💡 Design Decisions

**Why not use a pre-built UI component library?**
Every UI element — cards, chips, buttons, highlight blocks — is hand-crafted CSS. This gives complete control over the midnight blue / slate grey aesthetic and ensures nothing looks generic.

**Why modular agents instead of one big prompt?**
Each agent has one job. This means better accuracy, easier debugging, and the ability to run agents independently without wasting tokens.

**Why PyMuPDF over PyPDF2?**
PyPDF2 produces garbled text on most academic PDFs. PyMuPDF handles encoding errors gracefully and extracts clean UTF-8 text even from complex formatted papers.

---

## 🗺️ Roadmap

- [x] Executive Summary Agent
- [x] Section-by-Section Summarizer
- [x] ELI15 Mode
- [x] Keyword Extractor + Glossary
- [x] Claims & Limitations Highlighter
- [x] Interactive Keyword Chart
- [x] Word Cloud
- [x] Difficulty Score Algorithm
- [x] Reading Time Estimator
- [x] Math / LaTeX Extractor
- [x] Critical Audit Agent
- [x] Citation Linker
- [ ] Multi-paper comparison (upload 2 PDFs side by side)
- [ ] Export analysis as PDF report
- [ ] Chat with paper (Q&A mode)
- [ ] Citation network graph

---

## 👨‍💻 About the Developer

<div align="center">

**Aditya**
2nd Year Engineering Student · AI & Python Enthusiast

*Built Scholar-Agent Pro as a demonstration that students can build*
*production-grade AI tools without any budget or cloud infrastructure.*

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/YOUR_USERNAME)

</div>

---

## 📄 License

```
MIT License — free to use, modify, fork, and distribute.
If you use this project, a ⭐ star is appreciated!
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Built with ❤️ · Powered by Groq · Deployed on Streamlit Cloud**

*If this helped you, give it a ⭐ — it means a lot!*

</div>

