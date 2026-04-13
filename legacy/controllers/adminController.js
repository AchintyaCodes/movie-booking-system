const db = require('../config/db');

exports.getDashboardStats = async (req, res) => {
  const [[{ totalBookings }]] = await db.execute('SELECT COUNT(*) AS totalBookings FROM bookings');
  const [[{ totalMovies }]] = await db.execute('SELECT COUNT(*) AS totalMovies FROM movies');
  const [[{ totalUsers }]] = await db.execute('SELECT COUNT(*) AS totalUsers FROM users WHERE role="user"');
  res.render('admin/dashboard', { totalBookings, totalMovies, totalUsers });
};

exports.addMovie = async (req, res) => {
  const { title, release_date, duration, genre, story_line, film_director, rating } = req.body;
  const poster = req.file ? req.file.filename : null;
  await db.execute(
    'INSERT INTO movies (title, release_date, duration, genre, story_line, poster, film_director, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
    [title, release_date, duration, genre, story_line, poster, film_director, rating]
  );
  res.redirect('/admin/movies');
};

exports.editMovie = async (req, res) => {
  // Similar to addMovie, but with UPDATE query
};

exports.deleteMovie = async (req, res) => {
  await db.execute('DELETE FROM movies WHERE movie_id = ?', [req.params.id]);
  res.redirect('/admin/movies');
};

exports.addShow = async (req, res) => {
  const { movie_id, theatre_id, screen_id, start_time, end_time } = req.body;
  await db.execute(
    'INSERT INTO shows (movie_id, theatre_id, screen_id, start_time, end_time) VALUES (?, ?, ?, ?, ?)',
    [movie_id, theatre_id, screen_id, start_time, end_time]
  );
  res.redirect('/admin/shows');
};

exports.getAllBookings = async (req, res) => {
  const [bookings] = await db.execute(
    `SELECT b.*, u.first_name, u.last_name, m.title, t.name AS theatre, sc.screen_no
     FROM bookings b
     JOIN users u ON b.user_id = u.user_id
     JOIN shows s ON b.show_id = s.show_id
     JOIN movies m ON s.movie_id = m.movie_id
     JOIN theatres t ON s.theatre_id = t.theatre_id
     JOIN screens sc ON s.screen_id = sc.screen_id
     ORDER BY b.booking_date DESC`
  );
  res.render('admin/bookings', { bookings });
};
