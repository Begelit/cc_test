from django.urls import path
from . import views
import os
import pandas as pd
from urllib.parse import urljoin, urlparse

urls_map_df = pd.read_csv('urls_map.csv')

relative_urls_list =  [x.replace(' ', '') for x in urls_map_df['relative_path'].tolist()]

new_rel_list = list()

for link in relative_urls_list:
    if len(urlparse(link).netloc) < 1:
        if link[0] == '/':
            link = link[1:]
        if len(link) == 0:
            link = ''
        elif link[len(link)-1] != '/':
            link += '/'
            
        new_rel_list+=[link]

#print(new_rel_list)

urlpatterns = list()

for link in new_rel_list:
    urlpatterns.append(path(link, views.requests_processing))
'''
urlpatterns = [
    path('', views.requests_processing),
    #path('', views.home_page),
    #path('commandsrec/', views.commands_page),
]
'''