const express = require('express');
const router = express.Router();
const bookingController = require('../controllers/bookingController');

router.get('/my', bookingController.getMyBookings);

module.exports = router;