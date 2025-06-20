def generate_combinations(max_length=4):
    """Genera combinaciones numéricas básicas (solo educativo)."""
    from itertools import product
    chars = '0123456789'  # Solo números para demostración
    for length in range(1, max_length + 1):
        for combo in product(chars, repeat=length):
            yield ''.join(combo)
