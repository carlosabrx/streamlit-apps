import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App

Shown are the stock's opening, closing, and volume prices for SPCE!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'SPCE'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1w', start='2019-11-30', end='2021-01-07')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Open Price""")
st.line_chart(tickerDf.Open)
st.write("""
## Close Price""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price""")
st.line_chart(tickerDf.Volume)
