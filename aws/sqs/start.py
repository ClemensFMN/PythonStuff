# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 20:41:30 2024

@author: 700001473
"""

import boto3
import json
import uuid


sqs = boto3.client(
  service_name='sqs', 
  verify=False
)


# Create a SQS queue, check IAM that the use is allowed to do this
# response = sqs.create_queue(QueueName='My_QUEUE')


qs = sqs.list_queues()
print(qs)

response = sqs.get_queue_url(QueueName='My_QUEUE')
print(response['QueueUrl'])

res = sqs.send_message(QueueUrl = 'My_QUEUE', 
                       MessageAttributes = {'Title': {
                                               'DataType': 'String',
                                               'StringValue': 'The Whistler'}},
                       MessageBody = str(uuid.uuid1()))

msgId = res['MessageId']
print(msgId)


response = sqs.receive_message(QueueUrl='My_QUEUE')
print(response['Messages'][0]['MessageId'])
print(response['Messages'][0]['Body'])

receipt_handle = response['Messages'][0]['ReceiptHandle']
sqs.delete_message(
    QueueUrl='My_QUEUE',
    ReceiptHandle=receipt_handle)


