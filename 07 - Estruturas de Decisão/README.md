# 7. Estruturas de Decisão

Estruturas de decisão permitem que o código tome diferentes caminhos com base em condições específicas. Abaixo estão as principais estruturas de decisão:

## 7.1. if

A estrutura `if` executa um bloco de código se uma condição for verdadeira.

```
x = 10
if x > 5:
    print("x é maior que 5")
```

A palavra reservada `if` tem efeito de analisar uma decisão, “se” em caso afirmativo, realize determinada operação.

## 7.2. if-else

A estrutura `if-else` permite que o código execute um bloco alternativo se a condição for falsa.

```
x = 4
if x > 5:
    print("x é maior que 5")
else:
    print("x é menor ou igual a 5")
```

A palavra reservada: `else`, que significa “senão”, caso não entre na primeira opção, entrará na segunda.

## 7.3. if-elif-else

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

## 7.4. Nested if (if aninhado)

Blocos de `if` podem ser aninhados dentro de outros blocos `if` para testar múltiplas condições.

```
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x é maior que 5 e y é maior que 15")
```

Essas estruturas são fundamentais para controle de fluxo, permitindo que programas respondam dinamicamente a diferentes condições.