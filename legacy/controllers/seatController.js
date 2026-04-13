const db = require('../config/db');

// GET seats for a show
exports.getSeatsByShow = async (req, res) => {
  const showId = req.params.showId;

  const [seats] = await db.execute(`
   SELECT 
  s.seat_id,
  s.row_name,
  s.seat_number,
  CASE 
    WHEN EXISTS (
      SELECT 1 FROM tickets t
      JOIN bookings b ON t.booking_id = b.booking_id
      WHERE t.seat_id = s.seat_id AND b.show_id = ?
    ) THEN 'booked'
    ELSE 'available'
  END AS status
FROM seats s
JOIN screens sc ON s.screen_id = sc.screen_id
JOIN shows sh ON sh.screen_id = sc.screen_id
WHERE sh.show_id = ?
  `, [showId, showId]);

  res.render('seats', { seats, showId });
};

// BOOK seats
exports.bookSeats = async (req, res) => {
  const userId = 1; // TEMP (no login yet)
  const { show_id, seats } = req.body;

  const selectedSeats = Array.isArray(seats) ? seats : [seats];

  try {
    const [result] = await db.execute(
      "INSERT INTO bookings (user_id, show_id, status) VALUES (?, ?, ?)",
      [userId, show_id, 'CONFIRMED']
    );

    const bookingId = result.insertId;

    for (let seatId of selectedSeats) {
      await db.execute(
        "INSERT INTO tickets (booking_id, seat_id, price) VALUES (?, ?, ?)",
        [bookingId, seatId, 200]
      );
    }

    res.redirect('/bookings/my');
  } catch (err) {
    console.error(err);
    res.send("Booking failed");
  }
};