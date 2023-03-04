import os
import pandas as pd
from urllib.parse import urljoin, urlparse

html_source_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\Eng-2-Hindi\\Hindi_source\\html'
urls_dataframe_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\scrapper\\urls_dataframe.csv'
urls_map_path = 'C:\\Users\\DmitryL\\ClassCentral_Test\\links_map'

html_names_list = os.listdir(html_source_path)
urls_dataframe = pd.read_csv(urls_dataframe_path,index_col=None)
urls_map_dataframe = pd.DataFrame(columns = ['index', 'full_path', 'relative_path', 'file_name'])

for file_name in html_names_list:

    frame = urls_dataframe.loc[urls_dataframe['file_name']==file_name]

    full_url = frame['full_path'].tolist()[0]

    if urlparse(full_url).netloc == 'www.classcentral.com':
        relative_path = full_url.split(urlparse(full_url).netloc)[1]
    else:
        relative_path = full_url

    count = len(urls_map_dataframe)

    urls_map_dataframe.loc[count] = [
        file_name.split('.')[0],
        full_url,
        relative_path,
        file_name
    ]

    print(urls_map_dataframe.loc[count].tolist())

urls_map_dataframe.to_csv('urls_map.csv', index=False)

print(html_names_list)
print(urls_dataframe)