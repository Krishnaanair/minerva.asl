
import numpy as np    #import numpy to store images as arrays
import pandas as pd    #pandas library to display model summery
import seaborn as sns   #import seaborn for plot confusion_matrix (for testing purpuses)
import matplotlib.pyplot as plt    # for plot graphs
import cv2   #to read images
import skimage  #resize image size

# import tensorflow and keras to train and build model
import tensorflow as tf   

# import os library 
import os  



# importing some keras funtions and classes  
from keras.callbacks import EarlyStopping   
from sklearn.model_selection import train_test_split  
from keras.utils import to_categorical

import gc
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dense, Flatten


from sklearn.metrics import classification_report, confusion_matrix #to get reports(for testing)


print("Packages imported...")

"""### 2. Importing the dataset from training directory <a id=2></a>"""

batch_size = 64
imageSize = 64
target_dims = (imageSize, imageSize, 3)
num_classes = 29

train_len = 87000
train_dir = './data/mainData/asl_alphabet_train/asl_alphabet_train/'  #directory of training data set 

#loading all training data(87000 images) to RAM and store to X,Y variables
def get_data(folder):    
    X = np.empty((train_len, imageSize, imageSize, 3), dtype=np.float32)
    y = np.empty((train_len,), dtype=int)
    cnt = 0
    for folderName in os.listdir(folder):
        if not folderName.startswith('.'):
            if folderName in ['A']:
                label = 0
            elif folderName in ['B']:
                label = 1
            elif folderName in ['C']:
                label = 2
            elif folderName in ['D']:
                label = 3
            elif folderName in ['E']:
                label = 4
            elif folderName in ['F']:
                label = 5
            elif folderName in ['G']:
                label = 6
            elif folderName in ['H']:
                label = 7
            elif folderName in ['I']:
                label = 8
            elif folderName in ['J']:
                label = 9
            elif folderName in ['K']:
                label = 10
            elif folderName in ['L']:
                label = 11
            elif folderName in ['M']:
                label = 12
            elif folderName in ['N']:
                label = 13
            elif folderName in ['O']:
                label = 14
            elif folderName in ['P']:
                label = 15
            elif folderName in ['Q']:
                label = 16
            elif folderName in ['R']:
                label = 17
            elif folderName in ['S']:
                label = 18
            elif folderName in ['T']:
                label = 19
            elif folderName in ['U']:
                label = 20
            elif folderName in ['V']:
                label = 21
            elif folderName in ['W']:
                label = 22
            elif folderName in ['X']:
                label = 23
            elif folderName in ['Y']:
                label = 24
            elif folderName in ['Z']:
                label = 25
            elif folderName in ['del']:
                label = 26
            elif folderName in ['nothing']:
                label = 27
            elif folderName in ['space']:
                label = 28           
            else:
                label = 29
            print("ok")
            for image_filename in os.listdir(folder + folderName):
                img_file = cv2.imread(folder + folderName + '/' + image_filename)
                if img_file is not None:
                    img_file = skimage.transform.resize(img_file, (imageSize, imageSize, 3))
                    img_arr = np.asarray(img_file).reshape((-1, imageSize, imageSize, 3))
                    
                    X[cnt] = img_arr
                    y[cnt] = label
                    cnt += 1
    return X,y

# calling above function to get all images to X_train, y_train
X_train, y_train = get_data(train_dir)
print("Images successfully imported...")


print("The shape of X_train is : ", X_train.shape)
print("The shape of y_train is : ", y_train.shape)

#  Checking the shape of one image
print("The shape of one image is : ", X_train[0].shape)

# Viewing the image"
plt.imshow(X_train[0])
plt.show()


#  Making copies of original data(87000 images)
X_data = X_train
y_data = y_train
print("Copies made...")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.3,random_state=42,stratify=y_data)



# One-Hot-Encoding the categorical data
y_cat_train = to_categorical(y_train,29)
y_cat_test = to_categorical(y_test,29)



# Checking the dimensions of all the variables(for testing)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
print(y_cat_train.shape)
print(y_cat_test.shape)



# This is done to save CPU and RAM space while working on Kaggle Kernels. This will delete the specified data and save some space!
del X_data
del y_data
gc.collect()





# Building model 
model = Sequential()

model.add(Conv2D(32, (5, 5), input_shape=(64, 64, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))

model.add(Dense(29, activation='softmax'))

# get the summery of model
model.summary()



# Early Stopping and Compiling
# Early Stopping is done to make sure the model fitting stops at the most optimized accuracy point. After the early stopping point, the model might start overfitting. For testing purposes, this step can be skipped and complete training can be done.
early_stop = EarlyStopping(monitor='val_loss',patience=2)


# Compiling
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# Model fitting 
model.fit(X_train, y_cat_train,
          epochs=50,
          batch_size=64,
          verbose=2,
          validation_data=(X_test, y_cat_test),
         callbacks=[early_stop])


#  Metrics from model history
metrics = pd.DataFrame(model.history.history)
print("The model metrics are")
metrics

# Plotting the training loss
metrics[['loss','val_loss']].plot()
plt.show()


# lotting the testing loss
metrics[['accuracy','val_accuracy']].plot()
plt.show()


# Model evaluation
model.evaluate(X_test,y_cat_test,verbose=0)


# Predictions(testing predictions)
predictions =np.argmax(model.predict(X_test),axis=1)
print("Predictions done...")

# Classification report
print(classification_report(y_test,predictions))


# Confusion matrix heatmap
plt.figure(figsize=(12,12))
sns.heatmap(confusion_matrix(y_test,predictions))
plt.show()



# Saving the model 
model.save('ASL.h5')
print("Model saved successfully...")

