import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# import mplcyberpunk
import win32com.client as win32

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

# cálcular retornos diários
# colocando em porcentagem
retornos_diarios = dados_mercado.pct_change()
retorno_dolar = retornos_diarios["DOLAR"].iloc[-1]
retorno_ibovespa = retornos_diarios["IBOVESPA"].iloc[-1]
retorno_sp = retornos_diarios["S&P500"].iloc[-1]

# covertendo em porcentagem
retorno_dolar = str(round(retorno_dolar * 100, 2)) + "%"
retorno_ibovespa = str(round(retorno_ibovespa * 100, 2)) + "%"
retorno_sp = str(round(retorno_sp * 100, 2)) + "%"

# enviar os dados por e-mail
# abrir aplicação de e-mail do outlook
outlook = win32.Dispatch("outlook.application")
# criar e-mail
email = outlook.CreateItem(0)
# configurar e-mail que será enviado
email.To = "fernando_berbel@msn.com"
email.Subject = "Relatório de Mercado"
email.Body = f''' Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibovespa}.
* O Dólar teve o retorno de {retorno_dolar}.
* O S&P500 teve o retorno de {retorno_sp}.

Segue em anexo a peformance dos ativos nos últimos 6 meses.

Att,
Melhor estagiário do mundo
'''
# inserindo os anexos
# separando os arquivos
anexo_ibovespa = r"C:\Users\Fernando\Documents\Development\Varos\Aulas\Projeto 1\relatório-automatizado-de-mercado\src\ibovespa.png"
anexo_dolar = r"C:\Users\Fernando\Documents\Development\Varos\Aulas\Projeto 1\relatório-automatizado-de-mercado\src\dolar.png"
anexo_sp = r"C:\Users\Fernando\Documents\Development\Varos\Aulas\Projeto 1\relatório-automatizado-de-mercado\src\sp500.png"
# adicionando os anexos
email.Attachments.Add(anexo_ibovespa)
email.Attachments.Add(anexo_dolar)
email.Attachments.Add(anexo_sp)
# enviar e-mail
email.Send()
