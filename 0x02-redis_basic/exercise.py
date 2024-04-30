#!/usr/bin/env python3
"""writing strings to Redis"""

import uuid
import redis


class Cache:
    def __init__(self) -> None:
        """Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
