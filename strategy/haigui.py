# -*- coding: utf-8 -*-
import numpy as np
import operator

start = datetime(2011, 1, 1)
end = datetime(2015, 5, 25)
benchmark = 'HS300'
universe = set_universe('HS300')
capital_base = 100000

pos_pieces = 10
enter_window = 20
exit_window = 10
N = 4


def initialize(account):
    account.postion_size_hold = {}
    for stk in universe:
        account.postion_size_hold[stk] = 0


def handle_data(account):
    highest_price = account.get_attribute_history('highPrice', enter_window)
    lowest_price = account.get_attribute_history('lowPrice', exit_window)
    close_price = account.get_attribute_history('closePrice', exit_window)
    turnover_vol = account.get_attribute_history('turnoverVol', enter_window)
    for stock in account.universe:
        cnt_price = close_price[stock][-1]  # account.referencePrice[stock]
        cnt_turnover = turnover_vol[stock][-1]
        if cnt_price > highest_price[stock][:-1].max() and cnt_turnover > turnover_vol[stock][:-1].max() and account.postion_size_hold[stock] < N:
            order_to(stock, capital_base / pos_pieces / cnt_price / N)
            account.postion_size_hold[stock] += 1
        elif cnt_price < lowest_price[stock][:-1].min():
            order_to(stock, 0)
            account.postion_size_hold[stock] = 0
