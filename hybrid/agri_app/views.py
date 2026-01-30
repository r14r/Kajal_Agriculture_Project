from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
from datetime import datetime

from .models import Farmer, CropRecord, SoilRecord, WaterRecord
from .ai_engine import suggest_actions
from .openapi import OPENAPI_SCHEMA


@require_http_methods(["GET"])
def health(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'ok', 'time': 'now'})


@require_http_methods(["GET"])
def index(request):
    """Root endpoint - provides service info"""
    return JsonResponse({
        'service': 'Smart Agriculture Backend',
        'status': 'running',
        'endpoints': ['/docs/', '/api/health', '/api/farmers', '/api/records/soil', '/api/suggest'],
        'admin': '/admin/'
    })


@require_http_methods(["GET"])
def openapi_schema(request):
    return JsonResponse(OPENAPI_SCHEMA)


def docs(request: HttpRequest) -> HttpResponse:
    return render(request, 'docs.html', {'schema_url': '/openapi.json'})


def admin_dashboard(request: HttpRequest) -> HttpResponse:
    """Admin dashboard view"""
    return render(request, 'admin_dashboard.html')


def admin_farmers(request: HttpRequest) -> HttpResponse:
    """Admin farmers management view"""
    return render(request, 'admin_farmers.html')


def admin_crops(request: HttpRequest) -> HttpResponse:
    """Admin crops management view"""
    return render(request, 'admin_crops.html')


def admin_soil(request: HttpRequest) -> HttpResponse:
    """Admin soil records management view"""
    return render(request, 'admin_soil.html')


def admin_water(request: HttpRequest) -> HttpResponse:
    """Admin water records management view"""
    return render(request, 'admin_water.html')


@require_http_methods(["GET"])
def stats(request):
    """Get counts of all records for dashboard display"""
    try:
        farmers_count = Farmer.objects.count()
        crops_count = CropRecord.objects.count()
        soil_count = SoilRecord.objects.count()
        water_count = WaterRecord.objects.count()

        return JsonResponse({
            'farmers': farmers_count,
            'crops': crops_count,
            'soil': soil_count,
            'water': water_count
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'farmers': 0,
            'crops': 0,
            'soil': 0,
            'water': 0
        }, status=200)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def test(request):
    return JsonResponse({'state': 'ok'}, status=400)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def farmer_list_create(request):
    """Create a new farmer (POST) or list all farmers (GET)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')

            if not name:
                return JsonResponse({'error': 'name is required'}, status=400)

            farmer = Farmer.objects.create(
                name=name,
                phone=data.get('phone'),
                location=data.get('location')
            )
            return JsonResponse({
                'id': farmer.id,
                'name': farmer.name
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'GET':
        farmers = Farmer.objects.all()
        out = [{'id': f.id, 'name': f.name, 'phone': f.phone, 'region': f.location} for f in farmers]
        return JsonResponse(out, safe=False)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def farmer_detail(request, farmer_id):
    """Get, update, or delete a specific farmer"""
    farmer = get_object_or_404(Farmer, id=farmer_id)

    if request.method == 'GET':
        return JsonResponse({
            'id': farmer.id,
            'name': farmer.name,
            'phone': farmer.phone,
            'region': farmer.location
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            farmer.name = data.get('name', farmer.name)
            farmer.phone = data.get('phone', farmer.phone)
            farmer.location = data.get('region', farmer.location)
            farmer.save()

            return JsonResponse({
                'id': farmer.id,
                'name': farmer.name
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            farmer.delete()
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def soil_record_list_create(request):
    """Create a new soil record (POST) or list all soil records (GET)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            farmer_id = data.get('farmer_id')

            record = SoilRecord.objects.create(
                farmer_id=farmer_id,
                ph=data.get('ph'),
                nitrogen=data.get('nitrogen'),
                phosphorus=data.get('phosphorus'),
                potassium=data.get('potassium'),
                date_recorded=data.get('date_recorded') or datetime.now().isoformat()
            )
            return JsonResponse({'id': record.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'GET':
        records = SoilRecord.objects.all()
        out = [{
            'id': r.id,
            'farmer_id': r.farmer.id,
            'ph': r.ph,
            'nitrogen': r.nitrogen,
            'phosphorus': r.phosphorus,
            'potassium': r.potassium,
            'date_recorded': r.date_recorded
        } for r in records]
        return JsonResponse(out, safe=False)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def soil_record_detail(request, record_id):
    """Get, update, or delete a specific soil record"""
    record = get_object_or_404(SoilRecord, id=record_id)

    if request.method == 'GET':
        return JsonResponse({
            'id': record.id,
            'farmer_id': record.farmer.id,
            'ph': record.ph,
            'nitrogen': record.nitrogen,
            'phosphorus': record.phosphorus,
            'potassium': record.potassium,
            'date_recorded': record.date_recorded
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            record.farmer.id = data.get('farmer_id', record.farmer.id)
            record.ph = data.get('ph', record.ph)
            record.nitrogen = data.get('nitrogen', record.nitrogen)
            record.phosphorus = data.get('phosphorus', record.phosphorus)
            record.potassium = data.get('potassium', record.potassium)
            record.date_recorded = data.get('date_recorded', record.date_recorded)
            record.save()

            return JsonResponse({'id': record.id}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            record.delete()
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def water_record_list_create(request):
    """Create a new water record (POST) or list all water records (GET)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            record = WaterRecord.objects.create(
                farmer_id=data.get('farmer_id'),
                ph=data.get('ph'),
                ec=data.get('ec'),
                tds=data.get('tds'),
                date_recorded=data.get('date_recorded') or datetime.now().isoformat()
            )
            return JsonResponse({'id': record.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'GET':
        records = WaterRecord.objects.all()
        out = [{
            'id': r.id,
            'farmer_id': r.farmer.id,
            'ph': r.ph,
            'ec': r.ec,
            'tds': r.tds,
            'date_recorded': r.date_recorded
        } for r in records]
        return JsonResponse(out, safe=False)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def water_record_detail(request, record_id):
    """Get, update, or delete a specific water record"""
    record = get_object_or_404(WaterRecord, id=record_id)

    if request.method == 'GET':
        return JsonResponse({
            'id': record.id,
            'farmer_id': record.farmer.id,
            'ph': record.ph,
            'ec': record.ec,
            'tds': record.tds,
            'date_recorded': record.date_recorded
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            record.farmer.id = data.get('farmer_id', record.farmer.id)
            record.ph = data.get('ph', record.ph)
            record.ec = data.get('ec', record.ec)
            record.tds = data.get('tds', record.tds)
            record.date_recorded = data.get('date_recorded', record.date_recorded)
            record.save()

            return JsonResponse({'id': record.id}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            record.delete()
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def crop_record_list_create(request):
    """Create a new crop record (POST) or list all crop records (GET)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            record = CropRecord.objects.create(
                farmer_id=data.get('farmer_id'),
                crop_name=data.get('crop_name'),
                yield_kg=data.get('yield_kg'),
                date_recorded=data.get('date_recorded') or datetime.now().isoformat()
            )
            return JsonResponse({'id': record.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'GET':
        records = CropRecord.objects.all()
        out = [{
            'id': r.id,
            'farmer_id': r.farmer.id,
            'crop_name': r.crop_name,
            'yield_kg': r.yield_kg,
            'date_recorded': r.date_recorded
        } for r in records]
        return JsonResponse(out, safe=False)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def crop_record_detail(request, record_id):
    """Get, update, or delete a specific crop record"""
    record = get_object_or_404(CropRecord, id=record_id)

    if request.method == 'GET':
        return JsonResponse({
            'id': record.id,
            'farmer_id': record.farmer.id,
            'crop_name': record.crop_name,
            'yield_kg': record.yield_kg,
            'date_recorded': record.date_recorded
        })

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            record.farmer.id = data.get('farmer_id', record.farmer.id)
            record.crop_name = data.get('crop_name', record.crop_name)
            record.yield_kg = data.get('yield_kg', record.yield_kg)
            record.date_recorded = data.get('date_recorded', record.date_recorded)
            record.save()

            return JsonResponse({'id': record.id}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            record.delete()
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def suggest(request):
    """Get AI suggestions for agricultural actions"""
    try:
        data = json.loads(request.body)
        result = suggest_actions(data)
        return JsonResponse(result)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# Frontend views
def frontend_index(request: HttpRequest) -> HttpResponse:
    """Frontend home page"""
    return render(request, 'frontend/index.html')


def frontend_farmers(request: HttpRequest) -> HttpResponse:
    """Frontend farmers page"""
    return render(request, 'frontend/farmers.html')


def frontend_contact(request: HttpRequest) -> HttpResponse:
    """Frontend contact page"""
    return render(request, 'frontend/contact.html')
