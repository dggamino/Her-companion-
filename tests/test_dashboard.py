"""Tests de endpoints de dashboard."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_dashboard_estados(client: AsyncClient):
    """GET /api/v1/dashboard/estados retorna conteo por estado."""
    response = await client.get("/api/v1/dashboard/estados")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_dashboard_agentes(client: AsyncClient):
    """GET /api/v1/dashboard/agentes retorna conteo por agente."""
    response = await client.get("/api/v1/dashboard/agentes")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_dashboard_metricas(client: AsyncClient):
    """GET /api/v1/dashboard/metricas retorna métricas."""
    response = await client.get("/api/v1/dashboard/metricas")
    assert response.status_code == 200
    data = response.json()
    assert "total_expedientes" in data
    assert "creados_hoy" in data
    assert "cerrados_este_mes" in data
