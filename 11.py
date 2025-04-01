import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y=x^2')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

groups = ['ІПЗ-1/1', 'ІПЗ-2/1', 'ІПЗ-3/1', 'ІПЗ-4/1']
students = [23, 45, 12, 30]

plt.bar(groups, students)
plt.xlabel('Група')
plt.ylabel('Кількість студентів')
plt.title('Кількість студентів у різних групах')
plt.show()

import matplotlib.pyplot as plt

labels = ['Апельсини', 'Яблука', 'Банани', 'Виноград']
sizes = [25, 30, 20, 25]
colors = ['orange', 'green', 'yellow', 'purple']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Розподіл відсотків за категоріями')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 100 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.title('Діаграма розсіювання з випадковими даними')
plt.colorbar(label='Колірна шкала')
plt.show()