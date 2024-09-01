# 10. Dicionários

Dicionários são uma estrutura de dados nativa do Python, composta por elementos que possuem dois componentes: uma `chave` e um `valor`. Um dicionário possui a seguinte estrutura:

`dicionario = {chave0:valor0, chave1:valor1, chave2:valor2, ..., chaveN:valorN}`

Assim como as listas, um dicionário pode ser criado vazio ou já contendo um ou mais elementos, conforme o exemplo a seguir:

```
dicionario_vazio = {}
print(dicionario_vazio) # {}
```

Para acessar os elementos de um dicionário, utiliza-se uma sintaxe semelhante à das listas, com os colchetes `[]`, entretanto entre eles não vai o índice do elemento, e sim a sua chave.

```
dicionario_vazio = {}
dicionario_vazio['carro1'] = 1997
dicionario_vazio['carro2'] = 2000
print(dicionario_vazio) # {'carro1': 1997, 'carro2': 2000}
```

Além disso, é possível iterar sobre um dicionário, utilizando o método `keys()`, que retorna um iterador com todas as chaves do dicionário:

```
dicionario = {'a': 1, 'b': 2, 'c': 3}

for key in dicionario.keys():
    print('Chave do elemento: {c}'.format(c=key))
    print('Valor do elemento: {v}'.format(v=dicionario[key]))
    print(30*'-')
```

Dicionários também podem ser utilizados em conjunto com listas, permitindo a organização de conjuntos de dados mais complexos:

```
dicionario = [
    {
        "nome": "João",
        "idade": 25,
        "cidade": "Natal"
    },
    {
        "nome": "Maria",
        "idade": 30,
        "cidade": "Recife"
    },
    {
        "nome": "José",
        "idade": 27,
        "cidade": "João Pessoa"
    }
]
print(dicionario)
```

Por fim, os dicionários são uma excelente estrutura de dados para armazenar e manipular informações. Em Python, eles podem ser facilmente convertidos para JSON, um formato amplamente utilizado para o envio e recebimento de dados na web.