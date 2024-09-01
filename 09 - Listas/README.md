# 9. Listas 

Listas são coleções ordenadas e mutáveis que permitem armazenar vários elementos em uma única variável. Esses elementos podem ser de qualquer tipo, como inteiros, strings, ou até mesmo outras listas. As listas são delimitadas por colchetes `[]` e os elementos são separados por vírgulas, conforme o exemplo abaixo:

```
lista = []  # Lista vazia
lista = [1, "Python", 3.14]
```

Em Python, a lista é um objeto do tipo `list`, é uma estrutura de dados nativa da linguagem. Cada elemento em uma lista é associado a um índice, que começa em `0` e vai até `n-1`, onde `n` é número total de elementos:

| índice    | 0 |    1     |   2   | ... | n-1 |
| --------- | - | -------- | ----- | --- | --- |
| **lista** | 1 | "Python" | 3.142 | ... | 112 |

## 9.1. Principais Caraterísticas

- Ordenação: Os elementos possuem uma ordem definida e podem ser acessados por seus índices.
- Mutabilidade: É possível modificar, adicionar ou remover elementos após a criação da lista.
- Heterogeneidade: Uma lista pode conter diferentes tipos de dados, como números e strings.

## 9.2. Acessando Elementos da Lista

Elementos de uma lista são acessados através de índices, o código a seguir acessa o primeiro elemento da lista e armazena na variável `primeiro_elemento` e a variável `ultimo_elemento` acessa o último elemento da lista:

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeiro_elemento = lista[0]    # Acessa o primeiro elemento (1)
ultimo_elemento = lista[-1]     # Acessa o último elemento (10)
print(primeiro_elemento)    # Imprime o primeiro elemento
print(ultimo_elemento)  # Imprime o último elemento
```

Támbem é possível acessar um intervalo de elementos:

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
intervalo_lista = lista[0:2]    # Acessa os elementos do índice 0 ao 1 (não inclui o índice 2)
print(intervalo_lista)  # [1, 2]
```

Para modificar um elemento específico na lista, basta referenciar seu índice:

```
lista[1] = 20   # Modifica o valor no índice 1 para 20
```

## 9.3. Principais Métodos

Métodos são funções associadas a objetos. No caso das listas, esses métodos são invocados diretamente a partir do objeto lista.

`lista.metodo()`

**Nota:** Muitos métodos de listas são mutáveis, ou seja, modificam a própria lista. A seguir, são apresentados alguns dos principais métodos:

- append(): Adiciona um elemento ao final da lista.

```
lista = [1, "Python", 3.14]
lista.append("Hello")  # Adiciona "Hello" ao final da lista
print(lista)  # [1, "Python", 3.14, "Hello"]
```

- insert(): Insere um elemento em um índice específico.

```
lista = [1, "Python", 3.14]
lista.insert(1, "world") # Adiciona "world" no índice 1
print(lista)  # [1, "world", "Python", 3.14]
```

- remove(): Remove o primeiro elemento igual ao valor especificado.

```
lista = [1, "Python", 3.14]
lista.remove("Python")    # Remove "Python" da lista
print(lista)    # [1, 3.14]
```

- pop(): Remove um item da lista pelo índice e retorna o seu valor.

```
lista = [1, "Python", 3.14]
print(lista.pop(1)) # Python
print(lista)    # [1, 3.14]
```

- clear(): Remove todos os elementos da lista.

```
lista = [1, "Python", 3.14]
lista.clear()
print(lista)    # []
```

- index(): Retorna o índice do primeiro elemento igual ao valor especificado.

```
lista = [1, "Python", 3.14]
indice = lista.index("Python")
print(indice)    # 1
```

- count(): Retorna o número de vezes que o valor especificado ocorre na lista.

```
lista = [1, 2, 3, 5, 8, 1, 9, 1]
qtd_vezes = lista.count(1)
print(qtd_vezes)    # 3
```

- sort(): Ordena os elementos da lista em ordem crescente.

```
lista = [1, 2, 3, 5, 8, 1, 9, 1]
lista.sort()
print(lista)  # [1, 1, 1, 2, 3, 5, 8, 9]
```

- reverse(): Inverte a ordem dos elementos na lista.

```
lista = [1, 2, 3, 5, 8, 1, 9, 1]
lista.reverse() 
print(lista)    # [1, 9, 1, 8, 5, 3, 2, 1]
```

## 9.4. Fuções Sobre Listas

Funções são chamadas independentemente de objetos e podem receber listas como argumentos. Elas não pertencem diretamente ao objeto `list`, mas podem operar sobre ela.

`funcao(lista)`

A maioria das funções que operam em listas não modifica a lista original, mas retornam um novo valor. A seguir, são apresentadas algumas das principais funções:

 - len(): Retorna o número de elementos da lista.

```
lista = [1, 3, 4, 6, 8, 9, 10]
tamanho = len(lista)
print(tamanho)  # 7
```

- max(): Retorna o maior valor da lista.

```
lista = [1, 3, 4, 6, 8, 9, 10]
maior = max(lista)
print(maior)  # 10
```

- min(): Retorna o menor valor da lista.

```
lista = [1, 3, 4, 6, 8, 9, 10]
menor = min(lista)
print(menor)  # 1
```

- sum(): Retorna a soma dos elementos da lista (válido para listas numéricas).

```
lista = [1, 3, 4, 6, 8, 9, 10]
soma = sum(lista)
print(soma)  # 41
```

- sorted(): Retorna uma nova lista com os elementos ordenados.

```
lista = [10, 3, 4, 6, 8, 9, 1]
ordem = sorted(lista)
print(ordem)  # [1, 3, 4, 6, 8, 9, 10]
```

## 9.5. Iterando Listas

Para percorrer os elementos de uma lista, utiliza-se um loop `for`. O código a seguir define uma lista chamada `frutas` com cinco strings, cada uma representando uma fruta. O loop `for` itera sobre cada elemento da lista, atribuindo o valor atual à variável `fruta` em cada iteração. O comando `print` é então usado para exibir o valor de `fruta`. O resultado é que cada fruta na lista é impressa em uma linha separada.

```
frutas = ["maçã", "banana", "uva", "morango", "abacaxi"]
for fruta in frutas:
    print(fruta)
```