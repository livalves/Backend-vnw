# Segundo Exercício: Ordenação de Tuplas
# Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
# escreva uma função que retorne a lista ordenada pela idade de forma crescente.
# Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)
# Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”)

def ordenando_lista(lista):
    return sorted(lista, key=lambda x: x[1], reverse=False)

lista_ordenada = ordenando_lista([("Samuel", 20), ("Karynne", 18), ("Carol", 21), ("Kleber", 21), ("Vinicius", 22)])
print(lista_ordenada)