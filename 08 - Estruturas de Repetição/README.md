# 8. Estruturas de Repetição

Estruturas de repetição são fundamentais para executar um bloco de código várias vezes, de forma controlada. Elas permitem iterar sobre sequências, como listas e strings, ou repetir ações até que uma condição seja satisfeita. As principais estruturas de repetição em Python são `for` e `while`.

## 8.1. For Loop

O `for` é utilizado para iterar sobre elementos de uma sequência (como listas, tuplas, strings ou range). A cada iteração, o valor do elemento da sequência é atribuído a uma variável, e o bloco de código associado ao loop é executado.

```
for i in range(5):
    print(i)
```

Nesse exemplo, o loop `for` percorre a sequência gerada por `range(5)`, imprimindo os números de 0 a 4.

O padrão da função `range()` é 0 como valor inicial, no entanto, é possível especificar o valor inicial adicionando um parâmetro - `range(2,6)`, que significa os valores de 2 a 6 (mas não incluindo o 6).

## 8.2. While Loop

O `while` repete a execução de um bloco de código enquanto uma condição for verdadeira. A condição é avaliada antes de cada iteração, e se for falsa, o loop é interrompido.

```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Aqui, o `while` continua executando o bloco de código enquanto a variável `contador` for menor que 5, incrementando seu valor a cada iteração.

## 8.3. Controle de Loop: break e continue

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

## 8.4. Loops Aninhados

Python permite a utilização de loops dentro de outros loops, conhecidos como loops aninhados. Isso é útil para percorrer estruturas de dados mais complexas, como listas de listas.

```
for i in range(3):
    for j in range(2):
        print(f'i = {i}, j = {j}')
```

Esse código imprime todas as combinações possíveis dos valores de `i` e `j`.

As estruturas de repetição são ferramentas essenciais para a execução de tarefas repetitivas e para o processamento de dados em sequências.