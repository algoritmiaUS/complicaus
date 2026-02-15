import sys

def solve():
    # 1. Lectura rápida de toda la entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Usamos un iterador para procesar la entrada secuencialmente como scanf
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    # 2. Precomputación (Lookup Table)
    # Dado que al final hacemos (b & 255), solo nos importan los bits 0 al 7.
    # El bit 8 y superiores no afectan a los bits 0-7 en esta operación de prefijo XOR.
    lut = [0] * 256
    for i in range(256):
        c = i
        # Simulamos el bucle C++: rep(j,0,30) b[j+1] = b[j+1] ^ b[j]
        # Solo necesitamos iterar hasta j=6 para actualizar el bit 7 (j+1).
        # Los bits superiores serán filtrados por la máscara 255 de todos modos.
        for j in range(7):
            # Si el bit j es 1, invertimos el bit j+1
            if (c >> j) & 1:
                c ^= (1 << (j + 1))
        lut[i] = c  # Ya está implícito el & 255 porque c era < 256 y no operamos bits > 7

    # 3. Procesamiento y Salida
    # Para cada número de entrada, tomamos sus últimos 8 bits (& 255) 
    # y buscamos el resultado precalculado.
    results = []
    for _ in range(n):
        val = int(next(iterator))
        results.append(str(lut[val & 255]))

    # Imprimir todo junto separado por espacios con un salto de línea final
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == '__main__':
    solve()