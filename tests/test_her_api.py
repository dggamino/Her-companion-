"""Tests de integración para la API FastAPI."""

import pytest

pytest.importorskip("fastapi")

from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from her_api.main import app
from her_core.database import Base
from her_core.models import Expediente


@pytest.fixture
def client():
    """Cliente HTTP síncrono para tests de FastAPI."""
    return TestClient(app)


@pytest.fixture
async def db_session():
    """Sesión de base de datos en memoria para tests de API."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    test_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async def override_get_db():
        async with test_session() as session:
            yield session

    from her_api.routers.expedientes import get_db

    app.dependency_overrides[get_db] = override_get_db

    async with test_session() as session:
        yield session

    app.dependency_overrides.clear()
    await engine.dispose()


class TestHealth:
    """Tests para el endpoint de health check."""

    def test_health(self, client: TestClient) -> None:
        """El endpoint health responde correctamente."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["version"] == "0.1.0"


class TestExpedientesAPI:
    """Tests para endpoints CRUD de expedientes."""

    def test_crear_expediente(self, client: TestClient, db_session: AsyncSession) -> None:
        """Se puede crear un expediente via API."""
        response = client.post(
            "/api/v1/expedientes",
            json={
                "id": "EXP-API-001",
                "direccion": "Calle API 123",
                "observaciones": "Creado via API",
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["id"] == "EXP-API-001"
        assert data["direccion"] == "Calle API 123"

    def test_obtener_expediente(self, client: TestClient, db_session: AsyncSession) -> None:
        """Se puede obtener un expediente por ID."""
        import asyncio

        async def create():
            exp = Expediente(
                id="EXP-API-002",
                direccion="Avenida API 456",
                created_at=datetime.now(UTC),
            )
            db_session.add(exp)
            await db_session.commit()

        asyncio.run(create())

        response = client.get("/api/v1/expedientes/EXP-API-002")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "EXP-API-002"
        assert data["direccion"] == "Avenida API 456"

    def test_obtener_expediente_no_existe(self, client: TestClient, db_session: AsyncSession) -> None:
        """Obtener expediente inexistente devuelve 404."""
        response = client.get("/api/v1/expedientes/NO-EXISTE")
        assert response.status_code == 404

    def test_listar_expedientes(self, client: TestClient, db_session: AsyncSession) -> None:
        """Se pueden listar todos los expedientes."""
        import asyncio

        async def create():
            for i in range(2):
                exp = Expediente(
                    id=f"EXP-API-LIST-{i}",
                    direccion=f"Direccion {i}",
                    created_at=datetime.now(UTC),
                )
                db_session.add(exp)
            await db_session.commit()

        asyncio.run(create())

        response = client.get("/api/v1/expedientes")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
