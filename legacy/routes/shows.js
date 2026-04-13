const express = require('express');
const router = express.Router();

const showController = require('../controllers/showController');

// GET shows by movie
router.get('/:movieId', showController.getShowsByMovie);

module.exports = router;