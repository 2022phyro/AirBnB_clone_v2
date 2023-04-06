from fabric.api import run, env
from fabric.api import task
env.hosts = ['100.25.17.233']
@task
def mytask():
    run('uname')
