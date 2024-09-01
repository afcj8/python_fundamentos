# 4. Função Input

A função `input()` é usada para ler a entrada do usuário como uma string. Quando utiliza-se a função `input()`, o programa pausa a execução e espera o usuário digitar algo e pressionar Enter. Por exemplo:

```
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
```

Nesse exemplo, o programa pergunta ao usuário "Qual é o seu nome?", e o valor digitado é armazenado na variável `nome`. Em seguida, ele exibe "Olá, [nome]".

## 4.1. Conversão

A conversão de tipos é essencial, especialmente em operações matemáticas. Se a conversão não for realizada, as operações podem resultar em concatenação de strings em vez de cálculos numéricos. Por exemplo:

```
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
resultado = num1 + num2
print("O resultado é:", resultado)
```

Neste caso, se o usuário digitar `3` e `5`, a saída será `35` em vez de `8`, pois os valores foram concatenados como strings. Para obter o resultado correto, é necessário converter as entradas em números.

Mesmo que o usuário insira um número, o valor retornado pela função `input()` será uma string. Portanto, para realizar operações numéricas, é necessário converter a entrada utilizando funções como `int()` ou `float()`:

```
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1 + num2
print("O resultado é:", resultado)
```

Neste exemplo, as entradas são convertidas para inteiros, permitindo que a soma seja realizada corretamente.

## 4.2. Entrada múltipla

Caso seja necessário obter várias entradas de uma única vez, pode-se utilizar a função `split()` em conjunto com `map()` para separar e converter os valores:

```
numeros = input("Digite dois números separados por espaço: ").split()
num1, num2 = map(int, numeros)
print("A soma dos números é:", num1 + num2)
```

Neste exemplo, o usuário digita dois números separados por espaço. A função `split()` divide a string em uma lista, e `map()` é usado para converter cada item da lista em um inteiro.