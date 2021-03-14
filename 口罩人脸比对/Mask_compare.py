# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys
import ast
from typing import List

from alibabacloud_facebody20191230.client import Client as facebody20191230Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_facebody20191230 import models as facebody_20191230_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> facebody20191230Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id="AccessKey ID",
            # 您的AccessKey Secret,
            access_key_secret="AccessKey Secret"
        )
        # 访问的域名
        config.endpoint = 'facebody.cn-shanghai.aliyuncs.com'
        return facebody20191230Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        verify_face_mask_request = facebody_20191230_models.VerifyFaceMaskRequest(
            image_url='http://viapi-customer-temp.oss-cn-shanghai.aliyuncs.com/LTAI4G4LpkeEk6Yx7k2bX7LY/416afdd0-7de1-41a4-80b0-ff0852e5f5d1.png',
            ref_url='http://viapi-customer-temp.oss-cn-shanghai.aliyuncs.com/LTAI4G4LpkeEk6Yx7k2bX7LY/ab19f99e-3675-4c6f-b3b0-0e5ace231135.jpg'
        )
        result = client.verify_face_mask(verify_face_mask_request)
        result2 = str(result)
        final = ast.literal_eval(result2)
        print(final["body"])

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        verify_face_mask_request = facebody_20191230_models.VerifyFaceMaskRequest(
            image_url='http://viapi-customer-temp.oss-cn-shanghai.aliyuncs.com/LTAI4G4LpkeEk6Yx7k2bX7LY/416afdd0-7de1-41a4-80b0-ff0852e5f5d1.png',
            ref_url='http://viapi-customer-temp.oss-cn-shanghai.aliyuncs.com/LTAI4G4LpkeEk6Yx7k2bX7LY/ab19f99e-3675-4c6f-b3b0-0e5ace231135.jpg'
        )
        await client.verify_face_mask_async(verify_face_mask_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])


