#Entrar com um ângulo em graus e imprimir: 
# seno, co-seno, tangente, secante,
#co-secante e co-tangente deste ângulo.

from os import system
system ('cls')
import math

def calcular_trigonometria(angulo_graus):
    """Calcula as funções trigonométricas de um ângulo em graus."""

    try:
        angulo_radianos = math.radians(angulo_graus)

        seno = math.sin(angulo_radianos)
        cosseno = math.cos(angulo_radianos)
        tangente = math.tan(angulo_radianos)

        # Evitar divisão por zero para tangente, secante, cossecante e cotangente
        if abs(cosseno) < 1e-10:  # Usando uma tolerância para comparação com zero
            secante = float('inf')  # Representa infinito
            tangente = float('inf') if seno > 0 else float('-inf')
        else:
            secante = 1 / cosseno

        if abs(seno) < 1e-10:
            cossecante = float('inf')
            cotangente = float('inf') if cosseno > 0 else float('-inf')
        else:
            cossecante = 1 / seno
            cotangente = 1 / tangente

        return {
            "seno": seno,
            "cosseno": cosseno,
            "tangente": tangente,
            "secante": secante,
            "cossecante": cossecante,
            "cotangente": cotangente,
        }
    except ValueError:
        return "Ângulo inválido. Por favor, insira um número."

# Exemplo de uso:
try:
    angulo = float(input("Digite o ângulo em graus: "))
    resultados = calcular_trigonometria(angulo)

    if isinstance(resultados, dict):
        print(f"Para o ângulo de {angulo} graus:")
        print(f"Seno: {resultados['seno']:.4f}")
        print(f"Cosseno: {resultados['cosseno']:.4f}")
        print(f"Tangente: {resultados['tangente']:.4f}")
        print(f"Secante: {resultados['secante']:.4f}")
        print(f"Cossecante: {resultados['cossecante']:.4f}")
        print(f"Cotangente: {resultados['cotangente']:.4f}")
    else:
        print(resultados)
except ValueError:
    print("Entrada inválida. Digite um número.")