from flask import Blueprint, jsonify
from .models import Table

routes = Blueprint('routes', __name__)

@routes.route('/api/tables')
def get_tables():
    return jsonify([{ "id": t.id, "theme": t.theme  , "topic": t.topic, "tagline": t.tagline, "time": t.time, "date": t.date, "table_image": t.table_image
                     } for t in Table.query.all()])
