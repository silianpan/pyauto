import pexpect

ip = "113.62.127.199"
user = "root"
passwd = "password"
target_file = "/var/log/nginx/access.log"

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])
fout = open('mylog.txt', 'wb')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /root/nginx_access.tar.gz '+target_file)
    child.expect('#')
    print(child.before)
    child.sendline('exit')
    fout.close()
except EOFError:
    print("expect EOF")
except TimeoutError:
    print("expect TIMEOUT")

child = pexpect.spawn(
    '/usr/bin/scp', [user+'@'+ip+':/root/nginx_access.tar.gz', '/Users/panliu/Downloads'])
fout = open('mylog.txt', 'ab')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOFError:
    print("expect EOF")
except TimeoutError:
    print("expect TIMEOUT")
