import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# import mplcyberpunk

tickers = ["^BVSP", "^GSPC", "BRL=X"]

# pegar as cotações
dados_mercado = yf.download(tickers, period="6mo")
# pegar apenas os valores de fechamento do mercado
dados_mercado = dados_mercado["Adj Close"]
# tratar os dados eliminando dados faltantes
dados_mercado = dados_mercado.dropna()
# renomear as colunas
dados_mercado.columns = ["DOLAR", "IBOVESPA", "S&P500"]

dados_mercado
