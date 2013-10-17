# urbandict.py
# Simple interface to Urban Dictionary.
import requests

API_BASE = 'http://api.urbandictionary.com/v0/'

def define(term):
    """ Get definitions for `term`. """
    try:
        res = requests.get(API_BASE + 'define', params={'term': term}).json()
    except:
        return None
    
    if res['result_type'] == 'no_results':
        return None

    return {
        'tags': res['tags'],
        'definitions': [ parse_definition(item) for item in res['list'] ]
    }

def random():
    """ Get a random definition for a random term. """
    import random

    try:
        res = requests.get(API_BASE + 'random').json()
    except:
        return None

    return parse_definition(random.choice(res['list']))


def parse_definition(item):
    return {
        'id': item['defid'],
        'term': item['word'],
        'definition': item['definition'],
        'author': item['author'],
        'up': item['thumbs_up'],
        'down': item['thumbs_down'],
        'score': item['thumbs_up'] - item['thumbs_down'],
        'link': item['permalink']
    } 
