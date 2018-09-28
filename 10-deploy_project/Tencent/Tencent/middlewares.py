# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    """"""
    def __init__(self):
        self.user_agent = UserAgent()

    def process_request(self, request, spider):
        """"""
        user_agent = self.user_agent.random
        request.headers["User-Agent"] = user_agent

        


