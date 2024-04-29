#!/usr/bin/env python3
""" Update topics """


def update_topics(mongo_collection, name, topics):
    """ Update topics """
    return mongo_collection.update(
        {"name": name}, {"$set": {"topics": topics}}
    )
