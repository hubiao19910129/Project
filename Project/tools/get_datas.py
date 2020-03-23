from data.agent_template import *
import json

class GetDatas(object):
    def __init__(self, dataTemplate):
        if type(dataTemplate) is not str:
            self.dataTemplate = str(dataTemplate)
        else:
            self.dataTemplate = dataTemplate

    def get_datas(self):
        json_data = eval(self.dataTemplate)
        str_data = json.dumps(json_data)

        print("datas的值为：%s"%(str_data))
        print(type(str_data))
        return str_data
if __name__ == "__main__":
    GetDatas(ProfitRPCService).get_datas()
