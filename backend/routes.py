from flask import jsonify
from backend.app import app, db
from backend.models import Table

@app.before_request
def create_tables():
    db.create_all()
    if not Table.query.first():
        db.session.add_all([
            Table(
                theme="History",
                topic="The Renaissance",
                tagline="A Cultural Rebirth",
                time="10:00 AM",
                date="Sunday",
                table_image="/images/table-history.jpg"
            ),
            # Add more here...
        ])
        db.session.commit()

@app.route('/api/tables')
def get_tables():
    return jsonify([{
        "id": t.id,
        "theme": t.theme,
        "topic": t.topic,
        "tagline": t.tagline,
        "time": t.time,
        "date": t.date,
        "table_image": t.table_image
    } for t in Table.query.all()])
