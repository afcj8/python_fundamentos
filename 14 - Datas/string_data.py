from datetime import datetime

data_str = "01/09/2024 11:30:00"    # data no formato string
data_obj = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print(data_obj)   # Exibe a data e hora no formato: 2024-09-01 11:30:00