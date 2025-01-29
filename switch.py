import requests
from homeassistant.helpers.entity import ToggleEntity
from .const import DOMAIN

COMMANDS = {
    "pause": "M25",
    "resume": "M24",
    "stop": "M26",
    "light_on": "M146 r255 g255 b255",
    "light_off": "M146 r0 g0 b0",
}

class FlashForgeSwitch(ToggleEntity):
    def __init__(self, host, port, printer_ip, command):
        self._host = host
        self._port = port
        self._printer_ip = printer_ip
        self._command = command
        self._state = False
    
    def turn_on(self, **kwargs):
        self._send_command(COMMANDS[self._command])
        self._state = True
    
    def turn_off(self, **kwargs):
        self._send_command(COMMANDS[self._command])
        self._state = False
    
    def _send_command(self, command):
        url = f"http://{self._host}:{self._port}/api/execute/{self._printer_ip}/{command}"
        requests.get(url, timeout=5)