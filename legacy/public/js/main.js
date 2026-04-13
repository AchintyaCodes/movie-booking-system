// Seat selection logic
document.addEventListener('DOMContentLoaded', () => {
  const seats = document.querySelectorAll('.seat.available');
  const selectedSeats = [];
  const selectedSeatsSpan = document.getElementById('selectedSeats');
  const confirmBtn = document.getElementById('confirmBooking');

  seats.forEach(seat => {
    seat.addEventListener('click', () => {
      const seatId = seat.getAttribute('data-seat-id');
      if (seat.classList.contains('selected')) {
        seat.classList.remove('selected');
        const idx = selectedSeats.indexOf(seatId);
        if (idx > -1) selectedSeats.splice(idx, 1);
      } else {
        seat.classList.add('selected');
        selectedSeats.push(seatId);
      }
      selectedSeatsSpan.textContent = selectedSeats.join(', ');
    });
  });

  if (confirmBtn) {
    confirmBtn.addEventListener('click', () => {
      // AJAX POST to /bookings with selected seat IDs
      fetch('/bookings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          showId: window.showId, // set this variable in your EJS
          seatIds: selectedSeats,
          price: 200 // example price
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          window.location.href = `/confirmation?bookingId=${data.bookingId}`;
        } else {
          alert('Booking failed');
        }
      });
    });
  }
});
