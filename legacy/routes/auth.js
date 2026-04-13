const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');

// show pages
router.get('/login', authController.showLogin);
router.get('/register', authController.showRegister);

// handle form
router.post('/login', authController.login);
router.post('/register', authController.register);

// logout
router.get('/logout', authController.logout);

module.exports = router;