#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:16:43

# noinspection PyPackageRequirements
import chardet
import requests
from requests import HTTPError

from ..http.response import Response


# noinspection PyMethodMayBeStatic
class Download(object):
    """发送请求, 并获取响应报文, 并分解数据"""

    def send_request(self, request):
        if request.method.upper() == "GET":
            rv = requests.get(
                url=request.url,
                headers=request.headers,
                params=request.params,
                proxies=request.proxy
            )

        elif request.method.upper() == "post":
            rv = requests.get(
                url=request.url,
                headers=request.headers,
                params=request.params,
                proxiex=request.proxy,
                data=request.formdata
            )
        else:
            raise HTTPError("Not Support {} method".format(request.method))
        rv.encoding = chardet.detect(rv.content)["encoding"]
        return Response(
            url=rv.url,
            content=rv.content,
            headers=rv.headers,
            encoding=rv.encoding,
            status_code=rv.status_code
        )
