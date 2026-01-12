"""Minimal Flask backend for Smart Agriculture Management System.

Provides simple JSON APIs to store farmer/crop/soil/water data and request suggestions
from the built-in rule-based `ai_engine`.

Run: python backend/app.py
"""
from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import CORS
from sqlalchemy.exc import SQLAlchemyError
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from models import init_db, get_session, Farmer, CropRecord, SoilRecord, WaterRecord
from ai_engine import suggest_actions
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"sqlite:///{os.path.join(os.path.dirname(BASE_DIR), 'agri_data.db')}"

engine = init_db(DB_PATH)

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

# Enable CORS for all routes - allows frontend to make API requests
CORS(app, resources={r"/api/*": {"origins": "*"}})


def session_scope():
    session = get_session(engine)
    try:
        yield session
    finally:
        session.close()


@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'time': 'now'})


@app.route('/')
def index():
    # Helpful root route to avoid a 404 when visiting the server root
    return jsonify({
        'service': 'Smart Agriculture Backend',
        'status': 'running',
        'endpoints': ['/api/health', '/api/farmers', '/api/records/soil', '/api/suggest'],
        'admin': '/admin/'
    })


@app.route('/admin/')
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/admin/farmers')
def admin_farmers():
    return render_template('admin_farmers.html')


@app.route('/admin/crops')
def admin_crops():
    return render_template('admin_crops.html')


@app.route('/admin/soil')
def admin_soil():
    return render_template('admin_soil.html')


@app.route('/admin/water')
def admin_water():
    return render_template('admin_water.html')


@app.route('/api/stats')
def stats():
    """Get counts of all records for dashboard display."""
    try:
        from sqlalchemy import text
        session = get_session(engine)
        
        farmers_count = session.query(Farmer).count() if Farmer else 0
        crops_count = session.query(CropRecord).count() if CropRecord else 0
        soil_count = session.query(SoilRecord).count() if SoilRecord else 0
        water_count = session.query(WaterRecord).count() if WaterRecord else 0
        
        session.close()
        
        return jsonify({
            'farmers': int(farmers_count),
            'crops': int(crops_count),
            'soil': int(soil_count),
            'water': int(water_count)
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e), 'farmers': 0, 'crops': 0, 'soil': 0, 'water': 0}), 200


@app.route('/api/farmers', methods=['POST'])
def create_farmer():
    data = request.get_json() or {}
    name = data.get('name')
    if not name:
        return jsonify({'error': 'name is required'}), 400

    session = get_session(engine)
    try:
        f = Farmer(name=name, phone=data.get('phone'), location=data.get('location'))
        session.add(f)
        session.commit()
        return jsonify({'id': f.id, 'name': f.name}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/farmers', methods=['GET'])
def list_farmers():
    session = get_session(engine)
    try:
        rows = session.query(Farmer).all()
        out = [{'id': r.id, 'name': r.name, 'phone': r.phone, 'region': r.location} for r in rows]
        return jsonify(out)
    finally:
        session.close()


@app.route('/api/farmers/<int:farmer_id>', methods=['GET'])
def get_farmer(farmer_id):
    """Get a specific farmer by ID."""
    session = get_session(engine)
    try:
        farmer = session.query(Farmer).filter_by(id=farmer_id).first()
        if not farmer:
            return jsonify({'error': 'Farmer not found'}), 404
        return jsonify({
            'id': farmer.id,
            'name': farmer.name,
            'phone': farmer.phone,
            'region': farmer.location
        })
    finally:
        session.close()


@app.route('/api/farmers/<int:farmer_id>', methods=['PUT'])
def update_farmer(farmer_id):
    """Update a farmer record."""
    data = request.get_json() or {}
    session = get_session(engine)
    try:
        farmer = session.query(Farmer).filter_by(id=farmer_id).first()
        if not farmer:
            return jsonify({'error': 'Farmer not found'}), 404
        
        farmer.name = data.get('name', farmer.name)
        farmer.phone = data.get('phone', farmer.phone)
        farmer.location = data.get('region', farmer.location)
        
        session.commit()
        return jsonify({'id': farmer.id, 'name': farmer.name}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/farmers/<int:farmer_id>', methods=['DELETE'])
def delete_farmer(farmer_id):
    """Delete a farmer record."""
    session = get_session(engine)
    try:
        farmer = session.query(Farmer).filter_by(id=farmer_id).first()
        if not farmer:
            return jsonify({'error': 'Farmer not found'}), 404
        
        session.delete(farmer)
        session.commit()
        return jsonify({'success': True}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/soil', methods=['POST'])
def add_soil_record():
    data = request.get_json() or {}
    farmer_id = data.get('farmer_id')
    session = get_session(engine)
    try:
        rec = SoilRecord(
            farmer_id=farmer_id,
            ph=data.get('ph'),
            nitrogen=data.get('nitrogen'),
            phosphorus=data.get('phosphorus'),
            potassium=data.get('potassium'),
            date_recorded=data.get('date_recorded') or datetime.now().isoformat()
        )
        session.add(rec)
        session.commit()
        return jsonify({'id': rec.id}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/soil', methods=['GET'])
def list_soil_records():
    """List all soil records."""
    session = get_session(engine)
    try:
        rows = session.query(SoilRecord).all()
        out = [{
            'id': r.id,
            'farmer_id': r.farmer_id,
            'ph': r.ph,
            'nitrogen': r.nitrogen,
            'phosphorus': r.phosphorus,
            'potassium': r.potassium,
            'date_recorded': r.date_recorded
        } for r in rows]
        return jsonify(out)
    finally:
        session.close()


@app.route('/api/records/soil/<int:record_id>', methods=['GET'])
def get_soil_record(record_id):
    """Get a specific soil record."""
    session = get_session(engine)
    try:
        rec = session.query(SoilRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        return jsonify({
            'id': rec.id,
            'farmer_id': rec.farmer_id,
            'ph': rec.ph,
            'nitrogen': rec.nitrogen,
            'phosphorus': rec.phosphorus,
            'potassium': rec.potassium,
            'date_recorded': rec.date_recorded
        })
    finally:
        session.close()


@app.route('/api/records/soil/<int:record_id>', methods=['PUT'])
def update_soil_record(record_id):
    """Update a soil record."""
    data = request.get_json() or {}
    session = get_session(engine)
    try:
        rec = session.query(SoilRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        
        rec.farmer_id = data.get('farmer_id', rec.farmer_id)
        rec.ph = data.get('ph', rec.ph)
        rec.nitrogen = data.get('nitrogen', rec.nitrogen)
        rec.phosphorus = data.get('phosphorus', rec.phosphorus)
        rec.potassium = data.get('potassium', rec.potassium)
        rec.date_recorded = data.get('date_recorded', rec.date_recorded)
        
        session.commit()
        return jsonify({'id': rec.id}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/soil/<int:record_id>', methods=['DELETE'])
def delete_soil_record(record_id):
    """Delete a soil record."""
    session = get_session(engine)
    try:
        rec = session.query(SoilRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        
        session.delete(rec)
        session.commit()
        return jsonify({'success': True}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/water', methods=['POST'])
def add_water_record():
    data = request.get_json() or {}
    session = get_session(engine)
    try:
        rec = WaterRecord(
            farmer_id=data.get('farmer_id'),
            ph=data.get('ph'),
            ec=data.get('ec'),
            tds=data.get('tds'),
            date_recorded=data.get('date_recorded') or datetime.now().isoformat()
        )
        session.add(rec)
        session.commit()
        return jsonify({'id': rec.id}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/water', methods=['GET'])
def list_water_records():
    """List all water records."""
    session = get_session(engine)
    try:
        rows = session.query(WaterRecord).all()
        out = [{
            'id': r.id,
            'farmer_id': r.farmer_id,
            'ph': r.ph,
            'ec': r.ec,
            'tds': r.tds,
            'date_recorded': r.date_recorded
        } for r in rows]
        return jsonify(out)
    finally:
        session.close()


@app.route('/api/records/water/<int:record_id>', methods=['GET'])
def get_water_record(record_id):
    """Get a specific water record."""
    session = get_session(engine)
    try:
        rec = session.query(WaterRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        return jsonify({
            'id': rec.id,
            'farmer_id': rec.farmer_id,
            'ph': rec.ph,
            'ec': rec.ec,
            'tds': rec.tds,
            'date_recorded': rec.date_recorded
        })
    finally:
        session.close()


@app.route('/api/records/water/<int:record_id>', methods=['PUT'])
def update_water_record(record_id):
    """Update a water record."""
    data = request.get_json() or {}
    session = get_session(engine)
    try:
        rec = session.query(WaterRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        
        rec.farmer_id = data.get('farmer_id', rec.farmer_id)
        rec.ph = data.get('ph', rec.ph)
        rec.ec = data.get('ec', rec.ec)
        rec.tds = data.get('tds', rec.tds)
        rec.date_recorded = data.get('date_recorded', rec.date_recorded)
        
        session.commit()
        return jsonify({'id': rec.id}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/water/<int:record_id>', methods=['DELETE'])
def delete_water_record(record_id):
    """Delete a water record."""
    session = get_session(engine)
    try:
        rec = session.query(WaterRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        
        session.delete(rec)
        session.commit()
        return jsonify({'success': True}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/crop', methods=['POST'])
def add_crop_record():
    data = request.get_json() or {}
    session = get_session(engine)
    try:
        rec = CropRecord(
            farmer_id=data.get('farmer_id'),
            crop_name=data.get('crop_name'),
            yield_kg=data.get('yield_kg'),
            date_recorded=data.get('date_recorded') or datetime.now().isoformat()
        )
        session.add(rec)
        session.commit()
        return jsonify({'id': rec.id}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/crops', methods=['GET'])
def list_crop_records():
    """List all crop records."""
    session = get_session(engine)
    try:
        rows = session.query(CropRecord).all()
        out = [{
            'id': r.id,
            'farmer_id': r.farmer_id,
            'crop_name': r.crop_name,
            'yield_kg': r.yield_kg,
            'date_recorded': r.date_recorded
        } for r in rows]
        return jsonify(out)
    finally:
        session.close()


@app.route('/api/records/crop/<int:record_id>', methods=['GET'])
def get_crop_record(record_id):
    """Get a specific crop record."""
    session = get_session(engine)
    try:
        rec = session.query(CropRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        return jsonify({
            'id': rec.id,
            'farmer_id': rec.farmer_id,
            'crop_name': rec.crop_name,
            'yield_kg': rec.yield_kg,
            'date_recorded': rec.date_recorded
        })
    finally:
        session.close()


@app.route('/api/records/crop/<int:record_id>', methods=['PUT'])
def update_crop_record(record_id):
    """Update a crop record."""
    data = request.get_json() or {}
    session = get_session(engine)
    try:
        rec = session.query(CropRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        
        rec.farmer_id = data.get('farmer_id', rec.farmer_id)
        rec.crop_name = data.get('crop_name', rec.crop_name)
        rec.yield_kg = data.get('yield_kg', rec.yield_kg)
        rec.date_recorded = data.get('date_recorded', rec.date_recorded)
        
        session.commit()
        return jsonify({'id': rec.id}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/records/crop/<int:record_id>', methods=['DELETE'])
def delete_crop_record(record_id):
    """Delete a crop record."""
    session = get_session(engine)
    try:
        rec = session.query(CropRecord).filter_by(id=record_id).first()
        if not rec:
            return jsonify({'error': 'Record not found'}), 404
        
        session.delete(rec)
        session.commit()
        return jsonify({'success': True}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@app.route('/api/suggest', methods=['POST'])
def suggest():
    data = request.get_json() or {}
    # Accept payload like: { farmer_id, soil_ph, moisture, soil_type, crop, days_since_last_water }
    result = suggest_actions(data)
    return jsonify(result)


if __name__ == '__main__':
    # Run dev server
    app.run(host='0.0.0.0', port=5000, debug=False)
