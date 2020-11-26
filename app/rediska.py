import json
from functools import wraps
from typing import Callable

from rediscluster.client import RedisCluster

from app.models import Forecast

nodes = [
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"},
    {"host": "127.0.0.1", "port": "7003"},
]
redis = RedisCluster(startup_nodes=nodes, decode_responses=True)


def cache(f: Callable[..., Forecast]):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        try:
            cached = redis[res.timestamp]
        except KeyError:
            redis[res.timestamp] = json.dumps(res.as_json())
            print('Wrote to Redis')
            return res
        print('Read from Redis')
        return Forecast(**json.loads(cached))
    return wrapper
