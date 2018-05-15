import plotly as py
import plotly.graph_objs as go

import pandas_datareader as web
from datetime import datetime

df1 = web.DataReader("aapl", 'morningstar').reset_index()

appl = go.Candlestick(name="appl", x=df1.Date,
                       open=df1.Open,
                       high=df1.High,
                       low=df1.Low,
                       close=df1.Close
)

df2 = web.DataReader("ibm", 'morningstar').reset_index()
ibm = go.Candlestick(name="ibm", 
                        x=df2.Date,
                       open=df2.Open,
                       high=df2.High,
                       low=df2.Low,
                       close=df2.Close,
                       increasing=dict(line=dict(color= '#17BECF')),
                       decreasing=dict(line=dict(color= '#7F7F7F')) 
)

df3 = web.DataReader("googl", 'morningstar').reset_index()
googl = go.Candlestick(name="googl",
                       x=df3.Date,
                       open=df3.Open,
                       high=df3.High,
                       low=df3.Low,
                       close=df3.Close,
                       increasing=dict(line=dict(color= '#575E5F')),
                       decreasing=dict(line=dict(color= '#9F9F9F')) 
)

data = [appl, ibm, googl]
fig=dict(data=data, layout=dict(autosize=True))
py.offline.plot(fig, filename='simple_candlestick.html')