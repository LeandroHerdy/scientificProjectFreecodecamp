import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')

df = pd.read_csv('../data/Dados-Pesquisa.csv',
                 sep=',',
                 low_memory=False)

# Definindo a Quantidade
labels = df.Gender.value_counts().index
num = len(df.EmploymentField.value_counts().index)

# Criando uma Lista de Cores
listaHSV = [(x*1.0/num, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Gráfico de Pizza
fatias, texto = plt.pie(df.Gender.value_counts(), colors=listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor=(1.05, 1))
plt.title('sexo')
plt.show()
