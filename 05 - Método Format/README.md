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
print("O valor de pi com três casas decimais é {:.3f}".format(3.14159265359))   # 3.142
```

Saída: `O valor de pi com três casas decimais é 3.142`

## 5.1. f-strings

Embora o método `format()` seja muito útil, as f-strings introduzidas no Python 3.6 oferecem uma maneira ainda mais simples e rápida de formatar strings, usando uma sintaxe semelhante:

```
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
```