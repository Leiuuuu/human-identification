# encoding:utf-8

import requests
import base64
from urllib import parse
from pprint import *
import urllib
import json

'''
用户信息查询
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete"

params = "{\"user_id\":\"user1\",\"group_id\":\"group_repeat\"}"
access_token = '24.fd9a12d5930bc3972e420d6c07fed82f.2592000.1616723726.282335-18630025'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())