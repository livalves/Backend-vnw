# Primeiro Exercício: Soma de elementos pares
# Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os elementos pares contidos nela.
# Exemplo: [2,4,10,3,9,7,15,22]
# Saída: A soma dos pares é: x

def soma_pares(elementos):
    pares = []
    for i in elementos:
        if i % 2 == 0: 
            pares.append(i) 
    return sum(pares)

soma = soma_pares([2,4,10,3,9,7,15,22])
print(f"A soma dos pares é: {soma}")