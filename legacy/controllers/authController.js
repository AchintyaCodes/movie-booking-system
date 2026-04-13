const db = require('../config/db');
const bcrypt = require('bcrypt');

// show pages
exports.showLogin = (req, res) => {
  res.render('login');
};

exports.showRegister = (req, res) => {
  res.render('register');
};

// register
exports.register = async (req, res) => {
  const { name, email, password } = req.body;

  const hashedPassword = await bcrypt.hash(password, 10);

  await db.execute(
    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
    [name, email, hashedPassword]
  );

  res.redirect('/login');
};

// login
exports.login = async (req, res) => {
  const { email, password } = req.body;

  const [users] = await db.execute(
    "SELECT * FROM users WHERE email = ?",
    [email]
  );

  if (users.length === 0) {
    return res.send("User not found");
  }

  const user = users[0];

  const match = await bcrypt.compare(password, user.password);

  if (!match) {
    return res.send("Wrong password");
  }

  req.session.userId = user.user_id;

  res.redirect('/');
};

// logout
exports.logout = (req, res) => {
  req.session.destroy();
  res.redirect('/');
};