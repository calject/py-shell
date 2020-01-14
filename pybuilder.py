#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'calject'

import os
import argparse

import core.command as command
import core.system.output as output
from core.system.process import Process
from core.system.folder import Folder
from core.system.folder import FolderRead
from core.system.yaml import Yaml

# 系统判断
if os.name == 'nt':
    output.error('暂不支持windows系统', 1)
elif os.name == 'posix':
    home = command.run('echo $HOME')
else:
    output.error('暂不支持该系统类型构建[' + os.name + ']', 2)

# 初始化
process = Process()
folder = Folder(__file__)
folderRead = FolderRead(folder.dir)
yaml = Yaml(folder.file_path('pybuilder.yaml'))

parser = argparse.ArgumentParser(description="py-shell script")
parser.add_argument('--version', '-v', help="显示当前版本信息", action="store_true")
args = parser.parse_args()

if args.version:
    print(yaml.get('version'))
    exit(0)

# 检查并创建存储目录
confHome = yaml.get('home', '~').replace('~', home)
if os.path.isdir(confHome):
    pyHome = confHome
else:
    pyHome = os.path.join(home, confHome)

if not os.path.isdir(pyHome):
    os.mkdir(pyHome)

for model, value in yaml.get('models').items():
    fileList = folderRead.file_list(value.get('path', []), value.get('suffix', []))
    # print(fileList)

output.success('builder success')
