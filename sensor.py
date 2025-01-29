import requests
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

BASE_URL = "http://{host}:{port}/api/execute/{printer_ip}/{command}"

class FlashForgeSensor(Entity):
    def __init__(self, hass, host, port, printer_ip, sensor_type):
        self._host = host
        self._port = port
        self._printer_ip = printer_ip
        self._sensor_type = sensor_type
        self._state = None
        self._name = f"FlashForge {sensor_type.capitalize()}"
    
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        url = BASE_URL.format(host=self._host, port=self._port, printer_ip=self._printer_ip, command=self._sensor_type)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self._state = data.get("machine_status", "Unknown")
        except requests.exceptions.RequestException:
            self._state = "Unavailable"

