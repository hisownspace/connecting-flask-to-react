from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  age = db.Column(db.Integer)
  password = db.Column(db.String(50), nullable=False)
