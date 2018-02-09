import pandas as pd
import glob

location = 'C:/_kopp/Dropbox/Filipe/_github/opengov-br/'
cabeca = ('data_geracao,hora_geracao,ano_eleicao,num_turno,descricao_eleicao,'
          'sigla_uf,sigla_ue,codigo_municipio,nome_municipio,num_zona,num_secao,'
          'codigo_cargo,descricao_cargo,num_votavel,qtde_votos').split(',')

for year in range(2016,1999,-2):
    print('\n'+str(year))
	
    allFiles = glob.glob(location + "tse/"+str(year)+"/votacao_*.txt")
    votacao = pd.DataFrame()
    list_    = []
    for file_ in allFiles:
        try:
            df = pd.read_csv(file_,encoding='latin1', header=None, names=cabeca, sep=';', quotechar='"')
            df['filename'] = file_
            list_.append(df)
        except:
            print(file_)
    votacao = pd.concat(list_)
    '''votacao.to_pickle(location + 'votacao_' + str(year) + '.pickle')'''
    votacao.to_csv(location + 'tse/votacao'+ str(year) + '.csv')
votacao.head()
votacao.tail()