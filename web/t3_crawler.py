import cStringIO
import formatter
from htmllib import HTMLParser
import httplib
import os
import sys
import urllib
import urlparse
from time import ctime

logging_level = 'DEBUG'

class Retriever(object):
    __slots__ = ('url', 'file')
    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        filepath = '%s%s' % (host, parsed.path)    # host/path1/path2/...
        if not os.path.splitext(parsed.path)[1]:   # no file extension exist
            filepath = os.path.join(filepath, default)  # join with default file name
        linkdir = os.path.dirname(filepath)  ## get path without file name
        if not os.path.isdir(linkdir):  ## not an existed dir
            if os.path.exists(linkdir): ## there is a file with same name, delete the file
                if logging_level in ('DEBUG', 'INFO', 'WARN'):
                    print "** [%s] WARNING: file '%s' exist, delete it" % (ctime(), linkdir)
                os.unlink(linkdir)
            if logging_level in ('DEBUG', 'INFO'):
                print "[%s] INFO: create directory '%s'" % (ctime(), linkdir)
            os.makedirs(linkdir)   ## create the dir

        return url, filepath

    def download(self):
        try:
            if logging_level in ('DEBUG'):
                print "[%s] DEBUG: downloading '%s' to '%s'" % (ctime(), self.url, self.file)
            retval  = urllib.urlretrieve(self.url, self.file)
        except (IOError, httplib.InvalidURL) as e:
            retval = (("*** ERROR: bad URL '%s': %s" % (self.url, e)),)

        return retval

    def parse_links(self):
        f = open(self.file, 'r')
        data = f.read()
        f.close()

        parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
        parser.feed(data)
        parser.close()

        return parser.anchorlist


class Crawler(object):
    count = 0

    def __init__(self, url):
        self.q = [url]
        self.seen = set()
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]   # username@host:port  --> host
        self.dom = '.'.join(host.split('.')[-2:])  # get the last 2 fields

    def get_page(self, url, media=False):
        r = Retriever(url)
        fname = r.download()[0]   # filename, header
        if fname[0] == '*':
            print fname
            return

        Crawler.count += 1
        if logging_level in ('DEBUG', 'INFO'):
            print "[%s] INFO: File Downloaded! [count: %d]" % (ctime(), Crawler.count)
        self.seen.add(url)

        ftype = os.path.splitext(fname)[1]
        if ftype not in ('.htm', '.html'):
            return

        for link in r.parse_links():
            if link.startswith('mailto:'):
                if logging_level in ('DEBUG', 'INFO'):
                    print "[%s] INFO: discard mailto link: '%s'" % (ctime(), link)
                continue

            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3', '.mp4', '.m4v', '.flv', '.wav', '.midi'):
                    if logging_level in ('DEBUG', 'INFO'):
                        print "[%s] INFO: discard media file: '%s'" % (ctime(), link)
                    continue

            if not link.startswith('http://'):  ## relative path
                link = urlparse.urljoin(url, link)

            if link not in self.seen:
                if self.dom not in link:
                    if logging_level in ('DEBUG', 'INFO', 'WARN'):
                        print "** [%s] WARNING: discard, out of current domain:  '%s'" % (ctime(), link)
                else:
                    if link not in self.q:
                        self.q.append(link)
                        if logging_level in ('DEBUG', 'INFO'):
                            print "[%s] INFO: new link discovered: '%s'" % (ctime(), link)
                    else:
                        if logging_level in ('DEBUG'):
                            print "[%s] DEBUG: link already in Queue, discard: '%s'" % (ctime(), link)
            else:
                if logging_level in ('DEBUG'):
                    print "[%s] DEBUG: link already proceeded, discard: '%s'" % (ctime(), link)

    def go(self, media=False):
        while self.q:
            url = self.q.pop()
            self.get_page(url, media)


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = raw_input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''

    if not url:
        return

    if not url.startswith('http://') and not url.startswith('ftp://'):
        url = 'http://%s' % url

    robot = Crawler(url)
    robot.go()


if __name__ == '__main__':
    main()





