import os
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

sources_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\Eng-2-Hindi\\Hindi_source\\html'
new_html_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\exchange_href\\html\\main.html'

urls_map = pd.read_csv('C:\\Users\\DmitryL\\ClassCentral_Test\\links_map\\urls_map.csv')

source_file_path = os.path.join(sources_path, '0.html')
file = open(source_file_path,'rb')
soup = BeautifulSoup(file.read(), "html.parser")

print(urls_map)

#urls_list = urls_map['full_path'].tolist()
urls_list = [x.replace(' ', '') for x in urls_map['full_path'].tolist()]
relative_urls_list =  [x.replace(' ', '') for x in urls_map['relative_path'].tolist()]
print(urls_list)
#print(urls_map['full_path'].tolist())
false_count = 0

for count, a in enumerate(soup.find_all('a', href=True)):
    if len(urlparse(a['href']).netloc) == 0:
        full_url = urljoin('https://www.classcentral.com/', a['href'])
        print(count, "Found the URL:", a['href'])
        relative_url = a['href'].replace(' ', '')
        print(relative_url.replace(' ','') in relative_urls_list)
        if relative_url.replace(' ','') not in relative_urls_list:
            false_count+=1
        else:
            a['href'] = relative_url.replace(' ','')
    elif urlparse(a['href']).netloc == 'www.classcentral.com':
        full_url = a['href']
        relative_url = full_url.split('www.classcentral.com')[1].replace(' ', '')
        print(count, "Found the URL:", a['href'])
        print(relative_url.replace(' ','') in relative_urls_list)
        if relative_url.replace(' ','') not in relative_urls_list:
            false_count+=1
        else:
            a['href'] = relative_url.replace(' ','')
    else:
        full_url = a['href']
        print(count, "Found the URL:", a['href'])
        print(full_url.replace(' ','') in urls_list)
        if full_url.replace(' ','') not in urls_list:
            false_count+=1

print(false_count)
with open(new_html_path, "w", encoding="utf-8") as file:
    file.write(str(soup))


