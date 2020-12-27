# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/device_attributes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/device_attributes.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\026DeviceAttributesProtosP\001ZXgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/device_attributes_go_proto\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1tensorflow/core/framework/device_attributes.proto\x12\ntensorflow\"E\n\x10InterconnectLink\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08strength\x18\x03 \x01(\x05\"8\n\nLocalLinks\x12*\n\x04link\x18\x01 \x03(\x0b\x32\x1c.tensorflow.InterconnectLink\"Z\n\x0e\x44\x65viceLocality\x12\x0e\n\x06\x62us_id\x18\x01 \x01(\x05\x12\x11\n\tnuma_node\x18\x02 \x01(\x05\x12%\n\x05links\x18\x03 \x01(\x0b\x32\x16.tensorflow.LocalLinks\"\xac\x01\n\x10\x44\x65viceAttributes\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x02 \x01(\t\x12\x14\n\x0cmemory_limit\x18\x04 \x01(\x03\x12,\n\x08locality\x18\x05 \x01(\x0b\x32\x1a.tensorflow.DeviceLocality\x12\x13\n\x0bincarnation\x18\x06 \x01(\x06\x12\x1c\n\x14physical_device_desc\x18\x07 \x01(\tB\x91\x01\n\x18org.tensorflow.frameworkB\x16\x44\x65viceAttributesProtosP\x01ZXgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/device_attributes_go_proto\xf8\x01\x01\x62\x06proto3'
)




_INTERCONNECTLINK = _descriptor.Descriptor(
  name='InterconnectLink',
  full_name='tensorflow.InterconnectLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='tensorflow.InterconnectLink.device_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.InterconnectLink.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strength', full_name='tensorflow.InterconnectLink.strength', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=134,
)


_LOCALLINKS = _descriptor.Descriptor(
  name='LocalLinks',
  full_name='tensorflow.LocalLinks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='link', full_name='tensorflow.LocalLinks.link', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=192,
)


_DEVICELOCALITY = _descriptor.Descriptor(
  name='DeviceLocality',
  full_name='tensorflow.DeviceLocality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus_id', full_name='tensorflow.DeviceLocality.bus_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numa_node', full_name='tensorflow.DeviceLocality.numa_node', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='links', full_name='tensorflow.DeviceLocality.links', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=284,
)


_DEVICEATTRIBUTES = _descriptor.Descriptor(
  name='DeviceAttributes',
  full_name='tensorflow.DeviceAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.DeviceAttributes.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='tensorflow.DeviceAttributes.device_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory_limit', full_name='tensorflow.DeviceAttributes.memory_limit', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locality', full_name='tensorflow.DeviceAttributes.locality', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='incarnation', full_name='tensorflow.DeviceAttributes.incarnation', index=4,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='physical_device_desc', full_name='tensorflow.DeviceAttributes.physical_device_desc', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=459,
)

_LOCALLINKS.fields_by_name['link'].message_type = _INTERCONNECTLINK
_DEVICELOCALITY.fields_by_name['links'].message_type = _LOCALLINKS
_DEVICEATTRIBUTES.fields_by_name['locality'].message_type = _DEVICELOCALITY
DESCRIPTOR.message_types_by_name['InterconnectLink'] = _INTERCONNECTLINK
DESCRIPTOR.message_types_by_name['LocalLinks'] = _LOCALLINKS
DESCRIPTOR.message_types_by_name['DeviceLocality'] = _DEVICELOCALITY
DESCRIPTOR.message_types_by_name['DeviceAttributes'] = _DEVICEATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InterconnectLink = _reflection.GeneratedProtocolMessageType('InterconnectLink', (_message.Message,), {
  'DESCRIPTOR' : _INTERCONNECTLINK,
  '__module__' : 'tensorflow.core.framework.device_attributes_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.InterconnectLink)
  })
_sym_db.RegisterMessage(InterconnectLink)

LocalLinks = _reflection.GeneratedProtocolMessageType('LocalLinks', (_message.Message,), {
  'DESCRIPTOR' : _LOCALLINKS,
  '__module__' : 'tensorflow.core.framework.device_attributes_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.LocalLinks)
  })
_sym_db.RegisterMessage(LocalLinks)

DeviceLocality = _reflection.GeneratedProtocolMessageType('DeviceLocality', (_message.Message,), {
  'DESCRIPTOR' : _DEVICELOCALITY,
  '__module__' : 'tensorflow.core.framework.device_attributes_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DeviceLocality)
  })
_sym_db.RegisterMessage(DeviceLocality)

DeviceAttributes = _reflection.GeneratedProtocolMessageType('DeviceAttributes', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEATTRIBUTES,
  '__module__' : 'tensorflow.core.framework.device_attributes_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DeviceAttributes)
  })
_sym_db.RegisterMessage(DeviceAttributes)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
