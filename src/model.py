import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split


def split_data(df, target_column, test_split_size):
    X = df.drop([target_column], axis = 1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= test_split_size, random_state = 60)
    y_train = y_train.values.reshape(-1, 1)
    y_test = y_test.values.reshape(-1, 1)
    return X_train, X_test, y_train, y_test

def scale_data(df):
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    df = pd.DataFrame(df)
    return df
    

def clustering(df, number_of_clusters):
    kmeans = KMeans(n_clusters = number_of_clusters, random_state = 33)
    df = kmeans.fit_predict(df)
    return df