import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

file_path = r'C:\Users\admin\Downloads\QJPN628BIS.csv'
df = pd.read_csv(file_path, header=None, names=['Date', 'Index'], parse_dates=['Date'], index_col='Date')

print(df.head())

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Index'], marker='o', linestyle='-')
plt.title('Index to Time')
plt.xlabel('Date')
plt.ylabel('Index 2010=100')
plt.grid(True)
plt.show()

print(df.corr())

print(df.describe())

half_point = len(df) // 2
period1 = df.iloc[:half_point, :]
period2 = df.iloc[half_point:, :]

t_stat, p_value = ttest_ind(period1['Index'], period2['Index'])

print(f'T-статистика: {t_stat}')
print(f'P-значение: {p_value}')

alpha = 0.05
if p_value < alpha:
    print('Отвергаем нулевую гипотезу: средние значения различны')
else:
    print('Не отвергаем нулевую гипотезу: средние значения схожи')