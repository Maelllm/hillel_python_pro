import functools
import requests

from pprint import pprint

try:
    max_limit = int(input('Enter cache size '))  # We can put cache size in function, but i want to set it from start
except:
    max_limit = 2

# Put cache in global for saving results
deco_cache = {}
deco_cache_names = []
deco_cache_counter = []


def cache(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        global max_limit, deco_cache, deco_cache_names, deco_cache_counter
        cache_key = (args, tuple(kwargs.items()))
        if cache_key in deco_cache:
            deco_cache_counter[deco_cache_names.index(cache_key)] += 1
            return deco_cache[cache_key]
        result = function(*args, **kwargs)
        # pop-ing cache values if reached limit
        if len(deco_cache) >= max_limit:
            # remove least used element
            required_index = deco_cache_counter.index(min(deco_cache_counter))
            deco_cache.pop(deco_cache_names[required_index])
            deco_cache_names.pop(required_index)
            deco_cache_counter.pop(required_index)
        deco_cache[cache_key] = result
        deco_cache_names.append(cache_key)
        deco_cache_counter.append(1)
        return result

    return wrapper


@cache
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


# Some examples
fetch_url('https://dnipro.ithillel.ua/')
fetch_url('https://dnipro.ithillel.ua/')
fetch_url('https://www.google.com/')
fetch_url('https://www.google.com/')
fetch_url('https://www.ukr.net/')
fetch_url('https://www.ukr.net/')
fetch_url('https://dnipro.ithillel.ua/')
fetch_url('https://www.google.com/')
fetch_url('https://dnipro.ithillel.ua/')
fetch_url('https://dnipro.ithillel.ua/')

# Display cache
pprint(deco_cache)
