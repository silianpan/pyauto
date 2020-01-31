#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pyclamd
from threading import Thread


class Scan(Thread):

    def __init__(self, IP, scan_type, file):
        """构造方法"""
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""

    def run(self):
        """多进程run方法"""

        try:
            # 套接字
            cd = pyclamd.ClamdNetworkSocket(self.IP, 3310)
            # 探测连通性
            if cd.ping():
                self.connstr = self.IP+" connection [OK]"
                # 重载clamd病毒特征库，建议更新病毒库后做reload操作
                cd.reload()
                # 选择不同的扫描方式
                if self.scan_type == "contscan_file":
                    self.scanresult = "{0}\n".format(
                        cd.contscan_file(self.file))
                elif self.scan_type == "multiscan_file":
                    self.scanresult = "{0}\n".format(
                        cd.multiscan_file(self.file))
                elif self.scan_type == "scan_file":
                    self.scanresult = "{0}\n".format(cd.scan_file(self.file))
                time.sleep(1)
            else:
                self.connstr = self.IP+" ping error,exit"
                return
        except Exception as e:
            self.connstr = self.IP+" "+str(e)


# 扫描主机列表
IPs = ['192.168.1.21', '192.168.1.22']
# 扫描模式mutiscan_file、contscan_file、scan_file
scantype = "multiscan_file"
# 扫描路径
scanfile = "/data/www"
i = 1
# 线程数
threadnum = 2
scanlist = []

for ip in IPs:

    currp = Scan(ip, scantype, scanfile)
    scanlist.append(currp)

    # 当达到指定的线程数或IP列表数后启动、退出线程
    if i % threadnum == 0 or i == len(IPs):
        for task in scanlist:
            # 启动线程
            task.start()

        for task in scanlist:
            # 等待所有子线程退出，并输出扫描结果
            task.join()
            print(task.connstr)
            print(task.scanresult)
        scanlist = []
    i += 1
