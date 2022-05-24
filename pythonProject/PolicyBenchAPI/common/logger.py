#-*- coding utf-8 -*-
# @time  :  2021/12/31
#@Author : gaojunwen

'''调用该方法打印日志'''

import datetime
import logging


def logger():
    '''logging.basicCofig函数各参数：
    filename 指定日志文件名；
    filemode:指定日志文件打开的模式。'w',或者'a';
    format:指定输出的格式和内容，format可以输出很多有用的信息，
    level logging.INFO，
    '''
    logging.basicConfig(format='%(asctime)S - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s',
                        filename=f'../TestLogs/{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.txt',
                        level='INFO',
                        filemode='a'
    )
    return logging