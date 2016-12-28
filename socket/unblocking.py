import socket

s = socket.socket()
s.setblocking(0)

try:
    s.connect(('www.whu.edu.cn', 80))
except socket.error as e:
    print str(e)
    i = 0
    while True:
        try:
            print "We are connected to %s:%d" % s.getpeername()
            break
        except:
            print "Let's do some math while waiting: %d" % i
            i += 1
else:
    print "We are connected to %s:%d" % s.getpeername()