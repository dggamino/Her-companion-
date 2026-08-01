"""Tests para el paquete her_models."""

from datetime import UTC, datetime

from her_models.core import Expediente, crear_expediente


class TestExpediente:
    """Suite de tests para el modelo Expediente."""

    def test_creacion_basica(self) -> None:
        """Un expediente se crea con los campos obligatorios."""
        exp = crear_expediente("EXP-001", "Calle Falsa 123")

        assert exp.id == "EXP-001"
        assert exp.direccion == "Calle Falsa 123"
        assert exp.observaciones is None
        assert isinstance(exp.created_at, datetime)

    def test_creacion_con_observaciones(self) -> None:
        """Un expediente puede incluir observaciones opcionales."""
        exp = crear_expediente(
            "EXP-002",
            "Avenida Siempreviva 742",
            observaciones="Revisar documentación",
        )

        assert exp.observaciones == "Revisar documentación"

    def test_resumen_sin_observaciones(self) -> None:
        """El resumen omite observaciones cuando no existen."""
        exp = Expediente(
            id="EXP-003",
            direccion="Plaza Mayor 1",
            created_at=datetime.now(UTC),
        )

        assert exp.resumen() == "[EXP-003] Plaza Mayor 1"

    def test_resumen_con_observaciones(self) -> None:
        """El resumen incluye observaciones cuando existen."""
        exp = Expediente(
            id="EXP-004",
            direccion="Gran Vía 100",
            created_at=datetime.now(UTC),
            observaciones="Urgente",
        )

        assert "Gran Vía 100" in exp.resumen()
        assert "Urgente" in exp.resumen()

    def test_inmutabilidad(self) -> None:
        """Los expedientes son inmutables (frozen dataclass)."""
        exp = crear_expediente("EXP-005", "Calle Real 50")

        try:
            exp.direccion = "Otra dirección"
            assert False, "Debería haber fallado por inmutabilidad"
        except AttributeError:
            pass  # Expected
