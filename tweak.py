#!/usr/bin/env python
# coding: utf-8

# # import essentials library

# In[ ]:


import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.backend import clear_session
import numpy


# # Train model function

# In[ ]:




def train_model(neurons , model , epochs , test) : 
    print("\n" , " *** Summary *** " , "\n", "Iteration  : ", test , "\n" , "   Number of Neurons : ", neurons , "\n" , "   Number of Epochs : ",  epochs)
    model.add(Dense(units = neurons , input_dim = 28*28 , activation = 'relu'))
    model.add(Dense(units=200 , input_dim = 28*28 , activation = 'relu'))
    model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
    model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
    model.compile( optimizer= "Adam" , loss='categorical_crossentropy', 
                    metrics=['accuracy'] )
    return model


def validate(fit_model, epochs):
    text = fit_model.history
    accuracy = text['accuracy'][epochs-1] * 100
    accuracy = int(accuracy)
    f= open("accuracy.txt","w+")
    f.write(str(accuracy))
    f.close()
    print("    Accuracy for this Iteration is : " , accuracy ,"%")
    return accuracy


# # Load Model 

# In[ ]:


(train_X , train_y), (test_X , test_y) = mnist.load_data("mymnist.data")


# # Reshape data and change type

# In[ ]:



test_X = test_X.reshape(-1 , 28*28)
train_X = train_X.reshape(-1 ,  28*28)
test_X = test_X.astype("float32")
train_X = train_X.astype("float32")


# # One hot encoding

# In[ ]:



test_y = to_categorical(test_y)
train_y = to_categorical(train_y)


# # Initials

# In[ ]:


neurons = 10
accuracy = 0
epochs = 1
test = 1
flag = 0

while int(accuracy) < 96 :
    if flag == 1 :
        model = keras.backend.clear_session()
        neurons = neurons+10
        epochs = epochs+1 
        test = test + 1
    #model=reset_weights(model)
    model = Sequential()
    model = train_model(neurons , model , epochs , test)
    print("    calculating accuracy . . .")
    fit_model = model.fit(train_X ,  train_y , epochs = epochs , verbose =  False)
    accuracy=validate(fit_model , epochs)
    flag = 1


# In[ ]:


# import smtplib 
# # creates SMTP session 
# s = smtplib.SMTP('smtp.gmail.com', 587) 
# # start TLS for security 
# s.starttls()   
# # Authentication 
# s.login("abc@gmail.com", "*****") 
# # message to be sent 
# message = "Hey Developer, this is to inform you that your MNIST model finally  got the model trained with 99  accuracy "
# # sending the mail 
# s.sendmail("abc@gmail.com", "xyz@gmail.com", message) 
# # terminating the session 
# s.quit()


# In[ ]:





# In[ ]:




