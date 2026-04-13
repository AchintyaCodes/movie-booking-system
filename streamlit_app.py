import streamlit as st
import time
from database import get_connection, init_db
from auth import login_user, register_user

# --- CONFIG ---
st.set_page_config(page_title="CineVault", page_icon="🎬", layout="wide")
init_db()

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Outfit', sans-serif;
        background-color: #141414;
        color: white;
    }

    /* 🎬 NETFLIX INTRO ANIMATION */
    #splash-container {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background: #000;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        animation: fadeOut 1.5s forwards 2.5s;
    }

    .netflix-logo {
        color: #e50914;
        font-size: 8rem;
        font-weight: 900;
        letter-spacing: -5px;
        animation: zoomIn 2s ease-in-out;
        text-shadow: 0 0 30px rgba(229, 9, 20, 0.6);
    }

    @keyframes zoomIn {
        0% { transform: scale(0.5); opacity: 0; filter: blur(20px); }
        50% { transform: scale(1.1); opacity: 1; filter: blur(0px); }
        100% { transform: scale(1); opacity: 1; }
    }

    @keyframes fadeOut {
        to { opacity: 0; visibility: hidden; }
    }

    /* 💎 GLASSMORPHISM CARDS */
    .movie-card {
        background: rgba(40, 40, 40, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 0px;
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        overflow: hidden;
    }

    .movie-card:hover {
        transform: scale(1.05);
        border-color: #e50914;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }

    .movie-poster {
        width: 100%;
        border-radius: 12px 12px 0 0;
        aspect-ratio: 2/3;
        object-fit: cover;
    }

    /* 🔴 PREMIUM BUTTONS */
    .stButton>button {
        background: #e50914 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: bold !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover {
        background: #f40612 !important;
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(229, 9, 20, 0.4);
    }

    /* 🛋️ SEAT SELECTION */
    .seat {
        width: 35px;
        height: 35px;
        margin: 5px;
        border-radius: 6px;
        display: inline-block;
        border: 1px solid #333;
        transition: 0.2s;
        cursor: pointer;
    }
    .seat-available { background: #222; }
    .seat-selected { background: #e50914; border-color: #fff; }
    .seat-booked { background: #555; cursor: not-allowed; opacity: 0.5; }

</style>
""", unsafe_allow_html=True)

# --- SPLASH SCREEN ---
if 'splashed' not in st.session_state:
    st.markdown("""
        <div id="splash-container">
            <div class="netflix-logo">N</div>
        </div>
    """, unsafe_allow_html=True)
    st.session_state.splashed = True
    # In a real app we'd wait, but for Streamlit reactivity we just let it render

# --- SESSION STATE ---
if 'user' not in st.session_state:
    st.session_state.user = None
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- SIDEBAR NAV ---
with st.sidebar:
    st.markdown("<h1 style='color:#e50914; text-align:center;'>CINEVAULT</h1>", unsafe_allow_html=True)
    
    if st.session_state.user:
        st.write(f"Welcome back, **{st.session_state.user['first_name']}**!")
        if st.button("Sign Out", use_container_width=True):
            st.session_state.user = None
            st.rerun()
    else:
        if st.button("Sign In / Sign Up", use_container_width=True):
            st.session_state.page = "Auth"
            st.rerun()

    st.divider()
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
    if st.session_state.user:
        if st.button("🎫 My Bookings", use_container_width=True):
            st.session_state.page = "Bookings"
            st.rerun()

# --- PAGES ---

def home_page():
    # HERO SECTION
    st.markdown("""
        <div style="background: linear-gradient(to right, rgba(0,0,0,0.8), transparent), url('https://image.tmdb.org/t/p/original/rAiYKRLSXccP66vST1nq1YZvzsz.jpg'); 
                    background-size: cover; height: 450px; border-radius: 20px; padding: 50px; display: flex; flex-direction: column; justify-content: center;">
            <h1 style="font-size: 4rem; margin: 0;">INTERSTELLAR</h1>
            <p style="font-size: 1.2rem; max-width: 600px; color: #ccc;">Earth's dying. Astronauts cross a wormhole to find humanity a new home, where time and space bend in impossible ways.</p>
            <div style="display: flex; gap: 20px; margin-top: 20px;">
                <button style="background: #e50914; color: white; border: none; padding: 12px 30px; border-radius: 5px; font-weight: bold; cursor: pointer;">Play Trailer</button>
                <button style="background: rgba(255,255,255,0.2); color: white; border: none; padding: 12px 30px; border-radius: 5px; font-weight: bold; cursor: pointer;">Details</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.header("Now Showing")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()

    cols = st.columns(4)
    for i, movie in enumerate(movies):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="movie-card">
                    <img class="movie-poster" src="app/static/uploads/{movie['poster']}">
                    <div style="padding: 15px;">
                        <h4 style="margin: 0;">{movie['title']}</h4>
                        <p style="color: #e50914; font-size: 0.9rem;">{movie['genre']} • ⭐ {movie['rating']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Book Seats", key=f"book_{movie['movie_id']}", use_container_width=True):
                if not st.session_state.user:
                    st.warning("Please sign in to book seats!")
                else:
                    st.session_state.selected_movie = movie
                    st.session_state.page = "Seat Selection"
                    st.rerun()

def auth_page():
    st.title("Welcome back")
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign In"):
            user = login_user(email, password)
            if user:
                st.session_state.user = user
                st.session_state.page = "Home"
                st.rerun()
            else:
                st.error("Invalid credentials.")
                
    with tab2:
        fn = st.text_input("First Name")
        ln = st.text_input("Last Name")
        em = st.text_input("New Email")
        pw = st.text_input("New Password", type="password")
        if st.button("Register"):
            if register_user(fn, ln, em, pw):
                st.success("Account created! Please sign in.")
            else:
                st.error("Email already exists.")

def seat_selection_page():
    movie = st.session_state.selected_movie
    st.title(f"Visual Booking: {movie['title']}")
    st.write("---")
    
    st.markdown("<div style='text-align: center; border-top: 3px solid #555; margin: 20px auto; width: 60%; color: #555;'>SCREEN</div>", unsafe_allow_html=True)
    
    # 10x10 Seat Grid
    if 'selected_seats' not in st.session_state:
        st.session_state.selected_seats = set()

    rows = ["A", "B", "C", "D", "E", "F"]
    for row in rows:
        cols = st.columns(10)
        for i in range(1, 11):
            seat_id = f"{row}{i}"
            with cols[i-1]:
                is_selected = seat_id in st.session_state.selected_seats
                if st.button(seat_id, key=f"btn_{seat_id}", 
                             type="primary" if is_selected else "secondary",
                             use_container_width=True):
                    if is_selected:
                        st.session_state.selected_seats.remove(seat_id)
                    else:
                        st.session_state.selected_seats.add(seat_id)
                    st.rerun()

    st.write("---")
    if st.session_state.selected_seats:
        selected_list = ", ".join(sorted(list(st.session_state.selected_seats)))
        st.write(f"**Selected Seats:** {selected_list}")
        total = len(st.session_state.selected_seats) * 350
        st.write(f"**Total Price:** ₹{total}")
        
        if st.button("Confirm Booking"):
            st.balloons()
            st.success("Congratulations! Your tickets are booked.")
            time.sleep(2)
            st.session_state.selected_seats = set()
            st.session_state.page = "Home"
            st.rerun()

# --- ROUTING ---
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Auth":
    auth_page()
elif st.session_state.page == "Seat Selection":
    seat_selection_page()
elif st.session_state.page == "Bookings":
    st.title("My Bookings")
    st.info("Feature coming soon! Explore the UI for now.")
    if st.button("Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

