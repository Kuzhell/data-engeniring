import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import plotly.express as px
import numpy as np
import pandas as pd

x = np.linspace(-10, 10, 100)
y = x**2
df = pd.DataFrame({'X': x, 'Y': y})

fig = px.line(df, x='X', y='Y', title='Інтерактивний графік y = x^2')
fig.show()

import plotly.express as px
import pandas as pd

regions = ['Північ', 'Південь', 'Схід', 'Захід']
sales = [120, 150, 100, 130]

df = pd.DataFrame({'Регіон': regions, 'Продажі': sales})

fig = px.bar(df, x='Регіон', y='Продажі', title='Інтерактивна стовпчаста діаграма продажів за регіонами')
fig.show()

import plotly.express as px
import pandas as pd

labels = ['Апельсини', 'Яблука', 'Банани', 'Виноград']
sizes = [25, 30, 20, 25]
colors = {'Апельсини': 'orange', 'Яблука': 'red', 'Банани': 'yellow', 'Виноград': 'purple'}

df = pd.DataFrame({'Фрукт': labels, 'Частка': sizes})

fig = px.pie(df, names='Фрукт', values='Частка', title='Розподіл відсотків за категоріями',
             color='Фрукт',
             color_discrete_map=colors)
fig.update_traces(hovertemplate='%{label}: %{percent:.1%}')
fig.show()

import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
n_points = 100
prices = np.random.uniform(10, 100, n_points)
sales = np.random.randint(5, 50, n_points)
categories = np.random.choice(['Електроніка', 'Одяг', 'Книги'], n_points)
sizes = np.random.randint(20, 100, n_points)

df = pd.DataFrame({'Ціна': prices, 'Продажі': sales, 'Категорія товару': categories, 'Розмір': sizes})

fig = px.scatter(df, x='Ціна', y='Продажі', color='Категорія товару', size='Розмір',
                 hover_data=['Ціна', 'Продажі', 'Категорія товару'],
                 title='Взаємозв’язок між Ціною та Продажами з фільтрацією за категорією')
fig.show()

import plotly.express as px
import pandas as pd
import numpy as np

years = list(range(2013, 2023))
data = pd.DataFrame({
    'Рік': np.repeat(years, 4),
    'Регіон': ['Північ', 'Південь', 'Схід', 'Захід'] * 10,
    'Продажі': np.random.randint(50, 200, 40)
})

fig = px.bar(data, x='Регіон', y='Продажі', animation_frame='Рік', color='Регіон', title='Динаміка продажів у регіонах за останні 10 років')
fig.show()