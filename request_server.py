# -*- coding:utf-8 -*-
from base import BaseRequestHandler

STATISTICS_PAGE_API_PATH = {
    'top_stats': '/reddripETC/top_stats',
    'detect_trend': '/reddripETC/detect_trend',
    'summary': '/reddripETC/summary',
    'upload_trend': '/reddripETC/upload_trend',
}

res = {}


class StatisticsPageApi(BaseRequestHandler):
    def __init__(self, host: str = None, headers_info: dict = None, body_info: dict = None):
        super().__init__(host='127.0.0.1', headers_info=headers_info, body_info=body_info)


if __name__ == '__main__':
    for tag, url in STATISTICS_PAGE_API_PATH:
        res[tag] = StatisticsPageApi().request_get(url)
