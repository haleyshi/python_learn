# -*- coding: UTF-8 -*-

import nntplib
import socket

HOST = 'news.gmane.org'
GRNM = 'gmane.comp.python.committers'
USER = 'username'
PASS = 'password'

def main():
    try:
        #n = nntplib.NNTP(HOST, user=USER, password=PASS)
        n = nntplib.NNTP(HOST)
    except socket.gaierror as e:
        print 'ERROR: cannot reach host "%s"' % HOST
        print '     ("%s")' % eval(str(e))[1]
        return

    print '*** Connected to host "%s"' % HOST

    try:
        resp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError as e:
        print 'ERROR: cannot load group "%s"' % GRNM
        print '     ("%s")' % str(e)
        print '     Server may require authentication'
        print '     Please ensure the right username and password are used'
        n.quit()
        return
    except nntplib.NNTPTemporaryError as ee:
        print 'ERROR: group "%s" unavailable' % GRNM
        print '     ("%s")' % str(ee)
        n.quit()
        return

    print '*** Found newsgroup "%s"' % GRNM

    rng = "%s-%s" % (fst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print '''*** Found last article (#%s)

    From: %s
    Subject" %s
    Date: %s
    ''' % (lst, frm[0][1], sub[0][1], dat[0][1])

    rsp, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    print '*** First (<=20) meaningful lines:\n'
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not lower.startswith('>>>')) or lower.startswith('|') or lower.startswith('in article') or lower.endswith('writes:') or lower.endswith('wrote:'):
                continue

        if not lastBlank or (lastBlank and line):
            print '     %s' % line
            if line:
                count += 1
                lastBlank = False
            else:
                lastBlank = True

        if count >= 20:
            break


if __name__ == '__main__':
    main()