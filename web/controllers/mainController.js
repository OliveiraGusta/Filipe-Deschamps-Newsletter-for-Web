// controllers/mainController.js
const db = require('../models/db');

const mainController = {
  getIndex: (req, res) => {
    const { year, month, day } = req.params;

    if (year && month && day) {
      return mainController.getNews(req, res);
    }

    db.queryTable1((err, resultsTable1) => {
      if (err) {
        console.error('Erro na consulta da tabela1:', err);
        res.status(500).send('Erro interno do servidor');
        return;
      }

      db.queryTable2((err, resultsTable2) => {
        if (err) {
          console.error('Erro na consulta da tabela2:', err);
          res.status(500).send('Erro interno do servidor');
          return;
        }

        const combinedResults = {
          table1: formatDates(resultsTable1),
          table2: formatDates(resultsTable2)
        };

        res.render('index', { data: combinedResults });
      });
    });
  },

  getNews: (req, res) => {
    const { year, month, day } = req.params;
    const date = new Date(Number(year), Number(month) - 1, Number(day));
  
    if (isNaN(date.getTime())) {
      console.error('Data inválida na URL:', req.params);
      res.status(400).send('Data inválida na URL');
      return;
    }
    
    db.queryNewsByDate(date, (err, results) => {
      if (err) {
        console.error('Erro na consulta de notícias por data:', err);
        res.status(500).send('Erro interno do servidor');
        return;
      }
    
      const data = {
        news: formatDates(results),
        table2: results, // Certifique-se de passar os resultados para a propriedade correta
        year,
        month,
        day
      };
  
      res.render('newsByDate', { data });
    });
  }
  
  
}
  
  
function formatDates(data) {
  return data.map(item => ({
    ...item,
    news_date: formatDate(new Date(item.news_date)),
    subject_date: formatDate(new Date(item.subject_date))
  }));
}

function formatDate(date) {
  const options = { day: 'numeric', month: 'long', year: 'numeric' };
  return date.toLocaleDateString('pt-BR', options);
}

module.exports = mainController;
