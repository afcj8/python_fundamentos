# 11. Tuplas

A tupla é uma estrutura de dados semelhante a uma lista, porém com a característica de ser imutável. Visualmente, a diferença principal é que uma lista é criada utilizando colchetes `[]`, enquanto a tupla é criada utilizando parênteses `()`. Quando se afirma que uma tupla é imutável, isso significa que, após sua criação, seus elementos não podem ser alterados, removidos ou adicionados. A seguir, apresenta-se a estrutura de uma tupla:

```
tupla = (1, 2, 3, 4, 5)
print(tupla)    # (1, 2, 3, 4, 5)
```

Por ser imutável, a tupla é uma estrutura de dados mais rígida e segura, ideal para armazenar informações que devem permanecer inalteradas ao longo da execução do programa. Além disso, a tupla pode ser iterada utilizando um laço `for`, conforme exemplificado abaixo:

```
tupla = (1, 2, 3, 4, 5)
for t in tupla:
    print(t)    # 1, 2, 3, 4
```