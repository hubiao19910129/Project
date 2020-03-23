import json

class ReadJson(object):
    def __init__(self,filename):
        #路径：../
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            #return 后面加值，不可以是表达式，data = json.load(f)
            return  json.load(f)



if __name__ == '__main__' :
    rj=ReadJson("login_more.json").read_json()
    print("读取json数据：%s"%(rj))
    print(type(rj))

    datas = ReadJson("login_more.json").read_json()
    #新建空列表list，arrs
    arrs = []
    # 采用data.get，如果取不到值会报错
    # 使用遍历获取所有values
    for data in datas.values():
        # data为两个login对应的值，dict类型
        print("data数据为：%s"%(data))
        print(type(data))
        # 将dict取值添加到元组中，再将元组添加到列表里
        arrs.append((data.get("url"),
                    data.get("mobile"),
                    data.get("code"),
                    data.get("expect_resule"),
                    data.get("status_code")
                    ))
        print("arrs数据为：%s"%(arrs))
        print(type(arrs))

