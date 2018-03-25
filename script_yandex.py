import requests
#post
xml="""<?xml version="1.0" encoding="utf-8"?>
<request>
  <query>
    test
  </query>
  <groupings>
    <groupby attr="d" mode="deep" groups-on-page="10" docs-in-group="1" />
  </groupings>
</request>"""

r = requests.post("https://yandex.com/search/xml?user=uid&key=&l10n=fr&filter=strict", data=xml)
print(r.text)

#get
url = "https://yandex.com/search/xml?user=uid&key=03&query=test&lr=10502&l10n=en&sortby=tm.order%3Dascending&filter=strict&groupby=attr%3Dd.mode%3Ddeep.group$#headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.get(url)
print(r.text)
