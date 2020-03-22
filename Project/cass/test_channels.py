import unittest
from api.api_channels import ApiChannels
from parameterized import parameterized
from tools.read_json import ReadJson

def get_data():
    data = ReadJson("channel.json").read_json()
    arr = []
    # 采用data.get，如果取不到值会报错
    arr.append((data.get("url"),
                data.get("headers"),
                data.get("expect_resule"),
                data.get("status_code")
                ))
    return arr


class TestChannels(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,espect_result,status_code):
        # url     = "http://172.20.6.24:8083"
        # headers = {"Content-Type":"application/json","account":"15511119876","password":"9cbf8a4dcb8e30682b927f352d6559a0"}
        r = ApiChannels.api_get_channels(self,url,headers)

        print(r)

        self.assertEqual(espect_result,"OK")
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()