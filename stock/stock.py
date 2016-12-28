# -*- coding: utf-8 -*-

from prettytable import PrettyTable
#import csv

def parseFile(id):
    dataList = []
    dataDict = {}

    stockFile = {}

    if id == '510300':
        stockFile['name'] = '沪深300ETF'
        stockFile['file'] = '510300.txt'
    elif id == '159915':
        stockFile['name'] = '创业板'
        stockFile['file'] = '159915.txt'
    elif id == '159902':
        stockFile['name'] = '中小板'
        stockFile['file'] = '159902.txt'
    elif id == '510050':
        stockFile['name'] = '上证50ETF'
        stockFile['file'] = '510050.txt'
    elif id == '159901':
        stockFile['name'] = '深证100ETF'
        stockFile['file'] = '159901.txt'

    if not stockFile.has_key('file'):
        return;

    print id, stockFile['name'], stockFile['file']

    fo = open(stockFile['file'], 'r')

    lines = fo.readlines()
    for line in lines:
        items = line.split()
        if len(items) == 4:
            item = {}
            item2 = {}

            item['date'] = items[0]
            item['value1'] = items[1]
            item['value2'] = items[2]
            item['rate'] = items[3]

            item2['value1'] = items[1]
            item2['value2'] = items[2]
            item2['rate'] = items[3]

            dataList.append(item)
            dataDict[items[0]] = item2

    fo.close()

    return dataList, dataDict


def concatDate(y, m ,d):
    dateStr = str(y)
    dateStr += '-'

    if m < 10:
        dateStr += ('0' + str(m))
    else:
        dateStr += str(m)

    dateStr += '-'

    if d < 10:
        dateStr += ('0' + str(d))
    else:
        dateStr += str(d)

    return dateStr


def calculate(startY, startM, endY, endM, date, money, fee, dataDict, verbose=True):
    years = []
    for yy in range(startY+1, endY):
        years.append(yy)

    dates = []
    for dd in range(date, 32):
        dates.append(dd)
    for dd in range(date-1, 0, -1):
        dates.append(dd)

    used = 0
    quantity = 0
    value = 1

    if verbose:
        tableY = PrettyTable(["DATE", "EARN$", "EARN RATE", "$", "FEE", "#", "TOTAL#", "CURRENT$", "USED$"])

    # 1st year
    for mm in range(startM, 13):
        for dd in dates:
            dateStr = concatDate(startY, mm, dd)
            if dataDict.has_key(dateStr):
                item = dataDict[dateStr]
                value = float(item['value2'])
                earn = (quantity * value) - used - fee

                earnRate = 0
                if used > 0:
                    earnRate = earn / used

                num = (money - fee) / value
                quantity += num
                used += money
                if verbose:
                    tableY.add_row([dateStr, earn, earnRate, money, fee, num, quantity, quantity*value, used])
                    #print dateStr, "收益:", earn, "收益率", earnRate, "本期买入:", money, "手续费:", fee, "买入份额:", num, "总份额:", quantity, "市值:", quantity*value, "总投入:", used
                break;

    # full year
    for yy in years:
        for mm in range(1, 13):
            for dd in dates:
                dateStr = concatDate(yy, mm, dd)
                if dataDict.has_key(dateStr):
                    item = dataDict[dateStr]
                    value = float(item['value2'])
                    earn = (quantity * value) - used - fee

                    earnRate = 0
                    if used > 0:
                        earnRate = earn / used

                    num = (money - fee) / value
                    quantity += num
                    used += money
                    if verbose:
                        tableY.add_row([dateStr, earn, earnRate, money, fee, num, quantity, quantity * value, used])
                        #print dateStr, "收益:", earn, "收益率", earnRate, "本期买入:", money, "手续费:", fee, "买入份额:", num, "总份额:", quantity, "市值", quantity*value, "总投入:", used
                    break;

    # last year
    for mm in range(1, endM+1):
        for dd in dates:
            dateStr = concatDate(endY, mm, dd)
            if dataDict.has_key(dateStr):
                item = dataDict[dateStr]
                value = float(item['value2'])
                earn = (quantity * value) - used - fee

                earnRate = 0
                if used > 0:
                    earnRate = earn / used

                num = (money - fee) / value
                quantity += num
                used += money
                if verbose:
                    tableY.add_row([dateStr, earn, earnRate, money, fee, num, quantity, quantity * value, used])
                    #print dateStr, "收益:", earn, "收益率", earnRate, "本期买入:", money, "手续费:", fee, "买入份额:", num, "总份额:", quantity, "市值", quantity*value, "总投入:", used
                break;

    if used is 0:
        return 0, 0, 0, 0

    if verbose:
        print tableY

    return used, quantity, value, (quantity*value-5-used)/used


stockIds = ['159901', '159902', '159915', '510050', '510300']
periods = [{'startY': 2004, 'startM': 1, 'endY': 2009, 'endM': 12, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2004, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2010, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2011, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2012, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2013, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2014, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2015, 'startM': 1, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2015, 'startM': 6, 'endY': 2016, 'endM': 2, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True},
          {'startY': 2015, 'startM': 6, 'endY': 2016, 'endM': 10, 'date': 25, 'money': 2000, 'fee': 5, 'verbose': True}]

for id in stockIds:
    dataList, dataDict = parseFile(id)

    tableX = PrettyTable(["FROM", "TO", "DATE", "$", "FEE", "TOTAL$", "#", "VALUE", "EARN RATE"])

    for period in periods:
        startY = period['startY']
        startM = period['startM']
        endY = period['endY']
        endM = period['endM']
        date = period['date']
        money = period['money']
        fee = period['fee']
        verbose = period['verbose']

        tableX.align["FROM"] = "l"  # Left align
        tableX.align["TO"] = "l"  # Left align

        used, quantity, value, earnRate = calculate(startY, startM, endY, endM, date, money, fee, dataDict, verbose)

        tableX.add_row([str(startY)+"-"+str(startM), str(endY)+"-"+str(endM), date, money, fee, used, quantity, value, earnRate])
        #print startY, "-", startM, "~", endY, "-", endM, "定投日:",date, "定投金额:", money, "手续费:", fee, "总花费:", used, "份额:", quantity, "净值:", value, "收益率:", earnRate

    print tableX
    print




