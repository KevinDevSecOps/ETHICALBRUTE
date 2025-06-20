# **🔥 ETHICALBRUTE PRO - Herramienta Ética de Fuerza Bruta**  
**by [KevinDevSecOps](https://github.com/KevinDevSecOps) ❤️**  

**"El conocimiento es poder, pero la ética es nuestra brújula."**  

---

## **🔍 Descripción**  
**ETHICALBRUTE PRO** es una herramienta avanzada de *fuerza bruta ética* diseñada para **pentesters profesionales**, **equipos Red Team** y **entusiastas de la ciberseguridad** que buscan probar la resistencia de sistemas **con autorización previa**.  

🚀 **Perfecta para**:  
- Pruebas de penetración autorizadas (OSCP, CEH, EJPT).  
- Auditorías de seguridad en entornos controlados.  
- CTFs y laboratorios de hacking ético.  

⚠️ **ADVERTENCIA**:  
```diff
- SOLO USO LEGAL: Esta herramienta debe utilizarse ÚNICAMENTE en sistemas con permiso explícito.  
- El uso no autorizado es ILEGAL y está prohibido.  
```

---

## **✨ Características Principales**  

| **Módulo**               | **Tecnología**            | **Uso**                                   |  
|--------------------------|---------------------------|------------------------------------------|  
| **🔐 SSH Brute Force**    | Paramiko + Multihilo      | Ataque a credenciales SSH con soporte para keys. |  
| **🌐 HTTP/API Brute**     | Requests + Rotación de IP | Fuerza bruta en formularios web y APIs REST. |  
| **💾 Hash Cracking**      | PyCryptoDome + John       | Descifrado ético de hashes (MD5, SHA1, NTLM). |  
| **🛡️ WAF Bypass**        | User-Agents + Delays      | Evasión básica de Cloudflare/Akamai.     |  
| **📊 Burp Suite Integration** | Python-Burp-API       | Exportar resultados a Burp para análisis. |  

---

## **⚙️ Instalación**  

### **Requisitos**  
- Python 3.10+  
- Git  
- `sudo apt install john hashcat` (Para crackeo de hashes)  

### **Pasos**  
```bash
git clone https://github.com/KevinDevSecOps/ETHICALBRUTE.git  
cd ETHICALBRUTE  
pip install -r requirements-pro.txt  
```  

---

## **🚀 Uso Básico**  

### **1. Fuerza Bruta SSH**  
```python
from core.ssh_bruter import SSHAuditor  
from core.bruter import Bruter  

target = SSHAuditor("192.168.1.100")  
bruter = Bruter(target.test_credentials, threads=5)  

creds = [  
    {"username": "admin", "password": "P@ssw0rd!"},  
    {"username": "root", "password": "toor"}  
]  

bruter.run(creds)  
```  

### **2. Crackeo de Hashes**  
```bash
python3 core/hash_cracker.py -h md5 -f hashes.txt -w wordlists/rockyou.txt  
```  

### **3. Exportar a Burp Suite**  
```python
from burp import IBurpExtender  
from core.http import HTTPBruter  

class BurpExporter(IBurpExtender):  
    def registerExtenderCallbacks(self, callbacks):  
        self.callbacks = callbacks  
        bruter = HTTPBruter("https://target.com/login")  
        results = bruter.run_scan()  
        self.callbacks.issueAlert(f"¡Credenciales encontradas: {len(results)}!")  
```  

---

## **📌 Ejemplo de Uso en CTF**  
```bash
# Escaneo SSH con wordlist personalizada  
python3 main.py --ssh --target 10.10.10.5 --user admin --wordlist passwords.txt  

# Crackeo de hashes MD5  
python3 main.py --hash md5 --hash-file hashes.txt --wordlist rockyou.txt  
```  

---

## **❤️ Contribuir**  
¡Tus aportes son bienvenidos! Sigue estos pasos:  
1. Haz fork del proyecto.  
2. Crea una rama: `git checkout -b feature/nueva-funcion`.  
3. Haz commit: `git commit -m "feat: Añadí soporte para X"`.  
4. Haz push: `git push origin feature/nueva-funcion`.  
5. Abre un **Pull Request**.  

---

## **📜 Licencia**  
**MIT License** - Copyright © 2023 [KevinDevSecOps](https://github.com/KevinDevSecOps).  
```diff
+ Ética ante todo. Usa este conocimiento para proteger, no para dañar.  
```  

---

## **📞 Contacto**  
- **Twitter**: [@KevinDevSecOps](https://twitter.com/KevinDevSecOps)  
- **Email**: ethicalhacker@protonmail.com  

---

```python
# Código con ❤️ para hackers éticos.  
while ethics == True:  
    print("Hack the Planet (Responsibly!)")  
```  

**⭐ ¿Te gusta el proyecto? Dale una estrella en [GitHub](https://github.com/KevinDevSecOps/ETHICALBRUTE)!**
## 📅 Roadmap  
- [ ] Soporte para SSH (usando Paramiko)  
- [ ] Integración con Burp Suite  
- [ ] Dockerizar la herramienta
while you.coding == True:  
    print("Keep hacking the world (ethically!) ❤️🔥")
