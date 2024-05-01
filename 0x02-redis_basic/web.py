#!/usr/bin/env python3
"""implementing an expiring web cache and tracker"""

import redis
import requests
from typing import Callable
from functools import wraps


def track_get_page(fn: Callable) -> Callable:
    """track the number of times a URL is called"""
    @wraps(fn)
    def wrapper(url):
        """wrapper function"""
        client = redis.Redis()
        client.incr(f"count:{url}")
        cached_html = client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = fn(url)
        client.set(f'{url}', html, 10)
        return html
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """get page"""
    return requests.get(url).text
