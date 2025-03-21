!pip install streamz pandas matplotlib

import pandas as pd

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")

import pandas as pd
from streamz.dataframe import DataFrame as sDataFrame

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")
sdf = sDataFrame(example=df)

for _, row in df.iterrows():
    sdf.emit(row.to_frame().T)
    sdf.stream.sink(print)

import pandas as pd
from streamz.dataframe import DataFrame as sDataFrame

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")
sdf = sDataFrame(example=df)

filtered_df = df[df["Заклад освіти"] == "Назва закладу"]

for _, row in filtered_df.iterrows():
    sdf.emit(row.to_frame().T)

import pandas as pd

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")

specialty_counts = df["Спеціальність"].value_counts()
max_specialty = specialty_counts.idxmax()
min_specialty = specialty_counts.idxmin()

print("Найпопулярніша спеціальність:", max_specialty)
print("Найменш популярна спеціальність:", min_specialty)

import pandas as pd

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")

institution_counts = df["Заклад освіти"].value_counts()

print(institution_counts)

import pandas as pd

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")

specialty_counts = df["Спеціальність"].value_counts()
max_specialty = specialty_counts.idxmax(), specialty_counts.max()
min_specialty = specialty_counts.idxmin(), specialty_counts.min()

print("Найпопулярніша спеціальність:", max_specialty)
print("Найменш популярна спеціальність:", min_specialty)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")

specialty_counts = df["Спеціальність"].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(specialty_counts.index, specialty_counts.values, color="purple")
plt.xlabel("Спеціальність")
plt.ylabel("Кількість здобувачів")
plt.title("Кількість здобувачів за спеціальностями")
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("rkeb.xlsx", sheet_name="Здобувачі")

rfkit_df = df[df["Заклад освіти"] == "РФКІТ"]
specialty_counts_rfkit = rfkit_df["Спеціальність"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(specialty_counts_rfkit, labels=specialty_counts_rfkit.index, autopct='%1.1f%%', colors=plt.cm.Purples(range(len(specialty_counts_rfkit))))
plt.title("Кількість здобувачів за спеціальностями у РФКІТ")
plt.axis('equal')  
plt.show()
