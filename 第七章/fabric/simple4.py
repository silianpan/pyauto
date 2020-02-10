#!/usr/bin/env python
from fabric import task, Connection

# env.user = 'root'
# env.hosts = ['192.168.1.21', '192.168.1.22', '192.168.1.23']
# env.password = 'SKJh935yft#'
from fabric.transfer import Transfer
from invoke import Exit

connection = Connection(host='192.168.1.2', user='root',
                        connect_kwargs={'password': 'password'})


@task
def tar_task(c):
    c.run('cd /data/logs && tar -czf access.tar.gz access.log')


@task
def put_task(c):
    connection.run("mkdir -p /data/logs")
    try:
        c.run('/data/logs')
        Transfer(connection).put('/data/logs/access.tar.gz', '/data/logs/access.tar.gz')
    except OSError as e:
        raise Exit("Aborting file put task!" + str(e))


@task
def check_task(c):
    lmd5 = c.run('md5sum /data/logs/access.tar.gz', capture=True).split(' ')[0]
    rmd5 = connection.run("md5sum /data/logs/access.tar.gz").split(' ')[0]
    if lmd5 == rmd5:
        print("OK")
    else:
        print("ERROR")


# @task
def go():
    tar_task()
    put_task()
    check_task()


if __name__ == '__main__':
    go()
