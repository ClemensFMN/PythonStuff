# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:10:21 2024

@author: 700001473
"""

import boto3
import json
import hashlib


# https://www.geeksforgeeks.org/compare-two-files-using-hashing-in-python/
def hashfile(file):
    # A arbitrary (but fixed) buffer size
    BUF_SIZE = 65536
  
    # Initializing the sha256() method
    sha256 = hashlib.sha256()
  
    # Opening the file provided as the first commandline argument
    with open(file, 'rb') as f:
        while True:
            # reading data = BUF_SIZE from the file and saving it
            data = f.read(BUF_SIZE)
            # True if eof = 1
            if not data:
                break
            # Passing that data to that sh256 hash function
            sha256.update(data)
  
    # sha256.hexdigest() hashes all the input data passed to the sha256() via sha256.update()
    return sha256.hexdigest()




s3 = boto3.client(
  service_name='s3', 
  verify=False
)

bs = s3.list_buckets()
print(bs)

obs = s3.list_objects(Bucket='my-bucket-233')
print(obs)

s3.delete_object(Bucket='my-bucket-233', Key='test.jpg')

#s3.upload_file('test.jpg', 'my-bucket-233', 'test.jpg')

# obj = s3.get_object(Bucket='my-bucket-233', Key='test.jpg')

#s3.download_file('my-bucket-233', 'test.jpg', 'downloaded_file.jpg')


#hashfile('test.jpg')
#hashfile('downloaded_file.jpg')




