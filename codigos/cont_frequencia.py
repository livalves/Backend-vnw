# Terceiro Exercício: Contagem de Frequência
# Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
# caracteres da string e os valores representam quantas vezes cada caractere aparece.
# Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’]
# Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1}

def cont_frequencia(lista):
    dict_caracteres = {}
    for caracteres in lista:
        frequencia = lista.count(caracteres)
        dict_caracteres[caracteres] = frequencia
    return dict_caracteres

dict_caracteres = cont_frequencia(['Java', 'Java', 'Ruby', 'Javascript', 'Ruby'])
print(dict_caracteres)