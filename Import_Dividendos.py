## Importando informações de Dividendos das Ações listadas na B3
# Criado por: Higor Silva Rodrigues

import yfinance as yf
import pandas as pd
import investpy as inv

# Importando as ações Brasileiras
acoes_br = inv.stocks.get_stocks(country='brazil')

acoes = []
for a in acoes_br['symbol']:
    if len(a)<=5:
        acoes.append(a+'.SA')

# Baixando as Informações de Dividendos
for a in acoes:
    dividendos = yf.Ticker(a)
    dividendos = pd.DataFrame(dividendos.dividends)
    dividendos['Ticker']=a
    try:
        dividendos['Dividends'] = round(dividendos['Dividends'].astype('float64'),2)
        dividendos['Dividends'] = dividendos['Dividends'].apply(lambda x: str(x).replace(".",","))
    except:
        print(f'Erro ao importar os dividendos de - {a}')

    dividendos.to_csv(f'Dividendos - {a}.csv',encoding="utf-8",sep=';')    
   

