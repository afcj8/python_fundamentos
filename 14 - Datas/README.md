# 14. Datas

Em Python, a biblioteca `datetime` é uma ferramenta robusta para lidar com datas e horários. Com ela, é possível criar, manipular e extrair informações de objetos de data. A seguir, apresenta-se um exemplo básico de como obter a data e a hora atual:

```
from datetime import datetime

agora = datetime.now()
print(agora)    # Exibe o dia, mês, ano, hora, minuto, segundo e microsegundo atuais
```

Para extrair informações específicas, como o dia, o mês ou o ano, o processo é direto:

``` 
from datetime import datetime

dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year
print("Dia:", dia)  # dia atual
print("Mês:", mes)  # mês atual
print("Ano:", ano)  # ano atual
```

## 14.1. Formatação de Datas

A formatação de datas é uma tarefa comum, seja para exibir a data em um formato legível ou para converter uma string em um objeto de data. O módulo `datetime` oferece funcionalidades para ambas as tarefas. Para converter um objeto de data em uma string formatada, pode-se utilizar o método `strftime`:

```
from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)   # Exibe a data e hora no formato: dia/mês/ano hora:minuto:segundo
```

Para realizar o processo inverso, ou seja, converter uma string em um objeto de data, utiliza-se o método `strptime`:

```
from datetime import datetime

data_str = "01/09/2024 11:30:00"    # data no formato string
data_obj = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print(data_obj)   # Exibe a data e hora no formato: 2024-09-01 11:30:00
```

Outra operação comum ao lidar com datas é o cálculo da diferença entre duas delas. O `datetime` facilita essa operação:

```
from datetime import datetime

data1 = datetime(2024, 9, 1)
data2 = datetime(2024, 12, 25)
diferenca = data2 - data1
print(diferenca)  # Exibe a diferença entre as duas datas
```

Caso seja necessário criar um objeto de data para uma data específica, pode-se proceder da seguinte forma:

```
from datetime import datetime

natal = datetime(2024, 12, 25)
print("Natal:", natal)   # Natal: 2024-12-25 00:00:00
```

Por fim, ao trabalhar com formatação de datas em diferentes idiomas, a biblioteca `babel` pode ser utilizada para facilitar a localização:

```
from babel.dates import format_date
from datetime import datetime

data = datetime.now()
print("Data formatada:", format_date(data, locale='pt_BR'))   # data formatada em português
```