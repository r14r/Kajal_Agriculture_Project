# Django Backend - Quick Reference Guide

## Installation & Setup

```bash
# 1. Navigate to backend
cd backend.django

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser
```

## Running the Server

```bash
# Development (default port 8000)
python manage.py runserver

# Custom port
python manage.py runserver 0.0.0.0:5000

# Production (Gunicorn)
gunicorn agri_project.wsgi:application --bind 0.0.0.0:8000
```

## Common Commands

```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Shell (interactive Python with Django)
python manage.py shell

# Check for issues
python manage.py check

# Show SQL for a migration
python manage.py sqlmigrate agri_app 0001
```

## Project Structure

```
backend.django/
├── manage.py           # Management script
├── requirements.txt    # Dependencies
├── README.md          # Full documentation
│
├── agri_project/       # Project settings
│   ├── settings.py            # Main settings
│   ├── settings_dev.py        # Dev overrides
│   ├── settings_prod.py       # Prod settings
│   ├── urls.py                # URL routing
│   ├── wsgi.py                # WSGI config
│   └── asgi.py                # ASGI config
│
└── agri_app/          # Main application
    ├── models.py             # Database models
    ├── views.py              # API handlers
    ├── urls.py               # App routes
    ├── admin.py              # Admin config
    ├── ai_engine.py          # AI engine
    ├── migrations/           # DB migrations
    └── templates/            # HTML templates
```

## API Endpoints

### Health
```
GET /api/health/        → Health check
GET /api/stats/         → Get statistics
```

### Farmers
```
GET    /api/farmers/           → List all
POST   /api/farmers/           → Create
GET    /api/farmers/<id>/      → Get one
PUT    /api/farmers/<id>/      → Update
DELETE /api/farmers/<id>/      → Delete
```

### Soil Records
```
GET    /api/records/soil/         → List all
POST   /api/records/soil/         → Create
GET    /api/records/soil/<id>/    → Get one
PUT    /api/records/soil/<id>/    → Update
DELETE /api/records/soil/<id>/    → Delete
```

### Water Records
```
GET    /api/records/water/        → List all
POST   /api/records/water/        → Create
GET    /api/records/water/<id>/   → Get one
PUT    /api/records/water/<id>/   → Update
DELETE /api/records/water/<id>/   → Delete
```

### Crop Records
```
GET    /api/records/crops/        → List all
POST   /api/records/crop/         → Create
GET    /api/records/crop/<id>/    → Get one
PUT    /api/records/crop/<id>/    → Update
DELETE /api/records/crop/<id>/    → Delete
```

### AI Suggestions
```
POST /api/suggest/      → Get AI recommendations
```

## Model Fields

### Farmer
- `id` (int, PK)
- `name` (str, required)
- `phone` (str, optional)
- `location` (str, optional)
- `created_at` (datetime, auto)

### CropRecord
- `id` (int, PK)
- `farmer` (FK to Farmer)
- `crop_name` (str, required)
- `yield_kg` (float, optional)
- `date_recorded` (str, optional)
- `planted_on` (datetime, auto)
- `notes` (text, optional)

### SoilRecord
- `id` (int, PK)
- `farmer` (FK to Farmer)
- `ph` (float, optional)
- `nitrogen` (float, optional)
- `phosphorus` (float, optional)
- `potassium` (float, optional)
- `moisture` (float, optional)
- `soil_type` (str, optional)
- `date_recorded` (str, optional)
- `recorded_at` (datetime, auto)
- `notes` (text, optional)

### WaterRecord
- `id` (int, PK)
- `farmer` (FK to Farmer)
- `ph` (float, optional)
- `ec` (float, optional)
- `tds` (float, optional)
- `amount_l` (float, optional)
- `date_recorded` (str, optional)
- `recorded_at` (datetime, auto)
- `notes` (text, optional)

## Settings Configuration

### Development
```python
DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
DATABASE = SQLite (agri_data.db)
```

### Production
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
CORS_ALLOWED_ORIGINS = ['https://yourdomain.com']
DATABASE = PostgreSQL (recommended)
```

## Admin Interface

Access at: `http://localhost:8000/admin/`

- Login with superuser credentials
- Manage all models through admin
- Add/Edit/Delete records
- Advanced filtering and searching

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test agri_app

# Run specific test class
python manage.py test agri_app.tests.TestName

# With verbose output
python manage.py test --verbosity=2

# Specific test method
python manage.py test agri_app.tests.TestName.test_method
```

## Database Operations

```bash
# Create backup
sqlite3 agri_data.db ".dump" > backup.sql

# Restore from backup
sqlite3 agri_data.db < backup.sql

# Access database shell
python manage.py dbshell

# Reset database (caution!)
rm agri_data.db
python manage.py migrate
```

## Example API Calls

### Create a Farmer
```bash
curl -X POST http://localhost:8000/api/farmers/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "phone": "9876543210",
    "location": "Maharashtra"
  }'
```

### Get All Farmers
```bash
curl http://localhost:8000/api/farmers/
```

### Get AI Suggestions
```bash
curl -X POST http://localhost:8000/api/suggest/ \
  -H "Content-Type: application/json" \
  -d '{
    "soil_ph": 6.5,
    "moisture": 45,
    "soil_type": "loamy",
    "crop": "wheat"
  }'
```

## Troubleshooting

### 1. Port already in use
```bash
# Find process on port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Use different port
python manage.py runserver 0.0.0.0:5000
```

### 2. ModuleNotFoundError
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Update pip
pip install --upgrade pip
```

### 3. Database errors
```bash
# Reset migrations
python manage.py migrate --zero agri_app
python manage.py migrate

# Or reset completely
rm db.sqlite3
python manage.py migrate
```

### 4. Permission denied (migrations)
```bash
# Make scripts executable
chmod +x manage.py

# On Windows, should work automatically
```

## Deployment Checklist

- [ ] Set DEBUG = False
- [ ] Change SECRET_KEY
- [ ] Update ALLOWED_HOSTS
- [ ] Configure CORS origins
- [ ] Setup database (PostgreSQL)
- [ ] Collect static files
- [ ] Configure email settings
- [ ] Setup logging
- [ ] Use environment variables
- [ ] Enable HTTPS/SSL
- [ ] Setup monitoring
- [ ] Backup database regularly

## Useful Links

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Database Docs: https://sqlite.org/
- Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/

## Version Info

- Django: 4.2.0
- Python: 3.8+
- Database: SQLite (default) / PostgreSQL (production)
- API Style: REST
- CORS: Enabled

---

**Last Updated**: January 2026
**Status**: Production Ready ✓
