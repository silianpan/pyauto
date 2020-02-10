#!/usr/bin/env python
from fabric import task

'''
fab命令引用默认文件名为fabfile.py，如果使用非默认文件名称，则需通过’-f‘来指定
如：fab -H hostname/ip -f host_type.py host_type。
如果管理机和目标主机未配置密钥认证信任，将会提示输入目标主机对应账号登陆密码

有时不需要写一行Python代码也可以完成远程操作，直接使用命令行的形式，如：
fab -p password -H 192.168.1.2,192.168.1.3 -- 'uname -s'
'''

# @task(hosts=["my-server"])
@task
def host_type(c):
    # c = Connection(host='192.168.1.2', user='root',
    #                connect_kwargs={'password': 'password'})
    c.run('uname -s')
