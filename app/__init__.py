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
    telefono = request.form.get("telefono")
    date = request.form.get("date") or None
    grade = request.form.get("grade")
    country = request.form.get("country")
    comments = request.form.get("comments")
    how_did_you_find_us = request.form.get("how_did_you_find_us")

    semester = request.form.getlist("semester")
    stage = request.form.getlist("stage")

    semester_str = ",".join(semester)
    stage_str = ",".join(stage)

    new_lead = Lead(
        name=name,
        email=email,
        telefono=telefono,
        date=date,
        grade=grade,
        country=country,
        comments=comments,
        how_did_you_find_us=how_did_you_find_us,
        semester=semester_str,
        stage=stage_str
    )
    db.session.add(new_lead)
    db.session.commit()

    return redirect(url_for("index"))