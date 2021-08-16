# import sys
# # reload (sys)
# # sys.setdefaultencoding('UTF8')
import time
import json
import urllib3
import os
import base64
import codecs
import requests

def lambda_handler(event, context):
    while True:
        # used my own key
        url = f"https://api.airtable.com/v0/appjzQ0kWbadhXzq4/MainTable?fields%5B%5D=ID&fields%5B%5D=title&sort%5B0%5D%5Bfield%5D=ID&api_key=keyL2Fz58E72N4JEa"
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        request_response = json.loads(r.data.decode('utf-8'))
        # print(request_response)

        table_list=[]

        for record in request_response["records"]:
            table_list.append(record["fields"]["title"])

        table_list_length = len(table_list)    

        # print(table_list)
        # print(time.time())
        srez = table_list[int(time.time())%table_list_length:]+table_list[:int(time.time())%table_list_length]
        # print(srez)
        time.sleep(1)
        
        return  srez[:3]


# 
# temp=[]

# def lambda_handler(event, context):
#     global temp
#     while True:
#         for i in range(table_list_length):
#             # udaliaem 1 elem v nachale
#             temp.append(table_list.pop(0))
#             # vstavliaem ego v konets
#             table_list.append(temp[0])
#             temp=[]
#             time.sleep(1)
#             # print(table_list[0:3])
 
#             return table_list[0:3]
