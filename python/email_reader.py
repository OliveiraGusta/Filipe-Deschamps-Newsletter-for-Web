import imaplib
import email
from email import policy
from email.parser import BytesParser

class EmailReader:
    def __init__(self, email_address, password, server_address):
        self.email_address = email_address
        self.password = password
        self.server_address = server_address
        self.mail = None

    def connect(self):
        self.mail = imaplib.IMAP4_SSL(self.server_address)
        self.mail.login(self.email_address, self.password)
        self.mail.select('inbox')

    def read_emails(self, num_emails=1):
        status, messages = self.mail.search(None, 'FROM', 'newsletter@filipedeschamps.com.br')
        message_ids = messages[0].split()

        email_list = []
        for email_id in message_ids[-num_emails:]:
            raw_email = self.fetch_raw_email(email_id)
            email_info = self.extract_email_info(raw_email)
            email_list.append(email_info)

        return email_list

    def fetch_raw_email(self, email_id):
        status, msg_data = self.mail.fetch(email_id, '(RFC822)')
        return msg_data[0][1]

    def extract_email_info(self, raw_email):
        msg = BytesParser(policy=policy.default).parsebytes(raw_email)
        return {
            'subject': msg.get("Subject"),
            'from': msg.get("From"),
            'date': msg.get("Date"),
            'content': self.extract_email_content(msg)
        }

    def extract_email_content(self, msg):
        content = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    content += part.get_payload(decode=True).decode("utf-8", errors="ignore")
        else:
            content = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

        return content

    def disconnect(self):
        self.mail.logout()


