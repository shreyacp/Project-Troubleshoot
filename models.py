from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def __init__(self, id, username, password):
    self.id = id
    self.username = username
    self.set_password(password)

  def set_password(self, password):
    self.password = generate_password_hash(password, method='sha256')

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def __repr__(self):
    return f'<User {self.id}: {self.username}>'

class Workout(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(120), nullable=False)
  bodypart = db.Column(db.String(120), nullable=False)
  equipment = db.Column(db.String(120), nullable=False)
  level = db.Column(db.String(120), nullable=False)
  rating = db.Column(db.Float, nullable=False)

  def __init__(self, title, description, bodypart, equipment, level, rating):
    self.title = title
    self.description = description
    self.bodypart = bodypart
    self.equipment = equipment
    self.level = level
    self.rating = rating

class Routine(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  user = db.relationship('User', backref=db.backref('routine', lazy=True))
  workout = db.relationship('Workout', backref=db.backref('routine', lazy=True))

  def __init__(self, id, name, workout_id, user_id):
    self.id = id
    self.name = name
    self.workout_id = workout_id
    self.user_id = user_id