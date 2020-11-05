
## pylint: disable = invalid-name
"""
This is a script to set key in Redis Server for load testing.

Author:- OpsTree Solutions
"""
from redis.sentinel import Sentinel

import argparse
import json
import redis

def load_config(filepath):
    """For loading the connection details of Redis"""
    with open(filepath) as property_file:
        configs = json.load(property_file)
    return configs

def redis_populate(filepath):
    """Function to populate keys in Redis Server"""
    configs = load_config(filepath)
    # client = redis.StrictRedis(host=configs["redis_host"], port=configs["redis_port"])
    sentinel = Sentinel([(configs["redis_host"], configs["redis_port"])], socket_timeout=0.1)
    sentinel.discover_master('mymaster')
    client = sentinel.master_for('mymaster', socket_timeout=0.1)
    for i in range(100000):
        key='key'+str(i)
        value='value'+str(i)
        client.set(key,value)
        print(key,value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Redis Performance Testing")
    parser.add_argument("--filepath", help="Path of the Json File(Default is redis.json)")
    args = parser.parse_args()
    if args.filepath is not None:
        redis_populate(args.filepath)
