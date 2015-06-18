# -*- coding: utf-8 -*-
from data_api_client import Client
import config
import sys
import hashlib
import os
import json

class Base:

    def __init__(self):
        self.client = Client()
        self.client.init(config.token)

    def buildUrl(self, path, params):
        return path + "?" + "&".join([k+"="+v for k, v in params.items()])

    def getFromCache(self, url):
        m = hashlib.md5()
        m.update(url)
        psw = m.hexdigest()
        content = None
        try:
            content = open("/tmp/"+psw).read()
            content = json.loads(content)
        except Exception, e:
            print sys.stderr, "fail to find cache"
        return content

    def saveToCache(self, url, result):
        m = hashlib.md5()
        m.update(url)
        psw = m.hexdigest()
        content = None
        try:
            f = open("/tmp/"+psw, "w")
            f.write(json.dumps(result))
            f.close()
        except Exception, e:
            print >> sys.stderr, "fail to save cache"

    def getData(self, url, cache=True):
        if cache:
            data = self.getFromCache(url)
        else:
            data = None
        if data:
            return data
        try:
            code, result = self.client.getData(url)
            if code == 200:
                data = result
            else:
                print >> sys.stderr, code
        except Exception, e:
            # traceback.print_exc()
            raise e
        if cache:
            self.saveToCache(url, data)
        return data
