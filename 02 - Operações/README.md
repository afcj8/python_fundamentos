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