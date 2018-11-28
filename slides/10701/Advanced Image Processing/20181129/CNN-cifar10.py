
# coding: utf-8

# In[1]:


'''
keras third example : cnn of cifar10
'''
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D,MaxPooling2D
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

###---###
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)
###---###
im = plt.imshow(x_train[0],cmap = 'gray')
plt.show()
im2 = plt.imshow(x_train[1],cmap = 'gray')
plt.show()
###---###
x_train = x_train/255
x_test = x_test/255
###---###
y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)
###---###
model = Sequential()
model.add(Conv2D(32,(3,3),padding = 'same',input_shape = (32,32,3),activation = 'relu'))
model.add(Conv2D(32,(3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(64,(3,3),padding = 'same',activation = 'relu'))
model.add(Conv2D(64,(3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512,activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(10,activation = 'softmax'))
model.summary()
###---###
opt = keras.optimizers.rmsprop(lr = 0.0001,decay = 1e-6)
model.compile(loss = 'categorical_crossentropy',
             optimizer = opt,
             metrics = ['accuracy'])
###---###
datagen = ImageDataGenerator(rotation_range = 20,
                            zoom_range = 0.15,
                            horizontal_flip = True)
###---###
model.fit_generator(datagen.flow(x_train,y_train,batch_size=64),
                                steps_per_epoch = 1000,
                                epochs = 2,
                                validation_data = (x_test,y_test),
                                workers = 4,
                                verbose = 1)
###---###
scores = model.evaluate(x_test,y_test,verbose = 1)
print('Test loss:',scores[0])
print('Test accuracy:',scores[1])
###---###
###---###

