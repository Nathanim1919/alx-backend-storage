#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """List all documents in a collection
    Args:
        mongo_collection: Collection object
    Returns: List of documents or empty list
    """
    if (mongo_collection.count() == 0):
        return []
    else:
        return mongo_collection.find()
