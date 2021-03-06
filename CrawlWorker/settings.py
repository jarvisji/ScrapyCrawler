# -*- coding: utf-8 -*-

# Scrapy settings for CrawlWorker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CrawlWorker'

SPIDER_MODULES = ['CrawlWorker.spiders']
NEWSPIDER_MODULE = 'CrawlWorker.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CrawlWorker (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'CrawlWorker.pipelines.FeedWriterPipeline': 200,
    'CrawlWorker.pipelines.ContentWriterPipeline': 210,
}

DOWNLOAD_DELAY = 1