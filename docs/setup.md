# 🛠️ S.A.R.A.H. Setup & Installation Guide

**Autor:** Marc & Claude
**Stand:** Phase 1 Setup (noch nicht live)
**Für:** Lenovo ThinkCentre + Shelly Gen 1

---

## 📋 Voraussetzungen

### Hardware
- ✅ Lenovo ThinkCentre (oder ähnlicher Mini-PC)
- ✅ Ubuntu Linux 20.04+ (oder Raspberry Pi)
- ✅ Minimum: 4GB RAM, 2 CPU Cores
- ✅ Netzwerk: Ethernet oder WiFi
- ✅ Shelly Gen 1 Schaltaktor (getestet mit: Shelly 1)

### Software
- ✅ Git installiert
- ✅ Node.js 16+ & npm
- ✅ Python 3.8+
- ✅ pip (Python Package Manager)

### Netzwerk
- ✅ Lokales Netzwerk (192.168.x.x)
- ✅ Shelly auf gleicher IP-Range wie Zentrale
- ✅ Optional: Statische IP für Zentrale empfohlen

---

## 🚀 Installation - Schritt für Schritt

### Phase 0: System vorbereiten (Lenovo ThinkCentre)

```bash
# System aktualisieren
sudo apt update
sudo apt upgrade -y

# Git installieren
sudo apt install git -y

# Node.js installieren (über NodeSource)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y

# Python3 & pip installieren
sudo apt install python3 python3-pip -y

# Repository clonen
git clone https://github.com/GabbamorpH/S.A.R.A.H.---Projekt.git
cd S.A.R.A.H.---Projekt

✅ Checkpoint: node --version & python3 --version zeigen Versionen

Phase 1: NODE-RED Installation

# Node-RED global installieren
sudo npm install -g node-red

# Node-RED Dashboard 2.0 Module hinzufügen
# (Nach erstem Start)
cd ~/.node-red
npm install @flowfuse/node-red-dashboard@latest

NODE-RED starten: node-red

Im Browser öffnen: http://localhost:1880

✅ Checkpoint: NODE-RED läuft auf Port 1880

Phase 2: Shelly Netzwerk-Test
Shelly mit Strom versorgen & WiFi verbinden

Shelly einschalten
- In Router-Webinterface gehen
- IP-Adresse des Shelly notieren (z.B. 192.168.1.50)

Ping-Test: ping 192.168.1.50

Sollte Antwort bekommen ✅

HTTP-Test: curl http://192.168.1.50/status

Sollte JSON mit Status zurückgeben ✅

Deine Shelly IP: ____________ (notieren!)

Phase 3: NODE-RED Shelly-Flow
In NODE-RED (http://localhost:1880):

- Neue Flow erstellen

- Nodes platzieren:

  Inject Node (Input)
  HTTP Request Node
  Debug Node (Output)

HTTP Request konfigurieren:

- Method: GET
- URL: http://192.168.1.50/status (DEINE IP!)

Verbinden: Inject → HTTP Request → Debug

Deploy klicken

Test: Inject klicken → Debug sieht JSON ✅

Phase 4: Python Backend

# In Projekt-Root-Verzeichnis
cd S.A.R.A.H.---Projekt/python

# Virtual Environment erstellen
python3 -m venv venv

# Aktivieren
source venv/bin/activate  # Linux/Mac
# oder: venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt

requirements.txt erstellen (falls nicht vorhanden):

requests==2.28.1
asyncio==3.4.3
python-dotenv==0.20.0

Shelly API Wrapper testen:

python3 -c "from src.shelly_api import ShellyAPI; print('✅ Import erfolgreich')"

✅ Checkpoint: Import funktioniert

Phase 5: Integration NODE-RED + Python
In NODE-RED:

- HTTP Request Node → Call service Node
- URL: http://localhost:5000/api/shelly/control
- Method: POST
- Payload: {"device": "shelly1", "action": "on"}

Python Backend starten:

cd python
source venv/bin/activate
python3 src/main.py

Sollte auf http://localhost:5000 starten ✅

🧪 Erste Tests
Test 1: Shelly Status abrufen
curl http://192.168.1.50/status

✅ Sollte JSON zurückgeben

Test 2: Shelly einschalten
curl "http://192.168.1.50/relay/0?turn=on"

✅ Shelly sollte schalten

Test 3: NODE-RED Dashboard
http://localhost:1880/ui

✅ Dashboard sollte sichtbar sein

Test 4: Python API
curl http://localhost:5000/health

✅ Sollte {"status": "ok"} zurückgeben

📁 Projektstruktur nach Installation

S.A.R.A.H.---Projekt/
├── node-red/
│   ├── flows.json          # NODE-RED Flows
│   └── flows_cred.json     # Credentials
├── python/
│   ├── venv/               # Virtual Environment
│   ├── src/
│   │   ├── main.py
│   │   └── shelly_api.py
│   └── requirements.txt
└── docs/
    └── setup.md            # Du bist hier!

🆘 Troubleshooting
Problem: NODE-RED startet nicht
sudo npm uninstall -g node-red
sudo npm install -g node-red
node-red

Problem: Shelly nicht erreichbar
# Im Router prüfen, ob Shelly WiFi-Verbindung hat
# IP-Bereich muss gleich sein (192.168.1.x)
ping 192.168.1.50

Problem: Python Import-Fehler
# Virtual Environment neu erstellen
rm -rf python/venv
python3 -m venv python/venv
source python/venv/bin/activate
pip install -r python/requirements.txt

Problem: Port 1880 oder 5000 in use
# Prozess finden & killen
lsof -i :1880
kill -9 <PID>

✅ Checkliste - Erfolgreiches Setup
 - [] Node.js & Python installiert
 - [] NODE-RED läuft auf localhost:1880
 - [] Shelly-IP ermittelt & Ping funktioniert
 - []HTTP-Status-Request funktioniert
 - [] NODE-RED Shelly-Flow getestet
 - [] Python Virtual Environment aktiv
 - []Python Backend läuft auf localhost:5000
 - [] NODE-RED ↔ Python kommuniziert

🎯 Nächste Schritte
Nach erfolgreichem Setup:

→ docs/development.md - Entwicklungs-Guide
→ node-red/README.md - NODE-RED Details
→ python/README.md - Python Backend Details

📞 Support
Probleme? Schau in:

- Architecture - Systemübersicht
- GitHub Issues
- Oder kontaktiere: Marc & Claude

"Mit Struktur zum Erfolg." – Marc & Claude
