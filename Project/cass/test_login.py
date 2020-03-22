import unittest
from api.api_login import ApiLogin
from parameterized import  parameterized
from tools.read_json import ReadJson
#读取数据函数
def get_data():
    data = ReadJson("login.json").read_json()
    arr = []
    arr.append((data.get("url"),
                data.get("mobile"),
                data.get("code"),
                data.get("expect_resule"),
                data.get("status_code")
                ))
    # print(arr)
    return arr

class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,expect_resule,status_code):
        # url = "http://172.20.6.24:8083"
        # mobile = "15511119876"
        # code ="9cbf8a4dcb8e30682b927f352d6559a0"

        s = ApiLogin().api_post_login(url,mobile,code)

        print("打印结果",s)
        print(type(s))

        # self.assertEqual(200,200)
        self.assertEqual(expect_resule,"OK")
        # self.assertEqual(300, 300)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()