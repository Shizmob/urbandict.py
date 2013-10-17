# urbandict.py
# Simple interface to Urban Dictionary.
import requests

API_BASE = 'http://api.urbandictionary.com/v0/'

def define(term):
    try:
        res = requests.get(API_BASE + 'define', params={'term': term}).json()
    except:
        return None
    
    if res['results_type'] == 'no_results':
        return None

    return {
        'tags': res['tags'],
        'definitions': [{
            'id': item['defid'],
            'term': item['word']
            'definition': item['definition'],
            'author': item['author'],
            'up': item['thumbs_up'],
            'down': item['thumbs_down'],
            'score': item['thumbs_up'] - item['thumbs_down'],
            'link': item['permalink']
        } for item in res['list']]
    }

