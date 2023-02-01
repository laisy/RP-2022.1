import pandas as pd
import numpy as np

df = pd.read_csv('forestfires.csv', sep=',')

df['month'] = df['month'].map({
  'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
  'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
})


df['day'] = df['day'].map({
  'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4,
  'fri': 5, 'sat': 6, 'sun': 7
})

df['area'] = np.log(df.area + 1)

df.to_csv('forestfiresResultado.csv', sep=';', index=False)