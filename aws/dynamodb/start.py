# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:30:52 2024

@author: 700001473
"""

import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import uuid
import faker
f = faker.Faker()


dyndb = boto3.resource(
  service_name='dynamodb', 
  verify=False
)


table = dyndb.Table('test')

# table.creation_date_time

# for i in range(10):
#     res = table.put_item(
#         Item = {
#             'id': str(uuid.uuid1()),
#             'first_name': f.first_name(),
#             'last_name': f.last_name(),
#             'salary': int(f.bothify('###'))
#             }
#         )

# CAREFUL, this is not updated in real time :-(
# print(table.item_count)

response = table.scan(FilterExpression = Attr('salary').lt(500))

response['Count']

itms = response['Items']

for itm in itms:
    print(itm)

