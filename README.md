urbandict.py
============

An extremely simple interface to get Urban Dictionary definitions.

Installing
-----------
`python3 setup.py install`

API
---
`urbandict.define(term)`

Attempts to retrieve the definition of `term`. If no definitions were found, will return `None`. Else, will return a dict containing the following keys:
* `tags`: The tags Urban Dictionary associated with `term`.
* `definitions`: A list of definitions, each item a dict containing the following keys:
   - `id`: Definition ID.
   - `term`: The defined term. May be corrected for capitalization or otherwise.
   - `author`: Username of definition author.
   - `definition`: Definition text.
   - `up`: Amount of 'thumb ups' this definition received.
   - `down`: Amount of 'thumb downs' this definition received.
   - `score`: The amount of 'thumb ups' minus the amount of 'thumb downs'.
   - `link`: An HTTP permalink to the definition.


`urbandict.random()`

Return a random definition for a random term. See layout of a single `definitions` item from `urbandict.define()` as described above for return value.

Example
-------
````python
import urbandict

defs = urbandict.define('tsundere')
if defs:
    print('"Tsundere" means:')
    for i, defn in enumerate(defs['definitions']):
         print('{i}: {defn}'.format(i=i, defn=defn['definition']))  # 1. Tsundere is a slang born on the Internet, and it is a word to describe the nature...

defn = urbandict.random()
if defn:
    print('"{term}" means: {definition}'.format(**defn))  # "Big Swingin' Dick" means: Well-endowed - typically used by swingers looking for men with huge cocks!"
````

License
-------
urbandict.py is licensed under the WTFPL; see `LICENSE` for details.
