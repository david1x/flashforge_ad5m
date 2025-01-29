from homeassistant.components.camera import Camera
from .const import DOMAIN

class FlashForgeCamera(Camera):
    def __init__(self, printer_ip):
        super().__init__()
        self._printer_ip = printer_ip
        self._url = f"http://{printer_ip}:8080/?action=stream"
    
    def camera_image(self):
        response = requests.get(self._url, stream=True, timeout=10)
        return response.raw.read()
