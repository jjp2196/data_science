import pandas as pd
import numpy as np
import matplotlib as plt

def read_data(filename):
    df = pd.read_csv(filename, sep = ",", index_col = False)

def normalize(data):
	for i in range(0,data.shape[1]-1):
		data[:,i] = ((data[:,i] - np.mean(data[:,i]))/np.std(data[:, i]))
		
def plot_data(x, y):
	plt.xlabel('X Values')
	plt.ylabel('Y Values')
	plt.plot(x[:,0], y, 'bo')
	plt.show()
	
def hypothesis_function(x,theta):
	return np.matmul(x, theta)

def cost_function(x, y, theta):
	return ((hypothesis_function(x, theta)-y).T@(hypothesis_function(x, theta)-y))/(2*y.shape[0])
