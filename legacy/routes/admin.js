const express = require('express');
const router = express.Router();
const adminController = require('../controllers/adminController');
const isAdmin = require('../middleware/isAdmin');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

router.get('/dashboard', isAdmin, adminController.getDashboardStats);
router.get('/movies', isAdmin, (req, res) => res.render('admin/movies'));
router.post('/movies/add', isAdmin, upload.single('poster'), adminController.addMovie);
router.post('/movies/edit/:id', isAdmin, upload.single('poster'), adminController.editMovie);
router.post('/movies/delete/:id', isAdmin, adminController.deleteMovie);
router.get('/shows', isAdmin, (req, res) => res.render('admin/shows'));
router.post('/shows/add', isAdmin, adminController.addShow);
router.get('/bookings', isAdmin, adminController.getAllBookings);

module.exports = router;
