import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def create_model(csv_fle):
    df = pd.read_csv(csv_fle)
    X = np.array(df.drop(df.columns[0], axis=1))
    Y = np.array(df.iloc[:,0])
    print(Y)

    x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size=0.3)

    print(x_train)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)

    print("score: ",model.score(x_test,y_test))

    return model