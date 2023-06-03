import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import warnings

warnings.filterwarnings("ignore")
dataframe = pd.read_excel("./lab_iad_vars.xls", sheet_name="кластеризація")
dataframe.drop(columns=dataframe.columns[:2], axis=1, inplace=True)
inertias = []

def kmeans_clustering(data):
    inertias = []

    for i in range(1, data.shape[0]):
        kmeans = KMeans(n_clusters=i)
        model = kmeans.fit(data)
        inertias.append(model.inertia_)

    plt.plot(range(1, data.shape[0]), inertias, marker='o')
    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()
def prepare_data(data):
    prepared_data = [data.iloc[:, 0].to_numpy()[1:]]
    for i in range(1, data.shape[1]):
        prepared_data = np.append(prepared_data, [data.iloc[:, i].to_numpy()[1:]], axis=0)

    return prepared_data

data = prepare_data(dataframe)
kmeans_clustering(data)