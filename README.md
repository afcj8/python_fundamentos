# Introdução

Python é uma linguagem de programação de alto nível e de uso geral, amplamente empregada em diversas áreas, como desenvolvimento web, ciência de dados, automação de tarefas e Machine Learning. Criada por Guido van Rossum e lançada em 1991, Python se destaca por sua filosofia de projeto, que enfatiza a legibilidade do código através de uma sintaxe clara e o uso de indentação significativa. Com tipagem dinâmica e suporte a gerenciamento automático de memória, Python oferece flexibilidade tanto para iniciantes quanto para desenvolvedores experientes, tornando-se uma escolha popular em projetos de todos os tipos e complexidades.

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

# 13. Exceções

Exceções em Python são eventos que ocorrem durante a execução de um programa e interrompem o fluxo normal do código. Elas são utilizadas para gerenciar erros que podem surgir durante a execução de uma aplicação, fornecendo uma maneira estruturada de capturar e tratar esses erros.

As exceções são objetos derivados da classe base `BaseException`. Quando uma exceção é lançada (raise), a execução do programa é interrompida, e o controle é passado para o bloco de código que pode lidar com a exceção. Caso a exceção não seja tratada, o programa encerrará com uma mensagem de erro.

# 13.1. Tratamento de Exceções

Para tratar exceções, Python utiliza a estrutura `try-except`. O código suscetível a gerar uma exceção é inserido dentro do bloco `try`, e as exceções são tratadas no bloco `except`.

```
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida.")
```

# 13.2. Levantando Exceções

Exceções podem ser levantadas manualmente utilizando a palavra reservada `raise`. Isso é útil para sinalizar explicitamente que uma condição anômala foi encontrada.

```
def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

print(dividir(10, 0))  # ValueError: O divisor não pode ser zero.
```

# 13.3. Captura Genérica e Específica

Exceções podem ser capturadas de forma específica ou genérica. A captura específica é preferível, pois permite lidar com diferentes tipos de erros de maneira adequada.

```
try:
    resultado = int("texto")
except ValueError:
    print("Erro: não foi possível converter a string para um inteiro.")
except TypeError:
    print("Erro: tipo de dado inválido.")
```

# 13.4. Blocos else e finally

O bloco `else` é executado se nenhum erro ocorrer no bloco `try`, enquanto o bloco `finally` é executado independentemente de uma exceção ter sido lançada ou não. O `finally` é útil para liberar recursos, como fechar arquivos ou conexões de rede.

```
try:
    arquivo = open('dados.txt', 'w')  # Modo de escrita 'w'
    arquivo.write('Gravando dados no arquivo')
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    print("Dados gravados com sucesso.")
finally:
    print("Fechando o arquivo.")
    arquivo.close()

try:
    arquivo = open('dados.txt', 'r')  # Modo de leitura 'r'
    dados = arquivo.read()
    print("Conteúdo do arquivo:", dados)
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Fechando o arquivo.")
    arquivo.close()
```

# 13.5. Hierarquia de Exceções

As exceções em Python seguem uma hierarquia, onde exceções mais específicas derivam de classes mais genéricas. Por exemplo, `ZeroDivisionError` é uma subclasse de `ArithmeticError`, que por sua vez é uma subclasse de `Exception`.

# 13.6. Criação de Exceções Personalizadas

Exceções personalizadas podem ser criadas para representar erros específicos da lógica do programa. Essas exceções são definidas como subclasses de `Exception`.

```
class SaldoInsuficienteError(Exception):
    pass

def sacar(valor, saldo):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")
    saldo = saldo - valor
    return saldo

sacar(100, 50)
```

# 14. Datas

Em Python, a biblioteca `datetime` é uma ferramenta robusta para lidar com datas e horários. Com ela, é possível criar, manipular e extrair informações de objetos de data. A seguir, apresenta-se um exemplo básico de como obter a data e a hora atuais:

```
from datetime import datetime

agora = datetime.now()
print(agora)    # Exibe o dia, mês, ano, hora, minuto, segundo e microsegundo atuais
```

Para extrair informações específicas, como o dia, o mês ou o ano, o processo é direto:

``` 
from datetime import datetime

dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year
print("Dia:", dia)  # dia atual
print("Mês:", mes)  # mês atual
print("Ano:", ano)  # ano atual
```

# 14.1. Formatação de Datas

A formatação de datas é uma tarefa comum, seja para exibir a data em um formato legível ou para converter uma string em um objeto de data. O módulo `datetime` oferece funcionalidades para ambas as tarefas. Para converter um objeto de data em uma string formatada, pode-se utilizar o método `strftime`:

```
from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)   # Exibe a data e hora no formato: dia/mês/ano hora:minuto:segundo
```

Para realizar o processo inverso, ou seja, converter uma string em um objeto de data, utiliza-se o método `strptime`:

```
from datetime import datetime

data_str = "01/09/2024 11:30:00"    # data no formato string
data_obj = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print(data_obj)   # Converte e exibe a string como um objeto de data
```

Outra operação comum ao lidar com datas é o cálculo da diferença entre duas delas. O `datetime` facilita essa operação:

```
from datetime import datetime

data1 = datetime(2024, 9, 1)
data2 = datetime(2024, 12, 25)
diferenca = data2 - data1
print(diferenca)  # Exibe a diferença entre as duas datas
```

Caso seja necessário criar um objeto de data para uma data específica, pode-se proceder da seguinte forma:

```
from datetime import datetime

natal = datetime(2024, 12, 25)
print("Natal:", natal)   # Natal: 2024-12-25 00:00:00
```

Por fim, ao trabalhar com formatação de datas em diferentes idiomas, a biblioteca `babel` pode ser utilizada para facilitar a localização:

```
from babel.dates import format_date
from datetime import datetime

data = datetime.now()
print("Data formatada:", format_date(data, locale='pt_BR'))   # data formatada em português
```