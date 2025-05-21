from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from backend import routes

if __name__ == '__main__':
    app.run(debug=True)

'''


from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.app import db
from backend.models import Table, Booking, User  # <-- import Booking & User

bp = Blueprint('api', __name__)

@bp.route('/api/login', methods=['POST'])
def login():
    # implement login_user() using User.check_password()

@bp.route('/api/logout', methods=['POST'])
@login_required
def logout():
    # call logout_user()


@bp.route('/api/bookings', methods=['GET'])
@login_required
def get_bookings():
    return jsonify([b.to_dict() for b in Booking.query.filter_by(user_id=current_user.id)])

@bp.route('/api/bookings', methods=['POST'])
@login_required
def create_booking():
    data = request.get_json() or {}
    table_id = data.get('table_id')
    if not table_id:
        return jsonify({'error':'Missing table_id'}), 400
    b = Booking(table_id=table_id, user_id=current_user.id)
    db.session.add(b)
    db.session.commit()
    return jsonify(b.to_dict()), 201

# ─── Create & seed tables exactly once, before the first request ───────────────
@app.before_first_request
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
                table_image="table1.png"
            ),
            Table(
                theme="Philosophy",
                topic="Virtue Ethics",
                tagline="Being a Good Person",
                time="3:30 PM",
                date="Thursday",
                table_image="table1.png"
            ),
            Table(
                theme="Science",
                topic="The Big Bang Theory",
                tagline="How did the Universe Begin?",
                time="1:00 PM",
                date="Friday",
                table_image="table1.png"
            ),
            Table(
                theme="Technology",
                topic="Artificial Intelligence",
                tagline="The Future of Work",
                time="11:00 AM",
                date="Saturday",
                table_image="table1.png"
            ),
            Table(
                theme="History",
                topic="The Renaissance",
                tagline="A Cultural Rebirth",
                time="10:00 AM",
                date="Sunday",
                table_image="table1.png"
            ),
        ])
        db.session.commit()

# ─── Optional: run directly with `python -m backend.app` ────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
'''