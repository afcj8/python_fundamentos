dicionario = {'a': 1, 'b': 2, 'c': 3}

for key in dicionario.keys():
    print('Chave do elemento: {c}'.format(c=key))
    print('Valor do elemento: {v}'.format(v=dicionario[key]))
    print(30*'-')