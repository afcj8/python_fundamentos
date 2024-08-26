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
print("Você tem", idade, "anos")
```

Aqui, a entrada do usuário será convertida para um inteiro.

# 5. Método Format

O método `format()` em Python é utilizado para formatar strings de maneira flexível e poderosa, permitindo a inserção de variáveis ou valores em uma string de forma controlada e organizada. Ele oferece uma maneira mais legível e sofisticada de combinar strings e variáveis do que simplesmente concatená-las com o operador `+`.

```
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)
```

Saída:  "Meu nome é [nome] e eu tenho [idade] anos."

Os argumentos passados para `format()` podem ser posicionados com base na ordem em que são fornecidos:

```
print("O valor de {} é maior que {}.".format(10, 5))
```

Saída: `O valor de 10 é maior que 5.`

Pode-se usar nomes para passar argumentos, por exemplo:

```
print("O {animal} é {cor}.".format(animal="gato", cor="preto"))
```

Saída: `O gato é preto.`

O método `format()` permite especificar detalhes adicionais, como a precisão de números decimais:

```
print("O valor de pi com três casas decimais é {:.3f}".format(3.14159265359))
```

Saída: `O valor de pi com três casas decimais é 3.142`

# 5.1. f-strings

Embora o método `format()` seja muito útil, as f-strings introduzidas no Python 3.6 oferecem uma maneira ainda mais simples e rápida de formatar strings, usando uma sintaxe semelhante:

```
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
```

# 6. Comentários

Um comentário é uma palavra ou frase usada de forma explicativa. Este deve conter informações importantes que expliquem o trecho de código. Pode ser usado para explicar o significado de uma variável, informar como o script funciona, o que o script faz etc.

```
# A função print() é usada para exibir uma mensagem na tela.
print("Olá, mundo!")
```
Em Python, os comentários são caracterizados pelo símbolo `#`, e tudo que estiver escrito a sua frente será ignorado ao executar o programa. Entretando, este símbolo representa um comentário de uma linha, ou seja, apenas o que estiver na mesma linha que `#` será ignorado.

Para comentar um texto descritivo com duas ou mais linhas, é utilizado três aspas, sejam elas duplas ou simples, sempre no ínicio e fim do texto.

```
"""
Assim é feito um comentário de texto. Sua utilidade é comentar uma quantidade maior de informações e detalhes de uma só vez.
"""
```

# 7. Estruturas de Decisão

Estruturas de decisão permitem que o código tome diferentes caminhos com base em condições específicas. Abaixo estão as principais estruturas de decisão:

# 7.1. if

A estrutura `if` executa um bloco de código se uma condição for verdadeira.

```
x = 10
if x > 5:
    print("x é maior que 5")
```

A palavra reservada `if` tem efeito de analisar uma decisão, “se” em caso afirmativo, realize determinada operação.

# 7.2. if-else

A estrutura `if-else` permite que o código execute um bloco alternativo se a condição for falsa.

```
x = 4
if x > 5:
    print("x é maior que 5")
else:
    print("x é menor ou igual a 5")
```

A palavra reservada: `else`, que significa “senão”, caso não entre na primeira opção, entrará na segunda.

# 7.3. if-elif-else

Essa estrutura permite testar múltiplas condições. O bloco `elif` (else if) é avaliado apenas se as condições anteriores forem falsas. O `else` é executado se todas as condições forem falsas.

```
x = 5
if x > 5:
    print("x é maior que 5")
elif x == 5:
    print("x é igual a 5")
else:
    print("x é menor que 5")
```

# 7.4. Nested if (if aninhado)

Blocos de `if` podem ser aninhados dentro de outros blocos `if` para testar múltiplas condições.

```
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x é maior que 5 e y é maior que 15")
```

Essas estruturas são fundamentais para controle de fluxo, permitindo que programas respondam dinamicamente a diferentes condições.