from app import db

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(50))
    date = db.Column(db.Date)
    grade = db.Column(db.String(50))
    country = db.Column(db.String(100))
    comments = db.Column(db.Text)
    how_did_you_find_us = db.Column(db.String(50))
    semester = db.Column(db.String(255))    # comma-separated for multi-select
    stage = db.Column(db.String(255))       # comma-separated for multi-select

    def __repr__(self):
        return f"<Lead {self.name}>"
