import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Нанесение линий на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Выделение первой и последней точек.
    #ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    #ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей.
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break