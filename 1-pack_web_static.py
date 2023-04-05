#!/usr/bin/python3
"""This file uses fabric to generate a .tgz archive
from the contents of AirBnB_Clone using do_pack"""
#from fabric import Connection
import datetime
from fabric.api import run

def do_pack():
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"versions/web_static_{date}.tgz"
    command = f"tar -cvzf {name} web_static"
    try:
        run(command)
        return name
    except:
        return None
