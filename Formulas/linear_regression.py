import pandas as pd
import numpy as np
import matplotlib as plt

# Part 1: Function Definition

# Opens the file
def read_data(filename):
    df = pd.read_csv(filename, sep = ",", index_col = False)

# Forces values within a range of -1 and 1, equalizes dataset
def normalize(data):
	for i in range(0,data.shape[1]-1):
		data[:,i] = ((data[:,i] - np.mean(data[:,i]))/np.std(data[:, i]))
		
# Plots the Data
def plot_data(x, y):
	plt.xlabel('X Values')
	plt.ylabel('Y Values')
	plt.plot(x[:,0], y, 'bo')
	plt.show()
	
# Matrix Multiplication Function, Multiplies X Values by Theta
def hypothesis_function(x,theta):
	return np.matmul(x, theta)

# Cost Function, 
def cost_function(x, y, theta):
	return ((hypothesis_function(x, theta)-y).T@(hypothesis_function(x, theta)-y))/(2*y.shape[0])

# Gradient Descent function minimizes the cost from one point to next
def gradient_descent(x, y, theta, learning_rate=0.1, num_epochs=10):
	m = x.shape[0]
	j_err_list = []
	
	for _ in range(num_epochs):
		hyp_func_x = hypothesis_function(x, theta)
		cost = (1/m)*(x.T@(hyp_func_x - y))
		theta = theta - (learning_rate)*cost
		j_err_list.append(cost_function(x, y, theta))

	return theta, j_err_list 

# Further Resources:
# https://medium.com/analytics-vidhya/basics-and-beyond-linear-regression-c12d99a4df35
# https://towardsdatascience.com/coding-linear-regression-from-scratch-c42ec079902 

# Part 2: Function Implementation

x,y = read_data("winequality-red.csv")
y = np.reshape(y, (46,1))
x = np.hstack((np.ones((x.shape[0],1)), x))
theta = np.zeros((x.shape[1], 1))
learning_rate = 0.1
num_epochs = 50
theta, J_all = gradient_descent(x, y, theta, learning_rate, num_epochs)
J = cost_function(x, y, theta)
print("Cost: ", J)
print("Parameters: ", theta)

#for testing and plotting cost 
n_epochs = []
jplot = []
count = 0
for i in J_all:
	jplot.append(i[0][0])
	n_epochs.append(count)
	count += 1
jplot = np.array(jplot)
n_epochs = np.array(n_epochs)
