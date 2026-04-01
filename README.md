# NexusAI — Productivity Assistant
**AI Multi-Agent Productivity Assistant for Corporate Employees**

## Quick Start

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## Project Structure
```
productivity-assistant/
├── app.py                  ← Flask backend + SQLite API
├── requirements.txt        ← Python dependencies
├── instance/
│   └── productivity.db     ← SQLite database (auto-created)
└── templates/
    └── index.html          ← Full frontend dashboard
```

---

## Features Implemented

| Feature | Status |
|---|---|
| Dashboard with live stats | ✅ |
| Email inbox (processed by agents) | ✅ |
| Meeting detection & AI summaries | ✅ |
| Task manager (create, filter, complete) | ✅ |
| Daily productivity reports & chart | ✅ |
| AI Insights panel | ✅ |
| Agent activity log | ✅ |
| AI Agent trigger buttons | ✅ |
| Simulate new email (auto-creates meeting/task) | ✅ |
| SQLite database with 6 tables | ✅ |

---

## Database Schema (SQLite)

- **emails** — Raw emails fetched by n8n / Email Agent
- **meetings** — Detected meetings with AI summaries
- **tasks** — Actionable tasks extracted from emails
- **ai_insights** — AI-generated productivity tips
- **daily_reports** — Daily productivity scores & summaries
- **agent_logs** — Real-time activity log for all 5 agents

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/dashboard | Stats, insights, chart data, agent logs |
| GET | /api/emails | All processed emails |
| GET | /api/meetings | All meetings with summaries |
| GET | /api/tasks | All tasks (filter by ?status=pending/completed) |
| PATCH | /api/tasks/:id | Update task status |
| POST | /api/tasks | Create new task |
| GET | /api/reports | Last 14 days of productivity reports |
| POST | /api/emails/simulate | Simulate receiving a new email |
| POST | /api/agents/trigger | Manually trigger an AI agent |

---

## Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python 3, Flask
- **Database**: SQLite (via Python sqlite3)
- **AI (planned)**: Google Gemini API
- **Automation (planned)**: n8n workflow integration

---

## How to Connect n8n (Future Step)

1. Set up n8n with Gmail trigger
2. Point n8n HTTP Request node to: `POST http://localhost:5000/api/emails/simulate`
3. Pass email data as JSON body
4. The backend will process and store it automatically

---

## How to Connect Google Gemini (Future Step)

Replace the placeholder summary text in `app.py` with a call to:
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(f"Summarize this meeting email: {email_body}")
summary = response.text
```
