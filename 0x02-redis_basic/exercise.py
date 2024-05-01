#!/usr/bin/env python3
"""writing strings to Redis"""

import uuid
import redis
from typing import Any, Union
from functools import wraps


def count_calls(method: callable) -> callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: callable) -> callable:
    inputKey = method.__qualname__ + ':inputs'
    outputKey = method.__qualname__ + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        for arg in args:
            self._redis.rpush(inputKey, arg)
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputKey, result)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = lambda x: x) -> Any:
        """get data from redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data)

    def get_str(self, data) -> str:
        """convert bytes to str"""
        return data.decode('utf-8')

    def get_int(self, data) -> int:
        """convert bytes to int"""
        return int.from_bytes(data, byteorder='big')
