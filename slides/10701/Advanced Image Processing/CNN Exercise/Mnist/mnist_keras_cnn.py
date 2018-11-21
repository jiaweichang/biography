#Step 1. Import
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPool2D, Flatten
from keras.utils import np_utils

#Step 2. Load Data
nb_classes = 10
(x_train, y_train), (x_test, y_test) = mnist.load_data()



print(type(x_train))
print("x_train shape", x_train.shape)
print("y_train shape", y_train.shape)

#Step 3. Show Data
# fig = plt.figure()
# plt.subplot(2,1,1)
# plt.imshow(x_train[0], cmap="binary", interpolation="none")
# plt.title("image" + str(y_train[0]))
# plt.subplot(2,1,2)
# plt.hist(x_train[0].reshape(784))
# plt.title("Pixel Values")
# plt.show()

#Step 4. Prepare Training
img_size_x, img_size_y = 28, 28
x_train = x_train.reshape(x_train.shape[0], img_size_x, img_size_y, 1)
x_test = x_test.reshape(x_test.shape[0], img_size_x, img_size_y, 1)
input_shape = (img_size_x, img_size_y, 1)
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

#Step 5. One hot encoding
y_train = np_utils.to_categorical(y_train,nb_classes)
y_test = np_utils.to_categorical(y_test,nb_classes)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


#Step 6. Create model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=input_shape))
model.add(Conv2D(64, kernel_size=(3,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
model.summary()

#Step 7. Compile
model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])

#Step 8. Training
history = model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=2, validation_data=(x_test, y_test))

#Step 9. Check Accuracy
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training & Validation Accuracy')
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['training','validation'],loc='lower right')
plt.show()