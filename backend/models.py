from backend.app import db
from datetime import datetime

class User(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(120))
    email        = db.Column(db.String(120), unique=True)
    password     = db.Column(db.String(120))
    senior_icon  = db.Column(db.String(255))


class Student(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(120))
    email         = db.Column(db.String(120), unique=True)
    student_icon  = db.Column(db.String(255))


class Table(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'))
    student_id    = db.Column(db.Integer, db.ForeignKey('student.id'))

    theme         = db.Column(db.String(100))
    topic         = db.Column(db.Text)
    tagline       = db.Column(db.String(255))
    time          = db.Column(db.String(50))
    date          = db.Column(db.String(50))
    table_image   = db.Column(db.String(255))

    user          = db.relationship('User', backref='tables')
    student       = db.relationship('Student', backref='tables')


class Booking(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    table_id      = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp     = db.Column(db.DateTime, default=datetime.utcnow)

    table         = db.relationship('Table', backref='bookings')
    user          = db.relationship('User', backref='bookings')

    def to_dict(self):
        return {
            "id":           self.id,
            "table_id":     self.table_id,
            "theme":        self.table.theme,
            "tagline":      self.table.tagline,
            "time":         self.table.time,
            "date":         self.table.date,
            "table_image":  self.table.table_image,
            "booked_at":    self.timestamp.isoformat()
        }