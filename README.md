# Hybrid Agriculture Project

This is a hybrid Django application that combines the backend API with the frontend HTML interface.

## Project Structure

```
hybrid/
├── App/               # Django app
│   ├── templates/          # Django templates
│   │   ├── admin_*.html   # Admin interface templates
│   │   └── frontend/      # Frontend HTML pages
│   ├── migrations/         # Database migrations
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   └── urls.py             # URL routing
├── Agriculture/           # Django project settings
│   ├── settings.py         # Main settings
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI configuration
├── static/                 # Static files (CSS, JS)
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
└── manage.py               # Django management script
```

## Features

- **Frontend Pages**: Home, Farmers Directory, Contact
- **API Endpoints**: RESTful API for farmers, crops, soil, and water records
- **Admin Interface**: Django admin for data management
- **AI Integration**: Agricultural suggestions based on data

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Collect static files:
```bash
python manage.py collectstatic
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Access the application:
   - Frontend: http://localhost:8000/
   - API Info: http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/
   - API Docs: http://localhost:8000/docs/

## Available URLs

### Frontend Pages
- `/` or `/index.html` - Home page
- `/farmers.html` - Farmers directory
- `/contact.html` - Contact page

### API Endpoints
- `/api/` - API information
- `/api/health/` - Health check
- `/api/farmers/` - Farmers list and create
- `/api/farmers/<id>/` - Farmer detail
- `/api/records/soil/` - Soil records
- `/api/records/water/` - Water records
- `/api/records/crop/` - Crop records
- `/api/suggest/` - AI suggestions
- `/stats/` - Statistics

### Admin Pages
- `/admin/` - Admin dashboard
- `/admin/farmers/` - Farmers management
- `/admin/crops/` - Crops management
- `/admin/soil/` - Soil records management
- `/admin/water/` - Water records management

## Development

The project uses Django's template system with the `{% static %}` tag to reference CSS and JavaScript files. All static files are collected into the `staticfiles/` directory when running `collectstatic`.

## Database

The project uses SQLite database (`agri_data.db`) located in the parent directory. The database contains:
- Farmer records
- Crop records
- Soil records
- Water records
