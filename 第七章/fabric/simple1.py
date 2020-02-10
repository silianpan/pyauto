#!/usr/bin/env python

# env.user = 'root'
# env.hosts = ['192.168.1.21', '192.168.1.22']
# env.password = 'SKJh935yft#'
from fabric import ThreadingGroup

group = ThreadingGroup(
    "192.168.1.1", "192.168.1.2", user="root", connect_kwargs={'password': 'password'},
)


def local_task():
    group.run("uname -a")


def remote_task():
    group.run("cd / && ls -l")


if __name__ == '__main__':
    local_task()
    remote_task()
