#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def Login(self, logid, request):
    """
    Parameters:
     - logid
     - request
    """
    pass

  def Invoke(self, logid, request):
    """
    Parameters:
     - logid
     - request
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def Login(self, logid, request):
    """
    Parameters:
     - logid
     - request
    """
    self.send_Login(logid, request)
    return self.recv_Login()

  def send_Login(self, logid, request):
    self._oprot.writeMessageBegin('Login', TMessageType.CALL, self._seqid)
    args = Login_args()
    args.logid = logid
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_Login(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = Login_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "Login failed: unknown result")

  def Invoke(self, logid, request):
    """
    Parameters:
     - logid
     - request
    """
    self.send_Invoke(logid, request)
    return self.recv_Invoke()

  def send_Invoke(self, logid, request):
    self._oprot.writeMessageBegin('Invoke', TMessageType.CALL, self._seqid)
    args = Invoke_args()
    args.logid = logid
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_Invoke(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = Invoke_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "Invoke failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["Login"] = Processor.process_Login
    self._processMap["Invoke"] = Processor.process_Invoke

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_Login(self, seqid, iprot, oprot):
    args = Login_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = Login_result()
    try:
      result.success = self._handler.Login(args.logid, args.request)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("Login", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_Invoke(self, seqid, iprot, oprot):
    args = Invoke_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = Invoke_result()
    try:
      result.success = self._handler.Invoke(args.logid, args.request)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("Invoke", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class Login_args:
  """
  Attributes:
   - logid
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'logid', None, None, ), # 1
    (2, TType.STRING, 'request', None, None, ), # 2
  )

  def __init__(self, logid=None, request=None,):
    self.logid = logid
    self.request = request

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.logid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.request = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Login_args')
    if self.logid is not None:
      oprot.writeFieldBegin('logid', TType.STRING, 1)
      oprot.writeString(self.logid)
      oprot.writeFieldEnd()
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRING, 2)
      oprot.writeString(self.request)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.logid)
    value = (value * 31) ^ hash(self.request)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Login_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Login_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Invoke_args:
  """
  Attributes:
   - logid
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'logid', None, None, ), # 1
    (2, TType.STRING, 'request', None, None, ), # 2
  )

  def __init__(self, logid=None, request=None,):
    self.logid = logid
    self.request = request

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.logid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.request = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Invoke_args')
    if self.logid is not None:
      oprot.writeFieldBegin('logid', TType.STRING, 1)
      oprot.writeString(self.logid)
      oprot.writeFieldEnd()
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRING, 2)
      oprot.writeString(self.request)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.logid)
    value = (value * 31) ^ hash(self.request)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Invoke_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Invoke_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
