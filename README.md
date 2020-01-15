# py-shell

* `cal-shell`项目`python`版本，[cal-shell项目地址](https://github.com/calject/cal-shell)
* `python`编写的脚本管理项目

## 安装

### 安装一 (合并)

* 合并命令

```bash
git clone https://github.com/calject/py-shell.git && cd py-shell && pip3 install -r package.txt && python3 ./pybuilder.py -p && source ~/.bash_profile && source ~/.zshrc
```

### 安装二 (分步)

1. clone项目到任意目录或者`fork`到自己的github账户，然后执行`git clone`

```
git clone https://github.com/calject/py-shell.git
```

2. 安装模块`pip3 install -r ./package.txt` (注: 安装不成功配置下国内镜像源)

3. 在项目目录下执行`python3 ./pybuilder.py`命令

4. 执行`source ~/.zshrc` 或者 `source ~/.bash_profile`

5. 执行完成后在任意位置执行`pybuilder`(可在`pybuilder.yaml`中修改该命令别名)构建


#### 代理问题(如果pip安装失败,配置一下pip安装源)

* 配置安装源
```
mkdir -p ~/.pip && vim ~/.pip/pip.conf
```

* 豆瓣
```
[global]
index-url=https://pypi.douban.com/simple/
[install]
use-mirrors=true
mirrors=https://pypi.douban.com/simple/
trusted-host=pypi.douban.com
```

* 阿里
```
[global]
index-url=https://mirrors.aliyun.com/pypi/simple
[install]
use-mirrors=true
mirrors=https://mirrors.aliyun.com/pypi/simple
trusted-host=mirrors.aliyun.com
```

## 使用:

* 在`pybuilder.yaml`配置文件中配置相关生成脚本路径参数
