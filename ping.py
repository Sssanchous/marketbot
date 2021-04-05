import requests
import time
key = 'x36gQXE48Slzsnt2sR1meOZ9HMqRUA5'
def pinging():
    while True:
        1==1 
        urlsvin = 'https://market.csgo.com/api/v2/ping?key='+key
        ping = requests.get(urlsvin).json()
        print(ping['success'])
        if ping['success'] == False:
            print(ping)
        time.sleep(150)

pinging() 
        
