#!/usr/bin/env python
# coding: utf-8

# # Import essentials

# In[ ]:


import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.backend import clear_session
import numpy


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


# # model_training

# In[ ]:


model = Sequential()
model.add(Dense(units = 20 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=200 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
model.compile( optimizer= "Adam" , loss='categorical_crossentropy', 
             metrics=['accuracy'] )
fit_model = model.fit(train_X ,  train_y , epochs = 2 , verbose =  False)


# # accuracy_checking

# In[ ]:


text = fit_model.history
accuracy = text['accuracy'][1] * 100
accuracy = int(accuracy)
f= open("accuracy.txt","w+")
f.write(str(accuracy))
f.close()
print("Accuracy for the model is : " , accuracy ,"%")

