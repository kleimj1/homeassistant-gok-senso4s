from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import load_platform

DOMAIN = "gok_senso4s"

def setup(hass: HomeAssistant, config: dict):
    """Setup der GOK Senso4s Integration"""
    if DOMAIN not in config:
        return False

    hass.data[DOMAIN] = config[DOMAIN]
    load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
