# -*- coding: utf-8 -*-
from base import Base
import config


class Stock(Base):

    def getMktEqud(self, **kwargs):
        path = "/api/market/getMktEqud.json"
        params = {}
        params["secID"] = kwargs["secID"] if "secID" in kwargs else ""
        params["ticker"] = kwargs["ticker"] if "ticker" in kwargs else ""
        params["tradeDate"] = kwargs["tradeDate"] if "tradeDate" in kwargs else ""
        params["beginDate"] = kwargs["beginDate"] if "beginDate" in kwargs else ""
        params["endDate"] = kwargs["endDate"] if "endDate" in kwargs else ""
        params["field"] = kwargs["field"] if "field" in kwargs else ""
        url = self.buildUrl(path, params)
        return self.getData(url, False)

    def getMktBlockd(self, **kwargs):
        path = "/api/market/getMktBlockd.json"
        params = {}
        params["secID"] = kwargs["secID"] if "secID" in kwargs else ""
        params["ticker"] = kwargs["ticker"] if "ticker" in kwargs else ""
        params["tradeDate"] = kwargs["tradeDate"] if "tradeDate" in kwargs else ""
        params["beginDate"] = kwargs["beginDate"] if "beginDate" in kwargs else ""
        params["endDate"] = kwargs["endDate"] if "endDate" in kwargs else ""
        params["field"] = kwargs["field"] if "field" in kwargs else ""
        params["assetClass"] = kwargs["assetClass"] if "assetClass" in kwargs else ""
        url = self.buildUrl(path, params)
        return self.getData(url, False)

    def getBarRTIntraDay(self, **kwargs):
        path = "/market/getBarRTIntraDay.json"
        params = {}
        params["securityID"] = kwargs["securityID"] if "securityID" in kwargs else ""
        params["startTime"] = kwargs["startTime"] if "startTime" in kwargs else ""
        params["endTime"] = kwargs["endTime"] if "endTime" in kwargs else ""
        params["unit"] = "1"
        url = self.buildUrl(path, params)
        return self.getData(url, False)
