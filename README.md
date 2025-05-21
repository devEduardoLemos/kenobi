
# 🤖 Kenobi - Smart Opportunities Assistant - V1.0

**Kenobi** is a Python application that scrapes public funding calls (e.g., from FINEP), analyzes them using artificial intelligence (OpenAI), and delivers a polished summary via HTML email.


## 🚀 Features

- 🔍 **Scrapes** funding opportunities from FINEP's official website
- 🧠 **Analyzes and structures** the data using GPT-4o (ChatGPT)
- 📦 Converts raw data into clean **DTOs (Data Transfer Objects)**
- 📧 Generates styled **HTML email templates**
- 🧪 Provides local **preview rendering** for design testing
- ✅ Sends to multiple recipients via an external email API


## 📁 Project Structure

```
kenobi/
│
├── core/               # Main logic (scraping + OpenAI processing)
├── dtos/               # Data Transfer Objects
├── services/           # External services (email)
├── templates/          # Jinja2 email templates
├── tests/              # Preview/testing utilities
├── env/                # Python virtual environment (git-ignored)
├── .env                # Environment variables (e.g., API keys)
├── .gitignore
├── requirements.txt
└── README.md
````



## ⚙️ Requirements

- Python 3.9+
- Virtual environment (`venv` recommended)
- OpenAI API Key (GPT-4o model)
- Email API endpoint (local or remote)



## 📦 Installation

```bash
git clone https://github.com/your-username/kenobi.git
cd kenobi
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
````

## 🔐 Environment Configuration

Create a `.env` file at the project root with the following content:

```env
OPENAI_API_KEY=your-openai-api-key
```


## 🧪 Email Preview (Design Testing)

Run the preview script to generate and open the rendered email in your browser:

```bash
python kenobi/tests/preview_email.py
```

This will generate `kenobi/tests/email_preview.html` and open it automatically.



## 🚚 Running the Main Pipeline

This runs the full process: scrape → analyze → generate HTML → send email.

```bash
python kenobi/core/kenobi.py
```

## ✉️ Email API (Expected Format)

The application sends email content to the following endpoint:

```
POST http://<your-host:port>/api/email
Content-Type: application/json

{
  "from": "naoresponder@gruposkip.com",
  "to": "recipient@example.com",
  "subject": "Subject here",
  "body": "<html>...formatted email body...</html>"
}
```

---

## 🛣️ Future Roadmap

* [ ] Add new funding sources beyond FINEP
* [ ] Web dashboard to manage and filter opportunities
* [ ] User history and search filters
* [ ] Tagging and recommendation system


## 👨‍💻 Author

Developed by [Grupo Skip](https://gruposkip.com)



## 🧠 License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.

