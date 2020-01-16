#!/bin/zsh

# 更新项目代码

# [help]:更新项目代码

local remote branch isProcess=0
local -a remotes

cd $PYS_HOME
remotes=($(git remote))
branch=$(git branch | awk '/\*.*/{print $2}')

[[ -z $remotes ]] && {
    error "fatal: No remote repository specified.  Please, specify either a URL or a
remote name from which new revisions should be fetched."
}

[[ -n ${remotes[(I)origin]} ]] && {
    remote='origin'
} || {
    remote=${remotes[1]}
}
cd $PYS_HOME

git remote prune ${remote}

git fetch ${remote} ${branch}

git pull ${remote} ${branch}
