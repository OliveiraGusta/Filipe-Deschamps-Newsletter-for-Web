from email_processor import EmailProcessor
from database_manager import DatabaseManager

if __name__ == "__main__":
    email_address = 'gustavo.oliver456@gmail.com'
    password = 'hmfc mbza zkfs rmqr'
    server_address = 'imap.gmail.com'

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'newsletterdeschamps'
    }

    email_processor = EmailProcessor(email_address, password, server_address)
    db_manager = DatabaseManager(**db_config)

    try:
        email_processor.process_emails()
        #db_manager.delete_all_news()

    finally:
        db_manager.close_connection()
