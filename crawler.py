from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler
from icrawler.utils import Proxy, ProxyPool


class ProxiedGoogleImageCrawler(GoogleImageCrawler):
    def set_proxy_pool(self, pool=None):
        self.proxy_pool = ProxyPool()
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:1081', 'http'))
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:1081', 'https'))


class ProxiedBingImageCrawler(BingImageCrawler):
    def set_proxy_pool(self, pool=None):
        self.proxy_pool = ProxyPool()
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:1081', 'http'))
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:1081', 'https'))


def craw_from_baidu(list_word):
    for word in list_word:
        storage = {'root_dir': './crawled/baidu/' + word}
        crawler = BaiduImageCrawler(parser_threads=2,
                                    downloader_threads=8,
                                    storage=storage)
        crawler.crawl(keyword=word, max_num=100)


def craw_from_google(list_word):
    for word in list_word:
        storage = {'root_dir': './crawled/google/' + word}
        crawler = ProxiedGoogleImageCrawler(parser_threads=2,
                                            downloader_threads=8,
                                            storage=storage)
        crawler.crawl(keyword=word, max_num=1000)


def craw_from_bing(list_word):
    for word in list_word:
        storage = {'root_dir': './crawled/bing/' + word}
        crawler = ProxiedBingImageCrawler(parser_threads=2,
                                          downloader_threads=8,
                                          storage=storage)
        crawler.crawl(keyword=word, max_num=1000)


if __name__ == '__main__':
    dogs = [
        'alaskan malamute', 'chihuahua dog', 'dachshund',
        'french bulldog', 'husky', 'akita inu',
        'shiba inu', 'samoyed'
    ]
    craw_from_bing(dogs)
