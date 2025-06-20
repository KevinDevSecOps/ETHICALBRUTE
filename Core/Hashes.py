import subprocess
import tempfile

class HashCracker:
    @staticmethod
    def crack_hash(hash_str, hash_type="md5", wordlist="wordlists/rockyou.txt"):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.write(hash_str.encode())
            tmp.flush()
            cmd = ["john", tmp.name, f"--format={hash_type}", f"--wordlist={wordlist}"]
            try:
                subprocess.run(cmd, check=True)
                return True
            except subprocess.CalledProcessError:
                return False
