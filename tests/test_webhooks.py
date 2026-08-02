"""Tests de integración para webhooks WAHA."""

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
    """Sesión de base de datos en memoria para tests de webhook."""
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


class TestWebhookWaha:
    """Tests para el webhook de WAHA."""

    def test_webhook_crear_expediente(self, client: TestClient, db_session: AsyncSession) -> None:
        """Un mensaje de WAHA crea un nuevo expediente."""
        response = client.post(
            "/api/v1/webhooks/waha",
            json={
                "event": "message",
                "session": "default",
                "payload": {
                    "from": "34612345678@c.us",
                    "body": "Hola, quiero información sobre una propiedad",
                    "type": "chat",
                },
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["expediente_id"] == "WA-34612345678"

    def test_webhook_actualizar_expediente(
        self, client: TestClient, db_session: AsyncSession
    ) -> None:
        """Un segundo mensaje del mismo número actualiza el expediente."""
        import asyncio

        async def create():
            exp = Expediente(
                id="WA-34699999999",
                direccion="Contacto WhatsApp: 34699999999",
                observaciones="Mensaje previo",
                created_at=datetime.now(UTC),
            )
            db_session.add(exp)
            await db_session.commit()

        asyncio.run(create())

        response = client.post(
            "/api/v1/webhooks/waha",
            json={
                "event": "message",
                "session": "default",
                "payload": {
                    "from": "34699999999@c.us",
                    "body": "Nueva consulta sobre la misma propiedad",
                    "type": "chat",
                },
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_webhook_datos_incompletos(self, client: TestClient, db_session: AsyncSession) -> None:
        """Payload sin teléfono o mensaje devuelve 400."""
        response = client.post(
            "/api/v1/webhooks/waha",
            json={
                "event": "message",
                "payload": {"from": "", "body": ""},
            },
        )
        assert response.status_code == 400

    def test_webhook_payload_invalido(self, client: TestClient, db_session: AsyncSession) -> None:
        """Payload que no es JSON válido devuelve 400/422."""
        response = client.post(
            "/api/v1/webhooks/waha",
            data="no es json",
        )
        assert response.status_code in (400, 422)
