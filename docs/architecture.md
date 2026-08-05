# S.A.R.A.H. - Systemarchitektur

## Phase 1: GUI + Shelly-Steuerung (bis Ende 2026)

### Komponenten
1. **Lenovo ThinkCentre** - Zentrale Steuereinheit
   - OS: Ubuntu Linux
   - RAM: 8GB
   - CPU: Intel i5
   - Software: NODE-RED, Python

2. **Shelly Gen 1 Schaltaktor** - Smart Switches
   - Verbindung: WiFi
   - Protokoll: REST API (HTTP)
   
3. **Tablet** - Bedienoberfläche
   - Software: NODE-RED Dashboard 2.0

### System-Übersicht

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    A[Tablet - NODE-RED Dashboard 2.0] 
    B[NODE-RED - Logik & Automation]
    C[Python Backend]
    D[Shelly REST API]
    E[Shelly Schaltaktor 1]
    F[Shelly Schaltaktor 2 - später]
    
    A -->|HTTP/WebSocket| B
    B --> C
    C -->|HTTP-Request| D
    D --> E
    D --> F
    
    E -.->|Feedback| B
    F -.->|Feedback| B
      
      
      ### Workflow
      1. Benutzer interagiert mit Tablet-Dashboard
      2. NODE-RED empfängt Befehle
      3. Python-Logik evaluiert Anfrage
      4. HTTP-Request an Shelly
      5. Shelly schaltet Aktor
      6. Feedback zurück an Dashboard
      
      ### Nächste Schritte
      - [x] GitHub Repository erstellen
      - [ ] Shelly IP-Adresse ermitteln
      - [ ] HTTP-Request Test durchführen
      - [ ] NODE-RED Dashboard 2.0 installieren
      - [ ] Erste GUI Prototype bauen
      
      ---
      *Stand: Work in Progress - Marc & Claude*
