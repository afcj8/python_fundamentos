try:
    resultado = int("texto")
except ValueError:
    print("Erro: não foi possível converter a string para um inteiro.")
except TypeError:
    print("Erro: tipo de dado inválido.")