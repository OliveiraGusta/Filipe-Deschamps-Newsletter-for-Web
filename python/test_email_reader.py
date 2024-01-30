from email_reader import EmailReader

email_address = 'EMAIL'
password = 'PASSWORD'
server_address = 'imap.gmail.com'

email_reader = EmailReader(email_address, password, server_address)




try:
    email_reader.connect()
    last_emails = email_reader.read_emails()
    for email_info in last_emails:
        print("Assunto:", email_info['subject'])
        print("De:", email_info['from'])
        print()
        print("Conteúdo:", email_info['content'])
        print("Data:", email_info['date'])
        print("\n-------\n")

finally:
    email_reader.disconnect()
