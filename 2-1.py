import cStringIO
import formatter
from htmllib import HTMLParser
import httplib2
import os
import sys
import urllib.request
import urllib.parse
class Retriever(object):
    __slots__ = ('url','file')

    def __init__(self,url):
        self.url,self.file = self.get_file(url)

    def get_file(self,url,default='index.html'):
        'create usable local filename from url-----创建url的可用文件'

        parsed = urllib.parse.parse_qsl(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        filepath = '%s%s'%(host,parsed.path)

        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath,default)

        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
           if os.path.exists(linkdir):
             os.unlink(linkdir)
           os.makedirs(linkdir)
        return url,filepath

    def download(self):
        try:
            retval = urllib.urlretrieve(self.url,self.file)
        except(IOError,httplib2.InvalidURL) as e:
            retval =(('*** ERROR :bad URL "%s":%s'%(self.url,e)),)
        return retval

    def parse_links(self):
        f = open(self.file,'r')
        data = f.read()
        f.close()
        parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
        parser.feed(data)
        parser.close()
        return parser.anchorlist

class Crawler(object)
    count = 0
    def __int__(self,url):
        self.q = [url]
        self.seen = set()
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])

    def get_page(self,url,media =False):

