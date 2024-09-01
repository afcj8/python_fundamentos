# Introdução

Python é uma linguagem de programação de alto nível e de uso geral, amplamente empregada em diversas áreas, como desenvolvimento web, ciência de dados, automação de tarefas e Machine Learning. Criada por Guido van Rossum e lançada em 1991, Python se destaca por sua filosofia de projeto, que enfatiza a legibilidade do código através de uma sintaxe clara e o uso de indentação significativa. Com tipagem dinâmica e suporte a gerenciamento automático de memória, Python oferece flexibilidade tanto para iniciantes quanto para desenvolvedores experientes, tornando-se uma escolha popular em projetos de todos os tipos e complexidades.

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