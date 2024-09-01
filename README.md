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

# 8. Estruturas de Repetição

Estruturas de repetição são fundamentais para executar um bloco de código várias vezes, de forma controlada. Elas permitem iterar sobre sequências, como listas e strings, ou repetir ações até que uma condição seja satisfeita. As principais estruturas de repetição em Python são `for` e `while`.

# 8.1. For Loop

O `for` é utilizado para iterar sobre elementos de uma sequência (como listas, tuplas, strings ou range). A cada iteração, o valor do elemento da sequência é atribuído a uma variável, e o bloco de código associado ao loop é executado.

```
for i in range(5):
    print(i)
```

Nesse exemplo, o loop `for` percorre a sequência gerada por `range(5)`, imprimindo os números de 0 a 4.

O padrão da função `range()` é 0 como valor inicial, no entanto, é possível especificar o valor inicial adicionando um parâmetro - `range(2,6)`, que significa os valores de 2 a 6 (mas não incluindo o 6).

# 8.2. While Loop

O `while` repete a execução de um bloco de código enquanto uma condição for verdadeira. A condição é avaliada antes de cada iteração, e se for falsa, o loop é interrompido.

```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Aqui, o `while` continua executando o bloco de código enquanto a variável `contador` for menor que 5, incrementando seu valor a cada iteração.

# 8.3. Controle de Loop: break e continue

- `break`: Interrompe a execução do loop imediatamente, saindo dele.
- `continue`: Pula a iteração atual e passa para a próxima.

```
for i in range(10):
    if i == 5:
        break
    print(i)
```

Este loop imprime os números de 0 a 4. Quando `i` atinge 5, o `break` interrompe o loop.

```
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Nesse caso, o número 2 é pulado, e o loop imprime os números 0, 1, 3 e 4.

# 8.4. Loops Aninhados

Python permite a utilização de loops dentro de outros loops, conhecidos como loops aninhados. Isso é útil para percorrer estruturas de dados mais complexas, como listas de listas.

```
for i in range(3):
    for j in range(2):
        print(f'i = {i}, j = {j}')
```

Esse código imprime todas as combinações possíveis dos valores de `i` e `j`.

As estruturas de repetição são ferramentas essenciais para a execução de tarefas repetitivas e para o processamento de dados em sequências.

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

# 9.1. Principais Caraterísticas

- Ordenação: Os elementos possuem uma ordem definida e podem ser acessados por seus índices.
- Mutabilidade: É possível modificar, adicionar ou remover elementos após a criação da lista.
- Heterogeneidade: Uma lista pode conter diferentes tipos de dados, como números e strings.

# 9.2. Acessando Elementos da Lista

Elementos de uma lista são acessados através de índices, o código a seguir acessa o primeiro elemento da lista e armazena na variável `primeiro_elemento` e a variável `ultimo_elemento` acessa o último elemento da lista:

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeiro_elemento = lista[0]    # Acessa o primeiro elemento (1)
ultimo_elemento = lista[-1]     # Acessa o último elemento (10)
print(primeiro_elemento)
print(ultimo_elemento)
```

Támbem é possível acessar um intervalo de elementos:

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
intervalo_lista = lista[0:2]    # Acessa os elementos do índice 0 ao 1 (não inclui o índice 2)
print(intervalo_lista)
```

Para modificar um elemento específico na lista, basta referenciar seu índice:

```
lista[1] = 20   # Modifica o valor no índice 1 para 20
```

# 9.3. Principais Métodos

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

# 9.4. Fuções Sobre Listas

Funções são chamadas independentemente de objetos e podem receber listas como argumentos. Elas não pertencem diretamente ao objeto lista, mas podem operar sobre ele.

`funcao(lista)`

A maioria das funções que operam em listas não modifica a lista original, mas retornam um novo valor. A seguir, são apresentadas algumas das principais funções:

 - len(): Retorna o número de elementos da lista.

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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

# 9.5. Iterando Listas

Para percorrer os elementos de uma lista, utiliza-se um loop `for`. O código a seguir define uma lista chamada `frutas` com cinco strings, cada uma representando uma fruta. O loop `for` itera sobre cada elemento da lista, atribuindo o valor atual à variável `fruta` em cada iteração. O comando `print` é então usado para exibir o valor de `fruta`. O resultado é que cada fruta na lista é impressa em uma linha separada.

```
frutas = ["maçã", "banana", "uva", "morango", "abacaxi"]
for fruta in frutas:
    print(fruta)
```

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

# 11. Tuplas

A tupla é uma estrutura de dados semelhante a uma lista, porém com a característica de ser imutável. Visualmente, a diferença principal é que uma lista é criada utilizando colchetes `[]`, enquanto a tupla é criada utilizando parênteses `()`. Quando se afirma que uma tupla é imutável, isso significa que, após sua criação, seus elementos não podem ser alterados, removidos ou adicionados. A seguir, apresenta-se a estrutura de uma tupla:

```
tupla = (1, 2, 3, 4, 5)
print(tupla)    # (1, 2, 3, 4, 5)
```

Por ser imutável, a tupla é uma estrutura de dados mais rígida e segura, ideal para armazenar informações que devem permanecer inalteradas ao longo da execução do programa.

# 12. Funções (def)

As funções em Python permitem organizar e reutilizar código, encapsulando lógica em blocos que podem ser invocados conforme necessário. Isso facilita a manutenção e a legibilidade do código.

# 12.1. Definição de Função

Uma função é definida com a palavra reservada `def`, seguida pelo nome da função, uma lista de parâmetros opcionais entre parênteses e, finalmente, um bloco de código indentado que representa o corpo da função. O formato básico de uma função em Python é o seguinte:

```
def nome_da_funcao(parametros_opcionais):
    # Corpo da função
    return valor_opcional
```

- `def`: Palavra reservada usada para definir uma função.
- `nome_da_funcao`: Nome que identifica a função, utilizado para chamá-la posteriormente
- `parametros_opcionais`: Variáveis locais que a função pode receber para realizar suas operações. Podem ser zero ou mais parâmetros.
- `return` (opcional): Palavra reservada que especifica o valor que a função devolve como resultado. Se omitido, a função retorna `None`.

Para chamar uma função, é necessário declará-la no escopo do código e, se houver parâmetros, passá-los adequadamente.

```
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

nota1 = 7.5
nota2 = 8.0
media = calcular_media(nota1, nota2)    # Chama a função calcular_media
print(f"A média das notas é: {media:.2f}")  # A média das notas é: 7.75
```

**Obs.:** Variáveis de escopo local só podem ser utilizadas dentro da função em que foram declaradas, enquanto variáveis globais podem ser acessadas em todo o código.

# 12.2. Parâmetros de Funções

- Função sem Parâmetros e sem Retorno: Uma função sem parâmetros e sem retorno realiza uma tarefa específica sem necessitar de informações adicionais e sem retornar um valor ao final da execução. Esse tipo de função é útil quando a tarefa é independente de dados externos ou quando o resultado da operação não precisa ser utilizado em outro contexto.

```
def saudacao():
    print("Olá, bem-vindo(a)!")

saudacao()  # Olá, bem-vindo(a)!
```

- Função com Parâmetros e com Retorno: Funções com parâmetros e retorno permitem realizar operações com valores fornecidos e devolver um resultado ao final. Esse tipo de função é fundamental para criar operações que dependem de dados variáveis e cujos resultados são reutilizados.

```
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # 7
```

Nesta função, dois parâmetros são recebidos (`a` e `b`), e a soma deles é retornada. Ao atribuir o resultado da função `soma(3, 4)` a variável `resultado`, o valor obtido será 7.

**Obs.:** Os argumentos de uma função devem ser passados na ordem correta, e o número de argumentos na chamada da função deve corresponder ao número de parâmetros definidos.

- Função com Parâmetros Padrão: Funções que utilizam parâmetros padrão assumem um valor específico caso nenhum argumento seja fornecido. Isso confere flexibilidade à função, permitindo que seja chamada com um número variável de argumentos, sem comprometer a execução.

```
def peso(m, g=9.8):
    return m * g

print(peso(10))  # 98.0
print(peso(10, 10))  # 100
```

Quando a função é chamada sem um argumento, o valor padrão é utilizado. Caso contrário, o valor fornecido substitui o padrão.

- Função *args: A função `*args` permite que uma quantidade variável de argumentos seja passada para uma função. Esses argumentos são recebidos na forma de uma tupla, possibilitando a iteração sobre eles para realizar operações dentro da função. Isso é útil quando o número de argumentos é desconhecido ou variável.

```
def calcular_area_retangulo(largura, *args):
    areas = []
    for alturas in args:
        areas.append(largura * alturas)
        
    return areas

resultado = calcular_area_retangulo(2, 3, 4, 5)
print(resultado)    # [6, 8, 10]
```

Neste exemplo, a função `calcular_area_retangulo` utiliza `*args` para calcular a área de vários retângulos, sendo que a largura é fixa e as alturas variam conforme os argumentos fornecidos.

# 12.3. Funções Anônimas (Lambdas)

Funções anônimas, ou lambdas, são definidas em uma única linha utilizando a palavra reservada `lambda`, seguida pelos parâmetros e a expressão a ser retornada:

```
soma = lambda a, b: a + b
```

Essas funções são úteis quando se necessita de uma função temporária e simples. No exemplo a seguir, demonstra-se o uso de uma função lambda para calcular o quadrado de um número:

```
# função lambda para calcular o quadrado de um número
quadrado = lambda x: x**2

# usando a função lambda
resultado = quadrado(4)
print("Quadrado de 4:", resultado)
```

# 12.4. Funções Recursivas

Recursão é uma técnica em programação onde uma função chama a si mesma para resolver um problema. Para que uma função recursiva seja eficaz, é essencial que ela possua uma condição de parada, também conhecida como caso base, a fim de evitar loops infinitos.

```
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # 120
```

No exemplo acima, a função `fatorial` utiliza a recursão para calcular o fatorial de um número. A condição de parada é estabelecida quando o valor de `n` é igual a 0 ou 1, evitando que a função continue chamando a si mesma indefinidamente.