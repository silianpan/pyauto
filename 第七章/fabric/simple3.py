#!/usr/bin/env python
from fabric import ThreadingGroup, Connection

# env.user = 'root'
# env.gateway = '192.168.1.23'
# env.hosts = ['192.168.1.21', '192.168.1.22']
# env.passwords = {
#     'root@192.168.1.21:22': 'SKJh935yft#',
#     'root@192.168.1.22:22': 'SKJh935yft#',
#     'root@192.168.1.23:22': 'KJSD9325hgs'
# }
from fabric.transfer import Transfer
from invoke import Exit

group = ThreadingGroup(
    "172.16.95.1", user="root",
    gateway=Connection(host='113.62.127.199', user='root',
                       connect_kwargs={'password': 'Leiwuqi_891'}),
    connect_kwargs={'password': 'Leiwuqi_891'},
)

lpackpath = "./fileTestTranster.txt"
rpackpath = "/tmp/install"


# @task
def put_task():
    group.run("mkdir -p /tmp/install")
    for conn in group:
        try:
            Transfer(conn).put(lpackpath, rpackpath)
        except OSError as e:
            raise Exit("Aborting file put task!" + str(e))


# @task
def run_task():
    group.run("cd /tmp/install && cat fileTestTranster.txt")


# @task
def go():
    put_task()
    run_task()


if __name__ == '__main__':
    go()
