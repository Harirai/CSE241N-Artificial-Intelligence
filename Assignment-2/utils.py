import numpy as np
import random
import matplotlib.pyplot as plt
import json
def get_x_data(left, right, size):

    partitions = 10*size
    temp = list(np.arange(left, right, 1/partitions))
    temp = random.sample(temp, min(size, len(temp)) )

    return temp


def generate_data(data_type, train_range_left, train_range_right, train_size,
                        val_range_left, val_range_right, val_size, 
                        test_range_left, test_range_right, test_size):

    x_train = get_x_data(train_range_left, train_range_right, train_size)
    x_val = get_x_data(val_range_left, val_range_right, val_size)
    x_test = get_x_data(test_range_left, test_range_right, test_size)


    if data_type == 'linear':

        y_train = linear(x_train)
        y_val = linear(x_val)
        y_test = linear(x_test)

    elif data_type == 'poly':

        y_train = poly(x_train)
        y_val = poly(x_val)
        y_test = poly(x_test)

    elif data_type == 'linear_periodic':

        y_train = linear_periodic(x_train)
        y_val = linear_periodic(x_val)
        y_test = linear_periodic(x_test)

    # elif data_type == 'logarithmic':

    # 	y_train = logarithmic(x_train)	
    # 	y_val = logarithmic(x_val)
    # 	y_test = logarithmic(x_test)

    return x_train, y_train, x_val, y_val, x_test, y_test


def linear(data, slope=3, intercept=0.5):

    y = [slope*i + intercept + 2*np.random.random() for i in data]

    return y

def poly(data, x3_coeff = 1, x2_coeff = -4, x_coeff = 3, const = 3):

    y = []

    for i in data:

        exp = x3_coeff*(i**3) + x2_coeff*(i**2) + x_coeff*(i) + const + 2*np.random.random()

        y.append(exp)

    return y

def linear_periodic(data, x_coeff = 1, sin_coeff = 2, cos_coeff = 3):

    y = []

    for i in data:

        exp = x_coeff*(i) + sin_coeff*np.sin(i) + cos_coeff*np.cos(i) + 2*np.random.random()

        y.append(exp)

    return y

def save_hyper(prob_name, feat_type, param, epochs, lr, weight_init):
    '''
    Saves the parameters tuned for different sub-problems of the assignment into a file.
    This file is later used for evaluation purposes.
    '''
    
    prob_dict = dict()
    prob_dict['feat_type'] = feat_type
    prob_dict['param'] = param
    prob_dict['epochs'] = epochs
    prob_dict['lr'] = lr
    prob_dict['weight_init'] = weight_init

    filename = 'hyper_param.json'
    
    try:
        with open(filename, 'r') as fp:
            dict_hyper = json.load(fp)
    except:
        dict_hyper = dict()

    dict_hyper[prob_name] = prob_dict
    with open(filename, 'w') as fp:
        json.dump(dict_hyper, fp)

def plot(TRAIN_LOSS, VAL_LOSS,
               x_train, y_train, x_val, y_val,
               x_test, y_test, x_pred, y_pred):
    
    plt.figure(figsize=(15,10))
    ax1 = plt.subplot(1,2,1)
    plt.plot(TRAIN_LOSS,label='training curve')
    plt.plot(VAL_LOSS, label='validation curve')
    ax1.set_title('Learning Curves')
    plt.xlabel('epochs')
    plt.ylabel('Error')
    ax1.legend()

    plt.figure(figsize=(15,10))
    plt.scatter(x_pred, y_pred, color='r', s = 5, label='model fit')
    plt.scatter(x_val, y_val, s=10, label='validation data') 
    plt.scatter(x_test, y_test, s=10, label='test data') 
    plt.scatter(x_train, y_train, s=10, label='training data') 
    plt.title('Visualization of the Model Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
