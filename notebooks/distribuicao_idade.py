import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')

df = pd.read_csv('../data/Dados-Pesquisa.csv',
                 sep=',',
                 low_memory=False)
print(df.head())
print(df.describe())


# Gerando um histograma
df.Age.hist(bins=60)
plt.xlabel('Idade')
plt.ylabel('Número de Profissionais')
plt.title('Distrubuição de Idade')
plt.show()
