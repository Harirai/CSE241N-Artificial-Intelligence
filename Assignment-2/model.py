import numpy as np
import random
import matplotlib.pyplot as plt

class Model():

    def __init__(self, lr, feature_size, init = "random"):
        
        '''
            Arguments passed:
                1. lr           -> learning rate for the Linear Regression Model.
                2. feature_size -> number of features for the model(includes the bias term as well).
                3. init         -> defines how the weight initialisation is to be done. This can 
                                   be either 'random' or 'zeros'
        
        '''

        self.lr = lr
        
        if init == "random":
            self.W = np.random.random((feature_size, 1))

        elif init == "zeros":
            self.W = np.zeros((feature_size, 1))

        else:
            print("Weight Initialisation is not correct!")
            raise Exception


    def forward(self, features):

        '''
            Here, you have to implement the forward pass for Linear Regression. You should make 
            use of the weight matrix(W) initialised above and return the predictions for your model.
            
            Input: 
                1. features -> Depending upon the type of data(Linear, Polynomial or Linear Periodic), the shape of this 
                            feature vector will vary.
                            If n is the number of data points, then its shape is (n,feature_size)

            Return: 
                Make use of the weight matrix(W) and calculate your model's predictions. 
                Return a numpy array of shape (n,1), where n is same as the first dimension of 'features'. 
                
                STORE YOUR RESULT IN A NUMPY ARRAY NAMED 'answer'
                
                
        '''

        ## YOUR CODE STARTS HERE ##
        
        answer = np.dot(features, self.W)

        
        ## YOUR CODE ENDS HERE ##

        return answer

    def backward(self, y_pred, y_actual, features):

        '''

            Implement the backward pass of the Linear Regression Model to update the weight matrix(W) using the 
            Gradient Descent Algorithm. 
            
            Input:
                
                1. y_pred   -> predictions from your model estimated using the forward pass of your implementation above.
                               shape : (n,1)
                               
                2. y_actual -> actual values corresponding to the data points you estimated 'y_pred' for.
                               shape : (n,1)
                               
                3. features   -> features obtained for the given data points. 
                               shape : (n,feature_size)
                
            Return:
            
                You don't have to return anything here. You just have to update the weight matrix(W) using Gradient Descent.
            
            
        '''
        
        ## YOUR CODE STARTS HERE ##
        diff = np.subtract(y_pred, y_actual)
        # diff = np.square(diff)

        answer = np.dot(features.T, diff)
        answer = answer/y_pred.shape[0]
        answer = answer*self.lr
        self.W = np.subtract(self.W, answer)


        
        
        ## YOUR CODE ENDS HERE ##

    def loss(self, y_pred, y_actual):

        '''
            This function should estimate the loss corresponding to your model's predictions. Implement this function and
            return the scalar loss in a variable named 'loss'
            
            
            Input:
                
                1. y_pred   -> predictions from your model estimated using the forward pass of your implementation above.
                               shape : (n,1)
                               
                2. y_actual -> actual values corresponding to the data points you estimated 'y_pred' for.
                               shape : (n,1)
                               
            Return:
                
                Return the scalar loss calculated using the predicted values and actual values in a variable named 'loss'.
            
        '''
        
        
        ## YOUR CODE STARTS HERE ##
        
        
        loss = 0
        d = np.square(np.subtract(y_pred, y_actual))
        loss = np.sum(d, 0)
        loss = loss/(2*y_pred.shape[0])

        ## YOUR CODE ENDS HERE ##
        

        return loss


def get_features(data, data_type):

    '''
        data = (n,1) shape numpy array
        
        This function estimates and returns all the different types of feature vectors(Linear, Polynomial and Linear Periodic) 
        that we shall be using to fit our data points to. 
        
        You need to implement the empty code parts of this functions and calculate the features as instructed. Make use
        of appropriate numpy functions wherever required and return the final result as a numpy array too.
        
        Input:
            1. data      -> This argument corresponds to the data points for which we are supposed to calculate the features.
                            shape: (n,1)
                     
            2. data_type -> This is one of (Linear, Polynomial and Linear Periodic)
        
        Return:
        
            Return the required features in a variable named 'features' and follow the instructions below that'll 
            guide you through their formation.
            rerturn shape: (n,feature_size)
        
    '''


    if data_type == 'linear':

        '''
        
        Form a numpy array named 'features' of shape (n,2) with first column same as the 'data' and second column of 1s.
        eg: 
            if data = numpy.array([[1],
                                   [2]]), 
                                   
               then you should return the following numpy array:
                      
                      numpy.array([[1, 1],
                                   [2, 1]])             
                                   

        '''
        ## YOUR CODE STARTS HERE ##
        a = np.ones(data.shape[0])

        features = np.column_stack((data, a))
        
        
        ## YOUR CODE ENDS HERE ##
        assert features.shape==(data.shape[0],2)
        
        

    elif data_type == 'poly':
        
        '''
        
        Form a numpy array named 'features' of shape (n,4) with:
            1. first column as cube of data.
            2. second column as square of data.
            3. third column is same as the data itself.
            4. fourth column is a column of 1s.
            
        eg: 
            if data = numpy.array([[1],
                                   [2]]), 
                                   
               then you should return the following numpy array:
                      
                      numpy.array([[1, 1, 1, 1],
                                   [8, 4, 2, 1]])     
        


        '''
        ## YOUR CODE STARTS HERE ##
        
        o = np.ones(data.shape[0])

        s = np.square(data)

        features = np.column_stack((np.multiply(data, s), s, data, o))

        
        ## YOUR CODE ENDS HERE ##        
        assert features.shape==(data.shape[0],4)
        
        

    elif data_type == 'linear_periodic':

        '''
        
        Form a numpy array named 'features' of shape (n,4) with:
            1. first column same as the data itself.
            2. second column as the sine of data.
            3. third column as the cosine of data.
            4. fourth column is a column of 1s.
            
        eg: 
            if data = numpy.array([[1],
                                   [2]]), 
                                   
               then you should return the following numpy array:
                      
                      numpy.array([[1, sin(1), cos(1), 1],
                                   [2, sin(2), cos(2), 1]])
        
        
        '''
        
        ## YOUR CODE STARTS HERE ##
        o = np.ones(data.shape[0])
        si = np.sin(data)
        co = np.cos(data)
        features = np.column_stack((data, si, co, o))
        
        
        
        ## YOUR CODE ENDS HERE ##   
        assert features.shape==(data.shape[0],4)
        

    return features


