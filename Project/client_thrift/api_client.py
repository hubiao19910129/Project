# -*- coding: utf-8 -*-
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


from mpos_thrift.MposAccess import *

# #调用数据
import json
from data.agent import *
value_json = eval("ProfitRPCService")
value_str = json.dumps(value_json)
print(value_str)




class ApiClient(object):
    def __init__(self,ip,port,logid,value_str):
        self.ip = ip
        self.port = port
        self.logid = logid
        self.value_str = value_str

    def run(self):
        try:
            sockets = TSocket.TSocket(ip,port)
            transport = TTransport.TFramedTransport(sockets)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = Client(protocol)
            transport.open()

            #创建客户端
            if type(logid) is str:
               logid = logid
            else:
                logid = str(logid)
            res = client.Invoke(logid,value_str)

        except Exception as e:
            print(e)
            raise Exception("调用失败，调用接口为:{}".format(ip,port))

        else:
            print(res)
            transport.close()

if __name__ == "__main__":


    # 调用服务
    ip = "172.20.21.160"
    port = int(25658)
    logid = 10

    ApiClient(ip,port,logid,value_str).run()
