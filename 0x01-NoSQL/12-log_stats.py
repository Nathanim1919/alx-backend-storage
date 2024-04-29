#!/usr/bin/env python3
"""Log stats"""


from pymongo import MongoClient


def log_stats():
    """Log stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    total = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    path = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
