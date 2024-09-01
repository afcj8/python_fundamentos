# 1. Variáveis

São espaços na memória utilizados para armazenar valores. Esses valores podem ser de diversos tipos, como:

- Texto (string): "Olá, mundo!", "Python"
- Inteiros (int): 1024, 0, -15
- Decimais ou flutuantes (float): 10.5, 5.6, 2.0
- Booleano (boolean): verdadeiro ou falso

Para identificar o tipo de dado armazenado em uma variável, o Python oferece a função nativa `type()`, que pode ser usada para verificar o tipo da variável.

```
a = 10 # int
b = 5.2 # float
c = 'Python' # str
d = True # bool

print('Tipo de a:', type(a))
print('Tipo de b:', type(b))
print('Tipo de c:', type(c))
print('Tipo de d:', type(d))
```

# 1.1. Atribuições

A variável, como dito antes, tem o objetivo de guardar algum valor. Em Python, para se atribuir um valor a uma variável, deve-se seguir a seguinte sintaxe:

`[nome da variável] = [valor da variável]`

**Importante:** O símbolo “=” (igual) não tem o significado de igualdade matemática, mas indica um comando para guardar o valor especificado na posição de memória representada pela variável. É importante ressaltar que ao realizar essa operação, o valor antigo da variável é perdido.

**Obs.:** Também pode-se atribuir expressões a uma variável, como mostra o exemplo a seguir:

`[nome da variável] = [valor da variável 1] + [valor da variável 2]`

No exemplo acima, realiza-se uma soma simples, mas também é possível realizar operações mais complexas, como multiplicação, divisão, subtração, ou até mesmo operações envolvendo funções matemáticas e lógicas. Por exemplo:

`resultado = (valor1 * valor2) - (valor3 / valor4) + pow(valor5, 2)`

Este exemplo, realiza a multiplicação do `valor1` por `valor2`, subtraindo o resultado da divisão de `valor3` por `valor4`, e somando o quadrado de `valor5`. Isso demonstra como é possível combinar diversas operações para atribuir um resultado mais complexo a uma variável.