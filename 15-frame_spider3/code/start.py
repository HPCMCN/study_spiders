#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 16:03:20
# from myscrapy.http.request import Request
from myscrapy.core.engine import Engine
#
Engine().start()
# import redis
# import pickle


# def save_url(url):
#     pickle.dumps(Request(url))
#
#
# redis_client = redis.Redis(db=1)
#
# fp1 = "sssssssssssssssssssssssssss"
# fp2 = "sssssssssssssssssssssssssss"
# fp3 = "ssssssssssssssssssssssssss1"
#
# redis_client.rpop("request_queue")
# print redis_client.sadd("fingerprint", fp1)
# print redis_client.sismember("fingerprint", fp2)
# print redis_client.sismember("fingerprint", fp3)