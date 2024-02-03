const express = require('express');
const mainController = require('../controllers/mainController');

const router = express.Router();

router.get('/:year/:month/:day', mainController.getNews);

router.get('/', mainController.getIndex);

module.exports = router;
