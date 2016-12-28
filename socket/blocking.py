import socket

s = socket.socket()

try:
    s.connect(('www.google.cn', 80))
except socket.error as e:
    print str(e)

    try:
        print "We are connected to %s:%d" % s.getpeername()
    except:
        print "Connection failed!"

else:
    print "We are connected to %s:%d" % s.getpeername()