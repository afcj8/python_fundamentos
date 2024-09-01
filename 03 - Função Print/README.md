# 3. Função Print

A função `print()` é usada para exibir mensagens ou dados na tela. Ela pode exibir strings (texto), números, variáveis e até mesmo resultados de expressões. Por exemplo:

```
print("Olá, mundo!")
```

Esse código exibe a mensagem "Olá, mundo!" na tela.

**Importante:** Pode-se passar vários itens separados por vírgula, e o `print()` irá exibi-los na mesma linha, separados por um espaço:

```
print("A soma de 2 + 2 é:", 2 + 2)
```

Isso exibirá: `A soma de 2 + 2 é: 4`.

## 3.1. Separador (sep)

O parâmetro `sep` permite definir um separador diferente do espaço padrão. O separador pode ser qualquer texto, inclusive com várias letras. 

**Obs.:** O separador deve ser colocado após todos os dados na lista de parâmetros da função `print()`.

```
print("A", "B", "C", sep="-")
```

Isso exibirá: `A-B-C`.

## 3.2. Fim de Linha (end)

Por padrão, o comando `print()` adiciona uma quebra de linha ao mostrar todos os valores listados como parâmetros. O parâmetro `end` permite alterar o comportamento padrão de terminar a impressão com uma nova linha. Por exemplo:

```
print("Olá", end=" ")
print("mundo!")
```

Isso exibirá: `Olá mundo!` (na mesma linha).