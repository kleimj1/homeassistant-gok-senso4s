# 🏠 Home Assistant Integration für den GOK Senso4s Gas-Sensor

Diese Home Assistant **Custom Component** ermöglicht das **Auslesen von mehreren GOK Senso4s Gas-Sensoren** über **Bluetooth (BLE)**. Sie zeigt den **Füllstand der Gasflasche (%)** sowie die **Batteriespannung (V)** direkt in Home Assistant an.

🔥 **Features:**
- ✅ Unterstützung für **mehrere Gasflaschen & Sensoren**
- ✅ Anzeige von **Gasfüllstand (%)** & **Batteriespannung (V)**
- ✅ **Automatische Erkennung** der Sensoren über **MAC-Adressen**
- ✅ **Benachrichtigung** bei niedrigem Füllstand (< 20 %)
- ✅ **HACS-Unterstützung** für einfache Installation
- ✅ **Optimierte BLE-Kommunikation** für stabilere Verbindung

---

## 🚀 Installation über HACS

1. **Öffne Home Assistant** und navigiere zu **HACS > Integrationen**.
2. **Klicke auf "Benutzerdefiniertes Repository hinzufügen"**.
3. **Gib die URL ein:**  
   ```
   https://github.com/kleimj1/homeassistant-gok-senso4s
   ```
4. **Wähle als Kategorie "Integration"** und klicke auf **Hinzufügen**.
5. **Suche nach "GOK Senso4s"** in HACS und installiere die Integration.
6. **Neustart von Home Assistant erforderlich!**  

---

## ⚙️ Konfiguration in Home Assistant

Nach der Installation muss die Integration in der `configuration.yaml` hinzugefügt werden:

```yaml
gok_senso4s:
  sensors:
    "AA:BB:CC:DD:EE:FF": "Gasflasche 1"
    "11:22:33:44:55:66": "Gasflasche 2"
    "77:88:99:AA:BB:CC": "Gasflasche 3"
```

**🔄 Home Assistant anschließend neu starten!**

---

## 📊 Sensoren in Home Assistant

Nach der Konfiguration findest du die Sensorwerte in Home Assistant:

| Sensor | Bedeutung | Einheit |
|--------|----------|---------|
| `sensor.gasflasche_1` | Füllstand der Gasflasche | `%` |
| `sensor.gasflasche_1_voltage` | Batteriespannung des Sensors | `V` |

---

## 📡 Automatisierung: Warnung bei niedrigem Gasstand

Wenn der Füllstand **unter 20 %** fällt, kann Home Assistant eine **Benachrichtigung senden**:

```yaml
automation:
  - alias: "Warnung: Gasfüllstand niedrig"
    trigger:
      - platform: numeric_state
        entity_id: sensor.gasflasche_1
        below: 20
    action:
      - service: notify.mobile_app
        data:
          title: "⚠️ Gaswarnung!"
          message: "Der Füllstand von Gasflasche 1 ist unter 20% gefallen!"
```

---

## 🎛️ Lovelace Dashboard für mehrere Sensoren

Füge dein eigenes **Dashboard** hinzu:

```yaml
type: grid
cards:
  - type: gauge
    entity: sensor.gasflasche_1
    min: 0
    max: 100
    severity:
      green: 50
      yellow: 20
      red: 10

  - type: gauge
    entity: sensor.gasflasche_2
    min: 0
    max: 100
    severity:
      green: 50
      yellow: 20
      red: 10

  - type: gauge
    entity: sensor.gasflasche_3
    min: 0
    max: 100
    severity:
      green: 50
      yellow: 20
      red: 10
```

---

## 🛠️ Technische Details

- **BLE-Kommunikation:** Das Skript verwendet `gatttool`, um die Sensordaten per Bluetooth Low Energy auszulesen.
- **Automatische Verbindung:** Falls der Sensor beim ersten Versuch nicht antwortet, wird eine erneute Verbindung versucht.
- **Mehrere Sensoren:** Die Integration unterstützt **beliebig viele Gasflaschen**, indem einfach die **MAC-Adressen** in der `configuration.yaml` hinterlegt werden.

---

## 🔄 Zukünftige Features (Geplant)

✅ Unterstützung für **MQTT** (Daten per MQTT senden statt direkt in Home Assistant)  
✅ Optionale **manuelle Kalibrierung** der Sensoren  
✅ **BLE-Optimierung**, um Verbindungsprobleme weiter zu reduzieren  

---

## ❤️ Mitwirken & Support

👨‍💻 **Pull Requests sind willkommen!** Falls du Ideen oder Verbesserungen hast, erstelle gerne einen PR oder Issue.

🌍 **Starte dieses Repository auf GitHub, wenn dir das Projekt gefällt!**  

🔗 **GitHub:** [kleimj1/homeassistant-gok-senso4s](https://github.com/kleimj1/homeassistant-gok-senso4s)

---
🚀 **Viel Spaß mit der GOK Senso4s Integration in Home Assistant!** 🔥
