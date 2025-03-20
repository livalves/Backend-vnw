# Oitavo Exercício: Verificador de Palíndromos
# Função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
# pode ser lida da mesma forma de trás para frente) e False caso contrário.

def check_polindromos(palavra):
    return palavra.lower() == palavra.lower()[::-1]

polindromo = check_polindromos('radar')
print(polindromo)