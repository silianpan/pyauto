#!/usr/bin/python
# -*- coding: utf-8 -*-

import rrdtool
import time
import psutil

# 获取网卡入流量
total_input_traffic = psutil.net_io_counters()[1]
# 获取网卡出流量
total_output_traffic = psutil.net_io_counters()[0]
starttime = int(time.time())

# 将三个参数作为updatev参数，返回{'return_value':0L}则更新成功，反之失败
update = rrdtool.updatev('/home/test/rrdtool/Flow.rrd', '%s:%s:%s' %
                         (str(starttime), str(total_input_traffic), str(total_output_traffic)))
print(update)
