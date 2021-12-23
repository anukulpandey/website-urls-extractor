import requests
from bs4 import BeautifulSoup
from colors import *
from colorama import Fore

banner="""
   __  ______  __         __  __            __           
  / / / / __ \/ /        / / / /_  ______  / /____  _____
 / / / / /_/ / /  ______/ /_/ / / / / __ \/ __/ _ \/ ___/
/ /_/ / _, _/ /__/_____/ __  / /_/ / / / / /_/  __/ /    
\____/_/ |_/_____/    /_/ /_/\__,_/_/ /_/\__/\___/_/     
                                                         v 1.0.0
                                                         https://github.com/anukulpandey
"""

print(Fore.YELLOW+banner)

urls=[]
def url_grabber(url):
    html_doc=requests.get(url)._content
    soup = BeautifulSoup(html_doc, 'html.parser')
    for i in soup.find_all('a'):
        try:
            checked_url=url_checker(url,i['href'])
            yellow(f'{checked_url}')
            print()
            if checked_url not in urls:
                urls.append(checked_url)
        except Exception as e:
            pass

def url_checker(host,endpoint):
    if endpoint [0]=='w' or endpoint[0]=='h':
        return endpoint
    elif endpoint[0]=='/':
        return host+endpoint
    else:
        return host

def depth(n):
    for i in range(n+1):
        for u in range(urls.__len__()):
            url_grabber(urls[u])
