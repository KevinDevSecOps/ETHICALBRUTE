# 🔐 EthicalBrute - Framework de Fuerza Bruta Ético

[![License](https://img.shields.io/badge/License-GPLv3-blue)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellowgreen)](https://www.python.org/)
[![Tests](https://github.com/KevinDevSecOps/EthicalBrute/actions/workflows/tests.yml/badge.svg)](https://github.com/KevinDevSecOps/EthicalBrute/actions)

**Herramienta educativa para pruebas de resistencia controladas** con protecciones integradas contra uso malintencionado. Diseñada para pentesters, auditores y estudiantes de ciberseguridad.

```bash
# Instalación rápida
pip install git+https://github.com/KevinDevSecOps/EthicalBrute.git

# Demo con sitio de prueba autorizado
ethicalbrute demo --target http://testphp.vulnweb.com/
```

## 🌟 ¿Por qué EthicalBrute?
| Característica               | Beneficio                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| 🔒 **Whitelist integrada**    | Solo objetivos autorizados (nunca sitios reales)                          |
| ⏱️ **Límites automáticos**   | Delay entre intentos + máximo de peticiones                               |
| 📜 **Cumple con OSCP/EJPT**  | Ideal para preparar certificaciones éticas                                |
| 🛡️ **Hashing SHA-256**       | Nunca envía contraseñas en claro                                         |

## 🛠️ Módulos Principales
```python
from ethicalbrute import EthicalBrute

# 1. Fuerza bruta HTTP básica
tool = EthicalBrute("http://localhost:8080/")
tool.brute_force_login("admin", ["password", "123456"])

# 2. Generador de wordlists seguras
from ethicalbrute.wordlists import generate_wordlist
words = generate_wordlist(base_words=["admin", "sysadmin"], max_length=8)
```

## 📂 Estructura del Proyecto
```
ethicalbrute/
├── core/               # Lógica principal
│   ├── brute.py        # Ataques controlados
│   └── safety.py       # Validaciones
├── wordlists/          # Diccionarios de prueba
│   ├── top_100.txt     # Contraseñas comunes
│   └── custom/         # Wordlists personalizadas
└── tests/              # Pruebas unitarias
    ├── test_brute.py
    └── test_safety.py
```

## 🚀 Primeros Pasos
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/KevinDevSecOps/EthicalBrute.git
   cd EthicalBrute
   ```

2. **Configura entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -e .
   ```

3. **Ejecuta demo educativa**:
   ```bash
   ethicalbrute demo --learn
   ```

## 📌 Casos de Uso Válidos
- 🎓 **Enseñanza**: Demostrar importancia de contraseñas seguras
- 🔍 **Pentesting**: Pruebas en entornos controlados con permiso
- 🛡️ **Autoauditorías**: Verificar resistencia de tus propios sistemas

## ⚠️ Restricciones Éticas
- ✖️ **No funciona** en dominios fuera de la whitelist
- ✖️ **Requiere confirmación** para >50 intentos
- ✖️ **Incluye delays** configurables (mínimo 1.5 segundos)

## 🤝 ¿Cómo Contribuir?
1. Haz fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcion`)
3. Envía tu PR con:
   - Tests actualizados
   - Documentación clara

```bash
# Ejecuta tests antes de contribuir
pytest -v tests/ --cov=core/
```

## 📜 Licencia
GNU GPLv3 - [Ver licencia completa](LICENSE)

> **Warning**  
> **Ético ≠ Ilegal**: Este software solo debe usarse con permiso explícito por escrito. Los desarrolladores no asumen responsabilidad por mal uso.

---

Hecho con ❤️ por [@KevinDevSecOps](https://github.com/KevinDevSecOps) | [☕ Invítame un café](https://www.buymeacoffee.com/kevindevsecops
