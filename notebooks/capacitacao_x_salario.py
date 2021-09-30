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
df5 = df.dropna(subset=["ExpectedEarning"])
df5 = df5[df['MoneyForLearning'].isin(range(0, 60000))]

# Definindo os Valore de x e y
x = df5.MoneyForLearning
y = df5.ExpectedEarning

# Computando os Valores e Gerando o Gráfico
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-', color='red')
plt.xlabel('Investimento em Treinamento')
plt.ylabel('Expectativa Salarial')
plt.title('Investimento em Treinamento VS Expectativa Salarial')
plt.show()