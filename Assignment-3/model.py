import numpy as np

def sigmoid(z):
    """
    Sigmoid function implemented in numpy

    Arguments:
        1. z  ->	A numpy array of size n.

    Return:
        A numpy array where each element is now the sigmoid of its original value
    """

    output = None

    '''WRITE YOUR CODE HERE (one line of vectorised code)'''
    output = 1/(1+   np.exp(-z))

    '''END YOUR CODE HERE'''

    return output


class LogisticRegression(object):

    def __init__(self):
        """
        Initialise the logistic regression model. The weights are initialised as 'None',
        as the initially training samples are not given. Once we get those, the input size
        of the model will be determined.
        """

        # Model paramter
        self.weights = None

    def loss(self, X_data, Y_data):
        """
        Function to compute the loss function for Logistic Regression

        Calculate the loss function and gradients of loss with respect to weights
        for the data

        Arguments:
            1. X_data  ->	The input, which is a numpy array of size NxF where N is the 
                            the number of samples and F is the number of features.
            2. Y_data  ->	The correct labels for the data, a numpy array of size N

        Return:
            A tuple (loss, gradient)
        """

        loss, grad = None, None

        '''START YOUR CODE HERE'''
        Y_predict = sigmoid(np.matmul(X_data, self.weights))
        # Make a prediction using the sigmoid function and the weights
        loss = (1/np.shape(Y_data)[0])
        k = np.add(np.multiply(-1*Y_data.reshape(len(Y_predict),1),np.log(Y_predict)),np.multiply(Y_data.reshape(len(Y_predict),1) - 1,np.log(1 - Y_predict)))
        loss = loss * np.sum(k ,axis=0)

        grad = (1/np.shape(Y_data)[0])*np.matmul(np.transpose(X_data),np.subtract(Y_predict,Y_data.reshape(len(Y_predict),1))) 

        # Calculate the loss and gradients


        '''END YOUR CODE HERE'''


        return loss, grad


    def assign_predictions(self, X_data):
        """
        Make the final predictions for the examples in X_data

        Arguments:
            1. X_data  ->	The input to make predictions for. It is a numpy array of size NxF 
                            where N is the the number of samples and F is the number of features.

        Return:
            A vector of size N which contains 0 or 1 indicating the class label.
        """

        predict_func = np.vectorize(lambda x: 0 if x < 0 else 1)
        score = np.dot(X_data, self.weights)

        predictions = predict_func(score)

        return predictions

    def accuracy(self, X_test, Y_test):
        """
        Score the performance of the model with the given test labels

        Arguments:
            1. X_test  ->	Test input numpy array of size NxF.
            2. Y_test  ->	Test correct labels numpy array of size N.

        Return:
            The accuracy of the model. A single float value between 0 and 1.
        """

        Y_pred = self.assign_predictions(X_test)
        accuracy = 1 - np.float(np.count_nonzero(Y_pred - Y_test)) / X_test.shape[0]

        return accuracy

    def train(self, X_train, Y_train, lr=1e-4, num_iters=1000, num_print=50):
        """
        Learn the parameters from the given data and given hyperparamters,
        using batch gradient descent

        Arguments:
            1. X_train    ->	The input to learn from. It is a numpy array of size NxF 
                                where N is the the number of samples and F is the number of features.
            2. Y_train    ->	Correct labels for X_train. Vector of size N.
            3. lr  		  ->  	Learning rate for gradient descent
            4. num_iters  -> 	Number of iterations over training set
            5. print_freq ->	Frequency after which loss is printed
        """

        '''START YOUR CODE HERE'''
        # Initialise the weights in the variable self.weights
        self.weights = np.random.randn(np.shape(X_train)[1],1)


        # Perform iterations, use the loss function above to get the loss and gradient at each 
        # epoch and update wights using the learning rate
        for i in range(num_iters):
            loss, grad = self.loss(X_train, Y_train)
            rc = 0.001
            # Add regularisation to the loss (optional)
            loss = loss + (rc/(2*np.shape(X_train)[1]))*np.sum(np.power(self.weights,2),axis=0)
            grad = grad + (rc/np.shape(X_train)[1])*self.weights
            # Update weights
            self.weights = self.weights - lr*grad
            if i % (num_iters // num_print) == 0:
                print("Iteration %d of %d. Loss: %f LR: %f" % (i, num_iters, loss, lr))
        ''' END YOUR CODE HERE '''