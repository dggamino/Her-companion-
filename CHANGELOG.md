# Changelog

Todos los cambios notables de este proyecto se documentan en este
archivo, siguiendo el formato [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y [Versionado Semántico](https://semver.org/lang/es/).

Este archivo es obligatorio por HER-STD-0001, Criterio 10 —
Auditabilidad.

## [Unreleased]

### Fixed
- `.gitignore` excluía `logs/*.log` sin excepción, impidiendo
  versionar `logs/SPRINT-001-validation.log` pese a ser evidencia
  requerida por HER-STD-0001, Criterio 10 (Auditabilidad). Se añadió
  excepción `!logs/*-validation.log`.

## [0.1.0] — 2026-07-31

### Added
- Estructura inicial del repositorio HEREDITARIA-OS.
- `README.md` con descripción del proyecto y principio de gobierno.
- `PROJECT_STATE.md` con estado del Sprint 001.
- `install.sh` y `termux_setup.sh` para bootstrap en Android + Termux.
- `requirements.txt` inicial (sin dependencias, placeholder).
- `knowledge/README.md` describiendo la Base de Conocimiento
  Patrimonial y su relación con la Ontología y el Glosario.
- `scripts/update.sh` para actualización del repositorio local.
- `.gitignore` compatible con Python, Termux y datos sensibles
  (HER-STD-0001, Criterio 9).
- `LICENSE` propietaria.
- Árbol de directorios de gobierno (`governance/`) y demás carpetas
  base del sistema.

### Governance
- Cierre formal de la fase Architecture & Governance
  (Resolución AR-2026-07-31-001).
- Adopción de HER-ADR-0000 (Repository as Product, v1.1).
- Adopción de HER-STD-0001 (Repository Contract, v1.0, 10 criterios).
- Adopción de HER-STD-0002 (Sprint Freeze Rule).
