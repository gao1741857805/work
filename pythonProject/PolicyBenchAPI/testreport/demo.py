#-*- coding utf-8 -*-
# @time  :  2021/12/31
#@Author : gaojunwen

import requests
class RequirementApi():
    def Fangan_Requirement01(self):
        url = "接口地址"
        #param = {"name"}
        header = {
            "请求头"
        }
        res = requests.get(url,header=header)
        print(res.json())

    def Fangan_Requirement02(self):
        url = "接口地址"
        # param = {"name"}
        header = {
            "请求头"
        }
        payload={"请求体"}
        res = requests.get(url, header=header, json=payload)
        print(res.text)
if  __name__ == '__main__':
    re = RequirementApi()
    re.Fangan_Requirement()