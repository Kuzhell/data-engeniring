!pip install dask

import dask.dataframe as dd
import dask.array as da
from dask.delayed import delayed
from dask.distributed import Client
import dask.dataframe as dd
import pandas as pd
import time

client = Client()
client

pdf = pd.read_excel("rkeb.xlsx", sheet_name="Вступ", engine="openpyxl")

ddf = dd.from_pandas(pdf, npartitions=1)

print(ddf.head())
print(ddf.info())

num_rows = len(ddf)
print(f"кількість записів у датасеті: {num_rows}")

num_specialties = ddf['Cпеціальність'].nunique().compute()
print(f"спеціальності на вступ: {num_specialties}")

stats = ddf['Вступ'].describe().compute()
print(f"Статистика: {stats}")

grouped_specialties = ddf.groupby('Спеціальність')['Вступ'].sum().compute()
print(f"вступники за спеціальностями: {grouped_specialties}")

@delayed
def compute_mean(ddf, column):
    return ddf.groupby('Спеціальність')[column].mean()

mean_value = compute_mean(ddf, 'Вступ')
print("середнє значення вступників для кожної спеціальності:")
print(mean_value.compute())

from dask.distributed import Client

client = Client()
print(client)

result = ddf.groupby('Спеціальність')['Вступ'].sum().compute()
print(result)
