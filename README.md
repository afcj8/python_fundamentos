# Introdução

Python é uma linguagem de programação de alto nível e de uso geral, amplamente empregada em diversas áreas, como desenvolvimento web, ciência de dados, automação de tarefas e Machine Learning. Criada por Guido van Rossum e lançada em 1991, Python se destaca por sua filosofia de projeto, que enfatiza a legibilidade do código através de uma sintaxe clara e o uso de indentação significativa. Com tipagem dinâmica e suporte a gerenciamento automático de memória, Python oferece flexibilidade tanto para iniciantes quanto para desenvolvedores experientes, tornando-se uma escolha popular em projetos de todos os tipos e complexidades.

# 1. Variáveis

São espaços na memória utilizados para armazenar valores. Esses valores podem ser de diversos tipos, como:

- Texto (string): "Olá, mundo!", "Python"
- Inteiros (int): 1024, 0, -15
- Decimais ou flutuantes (float): 10.5, 5.6, 2.0
- Booleano (boolean): verdadeiro ou falso

Para identificar o tipo de dado armazenado em uma variável, o Python oferece a função nativa `type()`, que pode ser usada para verificar o tipo da variável.

# 1.1. Atribuições

A variável, como dito antes, tem o objetivo de guardar algum valor. Em Python, para se atribuir um valor a uma variável, deve-se seguir a seguinte sintaxe:

`[nome da variável] = [valor da variável]`

**Importante:** O símbolo “=” (igual) não tem o significado de igualdade matemática, mas indica um comando para guardar o valor especificado na posição de memória representada pela variável. É importante ressaltar que ao realizar essa operação, o valor antigo da variável é perdido.

**Obs.:** Também pode-se atribuir expressões a uma variável, como mostra o exemplo a seguir:

`[nome da variável] = [valor da variável 1] + [valor da variável 2]`

No exemplo acima, realiza-se uma soma simples, mas também é possível realizar operações mais complexas, como multiplicação, divisão, subtração, ou até mesmo operações envolvendo funções matemáticas e lógicas. Por exemplo:

`resultado = (valor1 * valor2) - (valor3 / valor4) + pow(valor5, 2)`

Este exemplo, realiza a multiplicação do `valor1` por `valor2`, subtraindo o resultado da divisão de `valor3` por `valor4`, e somando o quadrado de `valor5`. Isso demonstra como é possível combinar diversas operações para atribuir um resultado mais complexo a uma variável.

# 2. Operações

Em Python, como em outras linguagens, pode-se realizar operações aritméticas, relacionais (booleanas) e lógicas sobre os valores guardados nas variáveis.

# 2.1. Operações Aritméticas

As operações aritméticas são fundamentais para a resolução de equações. Elas incluem a adição, subtração, divisão e multiplicação, que, apesar de parecerem simples, são essenciais para a realização de qualquer cálculo matemático. A seguir, mostram-se as principais operações aritméticas nativas do Python.

| Operação      | Operador | Exemplo           |
| ------------- | -------- | ----------------- |
| Adição        |     +    | 5 + 3 = 8         |
| Subtração     |     -    | 8 - 3 = 5         |
| Divisão       |     /    | 10 / 3 = 3.333... |
| Multiplicação |     *    | 5 * 3 = 15        |
| Exponenciação |     **   | 5 ** 2 = 25       |
| Div. inteira  |     //   | 10 // 3 = 3       |
| Resto da div. |     %    | 10 % 3 = 1        |

# 2.2. Operações Relacionais (Booleanas)

Os símbolos ==, !=, >, >=, < e <= são utilizados em afirmações, que podem ser verdadeiras ou falsas. Se a afirmação for verdadeira, o programa devolve True, senão ele devolve False, seguindo a lógica abaixo:

| Operação    | Símbolo  | Exemplo           |
| ----------- | -------- | ----------------- |
| Igual       |    ==    | 5 == 3 --> False  |
| Diferente   |    !=    | 8 != 3 --> True   |
| Maior       |    >     | 10 > 3 --> True   |
| Maior-igual |    >=    | 5 >= 5 --> True   |
| Menor       |    <     | 5 < 2 --> False   |
| Menor-igual |    <=    | 10 <= 3 --> False |

# 2.3. Operações Lógicas

Essas afirmações de True ou False podem ser modificadas e relacionadas usando operações lógicas, sendo elas and, or e not.

# 2.3.1 Operador and

Permite que a expressão seja verdadeira quando ambos os valores lógicos sejam verdadeiros, resulta em falso caso contrário.

| a | b | a and b |
| - | - | ------- |
| v | v | v       |
| v | f | f       |
| f | v | f       |
| f | f | f       |

# 2.3.2 Operador or

Nesse caso, a condição é verdadeira quando qualquer um dos valores for verdadeiro. A condição é falsa em apenas um caso, quando ambos forem falsos.

| a | b | a or b  |
| - | - | ------- |
| v | v | v       |
| v | f | v       |
| f | v | v       |
| f | f | f       |

# 2.3.3 Operador not

A negação realiza uma inversão no valor lógico ao qual a operação é realizada. Caso seja falso o resultado é verdadeiro, caso verdadeiro o resultado é falso.

| a | not a   |
| - | ------- |
| v | f       |
| f | v       |

# 3. Função Print

A função `print()` é usada para exibir mensagens ou dados na tela. Ela pode exibir strings (texto), números, variáveis e até mesmo resultados de expressões. Por exemplo:

`print("Olá, mundo!")`

Esse código exibe a mensagem "Olá, mundo!" na tela.

**Importante:** Pode-se passar vários itens separados por vírgula, e o `print()` irá exibi-los na mesma linha, separados por um espaço:

`print("A soma de 2 + 2 é:", 2 + 2)`

Isso exibirá: `A soma de 2 + 2 é: 4`.

# 3.1. Separador (sep)

O parâmetro `sep` permite definir um separador diferente do espaço padrão. O separador pode ser qualquer texto, inclusive com várias letras. 

**Obs.:** O separador deve ser colocado após todos os dados na lista de parâmetros da função `print()`.

`print("A", "B", "C", sep="-")`

Isso exibirá: `A-B-C`.

# 3.2. Fim de Linha (end)

Por padrão, o comando `print()` adiciona uma quebra de linha ao mostrar todos os valores listados como parâmetros. O parâmetro `end` permite alterar o comportamento padrão de terminar a impressão com uma nova linha. Por exemplo:

```
print("Olá", end=" ")
print("mundo!")
```

Isso exibirá: `Olá mundo!` (na mesma linha).

# 4. Função Input

A função `input()` é usada para ler a entrada do usuário como uma string. Quando utiliza-se a função `input()`, o programa pausa a execução e espera o usuário digitar algo e pressionar Enter. Por exemplo:

```
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
```

Nesse exemplo, o programa pergunta ao usuário "Qual é o seu nome?", e o valor digitado é armazenado na variável `nome`. Em seguida, ele exibe "Olá, [nome]".

# 4.1. Conversão

Mesmo que o usuário digite um número, o valor retornado será uma string. Se precisar de um número, é necessário converter a entrada com funções como `int()` ou `float()`:

```
idade = int(input("Quantos anos você tem? "))
```

Aqui, a entrada do usuário será convertida para um inteiro.