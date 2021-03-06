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
from core.system.resource import Resource
from core.system.parse import Parse
from core.system.yaml import Yaml
from core.system.envSrc import EnvSrc

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

# 获取资源存储目录(pyHome)
confHome = yaml.get('home', '~').replace('~', home)
pyHome = confHome if os.path.isdir(confHome) else os.path.join(home, confHome)

# 判断资源存储根目录是否正确
if pyHome in ('/', '~', home, '~/', home + '/'):
    output.error('home路径参数错误, home路径不能为 ' + pyHome)

# 创建资源类(删除生成资源/创建资源存储目录/获取资源文件路径)
resource = Resource(pyHome, yaml.get('source_name', 'py-shell.source'))
envSrc = EnvSrc(home, resource.get_source_path())

# 检查脚本参数
parser = argparse.ArgumentParser(description="基于python编写的脚本管理项目")
parser.add_argument('--version', '-v', help="显示当前版本信息", action="store_true")
parser.add_argument('--process', '-p', help="显示生成输出信息", action="store_true")
parser.add_argument('--clear', '-c', help="清理生成资源", action="store_true")
args = parser.parse_args()

if args.version:
    output.c_print_exit(yaml.get('version'))
process.is_process = args.process

if args.clear:
    resource.clear()
    envSrc.clear()
    output.success_exit("clear success.")

# 清理并重新生成资源目录
resource.recreate()

# 解析路径并生成资源文件
parse = Parse(process, resource.get_dir('sources'))
for model, value in yaml.get('models').items():
    fileList = folderRead.file_list(value.get('path', []), value.get('suffix', []))
    parse.append(model, fileList)

# 写入系统内容文件
parse.system_export('PYS_HOME', folder.dir)
parse.system_export('PYS_SHRC', envSrc.get_shrc_path())
with open(folder.tmp_path('system.tmp'), 'r') as f:
    parse.system_content.append(f.read().replace('$command$', yaml.get('command')).replace('$resolver$', yaml.get('resolver')))

parse.handle(resource.get_source_path())

# 检查并写入环境配置(.bash_profile/.zshrc)

envSrc.write()

output.success('builder success')
