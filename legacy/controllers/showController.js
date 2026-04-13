const db = require('../config/db');

exports.getShowsByMovie = async (req, res) => {
  try {
    const [shows] = await db.execute(
      "SELECT * FROM shows WHERE movie_id = ?",
      [req.params.movieId]
    );

    console.log("SHOWS:", shows);

    res.render('shows', { shows });
  } catch (err) {
    console.error(err);
    res.send("Error loading shows");
  }
};