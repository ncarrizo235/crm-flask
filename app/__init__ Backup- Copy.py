from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///local.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models import Lead

@app.route("/")
def index():
    leads = Lead.query.all()
    return render_template("index.html", leads=leads)

@app.route("/add", methods=["POST"])
def add_lead():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")

    new_lead = Lead(name=name, email=email, phone=phone)
    db.session.add(new_lead)
    db.session.commit()

    return redirect(url_for("index"))
