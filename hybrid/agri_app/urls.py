from django.urls import path
from . import views

urlpatterns = [
    # Frontend pages
    path('', views.frontend_index, name='frontend_index'),
    path('farmers.html', views.frontend_farmers, name='frontend_farmers'),
    path('contact.html', views.frontend_contact, name='frontend_contact'),
    
    # API info endpoint
    path('api/', views.index, name='index'),
    path('stats/', views.stats, name='stats'),

    # API documentation endpoints
    path('openapi.json', views.openapi_schema, name='openapi_schema'),
    path('docs/', views.docs, name='docs'),
    
    # Health check endpoint
    path('api/health/', views.health, name='health'),
    
    # Admin views
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/farmers/', views.admin_farmers, name='admin_farmers'),
    path('admin/crops/', views.admin_crops, name='admin_crops'),
    path('admin/soil/', views.admin_soil, name='admin_soil'),
    path('admin/water/', views.admin_water, name='admin_water'),
    
    # Farmer endpoints
    path('api/farmers/', views.farmer_list_create, name='farmer_list_create'),
    path('api/farmers/<int:farmer_id>/', views.farmer_detail, name='farmer_detail'),
    
    # Soil record endpoints
    path('api/records/soil/', views.soil_record_list_create, name='soil_record_list_create'),
    path('api/records/soil/<int:record_id>/', views.soil_record_detail, name='soil_record_detail'),
    
    # Water record endpoints
    path('api/records/water/', views.water_record_list_create, name='water_record_list_create'),
    path('api/records/water/<int:record_id>/', views.water_record_detail, name='water_record_detail'),
    
    # Crop record endpoints
    path('api/records/crop/', views.crop_record_list_create, name='crop_record_list_create'),
    path('api/records/crop/<int:record_id>/', views.crop_record_detail, name='crop_record_detail'),
    path('api/records/crops/', views.crop_record_list_create, name='crop_records_list'),  # Alias for compatibility
    
    # AI suggestions endpoint
    path('api/suggest/', views.suggest, name='suggest'),
]
