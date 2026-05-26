# 🧠 Enterprise AI Meeting Assistant

AI-powered enterprise meeting summarization and action-item extraction system built using Python, Streamlit, and Google Gemini API.

---

# 🚀 Overview

Enterprise meetings often generate lengthy discussions, action items, deployment decisions, blockers, and follow-up tasks.

This project automates the entire meeting analysis workflow using Large Language Models (LLMs).

The system can:

✅ Generate intelligent meeting summaries  
✅ Extract action items automatically  
✅ Detect decisions made during meetings  
✅ Identify blockers and risks  
✅ Generate professional meeting notes  
✅ Process uploaded `.txt` meeting transcripts  
✅ Provide enterprise-ready meeting intelligence

---

# ✨ Features

- 📝 AI-Powered Meeting Summarization
- 📌 Automatic Action Item Extraction
- ⚠️ Risk & Blocker Detection
- 📋 Decision Tracking
- 📂 `.txt` Transcript Upload Support
- 🧠 LLM-Based Enterprise Meeting Intelligence
- 💻 Interactive Streamlit UI
- ⚡ Real-Time AI Processing
- 🔄 Workflow-Friendly Output Structure

---

# 🏗️ Project Architecture

```text
Enterprise-AI-Meeting-Assistant/
│
├── .venv/
│
├── src/
│   ├── __init__.py
│   ├── llm_helper.py
│   └── meeting_engine.py
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Technologies Used

- Python 3.11
- Streamlit
- Google Gemini API
- Prompt Engineering
- Enterprise AI Workflows
- dotenv
- LLM Orchestration

---

# 🔄 Workflow Process

## 1️⃣ Meeting Transcript Input

Users can either:

- Paste meeting transcripts manually
- Upload `.txt` transcript files

### Example Transcript

```text
The finance team confirmed budget approval.
John will prepare deployment reports.
Sarah will coordinate testing activities.
Deployment scheduled for Friday.
Security approval is still pending.
```

---

## 2️⃣ AI Meeting Analysis

The LLM analyzes the transcript and generates:

- Meeting Summary
- Key Discussion Points
- Decisions Made
- Action Items
- Risks / Blockers
- Next Steps

---

## 3️⃣ Structured Enterprise Output

### Example Output

```text
Meeting Summary:
The meeting focused on deployment readiness and pending approvals.

Action Items:
- John: Prepare deployment reports
- Sarah: Coordinate testing activities

Risks:
- Security approval is still pending

Next Steps:
- Complete approval process before Friday deployment
```

---

# 🧠 AI Capabilities Demonstrated

- Meeting Intelligence
- Prompt Engineering
- Enterprise AI Automation
- LLM Workflow Orchestration
- Structured Output Generation
- AI-Powered Productivity Systems
- Enterprise Decision Tracking
- Action Item Extraction
- Risk Identification

---

# 📌 Key Engineering Features

## 🧩 Modular Architecture

The application follows modular AI engineering practices:

- `llm_helper.py`
  → Handles Gemini API communication

- `meeting_engine.py`
  → Handles enterprise meeting analysis logic

- `app.py`
  → Streamlit frontend interface

---

## ⚡ Prompt-Driven AI Analysis

The system uses structured prompts to ensure:

- Consistent formatting
- Enterprise-style outputs
- Action-oriented responses
- Business-ready summaries

---

## 📂 File Upload Support

Supports enterprise workflow simulation through:

```text
.txt transcript uploads
```

allowing scalable meeting processing workflows.

---

# 🖥️ Streamlit Interface

The UI provides:

✅ Transcript upload  
✅ Manual transcript entry  
✅ AI-generated meeting analysis  
✅ Professional enterprise output formatting

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Enterprise-AI-Meeting-Assistant.git
```

---

## Create Virtual Environment

```bash
py -3.11 -m venv .venv
```

---

## Activate Virtual Environment

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

## Run Streamlit UI

```bash
streamlit run app.py
```

---

## Run Local Python Test

```bash
python main.py
```

---

# 🧪 Sample Enterprise Use Cases

## 📊 Project Status Meetings

- Deployment discussions
- Engineering sync meetings
- Sprint retrospectives

---

## 🏢 Enterprise Operations

- Cross-functional coordination
- Management review meetings
- Incident response discussions

---

## 🔐 Security & Compliance Meetings

- Compliance reviews
- Risk discussions
- Security approval workflows

---

# 📈 Future Improvements

- Multi-speaker identification
- Audio-to-text transcription
- PDF meeting export
- Email automation integration
- Slack / Teams integration
- Calendar integration
- AI meeting analytics dashboard
- Meeting history database
- Role-based access control
- n8n / Zapier workflow integration

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Enterprise AI systems
- LLM application development
- AI-powered productivity automation
- Prompt engineering
- Workflow orchestration
- Meeting intelligence systems
- Streamlit application development
- Modular AI architecture
- Structured AI outputs

---

# 📸 Example Application Screenshots

## 🧠 Enterprise Meeting Assistant UI

_Add screenshots here after deployment._

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- Google Gemini API
- Streamlit
- Python Open Source Community

---

# 👨‍💻 Author

Developed as part of an Enterprise AI Engineering portfolio project focused on:

- Applied LLM Systems
- Enterprise Workflow Automation
- AI Productivity Tools
- Real-World AI Applications
