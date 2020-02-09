import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

def load_data(filename):

	data = pd.read_csv(filename)
	X = data.iloc[:, :-1]

	y = data.iloc[:, -1]

	admitted = data.loc[y == 1]

	not_admitted = data.loc[y == 0]

	X = np.c_[np.ones((X.shape[0], 1)), X]

	y = y[:, np.newaxis]

	return X,y,admitted,not_admitted

def visualize_data(admitted,not_admitted):
	plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
	plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10,
		    label='Not Admitted')
	plt.xlabel('Marks in 1st Exam')
	plt.ylabel('Marks in 2nd Exam')
	plt.legend()
	plt.show()

def visualize_decision_boundary(admitted,not_admitted,X,parameters):
	x_values = [np.min(X[:, 1] - 2), np.max(X[:, 2] + 2)]
	y_values = - (parameters[0] + np.dot(parameters[1], x_values)) / parameters[2]
	plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
	plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10,
		    label='Not Admitted')
	plt.plot(x_values, y_values, label='Decision Boundary')
	plt.xlabel('Marks in 1st Exam')
	plt.ylabel('Marks in 2nd Exam')
	plt.legend()
	plt.show()

def save_hyperparameters(epochs, lr):
    '''
    Saves the parameters tuned for different sub-problems of the assignment into a file.
    This file is later used for evaluation purposes.
    '''
    
    prob_dict = dict()
    prob_dict['epochs'] = epochs
    prob_dict['lr'] = lr
    filename = 'hyper_param.json'
    
    try:
        with open(filename, 'r') as fp:
            dict_hyper = json.load(fp)
    except:
        dict_hyper = dict()

    dict_hyper['logistic'] = prob_dict
    with open(filename, 'w') as fp:
        json.dump(dict_hyper, fp)
