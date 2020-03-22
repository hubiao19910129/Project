# -*-encoding:utf-8-*-

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from mpos_thrift.MposAccess import *
from mpos_thrift.ttypes import *

class HelloHandler:
    #demo.thrift中定义的函数
    def hello_x(self,what):
        print("hello_x was called!")
        return "hello %s" % what

def run():
    #创建服务器
    handler = HelloHandler()
    # Processor = Processor(handler)
    processor = Processor(handler)

    #监听端口
    transport = TSocket.TServerSocket("localhost",9234)

    #选择传输层
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    #选择传输协议
    tfactory = TTransport.TBufferedTransportFactory()

    #指定格式：服务器、监听端口、传输协议、传输层
    server = TServer.TThreadPoolServer(processor,
                                       transport,
                                       tfactory,
                                       pfactory)

    #设置服务线程
    server.setNumThreads(5)
    print("service is running")
    server.serve()

if __name__ == "__main__":
    run()
