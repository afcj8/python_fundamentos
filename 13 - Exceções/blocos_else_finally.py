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