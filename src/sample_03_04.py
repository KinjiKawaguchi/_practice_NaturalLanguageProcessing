import glob
import json
import urllib.parse
import scrape
import sqllitedatastore as datastore

if __name__ == '__main__':
    datastore.connect()
    values = []
    for filename in glob.glob('./data/wikipedia/*.html'):
        with open(filename,encoding="utf-8") as fin:
            html = fin.read()
            text, title = scrape.scrape(html)
            print('scraped:', title)
            url = 'http://ja.wikipedia.org/wiki/{0}'.format(
                urllib.parse.quote(title))
            values.append((text, json.dumps({'url':url,'title':title})))
    datastore.load(values)
    
    print(list(datastore.get_all_ids(limit=-1)))
    datastore.close()