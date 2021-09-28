# -*- coding:utf-8 -*-
import requests


class BaseRequestHandler(object):
    def __init__(self, host):
        self.host = host
        # 默认请求头
        self.headers = {'Content-Type': 'application/json'}

    def _make_request_headers(self, request_url, request_method, request_body):
        """构造请求头"""
        headers = {}
        # 添加请求头信息
        self.headers.update(headers)

    @staticmethod
    def _make_request_body(start_time, end_time, **kwargs):
        request_body = {
            'start_time': start_time,
            'end_time': end_time,
        }
        if kwargs:
            request_body.update(kwargs)
        return request_body

    @staticmethod
    def _handler_res(res):
        """处理返回结果"""
        code = res.status_code
        if code == 200:
            return res.json()
        elif code == 400:
            print('do something')
        else:
            print('do something')

    def _request(self, request_url, params, request_method='GET'):
        """发送请求"""
        url = self.host + request_url
        request_body = self._make_request_body(**params)
        self._make_request_headers(request_url, request_method='GET', request_body=request_body)

        try:
            response = getattr(requests, request_method.lower())(url=url, json=request_body, headers=self.headers)
        except Exception as e:
            print(e)
        return self._handler_res(response)

    def request_get(self, url, params):
        return self._request(url, params, request_method='GET')

    def request_post(self, url, params):
        return self._request(url, params, request_method='POST')

    def get_top_stats_data(self, doc):
        """获取TOP统计数据"""
        url = '/reddripETC/top_stats'
        return self.request_get(url, doc)

    def get_summary_data(self, doc):
        """获取概要统计信息"""
        url = '/reddripETC/summary'
        return self.request_get(url, doc)

    def get_detect_trend_data(self, doc):
        """获取检测结果趋势"""
        url = '/reddripETC/detect_trend'
        return self.request_get(url, doc)

    def get_upload_trend_data(self, doc):
        """获取邮件投递趋势"""
        url = '/reddripETC/upload_trend'
        return self.request_get(url, doc)
