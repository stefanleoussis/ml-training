import numpy as np

def load_data():
    data = np.loadtxt("data/01_city_pop_restaurant_profit_training.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("data/02_city_pop_restaurant_profit_training.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y
