#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'calject'

import os

import core.command as command
import core.system.output as output
from core.system.process import Process
from core.system.folder import Folder
from core.system.yaml import Yaml

# 初始化
process = Process()
folder = Folder(__file__)

# 系统判断
if os.name == 'nt':
    output.error('暂不支持windows系统', 1)
elif os.name == 'posix':
    home = command.run('echo $HOME')
else:
    output.error('暂不支持该系统类型构建[' + os.name + ']', 2)

# 读配置文件
yaml = Yaml(folder.file_path('pybuilder.yaml'))

for model, value in yaml.get('models').items():
    print(model, value)
print(yaml.get('models'))

print(list(x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'))

confHome = yaml.get('home').replace('~', home)
if os.path.isdir(confHome):
    pyHome = confHome
else:
    pyHome = os.path.join(home, confHome)

if not os.path.isdir(pyHome):
    os.mkdir(pyHome)

print(yaml.get('version'))
