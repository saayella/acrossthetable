from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # ✅ Important line


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from backend.routes import routes
app.register_blueprint(routes)


@app.before_request
def create_tables():
    from backend.models import Table
    db.create_all()
    if not Table.query.first():
        db.session.add_all([
            Table(
                theme="Politics",
                topic="America's Tariff Policy",
                tagline="Recession or Growth?",
                time="2:00 PM",
                date="Wednesday",
                table_image="images/table1.png"
            ),
            Table(
                theme="Philosophy",
                topic="Virtue Ethics",
                tagline="Being a Good Person",
                time="3:30 PM",
                date="Thursday",
                table_image="images/table1.png"
            ),
            Table(
                theme="Science",
                topic="The Big Bang Theory",
                tagline="How did the Universe Begin?",
                time="1:00 PM",
                date="Friday",
                table_image="/images/table1.png"
            ),
            Table(
                theme="Technology",
                topic="Artificial Intelligence",
                tagline="The Future of Work",
                time="11:00 AM",
                date="Saturday",
                table_image="/images/table1.png"
            ),
            Table(
                theme="History",
                topic="The Renaissance",
                tagline="A Cultural Rebirth",
                time="10:00 AM",
                date="Sunday",
                table_image="/images/table1.png"
            ),
        ])
        db.session.commit()
