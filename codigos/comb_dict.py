# Sexto Exercício: Combinação de dicionários
# Função que recebe dois dicionários onde as chaves são strings e os valores são inteiros
# e combina os dicionários somando os valores das chaves que aparecem em ambos.

def combinando_dict(d1, d2):
    dict_novo = {}
    for k in set(d1) | set(d2):
        dict_novo[k] = d1.get(k, 0) + d2.get(k, 0)
    return dict(sorted(dict_novo.items()))

d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
dicionario = combinando_dict(d1, d2)
print(dicionario)

