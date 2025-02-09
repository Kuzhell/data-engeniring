print(df.columns)



import pandas as pd

file_path = '3.xlsx'

df = pd.read_excel(file_path, sheet_name="Здобувачі")

print("Перші 10 записів:")
print(df.head(10))

print("\nОсновна інформація про структуру даних:")
print(df.info())



import pandas as pd

file_path = '3.xlsx'
df = pd.read_excel(file_path, sheet_name="Здобувачі")

total_students = df["Здобувачів"].sum()
print(f"Загальна кількість здобувачів: {total_students}")

funding_type_counts = df.groupby("Фінансування")["Здобувачів"].sum()
print("\nКількість здобувачів за типом фінансування:")
print(funding_type_counts)

degree_counts = df.groupby("Освітній ступінь")["Здобувачів"].sum()
print("\nКількість здобувачів за освітнім ступенем:")
print(degree_counts)

top_specialties = df.groupby("Спеціальність")["Здобувачів"].sum().nlargest(3)
print("\nТри спеціальності з найбільшою кількістю здобувачів:")
print(top_specialties)



import pandas as pd

file_path = '3.xlsx'
df = pd.read_excel(file_path, sheet_name="Здобувачі")

filtered_degree = df[df["Освітній ступінь"] == "Фаховий молодший бакалавр"]
print("\nДані за освітнім ступенем 'Фаховий молодший бакалавр':")
print(filtered_degree)

df["Здобувачів"] = pd.to_numeric(df["Здобувачів"], errors='coerce')

institutions_over_50 = df.groupby("Заклад освіти")["Здобувачів"].sum().reset_index()
institutions_over_50 = institutions_over_50[institutions_over_50["Здобувачів"] > 50]

print("\nЗаклади освіти, у яких кількість здобувачів більше 50 осіб:")
print(institutions_over_50)


contract_students = df[(df["Фінансування"] == "Контракт") & (df["Здобувачів"] > 10)]
print("\nЗаклади з типом фінансування 'Контракт', де кількість здобувачів перевищує 10:")
print(contract_students)

students_by_specialty = df.groupby("Спеціальність")["Здобувачів"].sum()
print("\nЗагальна кількість здобувачів для кожної спеціальності:")
print(students_by_specialty)




import pandas as pd

file_path = '3.xlsx'
df = pd.read_excel(file_path, sheet_name="Здобувачі")

df["Тип/Фінансування"] = df["Тип закладу освіти"] + "/" + df["Фінансування"]

df["Рентабельність"] = df["Здобувачів"].where(df["Фінансування"] == "Контракт", 0) * 17000

contract_filtered = df[df["Фінансування"] == "Контракт"]
contract_filtered.to_excel("контрактні_здобувачі.xlsx", index=False)

students_by_specialty = df.groupby("Спеціальність")["Здобувачів"].sum().reset_index()
students_by_specialty.to_csv("здобувачі_за_спеціальністю.csv", index=False)
