from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
kaynak=urllib.request.urlopen('https://www.basketball-reference.com/friv/injuries.fcgi').read()

sayfa=BeautifulSoup(kaynak,'lxml')

for sakatliklar in sayfa.findAll('td'):
        print("--------------------")
        print(sakatliklar.get_text('td',{'class':'data-append-csv','data-stat':'csk'}))
        
        
        
        
