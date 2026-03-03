<div align="center">

# 🔬 Scholar-Agent Pro

### AI-Powered Research Paper Analysis Tool

![Python](https://img.shields.io/badge/Python-3.10+-3b82f6?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-06b6d4?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)
![Free](https://img.shields.io/badge/Cost-100%25_Free-f59e0b?style=for-the-badge)

**Stop spending hours reading research papers. Let AI do it in seconds.**

[🚀 Live Demo](#) · [📖 How to Use](#how-to-use) · [⚙️ Local Setup](#local-setup)

</div>

---

## ✨ What is Scholar-Agent Pro?

Scholar-Agent Pro is an AI-powered research assistant that analyzes any academic PDF in seconds.
Upload a paper, click an agent, get instant insights.

Built as a 2nd-year engineering project using Groq LLaMA 3.3 70B + Streamlit.

---

## 🤖 12 Agents

| Agent | Description |
|-------|-------------|
| 📋 Executive Summary | 3-sentence: Problem → Method → Result |
| 📚 Section Summarizer | Each section summarized separately |
| 🧒 ELI15 Mode | Explained like you're 15 years old |
| 🔑 Keyword + Glossary | Top terms + plain English definitions |
| 💡 Claims Highlighter | Strong claims vs admitted limitations |
| 📊 Keyword Chart | Interactive Plotly bar chart |
| ☁️ Word Cloud | Visual frequency map |
| 🧠 Difficulty Score | Complexity rated 1-10 |
| ⏱️ Reading Time | Minutes saved counter |
| ∑ Math Extractor | LaTeX equation rendering |
| 🔍 Critical Audit | Adversarial peer review |
| 🔗 Citation Linker | One-click Google Scholar |

---

## ⚙️ Local Setup
```bash
git clone https://github.com/YOUR_USERNAME/scholar-agent-pro.git
cd scholar-agent-pro
pip install -r requirements.txt
streamlit run scholar_agent.py
```

Get a free Groq API key at https://console.groq.com

---

## 📦 Tech Stack

| Tech | Purpose |
|------|---------|
| Streamlit | Web UI |
| Groq API | LLaMA 3.3 70B (free) |
| PyMuPDF | PDF extraction |
| Plotly | Interactive charts |
| WordCloud | Visual mapping |

---

<div align="center">
Built with ❤️ using Streamlit + Groq + Python
</div>
