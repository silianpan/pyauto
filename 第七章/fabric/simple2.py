#!/usr/bin/env python

# env.user = 'root'
# env.hosts = ['192.168.1.21', '192.168.1.22']
# env.password = "SKJh935yft#"
from fabric import ThreadingGroup

group = ThreadingGroup(
    "113.62.127.198", "113.62.127.199", user="root",
    connect_kwargs={'password': 'Leiwuqi_891'},
)


def input_raw():
    ret = input("please input directory name:")
    return ret if ret else '/home'


def worktask(dirname):
    group.run("ls -l " + dirname)


# @task
def go():
    getdirname = input_raw()
    worktask(getdirname)


if __name__ == '__main__':
    go()
