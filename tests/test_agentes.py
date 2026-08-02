"""Tests de integración para CRUD de agentes."""

import pytest

pytest.importorskip("fastapi")

from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from her_api.main import app
from her_core.database import Base
from her_core.models import Agente


@pytest.fixture
def client():
    """Cliente HTTP síncrono para tests de FastAPI."""
    return TestClient(app)


@pytest.fixture
async def db_session():
    """Sesión de base de datos en memoria para tests de agentes."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    test_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async def override_get_db():
        async with test_session() as session:
            yield session

    from her_api.routers.agentes import get_db
    from her_api.routers.expedientes import get_db as get_db_exp
    from her_api.routers.webhooks import get_db as get_db_web

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_db_exp] = override_get_db
    app.dependency_overrides[get_db_web] = override_get_db

    async with test_session() as session:
        yield session

    app.dependency_overrides.clear()
    await engine.dispose()


class TestAgentesAPI:
    """Tests para endpoints CRUD de agentes."""

    def test_crear_agente(self, client: TestClient, db_session: AsyncSession) -> None:
        """Se puede crear un agente via API."""
        response = client.post(
            "/api/v1/agentes",
            json={
                "id": "AG-API-001",
                "nombre": "María García",
                "telefono": "34612345678",
                "email": "maria@example.com",
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["id"] == "AG-API-001"
        assert data["nombre"] == "María García"

    def test_obtener_agente(self, client: TestClient, db_session: AsyncSession) -> None:
        """Se puede obtener un agente por ID."""
        import asyncio

        async def create():
            agente = Agente(
                id="AG-API-002",
                nombre="Carlos López",
                created_at=datetime.now(UTC),
            )
            db_session.add(agente)
            await db_session.commit()

        asyncio.run(create())

        response = client.get("/api/v1/agentes/AG-API-002")
        assert response.status_code == 200
        data = response.json()
        assert data["nombre"] == "Carlos López"

    def test_obtener_agente_no_existe(self, client: TestClient, db_session: AsyncSession) -> None:
        """Obtener agente inexistente devuelve 404."""
        response = client.get("/api/v1/agentes/NO-EXISTE")
        assert response.status_code == 404

    def test_listar_agentes(self, client: TestClient, db_session: AsyncSession) -> None:
        """Se pueden listar todos los agentes."""
        import asyncio

        async def create():
            for i in range(2):
                agente = Agente(
                    id=f"AG-API-LIST-{i}",
                    nombre=f"Agente {i}",
                    created_at=datetime.now(UTC),
                )
                db_session.add(agente)
            await db_session.commit()

        asyncio.run(create())

        response = client.get("/api/v1/agentes")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
