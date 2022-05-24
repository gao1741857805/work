#-*- coding utf-8 -*-
# @time  :  2021/12/31
#@Author : gaojunwen

'''
总用例执行入口
'''
import pytest
import  os
if __name__ == '__main__':
    for one in  os.listdir('../testreport/tmp'):
        if 'json' in one:
            os.remove(f'../testreport/tmp{one}')

    pytest.main(['tesrRequirement.py', '-s','-v','--alluredir','../testreport/tmp'])
    os.system('allure sever ../testreport/tmp')