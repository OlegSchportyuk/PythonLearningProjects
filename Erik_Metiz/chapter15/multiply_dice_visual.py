'''Моделирует умножение результатов бросков двух шестигранных костей
и визуализирует результаты'''

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Анализ результатов.
min_result = 1
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(min_result, max_result+1)]

# Визуализация результатов.
x_values = list(range(min_result, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying two D6 dice rolls 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_mult.html')