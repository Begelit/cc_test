from bs4 import BeautifulSoup, Comment
import googletrans
import os
from multiprocess import Pool

sources_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\Eng-2-Hindi\\source\\html'
hindi_sources_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\Eng-2-Hindi\\Hindi_source\\html'

def translator(html_name):
    global sources_path
    global hindi_sources_path
    source_file_path = os.path.join(sources_path, html_name)
    file = open(source_file_path,'rb')
    soup = BeautifulSoup(file.read(), "html.parser")

    print(html_name, 'START')

    for e in soup.find_all(text=True):
        if e.parent.name != 'script' and e.parent.name != 'style' and not isinstance(e, Comment) and e.string != 'html' and len(e.string) > 1:
            print(html_name)
            print(e.string)
            transtr = googletrans.Translator().translate(e.string, src='english', dest='hindi').text#.pronunciation#.text
            print(transtr)
            e.string.replace_with(transtr)
        
    print(html_name, 'END')

    hindi_sources_file_path = os.path.join(hindi_sources_path, html_name)
    with open(hindi_sources_file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))

if __name__ == '__main__':

    sources_list = os.listdir(sources_path)
    hindi_sources_list = os.listdir(hindi_sources_path)

    sources_set = set(sources_list)
    hindi_sources_set = set(hindi_sources_list)

    difference_list = list(sources_set.difference(hindi_sources_set))

    print(difference_list)

    with Pool(2) as p:
        p.map(translator, difference_list)
