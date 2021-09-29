# -*- coding:utf-8 -*-
import requests


class RequestHeaders(object):
    def __init__(self, content: dict):
        self.content = content

    def as_headers(self):
        return self.content


class RequestBody(object):
    def __init__(self, body_info: dict):
        self.body_info = body_info

    def as_body(self):
        return self.body_info


class BaseRequestHandler(object):
    def __init__(self, host, headers_info=None, body_info=None):
        self.host = host
        self.headers_info = headers_info
        self.body_info = body_info

    def _make_request_headers(self):
        """构造请求头"""
        if self.headers_info:
            headers_object = RequestHeaders(self.headers_info)
            headers = headers_object.as_headers()
        else:
            headers = {'Content-Type': 'application/json'}
        return headers

    def _make_request_body(self):
        """构造请求体"""
        if self.body_info:
            body_object = RequestBody(self.body_info)
            body = body_object.as_body()
        else:
            body = {}
        return body

    def _request(self, request_url, request_method='GET'):
        """发送请求"""
        url = self.host + request_url
        request_body = self._make_request_body()
        headers = self._make_request_headers()
        retry_times = 0
        while retry_times <= 3:
            try:
                if request_method == 'GET':
                    response = getattr(requests, 'get')(url=url, params=request_body, headers=headers)
                elif request_method == 'POST':
                    response = getattr(requests, 'post')(url=url, json=request_body, headers=headers)
                break
            except Exception as e:
                print(e)
                retry_times += 1
        return response

    @staticmethod
    def _handler_res(res):
        """处理返回结果"""
        res_data = res.json()
        return res_data

    def request_get(self, url):
        return self._request(url, request_method='GET')

    def request_post(self, url):
        return self._request(url, request_method='POST')
