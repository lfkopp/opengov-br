### obtain data from http://www.tse.jus.br/partidos/filiacao-partidaria/relacao-de-filiados

import urllib.request
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

url = 'http://filiaweb.tse.jus.br/filiaweb/portal/relacoesFiliados.xhtml'
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content.decode('utf-8','ignore'),'html.parser')
partidos = soup.find("select", {"id":"partido"})
ufs = soup.find("select", {"id":"uf"})
for uf in ufs.find_all('option', value=True):
    uf = uf['value']
    for partido in partidos.find_all('option', value=True):
        partido = partido['value']
        link = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_'+partido+'_'+uf+'.zip'
        with urlopen(link) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                for name in zfile.namelist():
                    if "filiados_" in name:
                        zfile.extract(name,'./opengov-br')
        #break
    #break
print("fim")
## ended in 1478 seconds
