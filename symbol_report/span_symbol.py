import os
from bs4 import BeautifulSoup

templates_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\django_proj\\djapp\\templates\\new_djapp_v2'
new_templates_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\django_proj\\djapp\\templates\\new_djapp_v3'

tem_list = os.listdir(templates_path)

for fname in tem_list:

    fpath = os.path.join(templates_path, fname)
    file = open(fpath,'rb')
    soup = BeautifulSoup(file.read(), "html.parser")

    for count, a in enumerate(soup.find_all('span')):
        try:
            if 'symbol-report' in a['class']:
                print("##############################################################")
                print("##############################################################")
                print("##############################################################")
                print(a['class'])
                a['class'].remove('symbol-report')
                #print(a['class'].remove('symbol-report'))
                print(a['class'])
                print(count)

        except:
            pass
    
    new_djapp_source_path = os.path.join(new_templates_path, fname)
    with open(new_djapp_source_path, "w", encoding="utf-8") as file:
        file.write(str(soup))