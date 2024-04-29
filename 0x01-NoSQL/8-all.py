#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    if (mongo_collection.count() == 0):
        return []
    else:
        return list(mongo_collection.find())
