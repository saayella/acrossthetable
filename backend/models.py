# backend/models.py
from datetime import datetime
from backend.app import db

class Table(db.Model):
    __tablename__ = 'table'
    id          = db.Column(db.Integer, primary_key=True)
    theme       = db.Column(db.String(100), nullable=False)
    topic       = db.Column(db.String(100), nullable=False)
    tagline     = db.Column(db.String(200), nullable=False)
    time        = db.Column(db.String(50),  nullable=False)
    date        = db.Column(db.String(50),  nullable=False)
    table_image = db.Column(db.String(200), nullable=False)
    student    = db.Column(db.String(100), nullable=False)
    student_image = db.Column(db.String(200), nullable=True)

# models.py
class Booking(db.Model):
    __tablename__ = 'booking'
    id         = db.Column(db.Integer, primary_key=True)
    table_id   = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    timestamp  = db.Column(db.DateTime, default=datetime.utcnow)
    table      = db.relationship('Table')  # <-- Ensure this line is here

    def to_dict(self):
        return {
            'id': self.id,
            'table_id': self.table_id,
            'theme': self.table.theme,
            'topic': self.table.topic,
            'time': self.table.time,
            'date': self.table.date,
            'tagline': self.table.tagline,
            'student': self.table.student,
            'table_image': self.table.table_image,
            'start_time': self.table.start_time if hasattr(self.table, 'start_time') else None,
            'video_link': self.table.video_link if hasattr(self.table, 'video_link') else None
        }

