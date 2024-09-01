# 12. Funções (def)

As funções em Python permitem organizar e reutilizar código, encapsulando lógica em blocos que podem ser invocados conforme necessário. Isso facilita a manutenção e a legibilidade do código.

## 12.1. Definição de Função

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

## 12.2. Parâmetros de Funções

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

- Função `*args`: A função `*args` permite que uma quantidade variável de argumentos seja passada para uma função. Esses argumentos são recebidos na forma de uma tupla, possibilitando a iteração sobre eles para realizar operações dentro da função. Isso é útil quando o número de argumentos é desconhecido ou variável.

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

## 12.3. Funções Anônimas (Lambdas)

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
print("Quadrado de 4:", resultado)  # Quadrado de 4: 16
```

## 12.4. Funções Recursivas

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