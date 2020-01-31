# -*- coding: utf-8 -*-
import os
import sys
import pycurl

URL = "http://www.baidu.com"
# 创建一个curl对象
c = pycurl.Curl()
# 请求的url
c.setopt(pycurl.URL, URL)

# 连接超时时间,5秒，设置0表示不等待
c.setopt(pycurl.CONNECTTIMEOUT, 5)

# 请求超时时间,5秒
c.setopt(pycurl.TIMEOUT, 5)
# 完成交互后强制断开连接，不重用
c.setopt(pycurl.FORBID_REUSE, 1)
# 指定HTTP重定向最大数
c.setopt(pycurl.MAXREDIRS, 1)
# 是否屏蔽下载进度条，非0则屏蔽
c.setopt(pycurl.NOPROGRESS, 1)
# 设置保存DNS信息的时间，默认为120秒
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
indexfile = open(os.path.dirname(
    os.path.realpath(__file__))+"/content.txt", "wb")
# 将返回的HTTP HEADER定向到indexfile文件对象
c.setopt(pycurl.WRITEHEADER, indexfile)
# 将返回的HTML内容定向到indexfile文件对象
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    # 提交请求
    c.perform()
except Exception as e:
    print("connecion error:"+str(e))
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
# HTTP状态码
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print("HTTP状态码：%s" % (HTTP_CODE))
print("DNS解析时间：%.2f ms" % (NAMELOOKUP_TIME*1000))
print("建立连接时间：%.2f ms" % (CONNECT_TIME*1000))
print("准备传输时间：%.2f ms" % (PRETRANSFER_TIME*1000))
print("传输开始时间：%.2f ms" % (STARTTRANSFER_TIME*1000))
print("传输结束总时间：%.2f ms" % (TOTAL_TIME*1000))

print("下载数据包大小：%d bytes/s" % (SIZE_DOWNLOAD))
print("HTTP头部大小：%d byte" % (HEADER_SIZE))
print("平均下载速度：%d bytes/s" % (SPEED_DOWNLOAD))

indexfile.close()
c.close()
