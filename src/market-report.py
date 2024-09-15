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

# escolhendo tema cyberpunk para os gráficos
# plt.style.use("cyberpunk")
# plotando gráfico do ibovespa
plt.plot(dados_mercado["IBOVESPA"])
# dando título para o gráfico
plt.title("IBOVESPA")
# plotar o gráfico na tela
plt.show()
# salvar a imagem do gráfico no computador
plt.savefig("ibovespa.png")

plt.plot(dados_mercado["DOLAR"])
plt.title("DOLAR")
plt.show()
plt.savefig("dolar.png")

plt.plot(dados_mercado["S&P500"])
plt.title("S&P500")
plt.show()
plt.savefig("sp500.png")
