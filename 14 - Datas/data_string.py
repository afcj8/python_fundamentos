from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)   # Exibe a data e hora no formato: dia/mês/ano hora:minuto:segundo