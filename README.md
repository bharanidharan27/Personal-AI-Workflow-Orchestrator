# 🤖 Personal AI Workflow Orchestrator (PAWO)

**PAWO** is a lightweight, AI-driven workflow automation platform that lets users describe goals in natural language and automatically generate, execute, and monitor multi-step workflows — powered by a minimal LLM-based orchestrator.

> MVP scope: single-developer project (~20 hrs total) focusing on goal-to-workflow generation, mock connectors, and simple sequential execution.

---

## 🌟 Overview

Modern users juggle repetitive digital tasks across multiple platforms. PAWO simplifies this by letting users type a goal like:

> “Summarize today’s emails and store the summary in Notion.”

The system:
1. Converts the goal into a structured JSON workflow using an LLM.  
2. Executes the workflow step-by-step through mock connectors.  
3. Displays the execution logs and outputs in a clean web interface.

---

## 🧩 Architecture (MVP)

User (React UI)
│
├── POST /generate → FastAPI Backend
│ │
│ ├── LLM → Generates JSON Workflow
│ └── Orchestrator → Executes Steps
│ │
│ └── Mock Connectors
│ • Gmail_Mock()
│ • LLM_Summarize()
│ • Notion_Mock()
│
└── GET /logs ← Returns run summary (JSON/SQLite)

---

## 🧠 Core Features (MVP)

| Feature | Description |
|----------|-------------|
| 🧾 **Goal-to-Workflow Generator** | Uses OpenAI API to transform user goals into JSON workflow plans. |
| ⚙️ **Sequential Orchestrator Engine** | Executes each step sequentially with shared context. |
| 🧱 **Mock Connectors** | Simulate Gmail and Notion integrations using local data. |
| 🖥️ **Minimal React UI** | Input field for goals, workflow preview, and execution log viewer. |
| 📜 **Execution Logs** | Stores run summaries locally (JSON/SQLite). |

---

## 🗂️ Folder Structure

pawo/
├── backend/
│ ├── main.py # FastAPI entrypoint
│ ├── orchestrator.py # Core workflow executor
│ ├── llm_generator.py # Goal-to-JSON converter
│ ├── connectors/
│ │ ├── gmail_mock.py
│ │ └── notion_mock.py
│ └── logs/
│ └── runs.json
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── GoalInput.jsx
│ │ │ ├── WorkflowViewer.jsx
│ │ │ └── LogViewer.jsx
│ │ └── App.jsx
│ └── package.json
│
├── README.md
└── requirements.txt

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | React + Tailwind CSS |
| Backend | FastAPI (Python) |
| AI | OpenAI API (gpt-4o-mini recommended) |
| Storage | JSON / SQLite for logs |
| Deployment | Local run via `uvicorn` & `npm start` |

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bharanidharan27/Personal-AI-Workflow-Orchestrator.git
cd pawo
```

### 2️⃣ Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"
uvicorn main:app --reload
```

### 3️⃣ Frontend Setup
```bash
cd frontend
npm install
npm start
```

### 4️⃣ Run the App 
1. Open http://localhost:3000 
2. Type a goal → View generated workflow → Execute → See logs!

🧪 Example Workflow (Mock)
Input Goal:
“Summarize my recent emails and add the summary to Notion.”
Generated Workflow (example JSON):
```
{
  "steps": [
    {"tool": "gmail_mock", "action": "fetch_emails"},
    {"tool": "llm_summarize", "action": "summarize"},
    {"tool": "notion_mock", "action": "create_page"}
  ]
}
```

Console Output (Execution Logs):
```
[Gmail_Mock] → 3 emails fetched.
[LLM_Summarize] → Summary generated.
[Notion_Mock] → Page 'Email Summary' created.
✅ Workflow completed successfully.
```
