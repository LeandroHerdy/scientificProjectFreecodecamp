import matplotlib.pyplot as plt
import pandas as pd
import colorsys

plt.style.use('seaborn-talk')
import warnings

df = pd.read_csv('../data/Dados-Pesquisa.csv',
                 sep=',',
                 low_memory=False)

# Definindo a qunatidade
num = len(df.EmploymentField.value_counts().index)

# Criando a Lista de Cores
listaHSV = [(x * 1.0 / num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df.EmploymentField.value_counts().index

# Gráfico de Pizza
fatias, texto = plt.pie(df.EmploymentField.value_counts(), colors=listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor=(1.3, 1))
plt.title('Área de Trabalho Atual')
plt.show()
