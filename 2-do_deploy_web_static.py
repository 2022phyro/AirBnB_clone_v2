#!/usr/bin/python3
"""This file uses fabric to generate a .tgz archive
from the contents of AirBnB_Clone using do_pack"""
from fabric.api import put, run, env
import os

env.hosts = ['3.84.238.62', '100.25.17.233']
def do_deploy(archive_path):
    """ This uses fabric to deploy a tar file to the server"""
    if not os.path.isfile(archive_path):
        return False
    name = archive_path.split('/')[-1]
    dest = "/tmp/{}".format(name)
    #print(dest)
    file_ = "/data/web_static/releases/{}".format(name.split('.')[0])
    #print(file_)
    try:
        put(archive_path, dest)
        run('mkdir -p {}'.format(file_))
        run("tar -xzf {} -C {}".format(dest, file_))
        run("rm {}".format(dest))
        run("mv {}/web_static* {}".format(file_, file_))
        run("rm -rf {}/web_static".format(file_))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(file_))
        return True
    except Exception:
        return False
