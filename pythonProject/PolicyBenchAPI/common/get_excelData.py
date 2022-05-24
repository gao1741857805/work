#-*- coding utf-8 -*-
# @time  :  2021/12/31
#@Author : gaojunwen

import xlrd
import json
import copy
def get_execlData(sheetName,caseName):
    '''
    获取中的数据
    :param sheetName : 表名
    :param caseName : 某一个接口的用例名
    :return：返回数据
    '''
    resList = []
    execlDir='../testdate/文件名.xls'
    wordBook=xlrd.open_workbook(execlDir,formatter_info=True)
    worksheet= wordBook.sheet_by_name(sheetName)
    idx=0
    for one in worksheet.col_valuse(2):
        if caseName in one:
            reqBodyData = worksheet.cell(idx,7).value
            resData = worksheet.cell(idx, 8).value
            resList.append(json.loads(reqBodyData),json.loads(resData))
            idx +=1
    return resList
def set_execlData():
    '''写入数据'''
    resList = []
    execlDir = '../testdate/文件名.xls'
    wordBook = xlrd.open_workbook(execlDir, formatter_info=True)
    wordBookNew = copy(wordBook)
    worksheetNew = wordBookNew.get_sheet(0)
    return wordBookNew,worksheetNew