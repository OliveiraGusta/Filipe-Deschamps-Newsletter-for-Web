from database_manager import DatabaseManager

if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'newsletterdeschamps'
    }

    db_manager = DatabaseManager(**db_config)

    try:
        '''
        # CREATE
        news_hard_values = ["2024-01-29",
                       "Curiosidade para o dia 29 de janeiro: em 1886, o engenheiro alemão Carl Benz dava entrada na patente do veículo movido por motor a gás, considerada hoje como a “certidão de nascimento” do automóvel. E após as notícias de hoje: programa de estágio em uma das poucas empresas no mundo que une tecnologia e saúde, e um depoimento no meu curso de programação para quem estuda em casa ou sozinho e sente que está enrolando/perdendo tempo."]
        db_manager.create_news(*news_hard_values)
        print("\nNotícia criada no Banco de Dados:")

        # READ
        news_list = db_manager.read_news()
        print("\nNotícias no Banco de Dados:")
        print(news_list)

        # UPDATE
        db_manager.update_news('news_date = "2024-01-26"', 'id = 0')
        print("\nNotícias atualizadas no Banco de Dados:")

        # DELETE
        db_manager.delete_news('id = 0')
        print("\nNotícia excluída  no Banco de Dados:")'''



    finally:
        db_manager.close_connection()
