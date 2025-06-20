# core/bruter.py
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class EthicalBruter:
    def __init__(self, target, threads=3, delay=1):
        self.target = target
        self.session = self._create_secure_session()  # ¡Sesión con retries!
    
    def _create_secure_session(self):
        session = requests.Session()
        retry = Retry(total=3, backoff_factor=1)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        return session
