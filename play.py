#Import the required libraries
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import random

#Dictionary of fruits
fruits = {0:"apple", 1:"banana", 2:"orange"}
choices = list(fruits.keys())
start = False

#Mapper
def mapper(val):
    return fruits[val]

#Load the model
model = load_model('mobilenet_model.h5')

#Captuing the video from the default webcam of your laptop. You can change the value from 0 to depending on your external camera.
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Collecting continuous frames of images which is a video
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    if start:

        #Draw a rectangle where you have to place the fruit/item you want to classify
        cv2.rectangle(frame, (200, 200), (450, 450), (0, 255, 255), 2)
        
        #region of image you want to crop for processing and classification
        roi = frame[200:450, 200:450]

        #Convert the image from BGR to RGB
        img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

        #Resizing the image to mobilenet input layer 0 shape
        img = cv2.resize(img, (224,224))
        
        #Calling predict function in the mobilenet model
        pred = model.predict(np.array([img]))

        #the argmanx value of the predictions array will be the result of the image shown
        result = np.argmax(pred[0])

        #The mapper gives the name of the fruit
        fruit_name = mapper(result)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.putText(frame, "Show me a/an " + fruits[num], (100, 50), font, 0.7, (255, 0, 0), 4, cv2.LINE_AA)
        
        #Game code
        if (num == result):
            cv2.putText(frame, "Great!!! that's a/an " + fruits[num], (100, 90), font, 0.7, (0, 255, 0), 4, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Sorry that's not a/an " + fruits[num], (100, 90), font, 0.7, (0, 0, 255), 4, cv2.LINE_AA)
    
    #Display the frame                          
    cv2.imshow("Play", frame)
    
    #Press the keys
    k = cv2.waitKey(10)

    #Press 's' to start the game
    if k == ord('s'):
        start = not start
        num = random.choice(choices)
    #Press 'r' to refresh the screen for a new item        
    if k == ord('r'):
        num = random.choice(choices)

    #Press 'q' to quit the game    
    if k == ord('q'):
        break
        
#Release the camera        
cap.release()

#Destroy all the windows at the end
cv2.destroyAllWindows()        
    