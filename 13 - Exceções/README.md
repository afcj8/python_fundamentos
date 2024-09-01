# 13. Exceções

Exceções em Python são eventos que ocorrem durante a execução de um programa e interrompem o fluxo normal do código. Elas são utilizadas para gerenciar erros que podem surgir durante a execução de uma aplicação, fornecendo uma maneira estruturada de capturar e tratar esses erros.

As exceções são objetos derivados da classe base `BaseException`. Quando uma exceção é lançada, a execução do programa é interrompida, e o controle é passado para o bloco de código que pode lidar com a exceção. Caso a exceção não seja tratada, o programa encerrará com uma mensagem de erro.

## 13.1. Tratamento de Exceções

Para tratar exceções, Python utiliza a estrutura `try-except`. O código suscetível a gerar uma exceção é inserido dentro do bloco `try`, e as exceções são tratadas no bloco `except`.

```
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida.")
```

## 13.2. Levantando Exceções

Exceções podem ser levantadas manualmente utilizando a palavra reservada `raise`. Isso é útil para sinalizar explicitamente que uma condição anômala foi encontrada.

```
def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

print(dividir(10, 0))  # ValueError: O divisor não pode ser zero.
```

## 13.3. Captura Genérica e Específica

Exceções podem ser capturadas de forma específica ou genérica. A captura específica é preferível, pois permite lidar com diferentes tipos de erros de maneira adequada.

```
try:
    resultado = int("texto")
except ValueError:
    print("Erro: não foi possível converter a string para um inteiro.")
except TypeError:
    print("Erro: tipo de dado inválido.")
```

## 13.4. Blocos else e finally

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

## 13.5. Hierarquia de Exceções

As exceções em Python seguem uma hierarquia, onde exceções mais específicas derivam de classes mais genéricas. Por exemplo, `ZeroDivisionError` é uma subclasse de `ArithmeticError`, que por sua vez é uma subclasse de `Exception`.

## 13.6. Criação de Exceções Personalizadas

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