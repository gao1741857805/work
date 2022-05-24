#-*- coding utf-8 -*-
# @time  :  2021/12/31
#@Author : gaojunwen
import json

import requests
from PolicyBenchAPI.configs.config import pb_host
from PolicyBenchAPI.common.get_excelData import get_execlData,set_execlData

####
#接口测试
###
# -*- 初始化模块 -*-
class Requirement():
    def __init__(self):
        self.header = {
            '''
            此处为请求头
            '''
        }
    def Fangan_Requirement01(self):
        '''
        具体接口方法
        '''
        url = f"{pb_host}/接口地址"
        param = get_execlData ('PolicyBenchAPICase','接口方法')[0][0]
        res = requests.get(url,param=param,headers=self.header)
        return res.json()

    def Fangan_Requirement02(self, inData):
        '''
        具体接口方法
        '''
        url = f"{pb_host}/接口地址"
        payload = inData
        res = requests.get(url,headers=self.header,json=payload)
        return res.json()




