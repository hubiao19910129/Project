import json
from test import Transmit
from test.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

ip_port = TSocket.TSocket('172.20.21.160',25658)
transport = TTransport.TBufferedTransport(ip_port)
#协议
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Transmit.Client(protocol)

transport.open()
#{"command_id" : "ProfitRPCService","date" : "2020-02-11","skipCheck":"1"}
data = {"command_id" : "ProfitRPCService","date" : "2020-02-11","skipCheck":"1"}
data_json = json.dumps(data)
data_str = data_json.encode("utf-8")

result = client.invoke(data_str)
print(result)

transport.close()

