import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def prep_data(dataset):

    dataset = dataset.assign(Girth=dataset["Length1"] * dataset["Width"])
    dataset = dataset[["Species", "Length1", "Length2", "Length3", "Height", "Width", "Girth", "Weight" ]]

    X = dataset[["Species", "Length2", "Height", "Width", "Girth"]].values
    y = dataset["Weight"].values
    
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))

    return X, y

