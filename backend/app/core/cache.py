import json
from app.core.redis import redis_client


def set_cache(key: str, value, ttl: int = 60):
    redis_client.setex(key, ttl, json.dumps(value))


def get_cache(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def delete_cache(key: str):
    redis_client.delete(key)
