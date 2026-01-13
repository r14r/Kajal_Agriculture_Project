# Migration from Flask to Django

## Overview
This Django backend is a direct migration of the Flask-based Smart Agriculture Management System. It maintains API compatibility while leveraging Django's built-in features like ORM, admin panel, and security.

## Key Changes from Flask

### Framework
- **Flask** → **Django** 4.2
- Manual SQLAlchemy models → Django ORM models
- Flask blueprints → Django app-based routing

### Database
- **SQLAlchemy ORM** → **Django ORM**
- Manual session management → Django's automatic connection pooling
- Same SQLite database file (agri_data.db)

### API Structure
- Flask route decorators → Django URL patterns and views
- Manual JSON responses → Django JsonResponse
- Manual CORS setup → django-cors-headers middleware

### Admin Interface
- No admin in Flask → Django built-in admin panel
- Custom admin templates → Django admin customization

### File Structure
```
Flask Version (backend/):
├── app.py
├── models.py
├── ai_engine.py
├── templates/

Django Version (backend.django/):
├── manage.py
├── agri_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── agri_app/              # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
├── requirements.txt
└── README.md
```

## API Compatibility

All endpoints remain the same:
- `/api/health/` - Health check
- `/api/farmers/` - Farmer CRUD
- `/api/records/soil/` - Soil records
- `/api/records/water/` - Water records
- `/api/records/crops/` - Crop records
- `/api/suggest/` - AI suggestions
- `/admin/` - Admin dashboard

## Migration Notes

### Advantages of Django Version
1. **Admin Interface** - Built-in Django admin for easy data management
2. **ORM Benefits** - Better query optimization and security
3. **Middleware** - Built-in CSRF protection, security headers
4. **Scalability** - Better suited for production deployments
5. **Community** - Larger ecosystem and third-party packages
6. **Testing** - Built-in testing framework

### Running the Django Version

```bash
# Setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Initialize database
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

### Data Migration
If migrating from the Flask version:
1. Keep the original `agri_data.db` file
2. Django ORM will automatically work with the existing schema
3. Run `python manage.py migrate` to ensure schema is up-to-date

## Deployment

### Development
```bash
python manage.py runserver 0.0.0.0:8000
```

### Production
```bash
# Using Gunicorn
gunicorn agri_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

## Future Enhancements

- Add DRF (Django REST Framework) for better API documentation
- Implement JWT authentication
- Add Celery for background tasks (e.g., AI processing)
- Add signals for automated logging
- Implement caching with Redis
