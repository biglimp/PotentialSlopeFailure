# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xd3\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x16\x00\x00\x00\x16\x08\x02\x00\x00\x00\x4b\xd6\xfb\x6c\
\x00\x00\x00\x06\x74\x52\x4e\x53\x00\x00\x00\x00\x00\x00\x6e\xa6\
\x07\x91\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x73\x49\x44\x41\x54\x38\
\x8d\xa5\xd4\xbb\x0e\x80\x30\x0c\x43\xd1\xa6\xe2\xff\x7f\xd9\x0c\
\x48\x05\xaa\x3c\xec\xb4\x13\xcb\xb9\xca\x80\x6c\x00\xc6\xd9\xbb\
\x1a\xc6\xcc\xd6\x37\x00\x53\xaf\xf8\xfa\xe7\xcd\x43\xaf\x25\x5c\
\x2f\x24\x22\x0f\x80\x4a\x24\x9e\xba\x22\xf7\x75\xa2\xf4\x45\x82\
\xf1\x59\x82\xf4\x61\x82\xf7\x7e\x42\xf2\x4e\x42\xf5\x7b\xa2\xe1\
\x7f\x89\x9e\x7f\x13\x6d\x3f\xf2\xff\x82\xdc\x81\x19\x9d\xc0\xef\
\x88\x7f\x85\xb4\x43\x4e\x42\xdd\xb1\xb9\x99\xc6\x1a\xdf\xf1\x3c\
\x3f\x21\xe6\x81\x3b\x27\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\
\x60\x82\
"

qt_resource_name = b"\
\x00\x07\
\x07\x3b\xe0\xb3\
\x00\x70\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x73\
\x00\x15\
\x04\x2e\xf6\xe5\
\x00\x50\
\x00\x6f\x00\x74\x00\x65\x00\x6e\x00\x74\x00\x69\x00\x61\x00\x6c\x00\x53\x00\x6c\x00\x6f\x00\x70\x00\x65\x00\x46\x00\x61\x00\x69\
\x00\x6c\x00\x75\x00\x72\x00\x65\
\x00\x0d\
\x0e\x4d\x81\x47\
\x00\x73\
\x00\x6c\x00\x6f\x00\x70\x00\x65\x00\x69\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x44\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x44\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x6b\xdb\xca\x1b\x90\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
