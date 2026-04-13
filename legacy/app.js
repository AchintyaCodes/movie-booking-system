const express = require('express');
const path = require('path');
require('dotenv').config();
const session = require('express-session');

const app = express();

// BODY
app.use(express.urlencoded({ extended: true }));

// SESSION
app.use(session({
  secret: 'secret123',
  resave: false,
  saveUninitialized: false
}));

// STATIC
app.use(express.static(path.join(__dirname, 'public')));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// VIEW
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// ROUTES
const movieRoutes = require('./routes/movies');
const showRoutes = require('./routes/shows');
const seatRoutes = require('./routes/seats');
const bookingRoutes = require('./routes/bookings');
const authRoutes = require('./routes/auth');

// 🔥 THIS FIXES YOUR ISSUE
app.get('/', (req, res) => {
  res.redirect('/movies');
});

// ROUTE STRUCTURE
app.use('/movies', movieRoutes);
app.use('/shows', showRoutes);
app.use('/seats', seatRoutes);
app.use('/bookings', bookingRoutes);
app.use('/', authRoutes);

// TEST
app.get('/test', (req, res) => {
  res.send("SERVER WORKING");
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});