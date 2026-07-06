# AI-Powered Productivity Assistant

A web-based, multi-agent AI application that automatically reads incoming emails, extracts actionable items, generates summaries, and presents everything on a unified dashboard — built to reduce the hours professionals spend manually managing emails, calendars, and tasks.

Developed as a team project by **Prabha Kamble** and **Rudranshsing Rajput**, guided by **Dr. Gauri Dhongade** at MIT World Peace University.

## Problem

Professionals spend 2–3 hours daily managing emails, and existing tools (email clients, calendars, task managers) operate in isolation — requiring manual, error-prone effort to bridge them.

## Solution

This project automates that bridge. Incoming Gmail messages are detected in near real-time, processed through a multi-agent AI pipeline, and turned into structured tasks, meeting entries, and summaries — all visible on a single dashboard, with zero manual intervention once configured.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python (Flask) |
| Automation | n8n (self-hosted via Docker) |
| AI / Intelligence | Google Gemini 1.5 Flash |
| Database | SQLite3 |
| Tunneling | ngrok |
| Frontend | HTML/CSS with Jinja2 templating |

## How It Works

1. **Ingestion** — n8n's Gmail Trigger polls the inbox every 60 seconds via OAuth2 and extracts new email metadata.
2. **Transmission** — n8n sends the email data as a JSON payload via HTTP POST to a Flask webhook, exposed to the internet through ngrok.
3. **Processing** — The Flask backend routes the content through a set of specialized agents.
4. **AI Analysis** — Relevant content is sent to the Gemini 1.5 Flash API for summarization and task/meeting extraction.
5. **Storage** — Structured results (summaries, tasks, meetings, logs) are saved to SQLite.
6. **Display** — The dashboard updates to show new emails, tasks, and meetings.

```
Gmail Inbox
     │
     ▼
n8n (Gmail Trigger, polls every 60s via OAuth2)
     │
     ▼  (JSON payload via HTTP POST)
Flask Backend (ngrok-exposed webhook)
     │
     ▼
Multi-Agent Processing Layer  ──▶  Google Gemini 1.5 Flash API
     │
     ▼
SQLite Database
     │
     ▼
Dashboard (Jinja2-rendered)
```

## Multi-Agent System

| Agent | Responsibility |
|---|---|
| Email Agent | Intake and initial processing of raw email data |
| Summary Agent | Condenses long threads into 2–3 sentence summaries via Gemini |
| Task Agent | Extracts actionable items into structured JSON via Gemini |
| Meeting Agent | Detects meeting-related keywords and auto-populates meeting entries |
| Insight Agent | Generates personalized productivity tips from daily stats |
| Reporting Agent | Compiles an end-of-day summary report |

## Current Limitations

- Relies on a local machine + ngrok free tier — the pipeline stops if the host machine goes offline
- Dashboard currently requires a manual refresh to show newly processed data; real-time auto-refresh is planned for the next phase
- Authentication is currently a placeholder and the database does not yet separate data by user, so it is not yet ready for multiple simultaneous users
- Some detection logic still relies on basic keyword matching alongside Gemini, which can occasionally produce false positives

## Roadmap

- Cloud deployment (Render/Railway) with a PostgreSQL database for 24/7 uptime
- Multi-user support with proper authentication and per-user data isolation
- Integrations with Jira (ticket creation), Slack/Teams (urgent notifications), and Google Calendar (auto-scheduling)

## Setup

```bash
git clone https://github.com/prabs1178/productivity_assistant.git
cd productivity_assistant
pip install -r requirements.txt
# Configure your .env with Gmail OAuth2 credentials and Gemini API key
python app.py
```

Separately, set up n8n (via Docker), configure the Gmail Trigger node with your OAuth2 credentials, and point it to your ngrok-exposed Flask webhook URL.

## Author

**Prabha Kamble** — [LinkedIn](https://linkedin.com/in/prabhakamble-0050a3314)
