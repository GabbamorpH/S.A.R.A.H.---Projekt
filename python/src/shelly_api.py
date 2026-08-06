"""
S.A.R.A.H. Shelly API Wrapper

Kommuniziert mit Shelly Gen 1 Geräten via HTTP REST API.
"""

import requests
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class ShellyAPI:
    """
    Wrapper für Shelly Gen 1 REST API.
    
    Beispiel:
    --------
    api = ShellyAPI("192.168.1.50")
    status = api.status()
    api.control("on")
    """
    
    def __init__(self, device_ip: str, timeout: int = 5):
        """
        Initialisiert Shelly API Client.
        
        Args:
            device_ip: IP-Adresse des Shelly (z.B. "192.168.1.50")
            timeout: Request Timeout in Sekunden
        """
        self.device_ip = device_ip
        self.base_url = f"http://{device_ip}"
        self.timeout = timeout
        logger.debug(f"ShellyAPI initialisiert für {device_ip}")
    
    # ==========================================
    # STATUS ABRUFEN
    # ==========================================
    
    def status(self) -> Dict[str, Any]:
        """
        Ruft kompletten Status des Shelly ab.
        
        Returns:
            Dict mit Status-Informationen:
            - ison: Boolean (ein/aus)
            - power: Leistung in Watt
            - temperature: Temperatur
            - etc.
        
        Raises:
            requests.ConnectionError: Wenn Shelly nicht erreichbar
            ValueError: Wenn Response ungültig
        """
        try:
            url = f"{self.base_url}/status"
            logger.debug(f"Rufe ab: {url}")
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()  # Exception bei HTTP Error
            
            data = response.json()
            logger.debug(f"Status von {self.device_ip}: {data}")
            
            return data
            
        except requests.ConnectionError as e:
            logger.error(f"Verbindung fehlgeschlagen zu {self.device_ip}: {str(e)}")
            raise
        except requests.Timeout:
            logger.error(f"Timeout bei {self.device_ip} nach {self.timeout}s")
            raise
        except Exception as e:
            logger.error(f"Fehler beim Status abrufen: {str(e)}")
            raise ValueError(f"Ungültige Response: {str(e)}")
    
    def get_power(self) -> float:
        """Gibt aktuelle Leistung in Watt zurück"""
        try:
            status = self.status()
            power = status.get('meters', [{}])[0].get('power', 0)
            return float(power)
        except Exception as e:
            logger.error(f"Fehler beim Power abrufen: {str(e)}")
            return 0.0
    
    def is_on(self) -> bool:
        """Gibt True zurück wenn Gerät eingeschaltet ist"""
        try:
            status = self.status()
            relay_status = status.get('relays', [{}])[0].get('ison', False)
            return bool(relay_status)
        except Exception as e:
            logger.error(f"Fehler beim is_on Check: {str(e)}")
            return False
    
    # ==========================================
    # STEUERUNG
    # ==========================================
    
    def control(self, action: str, relay: int = 0) -> bool:
        """
        Steuert Shelly Relais.
        
        Args:
            action: "on" oder "off"
            relay: Relay Nummer (default: 0)
        
        Returns:
            bool: True wenn erfolgreich
        
        Raises:
            ValueError: Wenn action ungültig
            requests.ConnectionError: Wenn nicht erreichbar
        """
        if action not in ["on", "off"]:
            raise ValueError(f"Ungültige action: {action}. Muss 'on' oder 'off' sein")
        
        try:
            url = f"{self.base_url}/relay/{relay}?turn={action}"
            logger.info(f"Steuere {self.device_ip} Relay {relay} → {action}")
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            logger.debug(f"Control erfolgreich: {response.text}")
            return True
            
        except requests.ConnectionError as e:
            logger.error(f"Verbindung fehlgeschlagen: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Fehler beim Steuern: {str(e)}")
            raise
    
    def turn_on(self, relay: int = 0) -> bool:
        """Schaltet Relais ein"""
        return self.control("on", relay)
    
    def turn_off(self, relay: int = 0) -> bool:
        """Schaltet Relais aus"""
        return self.control("off", relay)
    
    def toggle(self, relay: int = 0) -> bool:
        """Schaltet Relais um"""
        is_on = self.is_on()
        action = "off" if is_on else "on"
        return self.control(action, relay)
    
    # ==========================================
    # INFORMATIONEN
    # ==========================================
    
    def get_info(self) -> Dict[str, Any]:
        """Ruft Geräte-Informationen ab (Name, Modell, etc.)"""
        try:
            url = f"{self.base_url}/info"
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Fehler beim Info abrufen: {str(e)}")
            return {}
    
    def get_device_name(self) -> str:
        """Gibt Namen des Shelly Geräts zurück"""
        try:
            info = self.get_info()
            return info.get('name', 'Unknown')
        except Exception:
            return 'Unknown'
    
    # ==========================================
    # HEALTH CHECK
    # ==========================================
    
    def is_reachable(self) -> bool:
        """Prüft ob Shelly erreichbar ist"""
        try:
            self.status()
            logger.debug(f"{self.device_ip} ist erreichbar")
            return True
        except Exception as e:
            logger.warning(f"{self.device_ip} ist NICHT erreichbar: {str(e)}")
            return False


# ==========================================
# HELPER FUNKTIONEN
# ==========================================

def discover_shelly_devices(network_range: str = "192.168.1") -> list:
    """
    Versucht Shelly-Geräte im Netzwerk zu finden.
    
    Args:
        network_range: Z.B. "192.168.1" (sucht 1-254)
    
    Returns:
        Liste mit IP-Adressen gefundener Shellys
    
    Hinweis:
        Kann langsam sein! (bis zu 254 Requests)
    """
    found_devices = []
    logger.info(f"Suche Shelly-Geräte im Range {network_range}.x")
    
    for i in range(1, 255):
        ip = f"{network_range}.{i}"
        try:
            api = ShellyAPI(ip, timeout=1)
            if api.is_reachable():
                device_name = api.get_device_name()
                found_devices.append({
                    'ip': ip,
                    'name': device_name
                })
                logger.info(f"✓ Gefunden: {ip} ({device_name})")
        except Exception:
            pass  # Nicht gefunden, weitermachen
    
    logger.info(f"Discovery fertig: {len(found_devices)} Geräte gefunden")
    return found_devices
