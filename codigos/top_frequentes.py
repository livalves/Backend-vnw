# Sétimo Exercício: Top 3 mais frequentes
# Dada uma lista de números, crie uma função que retorne os três números mais frequentes
# em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.
# Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
# Saída: [2, 1, 4]


from collections import Counter

def top_frequentes(lista):
    dict_contagem = Counter(lista)
    dict_ord = sorted(dict_contagem.items(), key=lambda x: (-x[1], x[0]))
    return [k for k, v in dict_ord[:3]]

top = top_frequentes([1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5])
print(top)


