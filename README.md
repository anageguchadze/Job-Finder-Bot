# Job-Finder-Bot

A simple Flask-based web app that fetches and displays remote developer job listings from sources like RemoteOK, filtered by your chosen keywords.

## 🚀 Features

- Search for jobs by keyword (e.g., `python, django, scraping`)
- Fetches jobs from RemoteOK via RSS
- Minimal HTML interface (Jinja2 templating)
- Easily extendable to support more job boards or APIs

## 🗂 Project Structure

job-finder-bot/
├── app.py # Main Flask app
├── feeds/
│ └── remoteok.py # RSS job fetcher for RemoteOK
├── templates/
│ └── index.html # HTML interface
├── static/ # Optional static files (CSS/JS)
├── utils.py # Helper functions (optional)
├── config.py # Config variables (optional)
└── requirements.txt # Python dependencies

## ⚙️ Installation

1. Clone the repo:

git clone https://github.com/anageguchadze/Job-Finder-Bot.git
cd Job-Finder-Bot

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py
Then open http://127.0.0.1:5000 in your browser.

🛠 Future Improvements
Add more job boards (WeWorkRemotely, StackOverflow, Upwork, etc.)

Background job check with email or Telegram notifications

Database integration for storing and filtering results

Frontend improvements with CSS/JS

📄 License
MIT License

