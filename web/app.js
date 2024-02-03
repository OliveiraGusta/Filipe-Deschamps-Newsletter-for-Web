const express = require('express');
const mainRoutes = require('./routes/mainRoutes');

const app = express();

app.set('view engine', 'ejs');
app.use(express.static('public'));

app.use('/', mainRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor iniciado no link http://localhost:${PORT}`);
  console.log(`Teste de data no link http://localhost:${PORT}/2024/2/2`);
});
