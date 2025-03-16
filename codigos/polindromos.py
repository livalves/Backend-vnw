# Oitavo Exercício: Verificador de Palíndromos
# Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
# pode ser lida da mesma forma de trás para frente) e False caso contrário.
# Exemplo:
# entrada = "radar"
# Saída: True

def check_polindromos(palavra):
    return palavra.lower() == palavra.lower()[::-1]

polindromo = check_polindromos('radar')
print(polindromo)