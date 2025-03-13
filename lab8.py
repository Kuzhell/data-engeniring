
import pandas as pd
import matplotlib.pyplot as plt

file_path = "8.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

# Display the first 5 rows of each sheet
for sheet_name, df in sheets.items():
    print(f"Sheet: {sheet_name}")
    print(df.head(), "\n")

# Display sheet names and first 5 rows
for name, df in sheets.items():
    print(name, df.head(), sep="\n")

# Count missing values in each sheet
for name, df in sheets.items():
    print(name, df.isnull().sum(), sep="\n")

# Count unique educational institution names in a specific sheet
for name, df in sheets.items():
    if name == "Реєстр_коледжі":
        print(name, df["Назва закаладу освіти"].nunique(), sep="\n")

# Calculate the total number of applicants and graduates by institution
for name, df in sheets.items():
    if name == "Вступ":
        вступники = df.groupby("Заклад освіти")["Вступ"].sum()
        print(f"Загальна кількість вступників по кожному закладу ({name}):\n", вступники)
    elif name == "Випуск":
        випускники = df.groupby("Заклад освіти")["Випуск"].sum()
        print(f"Загальна кількість випускників по кожному закладу ({name}):\n", випускники)

# Find the specialty with the highest number of students in specific sheets
for name, df in sheets.items():
    if "Спеціальність" in df.columns: 
        if name == "Вступ":
            найбільше_вступників = df.groupby("Спеціальність")["Вступ"].sum().idxmax()
            print(f"Спеціальність з найбільшою кількістю студентів для вступу ({name}): {найбільше_вступників}")
        elif name == "Випуск":
            найбільше_випускників = df.groupby("Спеціальність")["Випуск"].sum().idxmax()
            print(f"Спеціальність з найбільшою кількістю студентів для випуску ({name}): {найбільше_випускників}")
        elif name == "Здобувачі":
            найбільше_здобувачів = df.groupby("Спеціальність")["Здобувачі"].sum().idxmax()
            print(f"Спеціальність з найбільшою кількістю студентів для здобувачів ({name}): {найбільше_здобувачів}")

# Plot the number of students by specialty for each sheet
for name, df in sheets.items():
    if "Спеціальність" in df.columns:
        if name == "Вступ":
            спец_вступ = df.groupby("Спеціальність")["Вступ"].sum()
            спец_вступ.plot(kind='bar', color='#ffcc00', figsize=(10, 6)) 
            plt.title(f"Кількість студентів за спеціальностями ({name})")
            plt.xlabel("Спеціальність")
            plt.ylabel("Кількість студентів")
            plt.xticks(rotation=45, ha='right')
            plt.show()
        elif name == "Випуск":
            спец_випуск = df.groupby("Спеціальність")["Випуск"].sum()
            спец_випуск.plot(kind='bar', color='#0056b3', figsize=(10, 6))  
            plt.title(f"Кількість студентів за спеціальностями ({name})")
            plt.xlabel("Спеціальність")
            plt.ylabel("Кількість студентів")
            plt.xticks(rotation=45, ha='right')
            plt.show()

# Plot the number of applicants over the years
for name, df in sheets.items():
    if "Рік" in df.columns and "Вступ" in df.columns:
        вступники_за_роками = df.groupby("Рік")["Вступ"].sum()
        вступники_за_роками.plot(kind='line', marker='o', color='b', figsize=(10, 6))
        plt.title(f"Зміни кількості вступників за роками ({name})")
        plt.xlabel("Рік")
        plt.ylabel("Кількість вступників")
        plt.grid(True)
        plt.show()

# Plot the distribution of teachers by type of experience
for name, df in sheets.items():
    if "Тип стажу" in df.columns and "Кількість" in df.columns:
        стаж_розподіл = df.groupby("Тип стажу")["Кількість"].sum()
        стаж_розподіл.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), colors=['#FF0000', '#000000', '#800000', '#D3D3D3'])
        plt.title(f"Розподіл викладачів за типом стажу ({name})")
        plt.ylabel('')  
        plt.show()
