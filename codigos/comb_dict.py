# Sexto Exercício: Combinação de dicionários
# Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são inteiros. 
# A função deve combinar os dicionários somando os valores das chaves que aparecem em ambos.
# Exemplo:
# d1 = {"a": 2, "b": 3, "c": 5}
# d2 = {"a": 1, "b": 4, "d": 7}
# Saída: {"a": 3, "b": 7, "c": 5, "d": 7}

def combinando_dict(d1, d2):
    dict_novo = {}
    for k in set(d1) | set(d2):
        dict_novo[k] = d1.get(k, 0) + d2.get(k, 0)
    return dict(sorted(dict_novo.items()))

d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
dicionario = combinando_dict(d1, d2)
print(dicionario)

