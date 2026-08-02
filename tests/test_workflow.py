"""Tests para el servicio de workflow."""

import pytest

pytest.importorskip("sqlalchemy")

from datetime import UTC, datetime

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from her_api.services.workflow import TransicionInvalidaError, asignar_agente, cambiar_estado
from her_core.database import Base
from her_core.models import Agente, EstadoExpediente, Expediente


@pytest.fixture
async def db_session():
    """Sesión de base de datos en memoria para tests."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    test_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with test_session() as session:
        yield session
    await engine.dispose()


class TestCambiarEstado:
    """Tests para transiciones de estado de expediente."""

    async def test_nuevo_a_en_proceso(self, db_session: AsyncSession) -> None:
        """Nuevo -> en_proceso es válido."""
        exp = Expediente(
            id="EXP-WF-001",
            direccion="Calle 1",
            created_at=datetime.now(UTC),
        )
        db_session.add(exp)
        await db_session.commit()

        result = await cambiar_estado(db_session, exp, EstadoExpediente.EN_PROCESO.value)
        assert result.estado == EstadoExpediente.EN_PROCESO.value

    async def test_nuevo_a_archivado(self, db_session: AsyncSession) -> None:
        """Nuevo -> archivado es válido."""
        exp = Expediente(
            id="EXP-WF-002",
            direccion="Calle 2",
            created_at=datetime.now(UTC),
        )
        db_session.add(exp)
        await db_session.commit()

        result = await cambiar_estado(db_session, exp, EstadoExpediente.ARCHIVADO.value)
        assert result.estado == EstadoExpediente.ARCHIVADO.value

    async def test_transicion_invalida(self, db_session: AsyncSession) -> None:
        """Cerrado -> nuevo es inválido."""
        exp = Expediente(
            id="EXP-WF-003",
            direccion="Calle 3",
            created_at=datetime.now(UTC),
            estado=EstadoExpediente.CERRADO.value,
        )
        db_session.add(exp)
        await db_session.commit()

        with pytest.raises(TransicionInvalidaError):
            await cambiar_estado(db_session, exp, EstadoExpediente.NUEVO.value)

    async def test_archivado_no_transita(self, db_session: AsyncSession) -> None:
        """Archivado no puede transitar a ningún estado."""
        exp = Expediente(
            id="EXP-WF-004",
            direccion="Calle 4",
            created_at=datetime.now(UTC),
            estado=EstadoExpediente.ARCHIVADO.value,
        )
        db_session.add(exp)
        await db_session.commit()

        with pytest.raises(TransicionInvalidaError):
            await cambiar_estado(db_session, exp, EstadoExpediente.EN_PROCESO.value)


class TestAsignarAgente:
    """Tests para asignación de agentes."""

    async def test_asignar_agente(self, db_session: AsyncSession) -> None:
        """Se puede asignar un agente a un expediente."""
        agente = Agente(
            id="AG-001",
            nombre="Juan Pérez",
            created_at=datetime.now(UTC),
        )
        exp = Expediente(
            id="EXP-WF-005",
            direccion="Calle 5",
            created_at=datetime.now(UTC),
        )
        db_session.add(agente)
        db_session.add(exp)
        await db_session.commit()

        result = await asignar_agente(db_session, exp, "AG-001")
        assert result.agente_id == "AG-001"
