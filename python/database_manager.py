import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            autocommit=True
        )
        self.cursor = self.connection.cursor()

    def create_news(self, news_date, news_text):
        command = f'INSERT INTO news(news_date, news_text) VALUES (%s, %s)'
        values = (news_date, news_text)
        self.cursor.execute(command, values)

    def read_news(self):
        command = 'SELECT id, news_date, news_text FROM news'
        self.cursor.execute(command)
        result_query = self.cursor.fetchall()
        return result_query

    def update_news(self, set_update, update_condition):
        command = f'UPDATE news SET {set_update} WHERE {update_condition}'
        self.cursor.execute(command)

    def delete_news(self, delete_condition):
        command = f'DELETE FROM news WHERE {delete_condition}'
        self.cursor.execute(command)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
