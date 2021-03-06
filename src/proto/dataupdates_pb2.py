# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataupdates.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dataupdates.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x64\x61taupdates.proto\",\n\x0bImageHeader\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\"V\n\nImageBlock\x12\x0c\n\x04left\x18\x01 \x01(\x05\x12\x0b\n\x03top\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x0e\n\x06pixels\x18\x05 \x01(\x0c\"\xa2\x01\n\x08\x46\x61\x63\x65\x44\x61ta\x12\x1e\n\x05\x65moji\x18\x01 \x01(\x0e\x32\x0f.FaceData.Emoji\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\n\n\x02\x64x\x18\x04 \x01(\x05\x12\n\n\x02\x64y\x18\x05 \x01(\x05\x12\r\n\x05theta\x18\x06 \x01(\x05\x12\x0e\n\x06\x64theta\x18\x07 \x01(\x05\x12\x0c\n\x04size\x18\x08 \x01(\x05\"\x1b\n\x05\x45moji\x12\t\n\x05HAPPY\x10\x00\x12\x07\n\x03SAD\x10\x01\"$\n\x03Msg\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04seed\x18\x02 \x01(\x06\"\xdb\x01\n\nDataUpdate\x12\x1b\n\x08\x66\x61\x63\x65\x64\x61ta\x18\x01 \x01(\x0b\x32\t.FaceData\x12\x11\n\x03msg\x18\x02 \x01(\x0b\x32\x04.Msg\x12\x1e\n\timg_block\x18\x03 \x01(\x0b\x32\x0b.ImageBlock\x12\x1d\n\x07img_hdr\x18\x04 \x01(\x0b\x32\x0c.ImageHeader\x12\x1f\n\x05utype\x18\x05 \x01(\x0e\x32\x10.DataUpdate.Type\"=\n\x04Type\x12\x0c\n\x08\x46\x41\x43\x45\x44\x41TA\x10\x00\x12\r\n\tIMG_BLOCK\x10\x01\x12\x0b\n\x07IMG_HDR\x10\x02\x12\x0b\n\x07MESSAGE\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FACEDATA_EMOJI = _descriptor.EnumDescriptor(
  name='Emoji',
  full_name='FaceData.Emoji',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HAPPY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=291,
  serialized_end=318,
)
_sym_db.RegisterEnumDescriptor(_FACEDATA_EMOJI)

_DATAUPDATE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='DataUpdate.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACEDATA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMG_BLOCK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMG_HDR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=517,
  serialized_end=578,
)
_sym_db.RegisterEnumDescriptor(_DATAUPDATE_TYPE)


_IMAGEHEADER = _descriptor.Descriptor(
  name='ImageHeader',
  full_name='ImageHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='ImageHeader.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='ImageHeader.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=21,
  serialized_end=65,
)


_IMAGEBLOCK = _descriptor.Descriptor(
  name='ImageBlock',
  full_name='ImageBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='ImageBlock.left', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top', full_name='ImageBlock.top', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='ImageBlock.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='ImageBlock.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pixels', full_name='ImageBlock.pixels', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=67,
  serialized_end=153,
)


_FACEDATA = _descriptor.Descriptor(
  name='FaceData',
  full_name='FaceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='emoji', full_name='FaceData.emoji', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='FaceData.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='FaceData.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dx', full_name='FaceData.dx', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dy', full_name='FaceData.dy', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='FaceData.theta', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dtheta', full_name='FaceData.dtheta', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='FaceData.size', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FACEDATA_EMOJI,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=318,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Msg.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='Msg.seed', index=1,
      number=2, type=6, cpp_type=4, label=1,
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
  serialized_start=320,
  serialized_end=356,
)


_DATAUPDATE = _descriptor.Descriptor(
  name='DataUpdate',
  full_name='DataUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='facedata', full_name='DataUpdate.facedata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='DataUpdate.msg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='img_block', full_name='DataUpdate.img_block', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='img_hdr', full_name='DataUpdate.img_hdr', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utype', full_name='DataUpdate.utype', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATAUPDATE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=578,
)

_FACEDATA.fields_by_name['emoji'].enum_type = _FACEDATA_EMOJI
_FACEDATA_EMOJI.containing_type = _FACEDATA
_DATAUPDATE.fields_by_name['facedata'].message_type = _FACEDATA
_DATAUPDATE.fields_by_name['msg'].message_type = _MSG
_DATAUPDATE.fields_by_name['img_block'].message_type = _IMAGEBLOCK
_DATAUPDATE.fields_by_name['img_hdr'].message_type = _IMAGEHEADER
_DATAUPDATE.fields_by_name['utype'].enum_type = _DATAUPDATE_TYPE
_DATAUPDATE_TYPE.containing_type = _DATAUPDATE
DESCRIPTOR.message_types_by_name['ImageHeader'] = _IMAGEHEADER
DESCRIPTOR.message_types_by_name['ImageBlock'] = _IMAGEBLOCK
DESCRIPTOR.message_types_by_name['FaceData'] = _FACEDATA
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['DataUpdate'] = _DATAUPDATE

ImageHeader = _reflection.GeneratedProtocolMessageType('ImageHeader', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEHEADER,
  __module__ = 'dataupdates_pb2'
  # @@protoc_insertion_point(class_scope:ImageHeader)
  ))
_sym_db.RegisterMessage(ImageHeader)

ImageBlock = _reflection.GeneratedProtocolMessageType('ImageBlock', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEBLOCK,
  __module__ = 'dataupdates_pb2'
  # @@protoc_insertion_point(class_scope:ImageBlock)
  ))
_sym_db.RegisterMessage(ImageBlock)

FaceData = _reflection.GeneratedProtocolMessageType('FaceData', (_message.Message,), dict(
  DESCRIPTOR = _FACEDATA,
  __module__ = 'dataupdates_pb2'
  # @@protoc_insertion_point(class_scope:FaceData)
  ))
_sym_db.RegisterMessage(FaceData)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), dict(
  DESCRIPTOR = _MSG,
  __module__ = 'dataupdates_pb2'
  # @@protoc_insertion_point(class_scope:Msg)
  ))
_sym_db.RegisterMessage(Msg)

DataUpdate = _reflection.GeneratedProtocolMessageType('DataUpdate', (_message.Message,), dict(
  DESCRIPTOR = _DATAUPDATE,
  __module__ = 'dataupdates_pb2'
  # @@protoc_insertion_point(class_scope:DataUpdate)
  ))
_sym_db.RegisterMessage(DataUpdate)


# @@protoc_insertion_point(module_scope)
