# Introdução

Python é uma linguagem de programação de alto nível e de uso geral, amplamente empregada em diversas áreas, como desenvolvimento web, ciência de dados, automação de tarefas e Machine Learning. Criada por Guido van Rossum e lançada em 1991, Python se destaca por sua filosofia de projeto, que enfatiza a legibilidade do código através de uma sintaxe clara e o uso de indentação significativa. Com tipagem dinâmica e suporte a gerenciamento automático de memória, Python oferece flexibilidade tanto para iniciantes quanto para desenvolvedores experientes, tornando-se uma escolha popular em projetos de todos os tipos e complexidades.

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