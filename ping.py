import requests
import time
key = 'key from market api'
def pinging():
    while True:
        1==1 
        url = 'https://market.csgo.com/api/v2/ping?key='+key
        ping = requests.get(url).json()
        print(ping['success'])
        if ping['success'] == False:
            print(ping)
        time.sleep(150)

pinging() 
        
