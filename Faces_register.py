# encoding:utf-8

import requests
import base64
from urllib import parse
from pprint import *
import urllib
import json

'''
人脸注册
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"

with open('F:/final_facial_recong/Test_photo.jpg','rb')as f:
    img_jpg = f.read()  # 以二进制读取图片
    img64 = base64.b64encode(img_jpg)  # 对图片进行base64编码
    params = {}
    params['image'] = img64
    params['image_type'] = 'BASE64'
    params['group_id'] = 'group_repeat'
    params['user_id'] = "liuyinjie"
    params['user_info'] = "刘寅杰照片"
    params['quality_control'] = "LOW"
    params['liveness_control'] = "NONE"


params = urllib.parse.urlencode(params).encode()
access_token = '24.fd9a12d5930bc3972e420d6c07fed82f.2592000.1616723726.282335-18630025'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())