# -*- coding: utf-8 -*-

import pandas as pd
import requests	

url = 'http://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sz'

data = {'__VIEWSTATE':'fHhS9rwB5VPvB+OJNgDnkSByE+QaaFa2V8SELVHBJbU+/iVFv6m5ragtTnOcxxxF8xzoTBqkEcuxFLyir1Prvw8xBh3MVOdrbBYs1ZI8DGLah+KqHX3CQEL2oqGAcpIbIKYiw0wIR8Q8rTq2w2zrFygE1sYDu/hSK1dpDybw6UvUYv+/2PgZjr6Jo73MpztyaLTeZA==',
         '__VIEWSTATEGENERATOR':'EC4ACD6F',
         '__EVENTVALIDATION':'cpCMp0Ziz3TWq+YwsDL/7fj6Mc//QOm5JdJlVLzGvK66drteJbleVtsq/KceDqyEHryaYa5L7L0eL69IfdIzamvwkPTLxmVoZnUtzvi1pmJF9k2z8RQarvFuJHp5WXuFKNlCfE2/Cu+SQSrwxxCzgEUXIy21l918D67y+nNyY29npTK5aJKRHoY6IpIpHms9KmzNL9HNR6RnEouZ88Pi8H/QMV3k3fvu1Vng2DFIPc0Z2rZwMlkzNQxKJ6DqVpjNGuYndBoeNerwHV0oEHL8ESO4rPx3PZXjWyJD4A0PhmXYU6/vPjAufy9uV8iPw7CpRMRMhPUar7Q2AphvHtMXrF5o11QBSgQzWVFNp743vgJaLuI3bm0MSZ6DhVV2B1DpxMUYQ0d9r06V1YIoXu0DTbQWcv6cud/EVD4UiBhrrFd5bi0j+DdDtPNOS2uFY9Lhx4Tfr4UHNR708aqn2Zn/8mNcIxZe11c/PXOoBvwEI6PuoZlSY29t2sRtVCi7GRTXYIssW35eRX1GYVgRFKtrkPnC81VqnD79L77HHVA4l8ctaYOP0Ctd/O1QEPQEcEJ0X4obWxUC5PNRBVthHz7k2JcBxY82xLUEeR0r2t5w6bV6tGB04a8npXV/SLCDnSKuBRahYDaLLMdDDOnbBDEAxaOolBZOQyfdMAugvNAYKO1Zz9yz6t+XC5nTBESd9Fc643YEoo1bvMENFZnYSCOfXhqytUAe1yfjQzBO/uh1QC+Vdlg9fpk51xS1oXWG6re7ZQc3zKUURUvyvMNxAvorGYIrfcUhqy+DhUshks4X9kaRegwQOnbqvIIJrfciCd97pI0MT5OH/+Nw5Y02sBtLcYZyxyV86jRyX5fVVrjU5kLTc8WZFCOrXjZ1DXDU12ozuLbzZdlh1crnDAdwzAuP5W1D5bKPREC7Zax8w5proRQJkTvzkTVYOMgkcPZjjhbrjerwKV1NRj9gSjQ8NvsWlvmowMNPiO9nYnLioOpda0B4Tdnjk4Lbd6lU3ZF4ZA3d8nv1bQqNqE9oIKBQomdwL078AkTLSUBapDYxQqqrjRBkR+YVgSCBjxBhr+Tokh1dddTnh8M/kUBkMMtJn8zfcih3X8coNXZbKT5vLjs4+DNL6Ckm/+vzJg3PWd/hI4LWs2+i47NyW5fzcpQyvLDBy7hiYr8=',
         'today':'20171128',
         'sortBy':'',
         'alertMsg':'',
         'ddlShareholdingDay':'16',
         'ddlShareholdingMonth':'10',
         'ddlShareholdingYear':'2017',
         'btnSearch.x':'34',
         'btnSearch.y':'9'}
header_info = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'Cache-Control':'max-age=0',
               'Connection':'keep-alive',
               'Content-Length':'1657',
               'Content-Type':'application/x-www-form-urlencoded',
               'Cookie':'TS0161f2e5=01412592762cdcbb87ac4e9c311547cf543977172891dc13efef3d8dcedfe3aaf6cc6b0526',
               'Host':'www.hkexnews.hk',
               'Origin':'http://www.hkexnews.hk',
               'Referer':'http://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sz',
               'Upgrade-Insecure-Requests':'1',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        



dates = pd.date_range('2017-3-17','2017-11-27')

def get_table(data):
    r = requests.post(url, headers = header_info,data=data)
    table = pd.read_html(r.text,attrs={'class':'result-table'},header=0)
    df = table[0]
    df = df.drop(index=0)
    return df   
def select_date(date):
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)
    data['ddlShareholdingDay'] = day
    data['ddlShareholdingMonth'] = month
    df = get_table(data)
    return df   
#df = select_date(dates[0])

df_list = [select_date(date) for date in dates]
