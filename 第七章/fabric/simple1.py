#!/usr/bin/env python
from fabric import task

# env.user = 'root'
# env.hosts = ['192.168.1.21', '192.168.1.22']
# env.password = 'SKJh935yft#'


@task
def local_task(c):
    c.run("uname -a")


@task
def remote_task(c):
    # 两个命令
    with c.run("/data/logs"):
        c.run("ls -l")
