# -*- coding: utf-8 -*-
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from mpos_thrift.MposAccess import *
import json

class ApiClient(object):
    def __init__(self,ip,port,logid,value_str):
        self.ip = ip
        self.port = port

        if type(logid) is not str:
            logid1 = str(logid)
            self.logid = logid1
        else:
            self.logid = logid

        if type(value_str) is not str:
            value_str1 = str(value_str)
            self.value_str = value_str1
        else:
            self.value_str = value_str

    def api_client(self):
        try:
            sockets = TSocket.TSocket(self.ip,self.port)
            transport = TTransport.TFramedTransport(sockets)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = Client(protocol)
            transport.open()

            #创建客户端
            json_response = client.Invoke(self.logid,self.value_str)

        except Exception as e:
            print(e)
            raise Exception("调用失败，调用接口为:{}".format(self.ip,self.port))

        else:
            response_data = json.loads(json_response)
            print("api_client调用结果为:%s"%(response_data))
            return response_data
            transport.close()


