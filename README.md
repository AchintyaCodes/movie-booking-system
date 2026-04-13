<h1 align="center">🎬 CineVault: Premium Movie Experience</h1>

<p align="center">
Netflix-style movie booking platform with interactive seat selection & modern glassmorphic UI
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-Live-red?style=for-the-badge&logo=streamlit"/>
  <img src="https://img.shields.io/badge/Backend-SQLite-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Focus-UI%2FUX%20Design-purple?style=for-the-badge"/>
</p>

---

## 🎬 Live Demo

👉 **[Launch CineVault](https://movie-booking-system.streamlit.app/)**
---

## ⚡ App Preview

<p align="center">
  <img src="https://image.tmdb.org/t/p/original/rAiYKRLSXccP66vST1nq1YZvzsz.jpg" width="90%">
</p>

---

# 🧠 Problem Statement

Traditional movie booking systems often feel static and dated. Users expect:
- Immersive cinematic visuals 🎥
- Smooth, reactive animations ⚡
- Highly intuitive seat selection 💺

👉 **CineVault** solves this by porting a legacy system to a modern Python-Streamlit stack with a focus on **Premium Aesthetic Intensity**.

---

# 🚀 Features

### 🎞️ Netflix-Style Intro
- Immersive splash screen with the iconic "N" branding.
- Smooth CSS transitions from intro to store-front.

### 💎 Glassmorphic Design
- Transparent, blurred card layouts for a high-end feel.
- Dynamic hover effects and micro-animations.

### 💺 Visual Seat Selection
- Interactive 10x10 seating grid.
- Real-time selection tracking with dynamic price calculation.

### 🔐 Secure Authentication
- Multi-user support with Bcrypt password hashing.
- Persistent session state for a seamless booking journey.

### ⚙️ Legacy Support
- Includes a `legacy/` directory containing the original Node.js/MySQL implementation.
- Demonstrates full-stack versatility.

---

# ⚙️ How It Works (PROCESS)

### 1️⃣ Database Porting
- Successfully migrated 10+ MySQL tables to a portable **SQLite** instance.
- Automated database seeding for "zero-config" local execution.

### 2️⃣ UI/UX Layering
- Used custom **CSS Keyframes** to create the Netflix splash animation.
- Implemented **Streamlit Session State** to handle multi-page navigation (Home → Auth → Booking).

### 3️⃣ Seat Selection Logic
- Developed a reactive grid where seats are dynamically identified and stored.
- Applied CSS-based button styling to mimic actual cinema seating.

### 4️⃣ Security Integration
- Integrated `bcrypt` for one-way hashing of user credentials.
- Ensured sensitive data is never stored in plain text.

---

# 📊 Documentation

### 🏠 Dashboard
The landing page greets users with a high-definition Hero section and a glassmorphic grid of currently showing movies.

---

### 💺 Seating Grid
The seating engine allows users to visually pick their spots, calculating totals on the fly before finalizing the booking with a "Balloons" celebration.

---

# 📚 What I Learned

This project was a deep dive into:

### 🎨 Visual Engineering
- Controlling Streamlit's look and feel with deep custom CSS.
- Implementing "Aesthetic Intensity" without compromising performance.

### ⚙️ System Migration
- Porting logic from **Node.js/Express** to **Python/Streamlit**.
- Rethinking session handling and database interactions for a single-page app architecture.

### 🛠️ Full-Stack Versatility
- Managing both a modern Python frontend and maintaining legacy Node.js assets in the same repository.

---

# 🛠️ Tech Stack

- 🐍 **Python** (Core Logic)
- 🌐 **Streamlit** (Frontend Framework)
- 🗄️ **SQLite** (Portable Database)
- 🔐 **Bcrypt** (User Security)

---

# 📂 Project Structure

```bash
movie-booking-system/
│
├── streamlit_app.py   # Main Cinema Interface
├── database.py        # SQLite Migration & Logic
├── auth.py            # Security & Session Auth
│
├── static/
│   └── uploads/       # Movie Posters (Interstellar, etc.)
│
├── legacy/            # Original Node.js Project Files
│   ├── app.js         # Express Entry Point
│   └── views/         # EJS Templates
│
├── requirements.txt
└── README.md
```

---

# ⚡ Run Locally

```bash
git clone https://github.com/AchintyaCodes/movie-booking-system.git
cd movie-booking-system

pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

# 🙌 Author

**Achintya Gupta**

- 🚀 Data Science & Engineering Student
- 💡 Passionate about building high-end AI systems and premium UIs

---

<p align="center">
⭐ Star this repo if you love the cinematic experience!
</p>
