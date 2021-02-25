# encoding:utf-8

import requests

'''
组列表查询
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist"

params = "{\"start\":0,\"length\":100}"
access_token = '24.fd9a12d5930bc3972e420d6c07fed82f.2592000.1616723726.282335-18630025'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())