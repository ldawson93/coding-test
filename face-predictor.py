#Question 2 - Lauretta.io coding test

'''
This program is for a hackattic face detection problem
Input: A URL string 
Output: A list of two-element list as follows
[[2, 1], [7, 3], [5, 4], [3, 1], [1, 7], [1, 0], [2, 3], [3, 2], [5, 5], [6, 4], [4, 5], [6, 0], [7, 4], [5, 7], [0, 7], [5, 6], [2, 6], [1, 6]]


Reference:
https://medium.com/analytics-vidhya/how-to-build-a-face-detection-model-in-python-8dc9cecadfe9

'''

import cv2
import numpy as np
import glob
import json
import requests

text_files = [] 
face_tiles= []

for file in glob.glob("C:\\Users\Desktop\dawson files\*.png"): # could not get the image using the access code
    text_files.append(file)
    
for ix in text_files:
    img = cv2.imread(ix,cv2.IMREAD_COLOR)
    imgtest = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #turn to greyscale
    face_cascade = cv2.CascadeClassifier('C:\\Users\Desktop\dawson files\haar.xml')
   
    faces = face_cascade.detectMultiScale(imgtest, scaleFactor=1, minNeighbors=5)   
    #scale factor compensates for faces nearer to the camera but the input is of pictures so set to 1
    
    for (x, y, w, h) in faces:
        #print(x,y)
        face_tiles.append([int(round(x/100)), int(round(y/100))]) #to scale to 8x8 frame

#print(face_tiles)
post_url= "http://hackattic.com/challenges/basic_face_detection/solve?access_token=b2ab91f1c3b79fac"
json_string = json.dumps(face_tiles)
r= requests.post(post_url, data=json_string) # could not get it to work as well

r.text
r.status_code
