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
  connection.query('SELECT id,subject_text, subject_date FROM news_subjects', callback);
}


module.exports = { queryTable1, queryTable2 };
