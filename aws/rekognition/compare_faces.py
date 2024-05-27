# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:08:40 2024

@author: 700001473
"""

# https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html
# function compare_faces
# search whether the face in source_file is contained in the people shown in target_file
# the function uses AWS to search for the face
# it returns a confidence value & a bounding box where the image has been found in target_file
# show_image shows the image and the bounding box





import boto3
from PIL import Image, ImageDraw



def show_image(filename, box):

    image = Image.open(filename)
    
    imgWidth, imgHeight = image.size
    left = imgWidth * box['Left']
    top = imgHeight * box['Top']
    width = imgWidth * box['Width']
    height = imgHeight * box['Height']

    print('Left: ' + '{0:.0f}'.format(left))
    print('Top: ' + '{0:.0f}'.format(top))
    print('Face Width: ' + "{0:.0f}".format(width))
    print('Face Height: ' + "{0:.0f}".format(height))

    points = (
        (left, top),
        (left + width, top),
        (left + width, top + height),
        (left, top + height),
        (left, top)

    )
    draw = ImageDraw.Draw(image)
    draw.line(points, fill='#00d400', width=2)
    image.show()



def compare_faces(sourceFile, targetFile):

    client = boto3.client('rekognition', verify=False)

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    if(response['FaceMatches'] == []):
        print("face not found")
        return(response)

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')
        

        show_image(target_file, position)
        

    imageSource.close()
    imageTarget.close()
    return response


# source_file = 'nehammer_1.jpg'
source_file = 'clemens.jpg'
target_file = 'group_1.jpg'
res = compare_faces(source_file, target_file)
