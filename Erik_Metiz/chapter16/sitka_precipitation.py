import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение дат и уровня осадков из файла.
    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        precipitation = float(row[3])
        dates.append(current_date)
        precipitations.append(precipitation)

# Нанесение данных на диаграмму.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='blue', alpha=0.5)

# Форматирование диаграммы.
plt.title("Daily precipitations - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


