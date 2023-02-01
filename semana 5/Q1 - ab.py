import pandas as pd
import collections

df = pd.read_csv('./student-por.csv', sep=';')

#binario nominal

df['school'] = df['school'].map({'GP': 0, 'MS': 1 })
df['sex'] = df['sex'].map({'F': 0, 'M': 1 })
df['address'] = df['address'].map({'U': 0, 'R': 1 })
df['famsize'] = df['famsize'].map({'LE3': 0, 'GT3': 1 })
df['Pstatus'] = df['Pstatus'].map({'T': 0, 'A': 1 })
df['schoolsup'] = df['schoolsup'].map({'yes': 1, 'no': 0})
df['famsup'] = df['famsup'].map({'yes': 1, 'no': 0})
df['paid'] = df['paid'].map({'yes': 1, 'no': 0})
df['activities'] = df['activities'].map({'yes': 1, 'no': 0})
df['nursery'] = df['nursery'].map({'yes': 1, 'no': 0})
df['higher'] = df['higher'].map({'yes': 1, 'no': 0})
df['internet'] = df['internet'].map({'yes': 1, 'no': 0})
df['romantic'] = df['romantic'].map({'yes': 1, 'no': 0})

## não binário nominal - cria novos atrbutos e elimina o antigo
df['MjobTeacher'] = df['Mjob'].map(collections.defaultdict(lambda: 0, { 'teacher': 1}))
df['MjobHealth'] = df['Mjob'].map(collections.defaultdict(lambda: 0, { 'health': 1}))
df['MjobServices'] = df['Mjob'].map(collections.defaultdict(lambda: 0, { 'services': 1}))
df['MjobAtHome'] = df['Mjob'].map(collections.defaultdict(lambda: 0, { 'at_home': 1}))
df['MjobOther'] = df['Mjob'].map(collections.defaultdict(lambda: 0, { 'other': 1}))
del df['Mjob']

df['FjobTeacher'] = df['Fjob'].map(collections.defaultdict(lambda: 0, { 'teacher': 1}))
df['FjobHealth'] = df['Fjob'].map(collections.defaultdict(lambda: 0, { 'health': 1}))
df['FjobServices'] = df['Fjob'].map(collections.defaultdict(lambda: 0, { 'services': 1}))
df['FjobAtHome'] = df['Fjob'].map(collections.defaultdict(lambda: 0, { 'at_home': 1}))
df['FjobOther'] = df['Fjob'].map(collections.defaultdict(lambda: 0, { 'other': 1}))
del df['Fjob']

df['reasonClose'] = df['reason'].map(collections.defaultdict(lambda: 0, { 'home': 1}))
df['reasonSchool'] = df['reason'].map(collections.defaultdict(lambda: 0, { 'reputation': 1}))
df['reasonCourse'] = df['reason'].map(collections.defaultdict(lambda: 0, { 'course': 1}))
df['reasonOther'] = df['reason'].map(collections.defaultdict(lambda: 0, { 'other': 1}))
del df['reason']

df['guardianMother'] = df['guardian'].map(collections.defaultdict(lambda: 0, { 'mother': 1}))
df['guardianFather'] = df['guardian'].map(collections.defaultdict(lambda: 0, { 'father': 1}))
df['guardianOther'] = df['guardian'].map(collections.defaultdict(lambda: 0, { 'other': 1}))
del df['guardian']

df.to_csv('./resultado.csv', sep=';', index=False)
