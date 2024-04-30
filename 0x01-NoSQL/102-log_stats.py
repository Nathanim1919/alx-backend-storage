#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


def log_stats():
    """Log stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    mongo_collection = client.logs.nginx
    print(f"{mongo_collection.estimated_document_count()} logs")
    print("Methods:")
    print(f"\tmethod GET: {mongo_collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {mongo_collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {mongo_collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {mongo_collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {mongo_collection.count_documents({'method': 'DELETE'})}")
    print(f"{mongo_collection.count_documents({'method': 'GET', 'path': '/status'})} status check")
    print("IPs:")
    ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == "__main__":
    log_stats()
