"""Database configuration for HEREDITARIA™ OS."""

from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    """Base declarativa para todos los modelos ORM."""


# Engine async con SQLite
engine = create_async_engine(
    "sqlite+aiosqlite:///data/hereditaria.db",
    echo=False,
)

# Session factory
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    """Crea todas las tablas definidas en los modelos."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
