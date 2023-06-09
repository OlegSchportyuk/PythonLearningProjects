import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=10)

# Назначение заголовка диаграммы и меток осей.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()