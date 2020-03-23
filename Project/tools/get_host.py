from tools.read_json import ReadJson
from data.host_template import *

class GetHost(object):
    def __init__(self,hostTemplate):
        if type(hostTemplate) is not str:
            self.hostTemplate = str(hostTemplate)
        else:
            self.hostTemplate = hostTemplate

    def get_host1(self):
        json_host = eval(self.hostTemplate)
        return json_host

    def get_host(self):
        json_host = eval(self.hostTemplate)
        list1 = []
        list1.append((
            json_host["ip"],
            json_host["port"],
            json_host["logId"],
        ))
        print("host的值为：%s"%(list1))
        return list1

if __name__ == "__main__":
    GetHost(agentTest).get_host()
