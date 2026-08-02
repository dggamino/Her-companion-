"""FastAPI application for HEREDITARIA™ OS."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from her_api.routers.expedientes import router as expedientes_router
from her_api.schemas import HealthResponse
from her_core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
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
