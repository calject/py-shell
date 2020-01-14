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
from core.system.handle import Handle
from core.system.yaml import Yaml

# 系统判断
if os.name == 'nt':
    output.error('暂不支持windows系统', 1)
elif os.name == 'posix':
    home = command.run('echo $HOME')
else:
    output.error('暂不支持该系统类型构建[' + os.name + ']', 2)

Handle.handle('alias', [1, 2, 3])

exit(0)

# 初始化
process = Process()
folder = Folder(__file__)
folderRead = FolderRead(folder.dir)
yaml = Yaml(folder.file_path('pybuilder.yaml'))

parser = argparse.ArgumentParser(description="基于python编写的脚本管理项目")
parser.add_argument('--version', '-v', help="显示当前版本信息", action="store_true")
parser.add_argument('--process', '-p', help="显示生成输出信息", action="store_true")
args = parser.parse_args()

if args.version:
    output.c_print_end(yaml.get('version'))
process.is_process = args.process

# 检查并创建存储目录
process.process('检查并创建存储目录')
confHome = yaml.get('home', '~').replace('~', home)
if os.path.isdir(confHome):
    pyHome = confHome
else:
    pyHome = os.path.join(home, confHome)

if not os.path.isdir(pyHome):
    os.mkdir(pyHome)

for model, value in yaml.get('models').items():
    fileList = folderRead.file_list(value.get('path', []), value.get('suffix', []))
    # todo: 处理model及路径
    # print(fileList)

output.success('builder success')
