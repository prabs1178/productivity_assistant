🚀 NexusAI — Project Activity & Integration Log

This document tracks the development milestones, technical challenges, and the current system workflow of the NexusAI project.

🏗️ 1. Current System Architecture

NexusAI is designed as a Multi-Agent System, where:

🖥️ Flask Server (Local) → Acts as the Command Center
🤖 n8n (Cloud) → Acts as the Remote Intelligence
🔄 System Flow
📧 Email Agent (n8n)
Monitors Gmail for new corporate communications.
🧠 AI Processor (Gemini)
Analyzes email intent (Meeting / Task)
Generates intelligent summaries
🌐 Bridge (ngrok)
Securely tunnels data from cloud → local machine
⚙️ Backend (Flask)
Receives AI-generated JSON
Stores data in a 6-table SQLite database
🎨 Frontend (HTML/CSS)
Displays real-time productivity insights
Shows agent activity logs
✅ 2. Completed Milestones
✔️ Core Setup
Flask server initialized with SQLite and 6-table schema
✔️ Environment Fix
Resolved “Fatal error in launcher”
Rebuilt .venv
Used python -m pip for clean installs
✔️ UI Routing Fix
Fixed TemplateNotFound error
Corrected render_template() paths
Aligned with templates/index.html
✔️ Public Tunneling
Successfully integrated ngrok for external access
🛠️ 3. Technical Integration: ngrok Setup

To maintain communication between AI agents and your local dashboard:

🌍 Public URL

https://miriam-nonobligatory-centennially.ngrok-free.dev

⚠️ Note: This URL changes after every restart

💻 Command Used

ngrok http 5000

🎯 Purpose
Enables the n8n HTTP Request node to send POST requests to:

/api/webhook
/api/emails/simulate

Even when the Flask server is behind a firewall.

🚀 4. Next Phase: n8n Workflow Construction

With the communication bridge established, the next step is building the n8n automation workflow.

🔧 Planned Workflow
⚡ Trigger
Gmail → On New Email

🧠 AI Node

Google Gemini
Analyze: {{ $json.body }}

🌐 Action Node

HTTP Request
POST → {{ ngrok_url }}/webhook
📝 5. Troubleshooting Log (Resolved Issues)
❌ Issue	🔍 Cause	✅ Resolution
ModuleNotFoundError	Flask not in .venv	Run python -m pip install flask
502 Bad Gateway	Flask server not running	Ensure python app.py is active
TemplateNotFound	Filename mismatch	Align route to index.html
📌 What To Do Next
📄 Create Activity File
Create a file named: Activity.md
📋 Copy Content
Paste this entire document into Activity.md

🔗 Update README
Add this line to your README.md:

For detailed development logs and ngrok setup, see [Activity.md](./Activity.md)
💡 Summary

NexusAI is evolving into a powerful AI-driven productivity assistant by combining:

Automation (n8n)
AI Intelligence (Gemini)
Backend Processing (Flask)
Real-time Dashboard (Frontend UI)