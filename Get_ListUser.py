# encoding:utf-8

import requests

'''
获取用户列表
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"

params = "{\"group_id\":\"group_repeat\"}"
access_token = 'access_token'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
