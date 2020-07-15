#Import the required libraries
import numpy as np
import matplotlib.pyplot as plt
import itertools

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.layers import BatchNormalization

#Path to train, test and valid datasets
train_path = 'datasets/train'
valid_path = 'datasets/valid'
test_path = 'datasets/test'

#Loading the images into batches into respective directories
train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224,224), classes=['apples', 'bananas', 'oranges'], batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224,224), classes=['apples', 'bananas', 'oranges'], batch_size=5)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224,224), classes=['apples', 'bananas', 'oranges'], batch_size=2, shuffle=False)

#Get the pretrained Mobilenet model. It is a light-weight model trained on Imagenet
mobile_model = tf.keras.applications.mobilenet.MobileNet()


#Fine-tuning the MobileNet model
model = Sequential()

for layer in mobile_model.layers[:-1]:
    model.add(layer)
    
for layer in model.layers:
    layer.trainable = False

#Add a dense layer at the last with number of nodes equal to number of classes you want to classify    
model.add(Dense(3, activation='softmax')) 

#Compiling the model
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

#Training the model
model.fit(train_batches, steps_per_epoch=4, validation_data=valid_batches, validation_steps=4, epochs=10, verbose=2)

#Saving the model
keras_file = "mobilenet_model.h5"
tf.keras.models.save_model(model, keras_file)