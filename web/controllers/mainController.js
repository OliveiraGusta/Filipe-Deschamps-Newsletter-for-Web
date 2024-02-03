const db = require('../models/db');

const mainController = {
  getIndex: (req, res) => {
    db.query('SELECT id, news_text, news_date FROM news', (err, results) => {
        if (err) {
        console.error('Erro na consulta:', err);
        res.status(500).send('Erro interno do servidor');
        return;
      }

      const formattedResults = results.map(item => ({
        ...item,
        news_date: formatNewsDate(new Date(item.news_date)),
      }));

      res.render('index', { data: formattedResults });
    });
  }
};

function formatNewsDate(date) {
    const options = {day: 'numeric', month: 'short', year: 'numeric' };
    return date.toLocaleDateString('en-US', options);
  }
  
  module.exports = mainController;