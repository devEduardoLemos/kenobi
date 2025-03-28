import os
import json
import requests
from jinja2 import Environment, FileSystemLoader
from kenobi.dtos.response_dto import ResponseDTO

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "..", "templates")
env = Environment(loader=FileSystemLoader(TEMPLATES_PATH))

def build_email_html(opportunities: list[ResponseDTO], subject: str) -> str:
    """Render the email HTML using Jinja2."""
    template = env.get_template("email_template.html")
    html = template.render(subject=subject, opportunities=opportunities)
    return html

def send_email(from_addr: str, to_addr: str, subject: str, html_body: str, api_url: str) -> requests.Response:
    """Send the rendered email as a JSON payload to the external API."""
    payload = {
        "from": from_addr,
        "to": to_addr,
        "subject": subject,
        "body": html_body
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(payload), headers=headers)
    return response
