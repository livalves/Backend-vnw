# Quarto Exercício: Contagem de Palavras
# Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
# Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
# Exemplo: ["banana maçã banana laranja maçã maçã"]
# Saída: {"banana": 2, "maçã": 3, "laranja": 1}

def cont_palavras(string):
    str_separada =  string.split(' ')
    dict_palavras = {}
    for palavra in str_separada:
        ocorrencia = str_separada.count(palavra)
        dict_palavras[palavra] = ocorrencia
    return dict_palavras

dict_palavras = cont_palavras("banana maçã banana laranja maçã maçã")
print(dict_palavras)