from  fabric.api import *

env.hosts = ['121.42.203.41']
env.user = 'root'
env.password = '@Tengfei05'


def hello():
    print "hello fabric"

def deploy():
    with cd('/home/tengfeia a/TestTo'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')