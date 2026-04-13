exports.getMyBookings = async (req, res) => {
  const userId = 1; // TEMP (since no login yet)

  try {
    const db = require('../config/db');

 const [bookings] = await db.execute(`
  SELECT 
    b.booking_id,
    m.title,
    s.start_time,
    GROUP_CONCAT(CONCAT(se.row_name, se.seat_number)) AS seats
  FROM bookings b
  JOIN shows s ON b.show_id = s.show_id
  JOIN movies m ON s.movie_id = m.movie_id
  JOIN tickets t ON b.booking_id = t.booking_id
  JOIN seats se ON t.seat_id = se.seat_id
  WHERE b.user_id = ?
  GROUP BY b.booking_id
`, [userId]);

    res.render("my-bookings", { bookings });
  } catch (err) {
    console.error(err);
    res.send("Error loading bookings");
  }
};