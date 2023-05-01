import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение дат и уровня осадков из файла.
    dates, precipitations = [], []
    name = ''
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        precipitation = float(row[3])
        dates.append(current_date)
        precipitations.append(precipitation)
        if not name:
            name = row[1]
        else:
            continue

# Нанесение данных на диаграмму.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='blue', alpha=0.5)

# Форматирование диаграммы.
plt.title(f"Daily precipitations, {name} - 2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


