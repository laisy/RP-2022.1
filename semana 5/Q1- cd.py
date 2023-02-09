import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import  KNeighborsRegressor

df = pd.read_csv(r'c:\Users\David\Desktop\RP-2022.1\semana 5\student-mat.csv', sep=';')


df['G3'] = df['G3'].map({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 
                        6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 1,
                        12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1,
                        18: 1, 19: 1, 20: 1})



df.to_csv(r'c:\Users\David\Desktop\RP-2022.1\semana 5\student-matResultado2.csv', sep=';', index=False)