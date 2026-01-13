# Django Backend - Green Farming Agriculture System

This is the Django version of the Smart Agriculture Management System backend.

## Quick Start

### 1. Setup Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
cd backend.django
pip install -r requirements.txt
```

### 3. Create Database and Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

The server will start at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /api/health/` - Health check endpoint
- `GET /api/stats/` - Get statistics (farmers, crops, soil, water counts)

### Farmer Management
- `GET /api/farmers/` - List all farmers
- `POST /api/farmers/` - Create a new farmer
- `GET /api/farmers/<id>/` - Get a specific farmer
- `PUT /api/farmers/<id>/` - Update a farmer
- `DELETE /api/farmers/<id>/` - Delete a farmer

### Soil Records
- `GET /api/records/soil/` - List all soil records
- `POST /api/records/soil/` - Create a new soil record
- `GET /api/records/soil/<id>/` - Get a specific soil record
- `PUT /api/records/soil/<id>/` - Update a soil record
- `DELETE /api/records/soil/<id>/` - Delete a soil record

### Water Records
- `GET /api/records/water/` - List all water records
- `POST /api/records/water/` - Create a new water record
- `GET /api/records/water/<id>/` - Get a specific water record
- `PUT /api/records/water/<id>/` - Update a water record
- `DELETE /api/records/water/<id>/` - Delete a water record

### Crop Records
- `GET /api/records/crops/` - List all crop records
- `POST /api/records/crop/` - Create a new crop record
- `GET /api/records/crop/<id>/` - Get a specific crop record
- `PUT /api/records/crop/<id>/` - Update a crop record
- `DELETE /api/records/crop/<id>/` - Delete a crop record

### AI Suggestions
- `POST /api/suggest/` - Get AI suggestions for agricultural actions

### Admin Interface
- `GET /admin/` - Django admin panel (requires login)
- `GET /admin/` (custom) - Admin dashboard
- `GET /admin/farmers/` - Manage farmers
- `GET /admin/crops/` - Manage crops
- `GET /admin/soil/` - Manage soil records
- `GET /admin/water/` - Manage water records

## Database

The application uses SQLite by default. The database file is stored as `agri_data.db` in the project root.

### Database Models

1. **Farmer** - Stores farmer information
   - id, name, phone, location, created_at

2. **CropRecord** - Stores crop-related data
   - id, farmer_id, crop_name, yield_kg, date_recorded, planted_on, notes

3. **SoilRecord** - Stores soil analysis data
   - id, farmer_id, ph, nitrogen, phosphorus, potassium, moisture, soil_type, date_recorded, recorded_at, notes

4. **WaterRecord** - Stores water quality data
   - id, farmer_id, ph, ec, tds, amount_l, date_recorded, recorded_at, notes

## Configuration

Edit `agri_project/settings.py` to customize:
- Database settings
- CORS allowed origins
- Static files location
- Other Django settings

## Production Deployment

For production, make sure to:

1. Set `DEBUG = False` in settings.py
2. Change the `SECRET_KEY` to a secure value
3. Update `ALLOWED_HOSTS` with your domain names
4. Use a production database (PostgreSQL recommended)
5. Use a production WSGI server (Gunicorn, uWSGI, etc.)
6. Set up proper static file serving
7. Enable HTTPS

## Development Commands

```bash
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Run development server with custom port
python manage.py runserver 0.0.0.0:5000
```

## CORS Configuration

By default, CORS is enabled for all origins in development. For production, update the `CORS_ALLOWED_ORIGINS` list in settings.py.

## AI Engine

The AI engine provides rule-based suggestions based on:
- Soil pH levels
- Soil moisture
- Soil type
- Crop type
- Days since last watering

Suggestions include confidence scores and detailed reasoning.

## Future Enhancements

- [ ] Add REST framework serializers
- [ ] Add comprehensive API documentation (Swagger/OpenAPI)
- [ ] Add user authentication and permissions
- [ ] Add more advanced AI suggestions
- [ ] Add data visualization and reporting
- [ ] Add image uploads for crop monitoring
