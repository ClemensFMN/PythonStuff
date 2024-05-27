# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:16:16 2024

@author: 700001473
"""

import boto3
import json

def detect_faces(filename):
    
    client = boto3.client('rekognition', verify = False)

    imageSource = open(filename, 'rb')

    response = client.detect_faces(Image={'Bytes': imageSource.read()},
                                   Attributes=['ALL'])

    print('Detected faces for ' + filename)
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))

        # Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Face Occluded: " + str(faceDetail['FaceOccluded']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))

    return response
    

# res = detect_faces('clemens.jpg')
res = detect_faces('nehammer_1.jpg')
 