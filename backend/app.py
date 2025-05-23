from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ─── Configuration ─────────────────────────────────────────────────────────────
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ─── Extensions ────────────────────────────────────────────────────────────────
CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)

# ─── Import models before routes/seeding ────────────────────────────────────────
from backend.models import Table, Booking

# ─── Register the API blueprint ────────────────────────────────────────────────
from backend.routes import bp as api_bp
app.register_blueprint(api_bp)

# ─── Create & seed tables ONCE at startup ──────────────────────────────────────
@app.before_request
def create_and_seed():
    db.create_all()
    if not Table.query.first():
        db.session.add_all([
            Table(
                theme="Politics",
                topic="America's Tariff Policy",
                tagline="Recession or Growth?",
                time="2:00 PM",
                date="Wednesday",
                table_image="table1.png",
                student="John Doe",
                student_image="student1.png"
            ),
            Table(
                theme="Philosophy",
                topic="Virtue Ethics",
                tagline="Being a Good Person",
                time="3:30 PM",
                date="Thursday",
                table_image="table2.png",
                student="Rosa Johnson",
                student_image="student2.png"
            ),
            Table(
                theme="Science",
                topic="The Big Bang Theory",
                tagline="How did the Universe Begin?",
                time="1:00 PM",
                date="Friday",
                table_image="table3.png",
                student="Michael Brown",
                student_image="student3.png"
            ),
            Table(
                theme="Tech",
                topic="Artificial Intelligence",
                tagline="The Future of Work",
                time="11:00 AM",
                date="Saturday",
                table_image="table4.png",
                student="Alison Smith",
                student_image="student4.png"
            ),
            Table(
                theme="History",
                topic="The Renaissance",
                tagline="A Cultural Rebirth",
                time="10:00 AM",
                date="Sunday",
                table_image="table5.png",
                student="David Wilson",
                student_image="student5.png"
            ),
        ])
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
