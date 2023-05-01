import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename1 = 'data/death_valley_2018_simple.csv'
filename2 = 'data/sitka_weather_2018_simple.csv'
files = [filename1, filename2]


def get_data(filename):
    '''Получение и чтение данных'''
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, column_header in enumerate(header_row):
            if column_header == 'TMAX':
                max_i = index
            if column_header == 'TMIN':
                min_i = index
            if column_header == 'NAME':
                name_i = index

        # Получение дат, температурных минимумов и максимумов из файла.
        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            try:
                high = int(row[max_i])
                low = int(row[min_i])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

                global name
                if not name:
                    name = row[name_i]
                else:
                    continue


def format_name(name):
    '''Форматирует название местности.'''
    words = name.split()
    words[0] = words[0].title()
    words[1] = words[1].title()
    return ' '.join(words)


def show_data(dates, highs, lows, name):
    '''Рисует диаграмму и выводит на экран.'''
    # Нанесение данных на диаграмму.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Форматирование диаграммы.
    title = f"Daily high and low temperatures - 2018\n{format_name(name)}"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.ylim(0, 135)

    plt.show()


if __name__ == '__main__':
    for file in files:
        dates, highs, lows = [], [], []
        name = ''
        get_data(file)
        show_data(dates, highs, lows, name)