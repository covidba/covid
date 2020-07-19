import unicodedata
import os
import re
import sys

from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import _pickle as pk
import datetime as dt
import pandas as pd
import numpy as np

sys.path.append("./model/main/")

def gerarTendenciaEstado(df, populacao):  
    df['date'] = pd.to_datetime(df['date'])
    from modelos import SIR, SEIR
    #Start the model with population size
    model = SIR(tamanhoPop = populacao)
    #model_seir = SEIR(tamanhoPop = populacao)
    #create a series with the cummulative number of cases
    y = df["totalCases"]
    #Give the number of days since the day of first case confirmed
    x = range(1,len(df["totalCases"]) + 1)

    try:
      model.fit(x = x, y = y)
    except:
      return 0

    #Predict the number of cases
    df["Expectativa"] = model.predict(x)

    #Projections about the future
    furtherCases = pd.DataFrame.from_dict({"date":pd.date_range(
      start = df['date'].max()+timedelta(days=1),
      end = df['date'].max()+timedelta(days=180))})

    df_proj = pd.concat([df,furtherCases])

    #create the new series to be predicted
    predictions = model.predict(df_proj)
    df_proj['Expectativa'] = predictions
    df_proj.set_index('date', inplace=True)

    content = ''
    for id, n in enumerate(df_proj['Expectativa']):
        a = "%s,%s,%s\n" % (str(df_proj.index[id])[:-9], n, df_proj['totalCases'][id])
        content += a

    b = "data,tendencia,confirmados\n"
    b += content
    return b


url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time_changesOnly.csv'
df1 = pd.read_csv(url, usecols=['date', 'country', 'state', 'city',
                                'ibgeID', 'newDeaths', 'deaths', 'newCases',
                                'totalCases', 'deaths_per_100k_inhabitants',
                                'totalCases_per_100k_inhabitants', 'deaths_by_totalCases',
                                '_source']) #, parse_dates=['data'])

lista_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 
 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 
 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 
 'SP', 'SE', 'TO']

for estado in lista_estados:
  dir = '/content/gdrive/My Drive/covid/tendencia/%s/' % estado
  if not os.path.isdir(dir):
    os.system("mkdir tendencia/%s" % estado)

ja_feitos = ["AC", "AL", "AP", "AM", "BA", "DF", "CE", "ES", "GO", "MA", "MS", "SP"]

for estado in lista_estados:
  if estado not in ja_feitos:
    print("Gerando para o estado %s..." % estado)
    a = (df1.loc[df1['state'].isin([estado])])

    lista_cidades = []
    for cidade in a['city']:
      if cidade not in lista_cidades:
        if "CASO SEM LOCALIZAÇÃO DEFINIDA" not in cidade:
          lista_cidades.append(cidade)

    cidade_pop = dict()
    city_info_url = "https://raw.githubusercontent.com/wcota/covid19br/master/cities_info.csv"
    df2 = pd.read_csv(city_info_url, usecols=['city', 'pop2019']) #, parse_dates=['data'])
    for id, cidade in enumerate (df2['city']):
        if cidade in lista_cidades:
            cidade_pop[cidade] = df2['pop2019'][id]

    for cidade in lista_cidades:
        nova = ''.join(ch for ch in unicodedata.normalize('NFKD', cidade)
        if not unicodedata.combining(ch))
        filename = '%s.csv' % nova.lower().replace(" ", "_")[:-3]
        dir = 'tendencia/%s/%s' % (estado, filename)
        ##if not os.path.isfile(dir):
        print("Gerando para a cidade %s" % cidade)
        new_df = df1.loc[df1['city'].isin([cidade]), ['date', 'totalCases']]
        a = gerarTendenciaEstado(new_df, cidade_pop[cidade])
        if a!=0:
          dir = 'tendencia/%s/%s' % (estado, filename)
          with open(dir, 'w') as f:
              f.write(a)
        #os.system("git add .")
        #os.system("git commit -m \"update tendencia\"")
        #git push origin master
