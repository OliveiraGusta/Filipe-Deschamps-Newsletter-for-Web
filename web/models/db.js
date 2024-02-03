const mysql = require('mysql2');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'newsletterdeschamps'
});

function queryTable1(callback) {
  connection.query('SELECT id, news_text, news_date FROM news', callback);
}

function queryTable2(callback) {
  connection.query('SELECT id, subject_text, subject_date FROM news_subjects', callback);
}

function queryNewsByDate(date, callback) {
  connection.query('SELECT id, news_text, news_date FROM news WHERE DATE(news_date) = ?', [date], (err, results) => {
    if (err) {
      console.error('Erro na consulta de notícias por data:', err);
      callback(err, null);
      return;
    }
    callback(null, results);
  });
}


module.exports = { queryTable1, queryTable2, queryNewsByDate };
