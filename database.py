import sqlite3
import os

DB_NAME = "cinevault.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Create Tables
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user',
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        story_line TEXT,
        poster TEXT,
        duration INTEGER,
        rating TEXT
    );

    CREATE TABLE IF NOT EXISTS theatres (
        theatre_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS shows (
        show_id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER NOT NULL,
        theatre_id INTEGER NOT NULL,
        start_time TEXT NOT NULL,
        price REAL DEFAULT 250.0,
        FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
        FOREIGN KEY (theatre_id) REFERENCES theatres(theatre_id)
    );

    CREATE TABLE IF NOT EXISTS bookings (
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        show_id INTEGER NOT NULL,
        seat_numbers TEXT NOT NULL,
        total_price REAL NOT NULL,
        booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (show_id) REFERENCES shows(show_id)
    );
    ''')

    # Seed Data (if empty)
    cursor.execute("SELECT COUNT(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO movies (title, genre, story_line, poster, duration, rating) VALUES (?, ?, ?, ?, ?, ?)", 
                      ("Interstellar", "Sci-Fi", "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", "interstellar.jpg", 169, "8.7"))
        cursor.execute("INSERT INTO movies (title, genre, story_line, poster, duration, rating) VALUES (?, ?, ?, ?, ?, ?)", 
                      ("Inception", "Sci-Fi", "A thief who steals corporate secrets through the use of dream-sharing technology.", "inception.jpg", 148, "8.8"))
        cursor.execute("INSERT INTO movies (title, genre, story_line, poster, duration, rating) VALUES (?, ?, ?, ?, ?, ?)", 
                      ("The Dark Knight", "Action", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham.", "dark_knight.jpg", 152, "9.0"))

        cursor.execute("INSERT INTO theatres (name, location) VALUES (?, ?)", ("CineVault Prime", "Manhattan, NY"))
        
        cursor.execute("INSERT INTO shows (movie_id, theatre_id, start_time, price) VALUES (1, 1, '2026-04-20 19:00:00', 350.0)")
        cursor.execute("INSERT INTO shows (movie_id, theatre_id, start_time, price) VALUES (2, 1, '2026-04-20 21:30:00', 300.0)")
        cursor.execute("INSERT INTO shows (movie_id, theatre_id, start_time, price) VALUES (3, 1, '2026-04-21 18:00:00', 300.0)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
