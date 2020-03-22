
'''
    目标：
        1、搜索测试套件
        2、运行测试套件、并生成测试报告
'''
#导包 unittest HTMLTestRunner time
import unittest
import time
# from tools.HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner import  HTMLTestRunner

# suite = unittest.defaultTestLoader.discover("./cass",pattern="test*.py")
test_case = r"D:\JLPAY\python2020\project\cass"
test_list = unittest.defaultTestLoader.discover(test_case,pattern="test*.py")

file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

with open(file_path,"wb") as f:
    HTMLTestRunner(stream=f,title="彪哥威武",description="测试环境 WIN7").run(test_list)
