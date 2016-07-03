from  fabric.api import *

env.hosts = ['120.24.240.199']
env.user = 'root'
env.password = '@Tengfei05'


def hello():
    print "hello fabric"

def deploy():
    with cd('/home/tengfei/api01/test/TestTo'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')