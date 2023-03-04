import os
from bs4 import BeautifulSoup
import googletrans

templates_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\django_proj\\djapp\\templates\\new_djapp'
new_templates_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\django_proj\\djapp\\templates\\new_djapp_v2'

tem_list = os.listdir(templates_path)

str_hindi = googletrans.Translator().translate('Search courses and more…', src='english', dest='hindi').text

for index, fname in enumerate(tem_list):

    fpath = os.path.join(templates_path, fname)
    file = open(fpath,'rb')
    soup = BeautifulSoup(file.read(), "html.parser")

    for count, a in enumerate(soup.find_all('input')):
        try:
            if 'search-input__input' in a['class']:
                a['placeholder'] = str_hindi
                print(index, a)
        except:
            pass
    new_djapp_source_path = os.path.join(new_templates_path, fname)
    with open(new_djapp_source_path, "w", encoding="utf-8") as file:
        file.write(str(soup))