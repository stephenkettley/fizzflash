from fastapi import Request, HTTPException
from app.core.redis import redis_client

RATE_LIMITS = {
    "/skills": 60,
    "/subdomains": 60,
    "/flashcards": 120,
    "/ai/flashcards": 10,
    "default": 100,
}


def get_limit(path: str):
    for key in RATE_LIMITS:
        if key in path:
            return RATE_LIMITS[key]
    return RATE_LIMITS["default"]


def rate_limit(request: Request):
    ip = request.client.host
    path = request.url.path

    limit = get_limit(path)

    key = f"rl:{ip}:{path}"

    current = redis_client.get(key)

    if current is None:
        redis_client.setex(key, 60, 1)
        return

    current = int(current)

    if current >= limit:
        raise HTTPException(status_code=429, detail="Too many requests")

    redis_client.incr(key)
