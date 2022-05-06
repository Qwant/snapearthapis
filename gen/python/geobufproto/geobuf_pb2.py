# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geobufproto/geobuf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='geobufproto/geobuf.proto',
  package='geobufproto',
  syntax='proto2',
  serialized_options=b'\n\017com.geobufprotoB\013GeobufProtoH\001P\001\242\002\003GXX\252\002\013Geobufproto\312\002\013Geobufproto\342\002\027Geobufproto\\GPBMetadata\352\002\013Geobufproto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18geobufproto/geobuf.proto\x12\x0bgeobufproto\"\xea\n\n\x04\x44\x61ta\x12\x12\n\x04keys\x18\x01 \x03(\tR\x04keys\x12!\n\ndimensions\x18\x02 \x01(\r:\x01\x32R\ndimensions\x12\x1f\n\tprecision\x18\x03 \x01(\r:\x01\x36R\tprecision\x12T\n\x12\x66\x65\x61ture_collection\x18\x04 \x01(\x0b\x32#.geobufproto.Data.FeatureCollectionH\x00R\x11\x66\x65\x61tureCollection\x12\x35\n\x07\x66\x65\x61ture\x18\x05 \x01(\x0b\x32\x19.geobufproto.Data.FeatureH\x00R\x07\x66\x65\x61ture\x12\x38\n\x08geometry\x18\x06 \x01(\x0b\x32\x1a.geobufproto.Data.GeometryH\x00R\x08geometry\x1a\xfd\x01\n\x07\x46\x65\x61ture\x12\x36\n\x08geometry\x18\x01 \x02(\x0b\x32\x1a.geobufproto.Data.GeometryR\x08geometry\x12\x10\n\x02id\x18\x0b \x01(\tH\x00R\x02id\x12\x17\n\x06int_id\x18\x0c \x01(\x12H\x00R\x05intId\x12/\n\x06values\x18\r \x03(\x0b\x32\x17.geobufproto.Data.ValueR\x06values\x12\"\n\nproperties\x18\x0e \x03(\rB\x02\x10\x01R\nproperties\x12/\n\x11\x63ustom_properties\x18\x0f \x03(\rB\x02\x10\x01R\x10\x63ustomPropertiesB\t\n\x07id_type\x1a\x96\x03\n\x08Geometry\x12\x33\n\x04type\x18\x01 \x02(\x0e\x32\x1f.geobufproto.Data.Geometry.TypeR\x04type\x12\x1c\n\x07lengths\x18\x02 \x03(\rB\x02\x10\x01R\x07lengths\x12\x1a\n\x06\x63oords\x18\x03 \x03(\x12\x42\x02\x10\x01R\x06\x63oords\x12:\n\ngeometries\x18\x04 \x03(\x0b\x32\x1a.geobufproto.Data.GeometryR\ngeometries\x12/\n\x06values\x18\r \x03(\x0b\x32\x17.geobufproto.Data.ValueR\x06values\x12/\n\x11\x63ustom_properties\x18\x0f \x03(\rB\x02\x10\x01R\x10\x63ustomProperties\"}\n\x04Type\x12\t\n\x05POINT\x10\x00\x12\x0e\n\nMULTIPOINT\x10\x01\x12\x0e\n\nLINESTRING\x10\x02\x12\x13\n\x0fMULTILINESTRING\x10\x03\x12\x0b\n\x07POLYGON\x10\x04\x12\x10\n\x0cMULTIPOLYGON\x10\x05\x12\x16\n\x12GEOMETRYCOLLECTION\x10\x06\x1a\xac\x01\n\x11\x46\x65\x61tureCollection\x12\x35\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x19.geobufproto.Data.FeatureR\x08\x66\x65\x61tures\x12/\n\x06values\x18\r \x03(\x0b\x32\x17.geobufproto.Data.ValueR\x06values\x12/\n\x11\x63ustom_properties\x18\x0f \x03(\rB\x02\x10\x01R\x10\x63ustomProperties\x1a\xed\x01\n\x05Value\x12#\n\x0cstring_value\x18\x01 \x01(\tH\x00R\x0bstringValue\x12#\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00R\x0b\x64oubleValue\x12$\n\rpos_int_value\x18\x03 \x01(\x04H\x00R\x0bposIntValue\x12$\n\rneg_int_value\x18\x04 \x01(\x04H\x00R\x0bnegIntValue\x12\x1f\n\nbool_value\x18\x05 \x01(\x08H\x00R\tboolValue\x12\x1f\n\njson_value\x18\x06 \x01(\tH\x00R\tjsonValueB\x0c\n\nvalue_typeB\x0b\n\tdata_typeBl\n\x0f\x63om.geobufprotoB\x0bGeobufProtoH\x01P\x01\xa2\x02\x03GXX\xaa\x02\x0bGeobufproto\xca\x02\x0bGeobufproto\xe2\x02\x17Geobufproto\\GPBMetadata\xea\x02\x0bGeobufproto'
)



_DATA_GEOMETRY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='geobufproto.Data.Geometry.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POINT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPOINT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINESTRING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTILINESTRING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POLYGON', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPOLYGON', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEOMETRYCOLLECTION', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=875,
  serialized_end=1000,
)
_sym_db.RegisterEnumDescriptor(_DATA_GEOMETRY_TYPE)


_DATA_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='geobufproto.Data.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='geometry', full_name='geobufproto.Data.Feature.geometry', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='geometry', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='geobufproto.Data.Feature.id', index=1,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_id', full_name='geobufproto.Data.Feature.int_id', index=2,
      number=12, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='intId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='geobufproto.Data.Feature.values', index=3,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='values', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='geobufproto.Data.Feature.properties', index=4,
      number=14, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', json_name='properties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_properties', full_name='geobufproto.Data.Feature.custom_properties', index=5,
      number=15, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', json_name='customProperties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='id_type', full_name='geobufproto.Data.Feature.id_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=338,
  serialized_end=591,
)

_DATA_GEOMETRY = _descriptor.Descriptor(
  name='Geometry',
  full_name='geobufproto.Data.Geometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='geobufproto.Data.Geometry.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lengths', full_name='geobufproto.Data.Geometry.lengths', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', json_name='lengths', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coords', full_name='geobufproto.Data.Geometry.coords', index=2,
      number=3, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', json_name='coords', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometries', full_name='geobufproto.Data.Geometry.geometries', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='geometries', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='geobufproto.Data.Geometry.values', index=4,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='values', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_properties', full_name='geobufproto.Data.Geometry.custom_properties', index=5,
      number=15, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', json_name='customProperties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATA_GEOMETRY_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=1000,
)

_DATA_FEATURECOLLECTION = _descriptor.Descriptor(
  name='FeatureCollection',
  full_name='geobufproto.Data.FeatureCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='geobufproto.Data.FeatureCollection.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='features', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='geobufproto.Data.FeatureCollection.values', index=1,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='values', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_properties', full_name='geobufproto.Data.FeatureCollection.custom_properties', index=2,
      number=15, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', json_name='customProperties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1003,
  serialized_end=1175,
)

_DATA_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='geobufproto.Data.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_value', full_name='geobufproto.Data.Value.string_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stringValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='geobufproto.Data.Value.double_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='doubleValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos_int_value', full_name='geobufproto.Data.Value.pos_int_value', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='posIntValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='neg_int_value', full_name='geobufproto.Data.Value.neg_int_value', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='negIntValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='geobufproto.Data.Value.bool_value', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='boolValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_value', full_name='geobufproto.Data.Value.json_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='jsonValue', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value_type', full_name='geobufproto.Data.Value.value_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1178,
  serialized_end=1415,
)

_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='geobufproto.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='geobufproto.Data.keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keys', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='geobufproto.Data.dimensions', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dimensions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='precision', full_name='geobufproto.Data.precision', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='precision', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_collection', full_name='geobufproto.Data.feature_collection', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='featureCollection', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature', full_name='geobufproto.Data.feature', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='feature', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='geobufproto.Data.geometry', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='geometry', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATA_FEATURE, _DATA_GEOMETRY, _DATA_FEATURECOLLECTION, _DATA_VALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data_type', full_name='geobufproto.Data.data_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=42,
  serialized_end=1428,
)

_DATA_FEATURE.fields_by_name['geometry'].message_type = _DATA_GEOMETRY
_DATA_FEATURE.fields_by_name['values'].message_type = _DATA_VALUE
_DATA_FEATURE.containing_type = _DATA
_DATA_FEATURE.oneofs_by_name['id_type'].fields.append(
  _DATA_FEATURE.fields_by_name['id'])
_DATA_FEATURE.fields_by_name['id'].containing_oneof = _DATA_FEATURE.oneofs_by_name['id_type']
_DATA_FEATURE.oneofs_by_name['id_type'].fields.append(
  _DATA_FEATURE.fields_by_name['int_id'])
_DATA_FEATURE.fields_by_name['int_id'].containing_oneof = _DATA_FEATURE.oneofs_by_name['id_type']
_DATA_GEOMETRY.fields_by_name['type'].enum_type = _DATA_GEOMETRY_TYPE
_DATA_GEOMETRY.fields_by_name['geometries'].message_type = _DATA_GEOMETRY
_DATA_GEOMETRY.fields_by_name['values'].message_type = _DATA_VALUE
_DATA_GEOMETRY.containing_type = _DATA
_DATA_GEOMETRY_TYPE.containing_type = _DATA_GEOMETRY
_DATA_FEATURECOLLECTION.fields_by_name['features'].message_type = _DATA_FEATURE
_DATA_FEATURECOLLECTION.fields_by_name['values'].message_type = _DATA_VALUE
_DATA_FEATURECOLLECTION.containing_type = _DATA
_DATA_VALUE.containing_type = _DATA
_DATA_VALUE.oneofs_by_name['value_type'].fields.append(
  _DATA_VALUE.fields_by_name['string_value'])
_DATA_VALUE.fields_by_name['string_value'].containing_oneof = _DATA_VALUE.oneofs_by_name['value_type']
_DATA_VALUE.oneofs_by_name['value_type'].fields.append(
  _DATA_VALUE.fields_by_name['double_value'])
_DATA_VALUE.fields_by_name['double_value'].containing_oneof = _DATA_VALUE.oneofs_by_name['value_type']
_DATA_VALUE.oneofs_by_name['value_type'].fields.append(
  _DATA_VALUE.fields_by_name['pos_int_value'])
_DATA_VALUE.fields_by_name['pos_int_value'].containing_oneof = _DATA_VALUE.oneofs_by_name['value_type']
_DATA_VALUE.oneofs_by_name['value_type'].fields.append(
  _DATA_VALUE.fields_by_name['neg_int_value'])
_DATA_VALUE.fields_by_name['neg_int_value'].containing_oneof = _DATA_VALUE.oneofs_by_name['value_type']
_DATA_VALUE.oneofs_by_name['value_type'].fields.append(
  _DATA_VALUE.fields_by_name['bool_value'])
_DATA_VALUE.fields_by_name['bool_value'].containing_oneof = _DATA_VALUE.oneofs_by_name['value_type']
_DATA_VALUE.oneofs_by_name['value_type'].fields.append(
  _DATA_VALUE.fields_by_name['json_value'])
_DATA_VALUE.fields_by_name['json_value'].containing_oneof = _DATA_VALUE.oneofs_by_name['value_type']
_DATA.fields_by_name['feature_collection'].message_type = _DATA_FEATURECOLLECTION
_DATA.fields_by_name['feature'].message_type = _DATA_FEATURE
_DATA.fields_by_name['geometry'].message_type = _DATA_GEOMETRY
_DATA.oneofs_by_name['data_type'].fields.append(
  _DATA.fields_by_name['feature_collection'])
_DATA.fields_by_name['feature_collection'].containing_oneof = _DATA.oneofs_by_name['data_type']
_DATA.oneofs_by_name['data_type'].fields.append(
  _DATA.fields_by_name['feature'])
_DATA.fields_by_name['feature'].containing_oneof = _DATA.oneofs_by_name['data_type']
_DATA.oneofs_by_name['data_type'].fields.append(
  _DATA.fields_by_name['geometry'])
_DATA.fields_by_name['geometry'].containing_oneof = _DATA.oneofs_by_name['data_type']
DESCRIPTOR.message_types_by_name['Data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {

  'Feature' : _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
    'DESCRIPTOR' : _DATA_FEATURE,
    '__module__' : 'geobufproto.geobuf_pb2'
    # @@protoc_insertion_point(class_scope:geobufproto.Data.Feature)
    })
  ,

  'Geometry' : _reflection.GeneratedProtocolMessageType('Geometry', (_message.Message,), {
    'DESCRIPTOR' : _DATA_GEOMETRY,
    '__module__' : 'geobufproto.geobuf_pb2'
    # @@protoc_insertion_point(class_scope:geobufproto.Data.Geometry)
    })
  ,

  'FeatureCollection' : _reflection.GeneratedProtocolMessageType('FeatureCollection', (_message.Message,), {
    'DESCRIPTOR' : _DATA_FEATURECOLLECTION,
    '__module__' : 'geobufproto.geobuf_pb2'
    # @@protoc_insertion_point(class_scope:geobufproto.Data.FeatureCollection)
    })
  ,

  'Value' : _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
    'DESCRIPTOR' : _DATA_VALUE,
    '__module__' : 'geobufproto.geobuf_pb2'
    # @@protoc_insertion_point(class_scope:geobufproto.Data.Value)
    })
  ,
  'DESCRIPTOR' : _DATA,
  '__module__' : 'geobufproto.geobuf_pb2'
  # @@protoc_insertion_point(class_scope:geobufproto.Data)
  })
_sym_db.RegisterMessage(Data)
_sym_db.RegisterMessage(Data.Feature)
_sym_db.RegisterMessage(Data.Geometry)
_sym_db.RegisterMessage(Data.FeatureCollection)
_sym_db.RegisterMessage(Data.Value)


DESCRIPTOR._options = None
_DATA_FEATURE.fields_by_name['properties']._options = None
_DATA_FEATURE.fields_by_name['custom_properties']._options = None
_DATA_GEOMETRY.fields_by_name['lengths']._options = None
_DATA_GEOMETRY.fields_by_name['coords']._options = None
_DATA_GEOMETRY.fields_by_name['custom_properties']._options = None
_DATA_FEATURECOLLECTION.fields_by_name['custom_properties']._options = None
# @@protoc_insertion_point(module_scope)
