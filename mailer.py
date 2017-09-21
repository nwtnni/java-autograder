import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:

    EMAIL = os.environ['EMAIL']
    PASSWORD = os.environ['PASSWORD']

    def __init__(self):
        this.server = smtplib.SMTP('smtp.gmail.com', 587)
        this.server.starttls()
        this.server.login(Mailer.EMAIL, Mailer.PASSWORD)

    def send(self, to_add, subject, body):
        msg = MIMEMultipart()
        msg['From'] = Mailer.EMAIL
        msg['To'] = to_add
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))  
        this.server.sendmail(Mailer.EMAIL, to_add, msg.as_string())

    def quit(self):
        this.server.quit()
