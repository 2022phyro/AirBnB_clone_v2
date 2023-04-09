#!/usr/bin/python3
"""This file uses fabric to generate a .tgz archive
from the contents of AirBnB_Clone using do_pack"""
import datetime
from fabric.api import local
import os


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
