# -*- coding: utf-8 -*-
import unittest
from tools.get_datas import GetDatas
from tools.get_host import GetHost
from parameterized import parameterized
from client_thrift.api_client import ApiClient

class TestAgentAddV2(unittest.TestCase):
    def test_agentAddV2(self):
        json_host = GetHost(hostTemplate="agentApiDev").get_host1()
        ip = json_host["ip"]
        port = json_host["port"]
        logId = json_host["logId"]
        value_str = GetDatas(dataTemplate="agentAddV2").get_datas()

        res = ApiClient(ip,port,logId,value_str).api_client()
        print("test_agentAddV2执行结果为：%s"%(res))

        ret_code = res["ret_code"]
        # print("断言ret_code取值为：%s"%(ret_code))
        self.assertEqual(ret_code,"00")

if __name__ == "__main__":
    unittest.main()

