import feedparser
from time import sleep
import base64

timeout = 15


class Robo_Feed(object):
    def __init__(self):
        self.data = []
        self.sites = {}
        self.headalllines = []

    def append_url(self, name, site):
        self.sites[name] = (site)

    def encrip(self, published):
        self.data.append(base64.standard_b64encode(published.encode('ascii')))


def feed_parser():
    def parseRSS(rss_url):
        return feedparser.parse(rss_url)

    def getHeadlines(rss_url):
        robo.headlines = []
        feed = parseRSS(rss_url)

        if (base64.standard_b64encode(feed.entries[0].published.encode('ascii')) in robo.data):
            return robo.headlines
        else:
            POSTAGEN = '*' + feed['feed']['title'] + '*' + "\n" + feed.entries[0].title + "\n" + feed.entries[
                0].link + "\n\r"
            print (POSTAGEN)
            robo.encrip(feed.entries[0].published)
            return robo.headlines

    for key, url in robo.sites.items():
        robo.headalllines.extend(getHeadlines(url))


robo = Robo_Feed()
robo.append_url('Oglobo', 'http://oglobo.globo.com/rss.xml?secao=ece_frontpage')
robo.append_url('ZeroHora', 'http://zh.clicrbs.com.br/rs/ultimas-noticias-rss/')

try:
    while True:
        feed_parser()
        sleep(timeout)
except KeyboardInterrupt:
    print ("Umteromped")
