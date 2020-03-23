# -*- coding: utf-8 -*-
#定时任务-跑立刷商户
ProfitRPCService = {"command_id" : "ProfitRPCService","date" : "2020-02-11","skipCheck":"1"}
#添加下级合伙人
agentAddV2 ={
    "command_id":"agentAddV2",
    "s_user_id":"50263545",    #添加人ID--必输项
    "operatorId":"",
    "phone":"15503231623",        #手机号--必输项，同时存数据库的Account、Phone
    "rule":{"1-0-10":0.31,
             "1-0-5":0.54},      #分润规则,JSON格式，如：{ "1-0-1":"0.56", "1-0-2":"0.59"}
    "withdraw":"0",    #是否允许提现，0表示不允许，1表示允许，默认0
    "taxPoint":"0",    #发票税点，默认0 ，不为0时范围必须为3-10，4代及4代以上不允许设置此值
    "profitRuleConfigId":{"1":"1754"},  #分润规则套餐ID{"机具类型":"套餐ID"}
    "logId":"docapi_logId",   #日志ID
    "s_user_id":"50263545",           #session 用户id
    "s_user_name":"胡彪",         #session 用户名
    "operatorId":"50263545"           #session 操作者ID
}
#确定协议
protocolConfirmRpc = {
    "command_id":"protocolConfirmRpc",
    "s_user_id":"",           #添加人ID--必输项
    "logId":"docapi_logId",
    "s_user_id":"",           #session 用户id
    "s_user_name":"",         #session 用户名
    "operatorId":""           #session 操作者ID
}
#个人完善资料
microAuthRpc ={
    "command_id":"microAuthRpc",
    "s_user_id":"",        #添加人ID--必输项
    "operatorId":"",       #
    "name":"",             #昵称--必输项
    "realName":"",         #真实姓名--必输项
    "bankCardNo":"",       #银行卡号--必输项
    "idNo":"",             #身份证号--必输项
    "certFacePic":"",      #身份证人像面照片--必输项
    "certBackPic":"",      #身份证国徽面照片--必输项
    "certBeginDate":"",    #身份证有效期开始--必输项
    "certEndDate":"",      #身份证有效期结束--必输项
    "accountPic":"",       #银行卡照片--必输项
    "bankCode":"",         #银行编码--必输项
    "bankSubName":"",      #开户行--必输项
    "bankUnionCode":"",    #联行号--必输项
    "logId":"docapi_logId",#
    "s_user_id":"",        #session 用户id
    "s_user_name":"",      #session 用户名
    "operatorId":""        #session 操作者ID
}

#企业完善资料
licenseAuthRpc ={
    "command_id":"licenseAuthRpc",
    "s_user_id":"",           #添加人ID--必填项
    "operatorId":"",          #
    "name":"",                #昵称--必填项
    "realName":"",            #真实姓名--必填项
    "bankCardNo":"",          #银行卡号--必填项
    "idNo":"",                #身份证号--必填项
    "certFacePic":"",         #身份证人像面照片--必填项
    "certBackPic":"",         #身份证国徽面照片--必填项
    "certBeginDate":"",       #身份证有效期开始--必填项
    "certEndDate":"",         #身份证有效期结束--必填项
    "accountPic":"",          #银行卡照片--必填项
    "bankCode":"",            #银行编码--必填项
    "bankSubName":"",         #开户行--必填项
    "bankUnionCode":"",       #联行号--必填项
    "licensePic":"",          #营业执照照片--必填项
    "licenseNo":"",           #营业执照号--必填项
    "licenseName":"",         #营业执照公司名--必填项
    "licenseBeginDate":"",    #营业执照有效期--必填项
    "licenseEndDate":"",      #
    "licenseType":"",         #营业执照类型--必填项
    "accountType":"",         #账户类型：1-对公 0-对私--必填项
    "protocolPic":"",         #协议照片--必填项
    "taxType":"",             #缴纳类型，1开票，2扣税
    "logId":"docapi_logId",   #
    "s_user_id":"",           #session 用户id
    "s_user_name":"",         #session 用户名
    "operatorId":""           #session 操作者ID
}

#确认分润规则
profitRuleConfirmRpc = {
    "command_id":"profitRuleConfirmRpc",
    "s_user_id":"",          #添加人ID--必输项
    "status":"",             #204=同意，205=不同意--必输项
    "logId":"docapi_logId",  #
    "s_user_id":"",          #session 用户id
    "s_user_name":"",        #session 用户名
    "operatorId":""          #session 操作者ID
}

#获取下级临时密码
getChildTmpPwd ={
    "command_id":"getChildTmpPwd",
    "s_user_id":"",   #添加人ID--必输项
    "subUserId":"",   #下级id--必输项
    "logId":"",       #
    "s_user_id":"",   #session 用户id
    "s_user_name":"", #session 用户名
    "operatorId":""   #session 操作者ID
}

#