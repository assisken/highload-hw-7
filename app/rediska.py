import json
from functools import wraps
from typing import Callable

from rediscluster.client import RedisCluster

from app.models import Forecast

nodes = [
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"},
    {"host": "127.0.0.1", "port": "7003"},
    {"host": "127.0.0.1", "port": "7004"},
    {"host": "127.0.0.1", "port": "7005"},
    {"host": "127.0.0.1", "port": "7006"},
]
redis = RedisCluster(startup_nodes=nodes, decode_responses=True)


def save(f: Callable[..., Forecast]):
    @wraps(f)
    def wrapper(*args, **kwargs):
        timestamp = kwargs.get('timestamp', None)
        res = f(*args, **kwargs)
        if timestamp is None:
            return res

        redis[timestamp] = json.dumps(res.as_json())
        print('Wrote to Redis')
        return res
    return wrapper


def cache(f: Callable[..., Forecast]):
    @wraps(f)
    def wrapper(*args, **kwargs):
        timestamp = kwargs.get('timestamp', None)
        if timestamp is None:
            return f(*args, **kwargs)
        try:
            cached = redis[timestamp]
        except KeyError:
            res = f(*args, **kwargs)
            redis[timestamp] = json.dumps(res.as_json())
            print('Wrote to Redis')
            return res
        print('Read from Redis')
        return Forecast(**json.loads(cached))
    return wrapper
