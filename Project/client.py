# -*-encoding:utf-8-*-

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import  TBinaryProtocol

from mpos_thrift.MposAccess import *

def run():
    try:
        transport = TSocket.TSocket("localhost",9234)
        transport = TTransport.TBufferedTransport(transport)
        #选择协议
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Client(protocol)
        transport.open()

        #创建客户端
        res = client.Invoke("agent_id",datastr)
        print(res)

        transport.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()