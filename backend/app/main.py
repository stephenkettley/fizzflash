from fastapi import FastAPI, Request
from app.api.router import api_router
from app.core.rate_limiter import rate_limit

app = FastAPI(title="FizzFlash API")
app.include_router(api_router)


@app.middleware("http")
async def limiter(request: Request, call_next):
    rate_limit(request)
    return await call_next(request)
