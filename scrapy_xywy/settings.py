# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_xywy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_xywy'

SPIDER_MODULES = ['scrapy_xywy.spiders']
NEWSPIDER_MODULE = 'scrapy_xywy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_xywy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
CONCURRENT_REQUESTS = 100
LOG_LEVEL = 'INFO'
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
REDIRECT_ENABLED = False
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_xywy.middlewares.ScrapyXywySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_xywy.middlewares.RotateUserAgentMiddleware': 543,
    # 'scrapy_xywy.middlewares.ProxyMiddleware': 500,
    'scrapy_xywy.downloadermiddleware.useragent.UserAgentMiddleware': None,  # 禁掉默认用户中间件
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_xywy.pipelines.QuestionPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
]

PROXIES = [
    {'ip_port': '121.40.108.76:80', 'user_pass': ''},
    {'ip_port': '115.231.111.160:3128', 'user_pass': ''},
    # {'ip_port': '120.9.81.61:8118', 'user_pass': ''},
    # {'ip_port': '124.152.80.237:80', 'user_pass': ''},
    # {'ip_port': '124.88.67.20:80', 'user_pass': ''},
    # {'ip_port': '221.216.94.77:808', 'user_pass': ''},
    # {'ip_port': '115.29.2.139:80', 'user_pass': ''},
    # {'ip_port': '124.88.67.24:80', 'user_pass': ''},
    # {'ip_port': '123.173.81.99:80', 'user_pass': ''},
    # {'ip_port': '183.78.183.156:82', 'user_pass': ''},
    # {'ip_port': '171.36.25.125:8123', 'user_pass': ''},
    # {'ip_port': '101.53.101.172:9999', 'user_pass': ''},
    # {'ip_port': '180.76.154.5:8888', 'user_pass': ''},
    # {'ip_port': '120.52.72.57:80', 'user_pass': ''},
    # {'ip_port': '111.161.126.106:80', 'user_pass': ''},
    # {'ip_port': '182.92.150.236:3128', 'user_pass': ''},
    # {'ip_port': '117.177.250.146:8080', 'user_pass': ''},
    # {'ip_port': '117.36.198.55:3128', 'user_pass': ''},
    # {'ip_port': '120.52.72.46:80', 'user_pass': ''},
    # {'ip_port': '1.197.14.102:8000', 'user_pass': ''},
    # {'ip_port': '124.206.133.227:80', 'user_pass': ''},
    # {'ip_port': '58.22.86.44:8000', 'user_pass': ''},
    # {'ip_port': '202.108.23.247:80', 'user_pass': ''},
    # {'ip_port': '60.191.180.38:3128', 'user_pass': ''},
    # {'ip_port': '120.52.72.72:80', 'user_pass': ''},
    # {'ip_port': '120.52.72.68:80', 'user_pass': ''},
    # {'ip_port': '117.177.250.147:83', 'user_pass': ''},
    # {'ip_port': '120.52.72.83:80', 'user_pass': ''},
    # {'ip_port': '113.195.243.86:9000', 'user_pass': ''},
    # {'ip_port': '223.100.98.44:8000', 'user_pass': ''},
    # {'ip_port': '221.206.72.203:8000', 'user_pass': ''},
    # {'ip_port': '223.100.98.44:8000', 'user_pass': ''},
    # {'ip_port': '180.175.163.154:8118', 'user_pass': ''},
    # {'ip_port': '202.100.167.170:80', 'user_pass': ''},
    # {'ip_port': '118.193.234.141:8080', 'user_pass': ''},
    # {'ip_port': '60.191.153.75:3128', 'user_pass': ''},
    # {'ip_port': '121.69.29.6:8118', 'user_pass': ''},
    # {'ip_port': '117.177.250.153:86', 'user_pass': ''},
    # {'ip_port': '60.191.158.211:3128', 'user_pass': ''},
    # {'ip_port': '', 'user_pass': ''},
    # {'ip_port': '', 'user_pass': ''},
]