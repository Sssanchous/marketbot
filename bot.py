import requests
import json

key = "0ZOhGE1B47jm79qcL624pr3xHI6O81Q"
name = input("Введите название предмета из стима")

def price_f4():
    url = 'https://market.csgo.com/api/v2/search-item-by-hash-name-specific?key='+key+'&hash_name='+name
    
    gun = requests.get(url+' (Factory New)').json()
    price = gun["data"]
    
    try:
        print("Цена по предмета (Прямо с завода)")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
        print("Цена пятого лота: ",  str(price[4]["price"])  .replace(' ', '')[:-2])
        print("Цена шестого лота: ",  str(price[5]["price"])  .replace(' ', '')[:-2])
    except IndexError:
        print("нет предмета")

    gun = requests.get(url+' (Minimal Wear)').json()
    price = gun["data"]

    try:
        print(".")
        print("Цена по предмета (Немного поношенное )")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
        print("Цена пятого лота: ",  str(price[4]["price"])  .replace(' ', '')[:-2])
        print("Цена шестого лота: ",  str(price[5]["price"])  .replace(' ', '')[:-2])
        print(".")
    except IndexError:
        print("нет предмета")

    gun = requests.get(url+" (Well-Worn)").json()
    price = gun["data"]

    try:
        print("Цена по предмета (Немного поношенное )")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
        print("Цена пятого лота: ",  str(price[4]["price"])  .replace(' ', '')[:-2])
        print("Цена шестого лота: ",  str(price[5]["price"])  .replace(' ', '')[:-2])
        print(".")
    except IndexError:
        print("нет предмета")

    

    
    
    


price_f4()
