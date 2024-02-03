const db = require('../models/db');

const mainController = {
  getIndex: (req, res) => {

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
  }
};

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
