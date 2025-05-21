from backend.app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    senior_icon = db.Column(db.String(255))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    student_icon = db.Column(db.String(255))

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    theme = db.Column(db.String(100))
    topic = db.Column(db.Text)
    tagline = db.Column(db.String(255))
    time = db.Column(db.String(50))
    date = db.Column(db.String(50))
    table_image = db.Column(db.String(255))

    user = db.relationship('User', backref='tables')
    student = db.relationship('Student', backref='tables')
