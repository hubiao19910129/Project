'''
目标：回顾parameterized参数化组件使用
安装：
    pip install parameterized
使用：
    @parameterized.expand(参数)
    参数：
        单个参数格式：列表 如[值1,值2]
        多个参数：外表嵌套元组: 如[(参数值1，参数值2)]
需求：
    输入用户名密码，数据分别为 1.admin ,123456 2.user002,654321

'''

import unittest
from parameterized import  parameterized

class TestPara(unittest.TestCase):
    @parameterized.expand([("admin1","123456"),("admin1","654321")])
    #参数值的个数必须要和参数的个数一致，否则报错
    def test_para(self,username,password):
        print("用户名：",username)
        print("密码：",password)


if __name__ == '__main__':
    TestPara.test_para()