import pandas

dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
currency = dfs[0]
currency = currency.ix[:,0:5]
currency.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']
currency[u'幣別'] = currency[u'幣別'].str.extract('(\w*)\s(\w*)')
print(currency)
currency.to_excel('currency.xlsx')