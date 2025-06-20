import threading
from queue import Queue
from core.utils import rate_limit

class Bruter:
    def __init__(self, target, threads=4, delay=1):
        self.target = target
        self.threads = threads
        self.delay = delay
        self.queue = Queue()
        self.found = False

    @rate_limit(delay=1)  # Evita DoS
    def brute_worker(self):
        while not self.queue.empty() and not self.found:
            creds = self.queue.get()
            if self.target.check(creds):
                self.found = True
                print(f"[+] Credenciales válidas: {creds}")
            self.queue.task_done()

    def run(self, credentials_list):
        for creds in credentials_list:
            self.queue.put(creds)
        
        for _ in range(self.threads):
            t = threading.Thread(target=self.brute_worker)
            t.daemon = True
            t.start()
        self.queue.join()
