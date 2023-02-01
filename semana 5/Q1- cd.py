import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import  KNeighborsRegressor

df = pd.read_csv('./student-matResultado.csv', sep=';')
acc1 = []
acc2 = []
target = df.pop("G3")

def std(accuracies, mean):
    total = 0
    for k in accuracies:
        total += (k - mean) ** 2

    result = (total / len(accuracies)) ** 0.5

    return result

for i in range(100):
    X_train, X_test, Y_train, Y_test = train_test_split(df, target, test_size=0.5)

    knn1 = KNeighborsRegressor(n_neighbors=1, weights="uniform", metric="euclidean")
    knn1.fit(X_train, Y_train)
    acc1.append(knn1.score(X_test,Y_test))

    del X_train['school']
    del X_train['sex']
    del X_train['address']
    del X_train['famsize']
    del X_train['Pstatus']
    del X_train['Medu']
    del X_train['Fedu']
    
    del X_train['MjobTeacher']
    del X_train['MjobServices']
    del X_train['MjobOther']

    del X_train['FjobTeacher']
    del X_train['FjobHealth']
    del X_train['FjobServices']
    del X_train['FjobAtHome']
    del X_train['FjobOther']

    del X_train['reasonClose']
    del X_train['reasonSchool']
    del X_train['reasonCourse']
    del X_train['reasonOther']

    del X_train['guardianMother']
    del X_train['guardianFather']
    del X_train['guardianOther']

    del X_train['schoolsup']
    del X_train['famsup']
    del X_train['paid']
    del X_train['activities']
    del X_train['nursery']
    del X_train['higher']
    del X_train['internet']
    del X_train['romantic']

    del X_test['school']
    del X_test['sex']
    del X_test['address']
    del X_test['famsize']
    del X_test['Pstatus']
    del X_test['Medu']
    del X_test['Fedu']
    
    del X_test['MjobTeacher']
    del X_test['MjobServices']
    del X_test['MjobOther']

    del X_test['FjobTeacher']
    del X_test['FjobHealth']
    del X_test['FjobServices']
    del X_test['FjobAtHome']
    del X_test['FjobOther']

    del X_test['reasonClose']
    del X_test['reasonSchool']
    del X_test['reasonCourse']
    del X_test['reasonOther']

    del X_test['guardianMother']
    del X_test['guardianFather']
    del X_test['guardianOther']

    del X_test['schoolsup']
    del X_test['famsup']
    del X_test['paid']
    del X_test['activities']
    del X_test['nursery']
    del X_test['higher']
    del X_test['internet']
    del X_test['romantic']

    knn2 = KNeighborsRegressor(n_neighbors=1, weights="uniform", metric="euclidean")
    knn2.fit(X_train, Y_train)
    acc2.append(knn2.score(X_test, Y_test))

media = sum(acc1)/len(acc1)
desvio = std(acc1,media)
intervalo1 = [(media-(1.96*desvio)),(media+(1.96*desvio))]
print(f"Media: {media}")
print(f"Intervalo: {intervalo1}"+'\n')

media = sum(acc2)/len(acc2)
desvio = std(acc2,media)
intervalo1 = [(media-(1.96*desvio)),(media+(1.96*desvio))]
print(f"Media: {media}")
print(f"Intervalo: {intervalo1}"+'\n')
