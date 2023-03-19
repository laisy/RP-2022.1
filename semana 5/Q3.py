import pandas as pd
import collections


df = pd.read_csv('./car.data.csv', header=None,
                  names=['price','maint','doors','persons','lug_boot','safety','value'])

df['price'] = df['price'].map({'low': 0, 'mid': 1, 'high': 2, 'vhigh': 3})
df['maint'] = df['maint'].map({'low': 0, 'mid': 1, 'high': 2, 'vhigh': 3})
df['doors'] = df['doors'].map({'2': 2, '3': 3, '4': 4, '5more': 55})
df['persons'] = df['persons'].map({'2': 2, '4': 4, 'more': 55})
df['lug_boot'] = df['lug_boot'].map({'small': 0, 'med': 1, 'big': 2,})
df['safety'] = df['safety'].map({'low': 0, 'mid': 1, 'high': 2,})
df['value'] = df['value'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3})

df.to_csv('./car.dataResultado.csv', sep=';', index=False)