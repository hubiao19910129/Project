import json



# with open("./data/login.json","r",encoding="utf-8") as f :
#     data = json.load(f)
#     print("获取数据为",data)

# def read_json():
#     with open("./data/login.json", "r", encoding="utf-8") as f:
#     return data = json.load(f)

# def read_json(filename):
#     with open("./data/filename", "r", encoding="utf-8") as f:
#     return data = json.load(f)

class ReadJson(object):
    def __init__(self,filename):
        #路径：../
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            #return 后面加值，不可以是表达式，data = json.load(f)
            return  json.load(f)



if __name__ == '__main__' :
    # ReadJson("login.json").read_json()
    # print(ReadJson("login.json").read_json())

    # data = ReadJson("login.json").read_json()
    # arr = []
    # #采用data.get，如果取不到值会报错
    # arr.append((data.get("url"),
    #             data.get("mobile"),
    #             data.get("code"),
    #             data.get("expect_resule"),
    #             data.get("status_code")
    #             ))
    # print(arr)

    # data = ReadJson("login.json").read_json()
    # arr = []
    # # 采用data.get，如果取不到值会报错
    # arr.append((data.get("url"),
    #             data.get("mobile"),
    #             data.get("code"),
    #             data.get("expect_resule"),
    #             data.get("status_code")
    #             ))
    # print(arr)

    #获取用户频道信息 调试
    data = ReadJson("channel.json").read_json()
    arr = []
    # 采用data.get，如果取不到值会报错
    arr.append((data.get("url"),
                data.get("headers"),
                data.get("expect_resule"),
                data.get("status_code")
                ))
    print(arr)
