import httpx
from bs4 import BeautifulSoup
from app.config import settings

class UrjaPortalClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.client = httpx.Client(timeout=15.0, follow_redirects=True)
        self.is_authenticated = False

    def login(self) -> bool:
        login_url = f"{self.base_url}/login"
        payload = {"username": settings.default_username, "password": settings.default_password}
        response = self.client.post(login_url, data=payload)
        
        if response.status_code in (200, 302):
            self.is_authenticated = True
            return True
        return False

    def ensure_auth(self):
        if not self.is_authenticated:
            self.login()

    def get_meter_details(self, meter_id: str) -> dict:
        self.ensure_auth()
        url = f"{self.base_url}/meters/{meter_id}"
        response = self.client.get(url)

        if response.status_code == 401 or "login" in str(response.url):
            self.login()
            response = self.client.get(url)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch meter {meter_id} (Status: {response.status_code})")

        soup = BeautifulSoup(response.text, "html.parser")

        serial_elem = soup.find("span", {"id": "meter-serial"})
        status_elem = soup.find("td", {"class": "status-value"})
        location_elem = soup.find("span", {"id": "meter-location"})

        return {
            "meter_id": meter_id,
            "serial_number": serial_elem.text.strip() if serial_elem else "UNKNOWN",
            "status": status_elem.text.strip() if status_elem else "UNKNOWN",
            "location": location_elem.text.strip() if location_elem else "UNKNOWN"
        }