# -*- coding: utf-8 -*-
from api.stock import Stock

if __name__ == "__main__":
    stock = Stock()
    result = stock.getMktEqud(ticker="600836", beginDate="20150615")
    print result
    # result = stock.getBarRTIntraDay(securityID="600836.XSHG", startTime="09:00", endTime="11:30")
    # print result
    # result = stock.getMktBlockd(tradeDate="20150616")
    # print result