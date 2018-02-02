from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

url ='http://arquivos.portaldatransparencia.gov.br/PortalTransparenciaEscolheTipoDePlanilha.asp?origem=Servidores&Planilha=0&fechar=1'
'''response = urllib.request.urlopen(url).readlines()
for line in response:
    print(line)
    break'''

with  urlopen(url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        for name in zfile.namelist():
            zfile.extract(name,'./opengov-br')

# ended in 211 seconds

#Cadastro de Empresas Inidôneas e Suspensas (CEIS)
#http://www.portaldatransparencia.gov.br/downloads/snapshot.asp?c=CEIS#get
#http://arquivos.portaldatransparencia.gov.br/downloads.asp?a=2018&m=01&d=05&consulta=CEIS
