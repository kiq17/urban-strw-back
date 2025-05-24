from email.message import EmailMessage
from .config import settings
from .emailTemplate import emailTemplate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def makeEmailTemplate(email: str, nome: str, otp: str) -> str:
    msg = MIMEMultipart('alternative')

    msg["Subject"] = "Verificar Conta"
    msg["From"] = settings.email_user
    msg["To"] = email
    msg.attach(MIMEText(emailTemplate(nome, otp), "html"))

    return msg.as_string()