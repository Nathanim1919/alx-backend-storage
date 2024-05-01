#!/usr/bin/env python3
"""implementing an expiring web cache and tracker"""

import redis
import requests
from typing import Callable
from functools import wraps

red = redis.Redis()


def get_page(url: str) -> str:
    """get the HTML content of a particular URL and return it"""
    key = f"count:{url}"
    red.incr(key)
    red.expire(key, 10)
    cached = red.get(url)
    if cached:
        return cached.decode('utf-8')
    else:
        r = requests.get(url)
        red.set(url, r.text)
        return r.text
