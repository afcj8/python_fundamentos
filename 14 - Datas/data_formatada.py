from babel.dates import format_date
from datetime import datetime

data = datetime.now()
print("Data formatada:", format_date(data, locale='pt_BR'))   # data formatada em português