import functools
import requests


def cache(function):
    @functools.wraps(function)
    def deco(*args, **kwargs):
        cache_key = (args, tuple(kwargs.items()))
        if cache_key in deco._cache:
            deco._cache_counter[deco._cache_names.index(cache_key)] += 1
            return deco._cache[cache_key]
        result = function(*args, **kwargs)
        # pop-ing cache values if reached limit
        if len(deco._cache) >= max_limit:
            # remove least used element
            required_index = deco._cache_counter.index(min(deco._cache_counter))
            deco._cache.pop(deco._cache_names[required_index])
            deco._cache_names.pop(required_index)
            deco._cache_counter.pop(required_index)
        deco._cache[cache_key] = result
        deco._cache_names.append(cache_key)
        deco._cache_counter.append(1)

        return result

    try:
        max_limit = int(input('Enter cache size '))
    except:
        max_limit = 2

    deco._cache = {}
    deco._cache_names = []
    deco._cache_counter = []

    return deco


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
