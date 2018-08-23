# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetCapitalDistribution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetCapitalDistribution.proto',
  package='Qot_GetCapitalDistribution',
  syntax='proto2',
  serialized_pb=_b('\n Qot_GetCapitalDistribution.proto\x12\x1aQot_GetCapitalDistribution\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"-\n\x03\x43\x32S\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\"\xb4\x01\n\x13\x43\x61pitalDistribution\x12\x14\n\x0c\x63\x61pitalInBig\x18\x01 \x02(\x01\x12\x14\n\x0c\x63\x61pitalInMid\x18\x02 \x02(\x01\x12\x16\n\x0e\x63\x61pitalInSmall\x18\x03 \x02(\x01\x12\x15\n\rcapitalOutBig\x18\x04 \x02(\x01\x12\x15\n\rcapitalOutMid\x18\x05 \x02(\x01\x12\x17\n\x0f\x63\x61pitalOutSmall\x18\x06 \x02(\x01\x12\x12\n\nupdateTime\x18\x07 \x02(\t\"S\n\x03S2C\x12L\n\x13\x63\x61pitalDistribution\x18\x01 \x01(\x0b\x32/.Qot_GetCapitalDistribution.CapitalDistribution\"7\n\x07Request\x12,\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x1f.Qot_GetCapitalDistribution.C2S\"p\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12,\n\x03s2c\x18\x04 \x01(\x0b\x32\x1f.Qot_GetCapitalDistribution.S2C')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetCapitalDistribution.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetCapitalDistribution.C2S.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=141,
)


_CAPITALDISTRIBUTION = _descriptor.Descriptor(
  name='CapitalDistribution',
  full_name='Qot_GetCapitalDistribution.CapitalDistribution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capitalInBig', full_name='Qot_GetCapitalDistribution.CapitalDistribution.capitalInBig', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capitalInMid', full_name='Qot_GetCapitalDistribution.CapitalDistribution.capitalInMid', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capitalInSmall', full_name='Qot_GetCapitalDistribution.CapitalDistribution.capitalInSmall', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capitalOutBig', full_name='Qot_GetCapitalDistribution.CapitalDistribution.capitalOutBig', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capitalOutMid', full_name='Qot_GetCapitalDistribution.CapitalDistribution.capitalOutMid', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capitalOutSmall', full_name='Qot_GetCapitalDistribution.CapitalDistribution.capitalOutSmall', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='Qot_GetCapitalDistribution.CapitalDistribution.updateTime', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=324,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetCapitalDistribution.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capitalDistribution', full_name='Qot_GetCapitalDistribution.S2C.capitalDistribution', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=409,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetCapitalDistribution.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetCapitalDistribution.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=466,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetCapitalDistribution.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetCapitalDistribution.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetCapitalDistribution.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetCapitalDistribution.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetCapitalDistribution.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=580,
)

_C2S.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_S2C.fields_by_name['capitalDistribution'].message_type = _CAPITALDISTRIBUTION
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['CapitalDistribution'] = _CAPITALDISTRIBUTION
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetCapitalDistribution_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalDistribution.C2S)
  ))
_sym_db.RegisterMessage(C2S)

CapitalDistribution = _reflection.GeneratedProtocolMessageType('CapitalDistribution', (_message.Message,), dict(
  DESCRIPTOR = _CAPITALDISTRIBUTION,
  __module__ = 'Qot_GetCapitalDistribution_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalDistribution.CapitalDistribution)
  ))
_sym_db.RegisterMessage(CapitalDistribution)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetCapitalDistribution_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalDistribution.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetCapitalDistribution_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalDistribution.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetCapitalDistribution_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCapitalDistribution.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
