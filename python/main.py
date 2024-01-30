import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='newsletterdeschamps',
)

cursor = connection.cursor()

# CRUD
#CREATE
def create_news():
    news_date = '2024-01-29'
    news_text = 'Pesquisa encontra “pressão descendente na qualidade do código” escrito pelo GitHub Copilot: o estudo analisou 153 milhões de linhas de código, identificando “tendências desconcertantes” para a manutenção de uma base no longo prazo. Foram encontradas correlações com a quantidade de código escrito com assistentes de IA e linhas que são revertidas ou atualizadas menos de duas semanas após serem criadas, e uma tendência crescente nas adições de código, sugerindo uma redução do reaproveitamento e refatoração. As informações são do site Visual Studio Magazine.'
    command = f'INSERT INTO news(news_date, news_text) VALUES ("{news_date}","{news_text}")'
    cursor.execute(command)
    connection.commit()


#READ
def read_news():
    command = 'SELECT * FROM news'
    cursor.execute(command)
    resultQuery = cursor.fetchall()
    print(resultQuery)
 

#UPDATE
def update_news():
    setUpdate = 'news_date = "2024-01-29"'
    whereCondition = 'id = 1'
    command = f'UPDATE news SET {setUpdate} WHERE {whereCondition}'
    cursor.execute(command)
    connection.commit()

#DELETE
def delete_news():
    whereCondition = 'id = 0'
    command = f'DELETE FROM news WHERE {whereCondition}'
    cursor.execute(command)
    connection.commit()

read_news()
cursor.close()
connection.close()