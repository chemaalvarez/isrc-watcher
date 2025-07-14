from fastapi import FastAPI
from backend.api.routes.health import router as health_router
from backend.api.routes.isrc import router as isrc_router
from backend.config.settings import settings

app = FastAPI(title=settings.project_name)

app.include_router(health_router, prefix=f"{settings.api_prefix}/health")
app.include_router(isrc_router, prefix=f"{settings.api_prefix}/isrc")
