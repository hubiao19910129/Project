namespace cpp mpos_thrift
namespace d mpos_thrift
namespace java com.jlpay.mpos.thirft.api
namespace php mpos_thrift
namespace perl mpos_thrift
namespace haxe mpos_thrift
namespace py mpos_thrift

//bool：布尔类型(true or value)，占一个字节
//byte：有符号字节
 
typedef i16 int16 //i16:16位有符号整型
 
typedef i32 int32 //i32:32位有符号整型
 
typedef i64 int64 //i64:64位有符号整型
 
//double：64位浮点数
 
//string：未知编码或者二进制的字符串

########### 指定调用方法 ##############
service MposAccess{
   string Login(1:string logid, 2:string request),
   #string Pay(1:string logid, 2:string request)
   string Invoke(1:string logid, 2:string request)
}

############# 使用命令 ###############
#thrift -r --gen cpp finance.thrift
#thrift -r --gen cpp:cob_style finance.thrift

#thrift-0.9.3.exe -r --gen py as_mpos.thrift
