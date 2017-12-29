# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:42:44 2017

@author: Rebecca Cui
"""
import time
import requests
import pandas as pd
import json
timeStamp = str(int(time.time()*1000))
#date = '20171116'
url_prefix = 'http://www.hkex.com.hk/chi/csm/DailyStat/data_tab_daily_'
def SchemaTr(dic):
    schema = dic['table']['schema'][0]
    tr = dic['table']['tr']
    tr = [d['td'][0] for d in tr]
    return schema,tr

def ToDf(Ds):
    total,top = Ds
    schema,tr = SchemaTr(total)
    df0 = pd.DataFrame(tr,index=schema,columns=['value'])
    schema,tr = SchemaTr(top)
    df1 = pd.DataFrame(tr,columns=schema)
    return (df0,df1)

def Result(date):
    url = url_prefix+date+'c.js?'+timeStamp
    r = requests.get(url)
    tabData = json.loads(r.text[10:])
    sh,hkh,sz,hks = [d['content'] for d in tabData]
    dfs = {}
    for ex in ('sh','hkh','sz','hks'):
        dfs['%s_df0'%ex],dfs['%s_df1'%ex] = ToDf(locals()[ex])
    return dfs

dfs = Result('20171115')
