# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:26:26 2024

@author: 700001473
"""

# https://docs.aws.amazon.com/rekognition/latest/dg/images-bytes.html

import boto3

def detect_labels_local_file(photo):


    client=boto3.client('rekognition', verify=False)
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print(response)
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    return(response)

photo='clemens.jpg'

# for many labels, a bounding box is also returned
# check res for these additional data
res = detect_labels_local_file(photo)
