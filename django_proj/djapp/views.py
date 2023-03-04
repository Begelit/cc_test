from django.shortcuts import render
import pandas as pd
from urllib.parse import urljoin, urlparse

urls_map_df = pd.read_csv('urls_map.csv')

#relative_urls_list =  [x.replace(' ', '') for x in urls_map_df['relative_path'].tolist()]

#new_rel_list = list()

for index, frame in urls_map_df.iterrows():
    relative_path = frame['relative_path'].replace(' ', '')
    urls_map_df.loc[index,'relative_path'] = urls_map_df.loc[index,'relative_path'].replace(' ', '')
    if len(urlparse(relative_path).netloc) < 1:
        if relative_path[len(relative_path)-1] != '/':
            #frame['relative_path'] = frame['relative_path'] + '/'
            urls_map_df.loc[index,'relative_path'] = relative_path + '/'
            #print(frame['relative_path'])
        #else:
            
    urls_map_df.loc[index,'relative_path']
print(urls_map_df)

# Create your views here.
def requests_processing(request):
    global urls_map_df
    #print('req',request.get_full_path())
    df_row = urls_map_df.loc[urls_map_df['relative_path'] == request.get_full_path()]
    file_name = df_row['file_name'].item()
    return render(request, 'new_djapp_v3/'+file_name)