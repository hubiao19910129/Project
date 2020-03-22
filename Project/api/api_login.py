#导包
import requests

class ApiLogin(object):
    # def api_post_login(self,url,mobile,code):
    def api_post_login(self, url,mobile,code):
        headers = {"Content-Type":"application/json"}
        # data    = {"mobile":"mobile","code":"code"}
        data = {"command_id":"agentUserLoginRpc","account":"mobile","password":"code"}
        return requests.post(url,headers=headers,json=data)