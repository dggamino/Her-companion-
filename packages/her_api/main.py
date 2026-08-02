"""FastAPI application for HEREDITARIA™ OS."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from her_api.routers.agentes import router as agentes_router
from her_api.routers.expedientes import router as expedientes_router
from her_api.routers.webhooks import router as webhooks_router
from her_api.schemas import HealthResponse
from her_core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Lifespan context manager for startup/shutdown events."""
    await init_db()
    yield


app = FastAPI(
    title="HEREDITARIA™ OS API",
    description="Sistema operativo de bienestar inmobiliario",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="ok", version="0.1.0")


app.include_router(expedientes_router)
app.include_router(agentes_router)
app.include_router(webhooks_router)
