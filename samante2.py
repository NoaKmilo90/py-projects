import feedparser
import requests


podcast = feedparser.parse('https://fapi-top.prisasd.com/podcast/playser/nadie_sabe_nada/itunestfp/podcast.xml')

titulo = podcast.entries[0].title

desc = podcast.entries[0].description

arch = podcast.entries[0].link

audio = requests.get(arch)

with requests.get(arch) as r:
    with open('samante.mp3', 'w') as f:
        f.write(r.content)

print(titulo)
print(desc)
print(arch)