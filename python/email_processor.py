from email_reader import EmailReader
from datetime import datetime
from database_manager import DatabaseManager

class EmailProcessor:
    def __init__(self, email_address, password, server_address):
        self.email_reader = EmailReader(email_address, password, server_address)

    def process_emails(self):
        try:
            self.email_reader.connect()
            last_emails = self.email_reader.read_emails()

            db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': '',
                'database': 'newsletterdeschamps'
            }
            db_manager = DatabaseManager(**db_config)

            try:
                for email_info in last_emails:
                    email_subject = email_info['subject']
                    email_date = self.format_email_date(email_info['date'])

                    db_manager.new_subject(email_date,email_subject)

                    news_list = self.extract_news(email_info)
                    for date, content in news_list:
                        if not db_manager.news_exists(date, content):
                            db_manager.create_news(date, content)

            finally:
                db_manager.close_connection()

        finally:
            self.email_reader.disconnect()

    def format_email_date(self, raw_date):
        date_object = datetime.strptime(raw_date, "%a, %d %b %Y %H:%M:%S %z")
        formatted_date = date_object.strftime("%Y-%m-%d")
        return formatted_date

    def extract_news(self, email_info):
        email_date = self.format_email_date(email_info['date'])
        email_content = email_info['content']

        lines = email_content.split('\n')
        filtered_lines = []

        for line in lines:
            if line.strip() == '':
                filtered_lines.append(f'new:')
            else:
                filtered_lines.append(f'{line}')

        filtered_content = '\n'.join(filtered_lines)

        news_list = []
        for news_item in filtered_content.split('new:'):
            if news_item.strip():
                news_lines = news_item.split('\n')
                content = '\n'.join(news_lines[1:])
                news_list.append((email_date, content))

        return news_list