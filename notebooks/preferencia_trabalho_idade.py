import matplotlib.pyplot as plt
import pandas as pd
import colorsys

plt.style.use('seaborn-talk')
import warnings

df = pd.read_csv('../data/Dados-Pesquisa.csv',
                 sep=',',
                 low_memory=False)

# Agrupando os Dados
bins = [0, 20, 30, 40, 50, 60, 100]
df['AgeRanges'] = pd.cut(df['Age'],
                         bins,
                         labels=['< 20', '20-30', '30-40', '40-50', '50-60', '< 60'])

df2 = pd.crosstab(df.AgeRanges,
                  df.JobPref).apply(lambda r: r/r.sum(), axis=1)

# Definindo a Quantidade
num = len(df.AgeRanges.value_counts().index)

# Criando Lista de Cores
listaHSV = [(x * 1.0 / num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Gráfico de Barras
ax1 = df2.plot(kind='bar', stacked=True, color=listaRGB, title='Preferência de Trabalho por Idade')
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, bbox_to_anchor=(1.51, 1))
plt.show()
