
`python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ utiltools-0.0.1-py3-none-any.whl`

```python

import scraper

s = '''
   Hello here's a random number 323-4321234blah
   crap formatting 3 21318 3068 and many other features
   for example 4six1-213-fivenine83
'''

expected_nums = [
   '3234321234',
   '3213183068',
   '4612135983'
]

nums = scraper.get_all_nums(s)

assert (nums == expected_nums)

```


pip3 install pexpect


`make build; make install`

