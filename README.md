# py-shell

* `cal-shell`项目`python`版本，[cal-shell项目地址](https://github.com/calject/cal-shell)
* `python`编写的脚本管理项目

## 安装

### 安装一 (合并)

* 合并命令

```bash
git clone https://github.com/calject/py-shell.git && cd py-shell && python3 ./pybuilder.py -p && source ~/.bash_profile && source ~/.zshrc
```

### 安装二 (分步)

1. clone项目到任意目录或者`fork`到自己的github账户，然后执行`git clone`

```
git clone https://github.com/calject/py-shell.git
```

2. 在项目目录下执行`python3 ./pybuilder.py`命令

3. 执行`source ~/.zshrc` 或者 `source ~/.bash_profile`

4. 执行完成后在任意位置执行`pybuilder`(可在`pybuilder.yaml`中修改该命令别名)构建


## 使用:

* 在`pybuilder.yaml`配置文件中配置相关生成脚本路径参数
