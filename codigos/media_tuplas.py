# Quinto Exercício: Tupla de médias
# Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
# notas, crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do
# aluno e sua média de notas.
# Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
# Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]

def calculo_media(dict_alunos):
    media_alunos = []
    for chave, valor in dict_alunos.items():
        media = sum(valor)/len(valor)
        media_alunos.append((chave, round(media, 2)))
    return media_alunos
    
media_alunos = calculo_media({"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]})  
print(media_alunos)

