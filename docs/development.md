# 👨‍💻 Development Guide - S.A.R.A.H.

**Für:** Developer, Contributors & Maintainer
**Autoren:** Marc & Claude
**Stand:** Phase 1 Development

---

## 🎯 Ziel dieses Guides

Dieser Guide zeigt:
- Wie man am Projekt arbeitet
- Wie man Code strukturiert
- Wie man testet & debuggt
- Wie man beiträgt (Git Workflow)

---

## 📦 Projekt-Struktur verstehen
S.A.R.A.H. Projekt-Struktur

## 📦 Projekt-Struktur

**Hauptordner:**

- **node-red/** - NODE-RED Flows & Dashboard
- **python/** - Python Backend & Logik
- **docs/** - Dokumentation
- **hardware/** - Hardware-Spezifikationen
- **scripts/** - Setup & Installation Scripts

**In python/:**

- src/ - Source Code
  - main.py - Einstiegspunkt
  - shelly_api.py - Shelly-Integration
  - automation/ - Automatisierungs-Logik
  - utils/ - Helper-Funktionen
- tests/ - Unit Tests
- venv/ - Virtual Environment
- requirements.txt - Dependencies

**In docs/:**

- architecture.md
- setup.md
- roadmap.md
- diagrams/ - Diagramme & Images

**Root:**

- README.md
- .gitignore
- LICENSE


---

## 🔧 Development Environment Setup

### 1. Repository klonen

  ```bash
  git clone https://github.com/GabbamorpH/S.A.R.A.H.---Projekt.git
  cd S.A.R.A.H.---Projekt

2. Python Environment

  cd python
  python3 -m venv venv
  source venv/bin/activate  # Linux/Mac
  # venv\Scripts\activate   # Windows

  pip install -r requirements.txt

3. NODE-RED starten

  # In separatem Terminal
  node-red
  # Öffne http://localhost:1880

4. Python Backend starten

  # In python/ Verzeichnis (mit aktivem venv)
  python3 src/main.py
  # Läuft auf http://localhost:5000

📝 Code-Style & Richtlinien
  Python
  Naming Convention:
    # ✅ GUT
  def get_shelly_status(device_id):
      pass

  class ShellyDevice:
    def __init__(self):
        pass

  TIMEOUT = 30
  device_list = []

  # ❌ SCHLECHT
  def GetShellyStatus(device_id):  # camelCase für Funktionen
      pass

  def g_s_s(device_id):  # Abkürzungen
      pass

Docstrings (für jede Funktion):

def control_shelly(device_ip: str, action: str) -> bool:
    """
    Steuert einen Shelly-Aktor.
    
    Args:
        device_ip: IP-Adresse des Shelly (z.B. "192.168.1.50")
        action: "on" oder "off"
    
    Returns:
        bool: True wenn erfolgreich, False wenn Fehler
    
    Raises:
        ValueError: Wenn action nicht "on" oder "off" ist
        requests.ConnectionError: Wenn Shelly nicht erreichbar
    """
    if action not in ["on", "off"]:
        raise ValueError(f"Invalid action: {action}")
    
    # Implementation...

Type Hints verwenden:
  # ✅ GUT - klar, was rein- und rauskommt
  def get_devices() -> List[Dict[str, Any]]:
      return []

  # ❌ SCHLECHT - unklar
  def get_devices():
      return []

NODE-RED Flows
Naming:
[COMPONENT] - [ACTION]

Beispiele:
- Shelly - Get Status
- Dashboard - Button Pressed
- Automation - Check Temperature

Kommentare in Flows:

- Komplexe Flows oben mit Beschreibung
- Jeder Sub-Flow hat einen Namen
- Errors sind logged (Debug Node)


🧪 Testing
Unit Tests (Python)

# Tests ausführen
cd python
python -m pytest tests/

# Mit Coverage
python -m pytest --cov=src tests/

Test-Struktur:

# tests/test_shelly_api.py
import pytest
from src.shelly_api import ShellyAPI

class TestShellyAPI:
    
    def test_status_returns_dict(self):
        """Test dass status() ein Dict zurückgibt"""
        api = ShellyAPI("192.168.1.50")
        result = api.status()
        assert isinstance(result, dict)
    
    def test_control_invalid_action_raises_error(self):
        """Test dass ungültige Actions einen Fehler werfen"""
        api = ShellyAPI("192.168.1.50")
        with pytest.raises(ValueError):
            api.control("invalid_action")

Integration Tests (NODE-RED + Python)

# Manuell testen:
1. NODE-RED auf localhost:1880 öffnen
2. Shelly-Flow starten
3. Debug-Nodes prüfen
4. Python API auf localhost:5000 prüfen

Hardware Tests

# Shelly direkt testen
curl http://192.168.1.50/status

# Mit Python
from src.shelly_api import ShellyAPI
api = ShellyAPI("192.168.1.50")
print(api.status())

🐛 Debugging
Python Debugging

# Mit print-Statements (schnell)
print(f"DEBUG: device_status = {device_status}")

# Mit Python Debugger
python -m pdb src/main.py
# Dann: b <line> (breakpoint), c (continue), n (next)

# Mit Logging (besser)
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"Status: {status}")


NODE-RED Debugging

1. Debug Node am Ende einfügen
2. Deploy klicken
3. Debug Output rechts prüfen
4. Struktur von msg.payload analysieren

Logs anschauen

# NODE-RED Logs
# Terminal wo node-red läuft anschauen

# Python Logs
# Terminal wo python läuft anschauen
# Oder: tail -f logs/app.log (wenn Logging konfiguriert)

🔄 Git Workflow (Marc & Claude)
Branching (für später, wenn mehr Contributors)

# Für jedes Feature einen Branch
git checkout -b feature/shelly-multi-device
# Arbeiten...
git add .
git commit -m "Add multi-device support"
git push origin feature/shelly-multi-device

# Pull Request auf main
# Code Review (Claude)
# Merge

Commit Message Format

[AREA] Beschreibung - Ticket #XX

Beispiele:
- [NODE-RED] Add dashboard layout - #5
- [PYTHON] Fix Shelly API timeout - #12
- [DOCS] Update setup guide
- [TEST] Add unit tests for ShellyAPI - #8

Push vor dem Committen

# Vor jedem Push: Tests laufen lassen
cd python && pytest tests/

# Dann pushen
git push origin <branch>

📝 Dokumentation schreiben
Inline-Dokumentation (Code)

def calculate_automation_state(temperature: float, time: str) -> str:
    """
    Berechnet den gewünschten Zustand basierend auf Temperatur & Zeit.
    
    Logic:
    - Wenn temp > 25°C und 09:00-17:00 → "cooling"
    - Wenn temp < 18°C und 17:00-09:00 → "heating"
    - Sonst → "auto"
    
    Args:
        temperature: Temperatur in Celsius
        time: Zeit im Format "HH:MM"
    
    Returns:
        str: "heating", "cooling" oder "auto"
    """

Externe Dokumentation (Markdown)
- Was: Was macht die Komponente?
- Warum: Warum ist es so designt?
- Wie: Wie nutzt man es?
- Beispiele: Code-Beispiele

🚀 Workflow: Neue Feature entwickeln
Beispiel: "Multi-Shelly Support"
1. Branch erstellen

git checkout -b feature/multi-shelly

2. Code schreiben

# python/src/shelly_api.py - erweitern

class ShellyManager:
    def __init__(self):
        self.devices = {}
    
    def add_device(self, name: str, ip: str):
        """Fügt ein Shelly-Gerät hinzu"""
        self.devices[name] = ShellyAPI(ip)
    
    def control_all(self, action: str):
        """Steuert alle Geräte"""
        for device in self.devices.values():
            device.control(action)

3. Testen

cd python
pytest tests/test_multi_shelly.py

4. Committen

git add python/src/shelly_api.py
git commit -m "[PYTHON] Add multi-Shelly support - #3"

5. NODE-RED anpassen

- Neue Flow für Multi-Shelly
- Mit neuer Python API verbinden
- Testen

6. Dokumentation updaten

git add docs/architecture.md
git commit -m "[DOCS] Update architecture for multi-Shelly"

7. Pushen & Mergen

git push origin feature/multi-shelly
# Pull Request → Code Review → Merge

🎓 Best Practices
✅ Regelmäßig committen - nicht alles auf einmal
✅ Tests schreiben - bevor/während Features
✅ Dokumentieren - während du entwickelst, nicht danach
✅ Code Review - Marc & Claude besprechen Changes
✅ Backup regelmäßig - git push nach jedem Meilenstein
✅ Kleine Changes - lieber 5x committen als 1x mega-Commit

❌ Alte Credentials committen
❌ Große Binaries (z.B. Videos, große Images)
❌ Ungetesteter Code pushen
❌ Kommentierter Code ohne Begründung lassen

📞 Support & Fragen
- Technische Fragen: Schau in architecture.md
- Installation Probleme: setup.md
- Bug gefunden? GitHub Issue öffnen

🔗 Links
- GitHub Repository
- Setup-Guide
- Architecture
- Roadmap

"Gut entwickeln heißt: Testen, Dokumentieren, Committen." – Marc & Claude
