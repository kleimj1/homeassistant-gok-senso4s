from homeassistant.helpers.entity import Entity
import logging
from .gok_ble import read_gok_sensor

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Erstelle Sensor-Entities für jeden Sensor in der Konfiguration."""
    sensors = []
    for mac, name in hass.data["gok_senso4s"].get("sensors", {}).items():
        sensors.append(GOKSenso4sSensor(name, mac))

    add_entities(sensors, True)

class GOKSenso4sSensor(Entity):
    """Repräsentiert einen GOK Senso4s Sensor"""

    def __init__(self, name, mac):
        self._name = name
        self._mac = mac
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    @property
    def unit_of_measurement(self):
        return "%"

    def update(self):
        """Aktualisiert die Sensordaten"""
        data = read_gok_sensor(self._mac)
        if "error" in data:
            _LOGGER.error(f"Fehler beim Abrufen von {self._mac}: {data['error']}")
            return

        self._state = data["gas_level"]
        self._attributes["voltage"] = data["voltage"]
