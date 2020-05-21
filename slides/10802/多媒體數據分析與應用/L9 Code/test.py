# 導入函式庫
from preprocess import *
# 模型讀檔
from tensorflow.keras.models import load_model
model = load_model('ASR.h5')  # load a HDF5 file 'model.h5'


# 預測(prediction)
mfcc = wav2mfcc('./data/cat/00b01445_nohash_0.wav')
mfcc_reshaped = mfcc.reshape(1, 20, 11, 1)
print("labels=", get_labels())
print("predict=", np.argmax(model.predict(mfcc_reshaped)))

