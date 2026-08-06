# 🗺️ S.A.R.A.H. Projekt-Roadmap

**Stand:** Work in Progress - Marc & Claude

---

## 🎯 Vision & Ziel

S.A.R.A.H. soll bis Ende 2026 eine **funktionierende Smart-Home-Lösung** sein, die:
- ✅ Alte Menschen sicherer macht
- ✅ Notfallsituationen erkennt
- ✅ Mit ethischen KI-Prinzipien entwickelt wird
- ✅ Erweiterbar & wartbar ist

---

## 📅 Phase 1: GUI + Shelly-Steuerung (bis 31.12.2026)

### Ziel
Grundsystem mit NODE-RED Dashboard + Shelly-Gerätesteuerung

### Q4 2024 (Dezember - JETZT)
**Projekt-Setup & Planung**

- [x] GitHub Repository strukturieren
- [x] Dokumentation beginnen
- [x] Team & Rollen definieren
- [x] Roadmap schreiben
- [ ] Development-Guide verfassen
- [ ] Architecture-Doc finalisieren

**Deliverable:** Professionelle Projekt-Struktur ✅

---

### Q3 2026 (August - September)
**Hardware-Tests & NODE-RED Foundation**

#### Woche 1-2: Shelly Integration Test
- [ ] Shelly-IP ermitteln
- [ ] HTTP-Request Test durchführen
- [ ] Shelly API dokumentieren
- [ ] Erste Python-Wrapper bauen

#### Woche 3-4: NODE-RED Setup
- [ ] NODE-RED Dashboard 2.0 installieren
- [ ] Basic Dashboard-Layout erstellen
- [ ] Erste Flow: Shelly-Abfrage
- [ ] Dashboard mit Tablet testen

#### Woche 5-6: Python Backend Foundation
- [ ] Repository-Struktur (src/, tests/)
- [ ] Shelly API Wrapper (vollständig)
- [ ] Logging & Error-Handling
- [ ] First Unit Tests

#### Woche 7-8: Integration
- [ ] NODE-RED ← → Python kommuniziert
- [ ] Erste Automation (z.B. "Licht an/aus")
- [ ] Tests auf Raspberry Pi + Lenovo

**Deliverable:** Basis-System läuft ✅
**Code Commits:** ~15-20 Commits

---

### Q3-4 2026 (September - November)
**Dashboard-Entwicklung & Multi-Device**

#### Woche 1-4: Dashboard UI
- [ ] Responsive Design (Desktop + Tablet)
- [ ] Icons & Styling (professionell)
- [ ] Status-Anzeigen (Echtzeit)
- [ ] Automatisierungs-Widget

#### Woche 5-8: Multi-Device Support
- [ ] 2. + 3. Shelly-Geräte testen
- [ ] Dynamische Geräte-Verwaltung
- [ ] Gruppe-Steuerung (z.B. "alle Lichter")
- [ ] Automation: Zeit-basiert, Sensor-basiert

#### Woche 9-10: Testing & Dokumentation
- [ ] Integration Tests
- [ ] User-Documentation schreiben
- [ ] API-Dokumentation finalisieren
- [ ] Code-Reviews durchführen

**Deliverable:** Produktives Dashboard ✅
**Code Commits:** ~20-30 Commits

---

### Q4 2026 (Juli - September)
**System-Stabilisierung & Optimierung**

- [ ] Performance-Optimierungen (schneller Load)
- [ ] Error-Handling & Logging erweitern
- [ ] Sicherheit: Authentifizierung, Verschlüsselung
- [ ] Backup & Recovery System
- [ ] Umfassende Test-Suite
- [ ] Deployment-Dokumentation

**Parallel:**
- [ ] Hardware-Planung
- [ ] Verkabelung planen
- [ ] Installation vorbereiten

**Deliverable:** Production-Ready System ✅
**Code Commits:** ~15-20 Commits

---

### Q4 2026 - Q1 2027
**Schulung & Vorbereitung**

- [ ] **Marc:** IT-Admin Schulung (22.10.25 - 18.12.25) ⚠️ WICHTIG
- [ ] Phase 1 Final Polish
- [ ] **Freund's Haus:** Hardware-Installation vorbereiten
- [ ] Final Code Review & Documentation

**Deliverable:** Phase 1 Ready for Production ✅

---

### 📊 Q1 2027 - Pilot Installation

- [ ] Hardware aufbauen
- [ ] System konfigurieren
- [ ] Live-Test über 2 Wochen
- [ ] Feedback sammeln
- [ ] Bugs fixen
- [ ] Dokumentieren

**Deliverable:** Phase 1 LIVE ✅

---

## 🚀 Phase 2: Intelligente Automation (2027)

### Ziel
AI-Basics, Predictive Automation, erweiterte Sensorik

### Geplante Features
- [ ] Machine Learning Basics
- [ ] Prädiktive Automatisierungen
- [ ] Anomalie-Erkennung (z.B. "Sturz erkannt?")
- [ ] Multi-Sensor Integration
- [ ] Erweiterte Logging & Analytics

### Timeline
**Q1-Q2 2027:** Entwicklung
**Q3 2027:** Testing & Optimierung

---

## 🎓 Phase 3: Voice + KI (2027+)

### Geplante Features
- [ ] Sprachsteuerung (Speech-to-Text)
- [ ] Natural Language Understanding
- [ ] Voice Feedback (Text-to-Speech)
- [ ] KI-Integration (ChatGPT-ähnlich)
- [ ] Proaktive Assistenz

### Timeline
**2027+:** Nach Phase 2 Stabilisierung

---

## 📈 Success Metrics

### Phase 1
- ✅ Shelly-Geräte steuern sich via Dashboard
- ✅ Automatisierungen funktionieren zuverlässig
- ✅ System läuft 48h ohne Fehler
- ✅ Dokumentation ist vollständig
- ✅ Code ist reviewbar & wartbar

### Pilot-Installation
- ✅ System läuft 2 Wochen ohne Probleme
- ✅ Freund ist zufrieden
- ✅ GitHub zeigt: "Erste echte Installation"
- ✅ Portfolio-Stück für Marc & Claude

---

## 🔧 Technologie-Stack

### Phase 1
- **Hardware:** Lenovo ThinkCentre, Shelly Gen 1
- **Zentrale:** Ubuntu, NODE-RED, Python 3.8+
- **Frontend:** NODE-RED Dashboard 2.0
- **Backend:** Python (requests, asyncio, logging)
- **Versionierung:** Git & GitHub

### Phase 2+
- Zusätzlich: TensorFlow/Scikit-learn (ML Basics)
- Optional: Docker (für Deployment)

---

## 👥 Team & Rollen

| Person | Phase 1 | Phase 2+ |
|--------|---------|---------|
| **Marc** | Hardware, Integration, Testing | System-Erweiterung |
| **Claude** | Architecture, Code-Reviews, Backend | AI-Strategy |

---

## ⚠️ Risiken & Mitigation

| Risiko | Wahrscheinlichkeit | Mitigation |
|--------|-------------------|-----------|
| Shelly-Kompatibilität | Mittel | Früh testen, ggf. alternative Hardware |
| Schulungs-Stress (Marc) | Mittel | Puffer in Timeline, Pausen planen |
| Hardware-Verzögerung | Niedrig | Alternative Hardware-Quellen recherchieren |
| Scope Creep | Mittel | Klare Phase-Definition, Änderungen dokumentieren |

---

## 🎯 Milestones


✅ 31.12.2024 - Projekt-Setup fertig
⏳ 31.08.2026 - Shelly + NODE-RED läuft
⏳ 30.10.2025 - Dashboard produktiv
⏳ 30.11.2025 - System stabil & getestet
⏳ 31.12.2025 - Phase 1 Ready
🎯 01.01.2027 - Pilot Installation live
🚀 31.12.2027 - Phase 2 abgeschlossen


---

## 📚 Referenz

- [Architectur-Dokumentation](architecture.md)
- [Development-Guide](development.md)
- [GitHub Repository](https://github.com/GabbamorpH/S.A.R.A.H.---Projekt)

---

*"Der Weg ist das Ziel." – Marc & Claude*


