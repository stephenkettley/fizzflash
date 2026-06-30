import json
from app.core.redis import redis_client


def set_cache(key: str, value, ttl: int = 60):
    redis_client.setex(key, ttl, json.dumps(value))


def get_cache(key: str):
    data = redis_client.get(key)
    if data is None:
        return None
    return json.loads(data)


def delete_cache(key: str):
    redis_client.delete(key)
