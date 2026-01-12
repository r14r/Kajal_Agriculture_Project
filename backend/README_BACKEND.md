Smart Agriculture Backend
=========================

This folder contains a minimal Flask backend with SQLite (SQLAlchemy) and a small rule-based AI engine.

Quick start
-----------

1. Create a virtual environment and activate it (Windows PowerShell example):

```powershell
python -m venv venv
.\n+venv\Scripts\Activate.ps1
```

2. Install requirements (project `requirements.txt` already contains Flask and related libs):

```bash
pip install -r requirements.txt
```

3. Run the backend:

```bash
python backend/app.py
```

4. Open `http://localhost:5000/api/health` to verify.

APIs
----

- `GET /api/health` - health check
- `POST /api/farmers` - create farmer {name, phone, location}
- `GET /api/farmers` - list farmers
- `POST /api/records/soil` - add soil reading {farmer_id, ph, moisture, soil_type, notes}
- `POST /api/records/water` - add water record {farmer_id, amount_l, notes}
- `POST /api/records/crop` - add crop record {farmer_id, crop_name, notes}
- `POST /api/suggest` - request suggestions (payload may include soil_ph, moisture, soil_type, crop, days_since_last_water)

Notes
-----
- The AI engine is rule-based and explainable (`backend/ai_engine.py`).
- Database file is created at project root as `agri_data.db`.
 
Production (recommended vs. dev server)
-------------------------------------

The built-in Flask development server (`python backend/app.py`) shows the warning "This is a development server".
To run in production or on a LAN reliably, use a WSGI server such as **Waitress** (cross-platform, works well on Windows) or **Gunicorn** (Linux/macOS).

Waitress (Windows / cross-platform):

1. Install:

```bash
pip install waitress
```

2. Run the production server from project root:

```bash
python -m backend.run_prod
```

Gunicorn (Linux/macOS):

```bash
pip install gunicorn
# run from project root
gunicorn backend.app:app --workers 3 --bind 0.0.0.0:5000
```

Firewall / network notes
- If you want to access the server from other machines on your LAN, ensure the host's firewall allows inbound TCP on the chosen port (default 5000).
- On Windows, you can create a firewall rule via PowerShell as Administrator:

```powershell
netsh advfirewall firewall add rule name="Flask 5000" dir=in action=allow protocol=TCP localport=5000
```

Process supervision
- For production, run the server under a process manager (systemd, NSSM on Windows, or a container) so it restarts automatically.
