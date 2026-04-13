const db = require('../config/db');

exports.getAllMovies = async (req, res) => {
  try {
    const [movies] = await db.execute("SELECT * FROM movies");

    res.render("index", { movies, userId: req.session.userId });
  } catch (err) {
    console.error(err);
    res.send("Error loading movies");
  }
};

exports.getMovieById = async (req, res) => {
  try {
    const [movies] = await db.execute(
      "SELECT * FROM movies WHERE movie_id = ?",
      [req.params.id]
    );

    const movie = movies[0];

    if (!movie) return res.send("Movie not found");

    const [shows] = await db.execute(
      `SELECT s.*, t.name AS theatre
       FROM shows s
       JOIN screens sc ON s.screen_id = sc.screen_id
       JOIN theatres t ON sc.theatre_id = t.theatre_id
       WHERE s.movie_id = ?`,
      [req.params.id]
    );

    movie.shows = shows;

    res.render("movie", {
      movie,
      userId: req.session.userId
    });

  } catch (err) {
    console.error(err);
    res.send("Error loading movie");
  }
};