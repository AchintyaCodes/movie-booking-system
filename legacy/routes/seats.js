const express = require('express');
const router = express.Router();
const seatController = require('../controllers/seatController');

// GET seats for a show
router.get('/:showId', seatController.getSeatsByShow);

// POST booking
router.post('/book', seatController.bookSeats);

module.exports = router; // ✅ VERY IMPORTANT