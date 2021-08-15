# def lambda_handler(event, context):
#     return "Hello, world and AWS!"
import sys
# reload (sys)
# sys.setdefaultencoding('UTF8')


import base64
import json
import time
import requests
import urllib3
import codecs

# used my api-key
url ="https://api.airtable.com/v0/appjzQ0kWbadhXzq4/MainTable?fields%5B%5D=ID&fields%5B%5D=title&sort%5B0%5D%5Bfield%5D=ID&api_key=keyL2Fz58E72N4JEa"
http = urllib3.PoolManager()
r = http.request('GET', url)
request_response = json.loads(r.data)
table_list=[]
# table_list_length = len(table_list)
for i in request_response["records"]:
    # (i["fields"]["title"]).decode('utf-8')
    table_list.append(i["fields"]["title"])
table_list_length = len(table_list)
temp=[]

def lambda_handler(event, context):
    global temp
    while True:
        for i in range(table_list_length):
            # udaliaem 1 elem v nachale
            temp.append(table_list.pop(0))
            # vstavliaem ego v konets
            table_list.append(temp[0])
            temp=[]
            time.sleep(1)
            # print(table_list[0:3])
 
            return table_list[0:3]
 
 
