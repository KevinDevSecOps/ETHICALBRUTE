import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class HTTPBruter:
    def __init__(self, url, data_payload):
        self.url = url
        self.data_payload = data_payload  # Ej: {"user": "{user}", "pass": "{pass}"}
        self.session = self._create_session()

    def _create_session(self):
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=1)
        session.mount('https://', HTTPAdapter(max_retries=retries))
        return session

    def check(self, credentials):
        try:
            data = {
                k: v.format(**credentials) 
                for k, v in self.data_payload.items()
            }
            r = self.session.post(self.url, data=data)
            return "Login failed" not in r.text
        except requests.RequestException:
            return False
