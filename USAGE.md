# 📖 Cómo Usar ETHICALBRUTE (Guía Completa)

## 🔍 Requisitos
- Python 3.10+
- Librerías: `pip install -r requirements.txt`
- Wordlists (opcional): Descarga `rockyou.txt` o crea la tuya.

## 🚀 Ejecución Básica
```bash
python3 ETHICALBRUTE.py -t http://target.com/login -u admin -w wordlist.txt
```

## 🛠️ Opciones Avanzadas
| Argumento   | Descripción                          | Ejemplo                     |
|-------------|--------------------------------------|-----------------------------|
| `-t/--target` | URL o IP del objetivo               | `-t 192.168.1.100`          |
| `-u/--user`   | Nombre de usuario a probar          | `-u admin`                  |
| `-w/--wordlist`| Ruta a la wordlist                 | `-w ~/wordlists/rockyou.txt`|
| `-T/--threads` | Número de hilos (default: 5)       | `-T 10`                     |

## ⚠️ Importante
- **Solo para pruebas autorizadas**.
- Usa `--delay 2` para evitar bloqueos por WAF.
```

---

#### **2. Ampliar Explicaciones**  
**Falta**:  
- **Ejemplos realistas** (sin targets reales):  
  ```bash
  # Ejemplo para CTF:
  python3 ETHICALBRUTE.py -t http://ctf.example.com/login -u guest -w common_passwords.txt
  ```  
- **Cómo generar wordlists**:  
  ```bash
  crunch 6 8 0123456789 -o num_wordlist.txt  # Genera combinaciones numéricas
  ```  
- **Salida esperada**:  
  ```bash
  [+] Probando credenciales: admin:password123
  [!] Éxito: Credenciales válidas -> admin:Admin@123
  ```
