# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:15:32 2024

@author: 700001473
"""

import boto3

client = boto3.client(
    service_name='ec2',
    verify=False)

#ec2 = boto3.resource('ec2', verify=False)

res = client.describe_instances()
print(res)

inst = client.run_instances(ImageId='ami-02fe204d17e0189fb', InstanceType='t2.nano', KeyName='AWSKey', SecurityGroupIds=['sg-06f15069'], MaxCount=1, MinCount=1)

print(inst)
