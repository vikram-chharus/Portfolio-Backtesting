#!/usr/bin/env python
# coding: utf-8

# In[5]:


from nsepy import get_history
import pandas as pd
from datetime import date


# In[35]:


def getRate(symbol, s_date):
    data = get_history(start=s_date, end=s_date, symbol=symbol)
    if len(data)>0:
        return data.head(1).Close[0]
    else:
        return 0


# In[39]:


def portfolio(data):
    pro = list()
    for symbol in data["symbols"]:
        initial_price = getRate(symbol, data["from_date"])
        final_price = getRate(symbol, data["to_date"])
        amount_to_buy = (data["investment_per_stock"][symbol]/data["total_investment"])*100
        pro.append({symbol: final_price*amount_to_buy - initial_price*amount_to_buy})
    
    return pro
    


# In[41]:


input_format = {
    "total_investment": 100000,
"symbols": ["SBIN", "GAIL"],
"investment_per_stock": {"SBIN":25,  "GAIL":75},
"from_date": date(2015, 1, 1),
"to_date": date(2020, 5, 1)
        }


# In[44]:
portfolio(input_format)




