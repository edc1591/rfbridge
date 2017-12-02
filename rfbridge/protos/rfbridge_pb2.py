# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rfbridge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rfbridge.proto',
  package='rfbridge',
  syntax='proto3',
  serialized_pb=_b('\n\x0erfbridge.proto\x12\x08rfbridge\"4\n\x0e\x43ommandRequest\x12\"\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\x11.rfbridge.Command\"\x11\n\x0f\x43ommandResponse*K\n\x07\x43ommand\x12\t\n\x05LIGHT\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x08\n\x04SLOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04\x46\x41ST\x10\x04\x12\x0b\n\x07REVERSE\x10\x05\x32P\n\x08RFBridge\x12\x44\n\x0bSendCommand\x12\x18.rfbridge.CommandRequest\x1a\x19.rfbridge.CommandResponse\"\x00\x62\x06proto3')
)

_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='rfbridge.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIGHT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAST', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=101,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_COMMAND)

Command = enum_type_wrapper.EnumTypeWrapper(_COMMAND)
LIGHT = 0
STOP = 1
SLOW = 2
MEDIUM = 3
FAST = 4
REVERSE = 5



_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='rfbridge.CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='rfbridge.CommandRequest.command', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=80,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='rfbridge.CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=99,
)

_COMMANDREQUEST.fields_by_name['command'].enum_type = _COMMAND
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE
DESCRIPTOR.enum_types_by_name['Command'] = _COMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommandRequest = _reflection.GeneratedProtocolMessageType('CommandRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDREQUEST,
  __module__ = 'rfbridge_pb2'
  # @@protoc_insertion_point(class_scope:rfbridge.CommandRequest)
  ))
_sym_db.RegisterMessage(CommandRequest)

CommandResponse = _reflection.GeneratedProtocolMessageType('CommandResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDRESPONSE,
  __module__ = 'rfbridge_pb2'
  # @@protoc_insertion_point(class_scope:rfbridge.CommandResponse)
  ))
_sym_db.RegisterMessage(CommandResponse)



_RFBRIDGE = _descriptor.ServiceDescriptor(
  name='RFBridge',
  full_name='rfbridge.RFBridge',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=178,
  serialized_end=258,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendCommand',
    full_name='rfbridge.RFBridge.SendCommand',
    index=0,
    containing_service=None,
    input_type=_COMMANDREQUEST,
    output_type=_COMMANDRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RFBRIDGE)

DESCRIPTOR.services_by_name['RFBridge'] = _RFBRIDGE

# @@protoc_insertion_point(module_scope)
