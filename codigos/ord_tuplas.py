# Segundo Exercício: Ordenação de Tuplas
# Função que recebe uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade
# e retorna uma lista ordenada pela idade de forma crescente.

def ordenando_lista(lista):
    return sorted(lista, key=lambda x: x[1], reverse=False)

lista_ordenada = ordenando_lista([("Samuel", 20), ("Karynne", 18), ("Carol", 21), ("Kleber", 21), ("Vinicius", 22)])
print(lista_ordenada)