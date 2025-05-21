#kenobi/services/__init__.py

# External service integrations (email, APIs, etc.)

from .email_service import build_email_html, send_email

__all__ = ["build_email_html", "send_email"]
