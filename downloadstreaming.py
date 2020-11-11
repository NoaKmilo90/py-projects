import requests
import time
print('Pega el link del streaming')
print('p.ej http://media.ohc.cu/habanaradio')
url = input()
print('Indroduce el intervalo de grabación en minutos')
interval = int(input())
r = requests.get(url, stream=True)
with open('streaming7.mp3', 'wb') as f:
    try:
        for block in r.iter_content(1024):
            f.write(block)
    except KeyboardInterrupt:
        pass
print('Listo')
input('Para terminar pulse Intro')
quit()