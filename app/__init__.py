from flask import Flask, render_template
from .config import Config
from .models import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
  return render_template("base.html")

@app.route("/<string:name>")
def intro(name):
  return render_template("greeting.html", name=name)
