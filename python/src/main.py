"""
S.A.R.A.H. Backend - Flask Application

Startet den Python Backend Server.
Kommuniziert mit NODE-RED & Shelly-Geräten.
"""

import logging
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Logging konfigurieren
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Umgebungs-Variablen laden
load_dotenv()

# Flask App erstellen
app = Flask(__name__)

# ============================================
# HEALTH CHECK
# ============================================

@app.route('/health', methods=['GET'])
def health():
    """Health-Check Endpoint"""
    return jsonify({
        'status': 'ok',
        'service': 'S.A.R.A.H. Backend'
    }), 200


# ============================================
# SHELLY ENDPOINTS
# ============================================

@app.route('/api/shelly/status', methods=['POST'])
def shelly_status():
    """
    Ruft Status eines Shelly-Geräts ab.
    
    Body:
    {
        "device_ip": "192.168.1.50"
    }
    """
    try:
        data = request.get_json()
        device_ip = data.get('device_ip')
        
        if not device_ip:
            return jsonify({'error': 'device_ip erforderlich'}), 400
        
        logger.info(f"Abrufen Status von {device_ip}")
        
        # TODO: Später mit shelly_api.py verbinden
        # from .shelly_api import ShellyAPI
        # api = ShellyAPI(device_ip)
        # status = api.status()
        
        return jsonify({
            'device_ip': device_ip,
            'status': 'on',
            'power': 0,
            'temperature': 45.2
        }), 200
        
    except Exception as e:
        logger.error(f"Fehler beim Status abrufen: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/shelly/control', methods=['POST'])
def shelly_control():
    """
    Steuert ein Shelly-Gerät.
    
    Body:
    {
        "device_ip": "192.168.1.50",
        "action": "on"
    }
    """
    try:
        data = request.get_json()
        device_ip = data.get('device_ip')
        action = data.get('action')
        
        if not device_ip or not action:
            return jsonify({'error': 'device_ip und action erforderlich'}), 400
        
        if action not in ['on', 'off']:
            return jsonify({'error': 'action muss "on" oder "off" sein'}), 400
        
        logger.info(f"Steuere {device_ip} → {action}")
        
        # TODO: Später mit shelly_api.py verbinden
        # from .shelly_api import ShellyAPI
        # api = ShellyAPI(device_ip)
        # api.control(action)
        
        return jsonify({
            'device_ip': device_ip,
            'action': action,
            'status': 'success'
        }), 200
        
    except Exception as e:
        logger.error(f"Fehler beim Steuern: {str(e)}")
        return jsonify({'error': str(e)}), 500


# ============================================
# AUTOMATION ENDPOINTS
# ============================================

@app.route('/api/automation/status', methods=['GET'])
def automation_status():
    """Gibt Status der Automatisierungen aus"""
    return jsonify({
        'automations_active': 3,
        'last_trigger': '2024-12-19 10:30:00',
        'status': 'running'
    }), 200


# ============================================
# ERROR HANDLING
# ============================================

@app.errorhandler(404)
def not_found(error):
    """404 Error Handler"""
    return jsonify({'error': 'Endpoint nicht gefunden'}), 404


@app.errorhandler(500)
def server_error(error):
    """500 Error Handler"""
    logger.error(f"Server Error: {str(error)}")
    return jsonify({'error': 'Interner Serverfehler'}), 500


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True') == 'True'
    
    logger.info(f"S.A.R.A.H. Backend startet auf Port {port}")
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
