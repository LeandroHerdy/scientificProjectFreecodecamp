import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('../data/Dados-Pesquisa.csv',
                 sep=',',
                 low_memory=False)

# Criando um Subset dos Dados
df4 = df.dropna(subset=['HoursLearning'])
df4 = df4[df['Age'].isin(range(0, 70))]

# Definindo os Valore de x e y
x = df4.Age
y = df4.HoursLearning

# Computando os Valores e Gerando o Gráfico
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-', color='red')
plt.xlabel('Idade')
plt.ylabel('Horas de Treinamento')
plt.title('Idade por Hora de Treinamento')
plt.show()