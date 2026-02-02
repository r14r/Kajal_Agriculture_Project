"""Simple rule-based AI engine for agriculture suggestions.

This module provides deterministic suggestions (no external APIs).
It is intentionally small and explainable so farmers can trust the outputs.
"""
from datetime import datetime


def suggest_for_soil(soil_ph=None, moisture=None, soil_type=None, crop=None):
    suggestions = []

    # PH based suggestions
    if soil_ph is not None:
        if soil_ph < 5.5:
            suggestions.append({
                'action': 'Apply lime (chalk) carefully',
                'reason': f'soil pH={soil_ph} (very acidic) — lime raises pH',
                'confidence': 0.8,
            })
        elif soil_ph < 6.5:
            suggestions.append({
                'action': 'Apply organic compost / jivamrut',
                'reason': f'soil pH={soil_ph} (slightly acidic) — organic matter buffers pH',
                'confidence': 0.7,
            })
        elif soil_ph > 8.0:
            suggestions.append({
                'action': 'Reduce alkalinity — use acidifying organic matter',
                'reason': f'soil pH={soil_ph} (alkaline)',
                'confidence': 0.6,
            })

    # Moisture based suggestions
    if moisture is not None:
        if moisture < 20:
            suggestions.append({
                'action': 'Increase irrigation frequency',
                'reason': f'moisture={moisture}% — soil is dry',
                'confidence': 0.9,
            })
        elif moisture > 80:
            suggestions.append({
                'action': 'Improve drainage and reduce watering',
                'reason': f'moisture={moisture}% — soil is waterlogged',
                'confidence': 0.85,
            })

    # Soil type and crop-specific tips
    if crop:
        crop = crop.lower()
        if 'mirchi' in crop or 'chili' in crop:
            suggestions.append({
                'action': 'Mulch and drip irrigation',
                'reason': 'Mirchi benefits from consistent moisture and mulching',
                'confidence': 0.8,
            })
        if 'methi' in crop or 'fenugreek' in crop:
            suggestions.append({
                'action': 'Avoid over-watering; light irrigation',
                'reason': 'Methi prefers well-drained soil',
                'confidence': 0.75,
            })

    # Generic tips
    if soil_type:
        st = soil_type.lower()
        if 'sandy' in st:
            suggestions.append({
                'action': 'Increase organic matter and mulch',
                'reason': 'Sandy soils hold less water and nutrients',
                'confidence': 0.8,
            })
        if 'clay' in st:
            suggestions.append({
                'action': 'Improve drainage, consider raised beds',
                'reason': 'Clay soils may compact and hold too much water',
                'confidence': 0.75,
            })

    if not suggestions:
        suggestions.append({
            'action': 'Soil looks balanced — maintain organic practices',
            'reason': 'No specific issues detected from provided inputs',
            'confidence': 0.5,
        })

    # Add timestamp and return
    return {
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'suggestions': suggestions,
    }


def suggest_actions(payload: dict):
    """High-level entrypoint. Accepts a payload with optional keys:
    - soil_ph, moisture, soil_type, crop, days_since_last_water
    """
    soil_ph = payload.get('soil_ph')
    moisture = payload.get('moisture')
    soil_type = payload.get('soil_type')
    crop = payload.get('crop')
    days = payload.get('days_since_last_water')

    out = suggest_for_soil(soil_ph=soil_ph, moisture=moisture, soil_type=soil_type, crop=crop)

    if days is not None:
        if days >= 10:
            out['suggestions'].append({
                'action': 'Immediate irrigation advised',
                'reason': f'No watering for {days} days — risk of crop stress',
                'confidence': 0.9,
            })
        elif days >= 5:
            out['suggestions'].append({
                'action': 'Check soil moisture; consider irrigation',
                'reason': f'{days} days since last water',
                'confidence': 0.7,
            })

    return out
