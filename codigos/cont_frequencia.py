# Terceiro Exercício: Contagem de Frequência
# Função que recebe uma lista de strings e retorna um dicionário onde as chaves são as
# palavras e os valores representam quantas vezes cada palavra aparece.

def cont_frequencia(lista):
    dict_caracteres = {}
    for caracteres in lista:
        frequencia = lista.count(caracteres)
        dict_caracteres[caracteres] = frequencia
    return dict_caracteres

dict_caracteres = cont_frequencia(['Java', 'Java', 'Ruby', 'Javascript', 'Ruby'])
print(dict_caracteres)