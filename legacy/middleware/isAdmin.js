module.exports = function isAdmin(req, res, next) {
  if (req.session && req.session.role === 'admin') {
    return next();
  }
  req.flash('error', 'Admins only.');
  res.redirect('/');
};
