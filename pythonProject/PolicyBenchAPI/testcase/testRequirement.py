#-*- coding utf-8 -*-
# @time  :  2021/12/31
#@Author : gaojunwen
from symtable import Class

import pytest
from PolicyBenchAPI.apilib.requiremeny import Requirement
from PolicyBenchAPI.common.get_excelData import get_execlData

class TestRequirement():
    def setup_class(self):
        print("------------start run test TestCase-----------------")

    @pytest.mark.parametrize('inData,resData', get_execlData('policyBenApicase', '接口方法'))
    def test_search_requirement(self, inData, resData):
        try:
            res = TestRequirement.Fangan_Requirement01(self, inData, resData)
            print('实际相应结果======', res)
            assert res["data"]["list"][0]["masterPolcyName"]
        except Exception as err:
            raise err

    @pytest.mark.parametrize('inData,resData', get_execlData('policyBenApicase', '接口方法'))
    def test_search_requirement(self, inData, resData):
        try:
            res = TestRequirement.Fangan_Requirement02(self, inData, resData)
            print('实际相应结果======', res)
            assert res["resultCode"] == resData["resultCode"]
        except Exception as err:
            raise err

        def teardown_class(self):
                print("------------stop run test TestCase-----------------")


if __name__ == '__main__':
    pytest.main(['testResquirement.py', '-s'])
