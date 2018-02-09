import urllib.request
from bs4 import BeautifulSoup

url = 'http://idg.receita.fazenda.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-abertos-do-cnpj'
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content.decode('utf-8','ignore'),'html.parser')
table = soup.find("table", attrs = {'class' : 'plain'})
for a in table.find_all('a', href=True):
    link=a['href']
    uf = link[-2:]
    f = open("./opengov-br/cnpj_" + uf + ".txt","w+")
    g = open("./opengov-br/socio_" + uf + ".txt","w+")
    print("downloading data from " + uf + ": " + link)
    response = urllib.request.urlopen(link).readlines()
    for line in response:
        try:
            line = str(line.strip().decode('latin1'))
            if line[0:2] == '01':
                f.write("uf:"+uf+";cnpj:" + line[2:16]+";razao:" + line[16:]+"\n")
            if line[0:2] == '02':
                g.write("uf:"+uf+";cnpj:" + line[2:16]+";tipo:" + line[16:17]+";cpf:" + line[17:31].strip() +";quadro:" + line[31:33]+";nome:" + line[33:].strip()+"\n")
        except:
            print(line)
    f.close()
    g.close()
print("fim")
## ended in 2700 seconds
