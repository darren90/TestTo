#-*- coding: UTF-8 -*-

from  fabric.api import *

env.hosts = ['121.42.203.41']
env.user = 'root'
env.password = '@Tengfei05'


def hello():
    print "hello fabric"

# 只是拉取代码而已
def pullgit():
    with cd('/home/tengfei/TestTo'):
        # run('git pull')
        run('git fetch --all')
        run('git reset --hard origin/master ')
        run('git pull')

# 部署应用
def deploy():
    with cd('/home/tengfei/TestTo'):
        # run('git pull')
        run('git fetch --all')
        run('git reset --hard origin/master ')
        run('git pull')
        sudo('supervisorctl restart autohome')
        sudo('supervisorctl status')


def schedu():
    with cd('/home/tengfei/TestTo/autohome/spider'):
        run('phython tv.py &')

