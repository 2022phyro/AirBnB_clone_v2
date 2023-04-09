#!/usr/bin/python3
"""This file uses fabric to generate a .tgz archive
from the contents of AirBnB_Clone using do_pack"""
from fabric.api import put, run, env, local
import datetime
import os
from fabric.decorators import runs_once


env.hosts = ['3.84.238.62', '100.25.17.233']


@runs_once
def do_pack():
    """ This uses fabric to create a tar file"""
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(date)
    command = "tar -cvzf {} web_static".format(name)
    if not os.path.isdir("versions"):
        res = local('mkdir versions')
    res = local(command)
    if res.failed:
        return None
    return name


def do_deploy(archive_path):
    """ This uses fabric to deploy a tar file to the server"""
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.split('/')[-1]
        dest = "/tmp/{}".format(name)
        file_ = "/data/web_static/releases/{}".format(name.split('.')[0])
        put(archive_path, "/tmp/")
        run('mkdir -p {}'.format(file_))
        run("tar -xzf {} -C {}".format(dest, file_))
        run("rm {}".format(dest))
        run("mv {}/web_static/* {}".format(file_, file_))
        run("rm -rf {}/web_static".format(file_))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(file_))
        return True
    except Exception:
        return False


def deploy():
    """This function calls do_pack and do_deploy
    do_pack creates a snapshot while do_deploy then
    deploys that snapshot to the whole servers"""
    name = do_pack()
    if name is None:
        return False
    val = do_deploy(name)
    return val
