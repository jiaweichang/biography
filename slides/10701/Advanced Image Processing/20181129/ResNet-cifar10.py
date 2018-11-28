
# coding: utf-8

# In[ ]:


import keras
from keras.models import Model
from keras.utils import to_categorical                      #使label做one-hot encoding
from keras.datasets import cifar10                          #本次實例使用dataset
from keras.layers import Dense,Conv2D,Activation            #Dense建構一般層、Conv2D建構CNN層
from keras.layers import BatchNormalization                 #可加速收斂、控制overfitting，所以不用Dropout
from keras.layers import AveragePooling2D,Input,Flatten     #Flatten將多維輸入壓成一維，用於CNN層過渡到fully connected
from keras.regularizers import l2                           #使用l2正規化減少overfitting
from keras.callbacks import ModelCheckpoint                 #調用fit中callback參數，ModelCheckpoint每一個epoch存一次模型
from keras.callbacks import LearningRateScheduler           #動態調整學習率
from keras.callbacks import ReduceLROnPlateau               #訓練停滯時降低學習率
import matplotlib.pyplot as plt                             #可視化套件

###---load dataset---###
(x_train,y_train),(x_test,y_test) = cifar10.load_data()

###---normalization---###
x_train = x_train/255
x_test = x_test/255                                                    

###---one-hot encoding---###
y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)

###---define resnet_block---###
#使用keras中functional方式建立神經網路層 : ly=NN(參數)(input)#
def resnet_block(inputs,filters=16,kernel_size=(3,3),strides=1,activation='relu'):
    x = Conv2D(filters,kernel_size=kernel_size,strides=strides,
              padding='same',kernel_initializer='he_normal',
              kernel_regularizer=l2(1e-4))(inputs)
    x = BatchNormalization()(x)
    if(activation):
        x = Activation(activation)(x)
    return x


###---adding layers---###
def resnet20(input_shape):
    inputs = Input(shape = input_shape)
    
    x = resnet_block(inputs)                        #輸入層
    
    for ly in range(6):                             #六層filter=16的shortcut connection
        w1 = resnet_block(inputs=x)
        w2 = resnet_block(inputs=w1,activation=None)
        x = keras.layers.add([x,w2])                #ResNet精隨!!!! 加上identity mapping
        x = Activation('relu')(x)
        
    for ly2 in range(6):                                                 #六層filter=32的shortcut connection
        if ly2 == 0:
            w1 = resnet_block(inputs=x,filters=32,strides=2)         #為使前一層的輸出shape與本層的輸入shape一致，strides=2
        else:
            w1 = resnet_block(inputs=x,filters=32)
        w2 = resnet_block(inputs=w1,activation=None,filters=32)
        
        if ly2 == 0:
            x = Conv2D(32,kernel_size=3,strides=2,padding='same',        #對第一層filter=32的x多做一次CNN使輸出shape與w2一致
                       kernel_initializer='he_normal',
                       kernel_regularizer=l2(1e-4))(x)
        x = keras.layers.add([x,w2])                                     #ResNet精隨!!!! 加上identity mapping
        x = Activation('relu')(x)
        
    for ly3 in range(6):                                                 #六層filter=64的shortcut connection
        if ly3 == 0:
            w1 = resnet_block(inputs=x,filters=64,strides=2)
        else:
            w1 = resnet_block(inputs=x,filters=64)
        w2 = resnet_block(inputs=w1,activation=None,filters=64)
        
        if ly3 == 0:
            x = Conv2D(64,kernel_size=3,strides=2,padding='same',        #對第一層filter=64的x多做一次CNN使輸出shape與w2一致
                       kernel_initializer='he_normal',
                       kernel_regularizer=l2(1e-4))(x)
        x = keras.layers.add([x,w2])                                     #ResNet精隨!!!! 加上identity mapping
        x = Activation('relu')(x)
        
    x = AveragePooling2D(pool_size=2)(x)                                 
    y = Flatten()(x)
    outputs = Dense(10,activation='softmax',kernel_initializer='he_normal')(y)  #輸出層
    
    model = Model(inputs=inputs,outputs=outputs)                         
    return model

###---調整模型參數###
model = resnet20((32,32,3))                     #cifar10的shape(32,32,3)
model.compile(loss='categorical_crossentropy',
             optimizer=keras.optimizers.Adam(),
             metrics=['accuracy'])
model.summary()

###---Callback---###
checkpoint = ModelCheckpoint(filepath='./cifar10_resnet.h5',
                           monitor = 'val_acc',verbose=1,
                           save_best_only=True)

def lr_sch(epoch):
    if epoch<50:
        return 1e-3
    if 50<=epoch<100:
        return 1e-4
    if epoch>=100:
        return 1e-5
    
lr_scheduler = LearningRateScheduler(lr_sch)
lr_reducer = ReduceLROnPlateau(monitor='val_acc',factor=0.2,patience=5,
                              mode='max',min_lr=1e-3)
callbacks = [checkpoint,lr_scheduler,lr_reducer]




###---餵資料---###
model.fit(x_train,y_train,batch_size=64,epochs=200,validation_data=(x_test,y_test),verbose=1,callbacks=callbacks)


###---印出結果---###
scores = model.evaluate(x_test,y_test,verbose=1)
print('Test loss:',scores[0])
print('Test accuracy:',scores[1])

###---------------###

