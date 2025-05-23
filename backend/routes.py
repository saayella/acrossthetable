from flask import Blueprint, request, jsonify
from backend.app import db
from backend.models import Table, Booking
import traceback
bp = Blueprint('api', __name__)

@bp.route('/api/tables', methods=['GET'])
def get_tables():
    tables = Table.query.all()
    return jsonify([
        {
            'id':          t.id,
            'topic':       t.topic,
            'theme':       t.theme,
            'tagline':     t.tagline,
            'time':        t.time,
            'date':        t.date,
            'table_image': t.table_image,
            'student':     t.student,
            'student_image': t.student_image
            
        }
        for t in tables
    ])

@bp.route('/api/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.order_by(Booking.timestamp.desc()).all()
    return jsonify([b.to_dict() for b in bookings])

@bp.route('/api/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json(force=True) or {}
        table_id = data.get('table_id')
        if not table_id:
            return jsonify({'error': 'Missing table_id'}), 400

        # Attempt to create and save the booking
        b = Booking(table_id=table_id)
        db.session.add(b)
        db.session.commit()
        return jsonify(b.to_dict()), 201

    except Exception as e:
        # Print full traceback in your Flask console
        traceback.print_exc()
        # Return the error message in the HTTP response
        return jsonify({
            'error': 'Server error',
            'details': str(e)
        }), 500
@bp.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    db.session.delete(booking)
    db.session.commit()
    return jsonify({'message': 'Booking cancelled'}), 200