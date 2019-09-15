#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:01:30 2019

@author: manzars
"""
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
url = "http://www.the-bca.com/index.php/member-companies"

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")

divs = soup.findAll('div', {'class': 'entrieslist_details'})
links = []
for div in divs:
    links.append(urljoin(url ,div.a.attrs['href']))

file = open('assignment.csv', 'w')
header = "Company Name, Email, Telephone, Contact Person, Website\n"
file.write(header)
for link in links:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'lxml')
    div = soup.findAll('div', {'class': 'dtls_content'})
    try:
        web = div[-1].a.attrs['href']
    except:
        web = 'NaN'
        
    try:
        name = div[0].text.replace('\r', '').replace('\n', '').replace('\t', '')
    except:
        name = 'NaN'
        
    try:
        email = div[3].text.replace('\r', '').replace('\n', '').replace('\t', '')
    except:
        email = 'NaN'
        
    try:
        tel =  div[2].text.replace('\r', '').replace('\n', '').replace('\t', '')
    except:
        tel = 'NaN'
        
    try:
        con_per_name = div[1].text.replace('\r', '').replace('\n', '').replace('\t', '')
    except:
        con_per_name = 'NaN'
    
    file.write(name.replace(',', '') + ', ' + email.replace(',', '') + ', ' + tel.replace(',', '') + ', ' + con_per_name.replace(',', '') + ', ' + web.replace(',', '') + '\n')
    print(name)
file.close()