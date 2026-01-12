# Admin Dashboard Guide

## Overview

The Agriculture Admin Dashboard provides a complete web-based interface for managing all aspects of your agriculture data:

- **Farmers**: Create, edit, and delete farmer records
- **Crops**: Track crop records with yield information
- **Soil Records**: Monitor soil metrics (pH, nitrogen, phosphorus, potassium)
- **Water Records**: Track water quality metrics (pH, EC, TDS)

## Access the Admin Panel

1. Start the backend: `python backend/app.py` (development) or `python -m backend.run_prod` (production)
2. Open your browser to: **http://localhost:5000/admin/**
3. Navigate between sections using the top navigation menu

## Features

### Dashboard
- Overview cards showing total counts of all records
- Quick stats on farmers, crops, soil, and water records

### Farmers Management
- **View all farmers** with their contact information
- **Add a new farmer** with name, region, and phone number
- **Edit existing farmers** to update their information
- **Delete farmers** from the system

### Crops Management
- **View all crop records** with yield information
- **Add new crop records** linking to a farmer
- **Track yield in kg** for each crop entry
- **Record dates** for each crop entry
- **Edit or delete** existing crop records

### Soil Records
- **Monitor soil quality** with detailed parameters:
  - pH level
  - Nitrogen (mg/kg)
  - Phosphorus (mg/kg)
  - Potassium (mg/kg)
- **Add new soil tests** for farmers
- **Edit previous records** to correct or update data
- **Delete outdated records**

### Water Records
- **Track water quality** with important metrics:
  - pH level
  - EC (Electrical Conductivity) in µS/cm
  - TDS (Total Dissolved Solids) in mg/L
- **Record dates** for water quality testing
- **Manage water records** for different farmers

## API Endpoints (JSON)

### Farmers
- `GET /api/farmers` - List all farmers
- `POST /api/farmers` - Create a new farmer
- `GET /api/farmers/<id>` - Get a specific farmer
- `PUT /api/farmers/<id>` - Update a farmer
- `DELETE /api/farmers/<id>` - Delete a farmer

### Crop Records
- `GET /api/records/crops` - List all crop records
- `POST /api/records/crop` - Create a new crop record
- `GET /api/records/crop/<id>` - Get a specific crop record
- `PUT /api/records/crop/<id>` - Update a crop record
- `DELETE /api/records/crop/<id>` - Delete a crop record

### Soil Records
- `GET /api/records/soil` - List all soil records
- `POST /api/records/soil` - Create a new soil record
- `GET /api/records/soil/<id>` - Get a specific soil record
- `PUT /api/records/soil/<id>` - Update a soil record
- `DELETE /api/records/soil/<id>` - Delete a soil record

### Water Records
- `GET /api/records/water` - List all water records
- `POST /api/records/water` - Create a new water record
- `GET /api/records/water/<id>` - Get a specific water record
- `PUT /api/records/water/<id>` - Update a water record
- `DELETE /api/records/water/<id>` - Delete a water record

### Statistics
- `GET /api/stats` - Get dashboard statistics (farmer, crop, soil, water counts)

## Testing with curl (PowerShell)

### Create a Farmer
```powershell
$body = @{
    name = "Raj Kumar"
    region = "Maharashtra"
    phone = "9876543210"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/farmers" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

### Add Soil Record
```powershell
$body = @{
    farmer_id = 1
    ph = 6.5
    nitrogen = 45.2
    phosphorus = 22.8
    potassium = 180.5
    date_recorded = "2026-01-11"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/records/soil" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

### Get AI Suggestions
```powershell
$body = @{
    farmer_id = 1
    soil_ph = 6.5
    nitrogen = 45
    phosphorus = 23
    crop = "wheat"
    days_since_last_water = 5
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/api/suggest" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

## Database

- **Location**: `agri_data.db` in your project root
- **Type**: SQLite
- **Auto-created**: Yes, on first run
- **No migration needed**: Schema is automatically created

## Tips

1. **Use the admin panel** for easiest data entry
2. **Farmers are required** for most records (crop, soil, water)
3. **All dates** are optional and auto-filled with current date if not provided
4. **Delete operations** are permanent - confirm before deleting
5. **For bulk operations**, consider using the API directly with scripts

## Troubleshooting

### Admin pages show "Loading..." indefinitely
- Check browser console (F12) for network errors
- Ensure backend is running on port 5000
- Check firewall settings if accessing from another machine

### "Farmer not found" error
- Ensure you created a farmer first
- Use a valid farmer ID when creating related records
- Check the farmer ID in the Farmers page

### Database locked error
- Ensure only one instance of the backend is running
- Close any external database editors
- Restart the backend if the error persists

## Next Steps

- Integrate frontend contact form with `/api/suggest` endpoint for AI recommendations
- Add authentication if deploying to production
- Export data to CSV/Excel for external analysis
- Set up automated backups of `agri_data.db`
