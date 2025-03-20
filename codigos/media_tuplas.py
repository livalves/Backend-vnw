# Quinto Exercício: Tupla de médias
# Função que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
# notas e retorna uma lista de tuplas, onde cada tupla contém o nome do aluno e sua média de notas.

def calculo_media(dict_alunos):
    media_alunos = []
    for chave, valor in dict_alunos.items():
        media = sum(valor)/len(valor)
        media_alunos.append((chave, round(media, 2)))
    return media_alunos
    
media_alunos = calculo_media({"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]})  
print(media_alunos)

