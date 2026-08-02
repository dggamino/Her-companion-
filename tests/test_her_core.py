"""Tests para el paquete her_core (ORM + persistencia)."""

from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from her_core.database import Base
from her_core.models import Expediente


@pytest.fixture
async def db_session():
    """Sesión de base de datos en memoria para tests."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

    await engine.dispose()


class TestExpedienteORM:
    """Suite de tests para el modelo Expediente ORM."""

    async def test_creacion_y_persistencia(self, db_session: AsyncSession) -> None:
        """Un expediente se crea y persiste en la base de datos."""
        exp = Expediente(
            id="EXP-ORM-001",
            direccion="Calle Falsa 123",
            created_at=datetime.now(UTC),
        )
        db_session.add(exp)
        await db_session.commit()

        result = await db_session.get(Expediente, "EXP-ORM-001")
        assert result is not None
        assert result.id == "EXP-ORM-001"
        assert result.direccion == "Calle Falsa 123"
        assert result.observaciones is None

    async def test_creacion_con_observaciones(self, db_session: AsyncSession) -> None:
        """Un expediente puede incluir observaciones opcionales."""
        exp = Expediente(
            id="EXP-ORM-002",
            direccion="Avenida Siempreviva 742",
            created_at=datetime.now(UTC),
            observaciones="Revisar documentación",
        )
        db_session.add(exp)
        await db_session.commit()

        result = await db_session.get(Expediente, "EXP-ORM-002")
        assert result is not None
        assert result.observaciones == "Revisar documentación"

    async def test_resumen(self, db_session: AsyncSession) -> None:
        """El método resumen funciona correctamente."""
        exp = Expediente(
            id="EXP-ORM-003",
            direccion="Plaza Mayor 1",
            created_at=datetime.now(UTC),
        )
        db_session.add(exp)
        await db_session.commit()

        result = await db_session.get(Expediente, "EXP-ORM-003")
        assert result is not None
        assert result.resumen() == "[EXP-ORM-003] Plaza Mayor 1 (nuevo)"

    async def test_resumen_con_observaciones(self, db_session: AsyncSession) -> None:
        """El resumen incluye observaciones cuando existen."""
        exp = Expediente(
            id="EXP-ORM-004",
            direccion="Gran Vía 100",
            created_at=datetime.now(UTC),
            observaciones="Urgente",
        )
        db_session.add(exp)
        await db_session.commit()

        result = await db_session.get(Expediente, "EXP-ORM-004")
        assert result is not None
        assert "Gran Vía 100" in result.resumen()
        assert "Urgente" in result.resumen()
