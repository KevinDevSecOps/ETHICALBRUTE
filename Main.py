import time
from src.password_checker import check_password
from src.generator import generate_combinations
from tqdm import tqdm

def ethical_bruteforce(target_password, max_length=4):
    print("[+] Iniciando Ethical BruteForce (Modo Educativo)")
    print(f"[+] Objetivo: '{target_password}' (solo prueba local)")
    
    found = False
    for guess in tqdm(generate_combinations(max_length), desc="Probando combinaciones"):
        if check_password(guess, target_password):
            print(f"\n[+] Contraseña encontrada: '{guess}'")
            found = True
            break
    
    if not found:
        print("\n[-] Contraseña no encontrada (prueba aumentar longitud)")

if __name__ == "__main__":
    ethical_bruteforce("123")  # Ejemplo: Solo prueba con "123"
