# PROJECT_STATE

Última actualización: 2026-07-31
Sprint activo: SPRINT 001
Estado general: Execution Mode

## Fase

- Architecture & Governance: **Cerrada** (Resolución AR-2026-07-31-001)
- Execution: **En curso** (SPRINT 001)

## Sprint 001 — Infraestructura mínima reproducible

### Objetivo
Inicializar HEREDITARIA-OS con la infraestructura mínima reproducible
y versionable, compatible con Android 14/15 + Termux.

### Artefactos entregados
- [x] README.md
- [x] PROJECT_STATE.md
- [x] CHANGELOG.md
- [x] VERSION
- [x] LICENSE
- [x] .gitignore
- [x] install.sh
- [x] termux_setup.sh
- [x] requirements.txt
- [x] knowledge/README.md
- [x] scripts/update.sh

### Criterios de éxito
- [x] Archivos base existen
- [x] Estructura de directorios creada
- [ ] Proyecto clonado y verificado desde GitHub (pendiente de push real)
- [ ] Inicializado desde Android + Termux (pendiente de validación en dispositivo)
- [x] Estado registrado en este archivo
- [ ] Validación del sprint sin inconsistencias (pendiente de cierre)

## Documentos de gobierno vigentes

| Documento | Estado |
|---|---|
| HER-001 — Manifiesto | Aprobado |
| HER-RFC-001 — WhatsApp First Architecture | Aprobado (Draft v0.1) |
| HER-ADR-0000 — Repository as Product | Aprobado (v1.1) |
| HER-STD-0001 — Repository Contract | Aprobado (v1.0, 10 criterios) |
| HER-STD-0002 — Sprint Freeze Rule | Aprobado |
| HER-000 — Constitución del Proyecto | Pendiente (reevaluar tras Sprint 003) |
| Bootstrap Prompt | v1.0 |

## Supuestos no verificados

Registrados por restricción de HER-STD-0001 y el Bootstrap Prompt v1.0.
Ninguno de estos supuestos debe tratarse como hecho de arquitectura
hasta ser validado en entorno real.

- WAHA puede operar de forma continua sobre Termux en un dispositivo
  Android sin verse afectado por Doze mode / gestión de batería.
- GitHub Actions en repositorio privado se mantiene dentro de límites
  de minutos gratuitos del Free Tier para el volumen esperado.
- Netlify Functions (Free Tier) es suficiente para necesidades futuras
  de lógica server-side (ej. webhook WAHA), aún no confirmado.
- Termux permite instalar todas las dependencias de `requirements.txt`
  sin requerir compilación nativa adicional (a validar según crezca
  la lista de dependencias).

## Pendientes registrados como Issue

- ISSUE-001 (`governance/issues/SPRINT-001.md`): materializar la
  Resolución AR-2026-07-31-001 en `governance/resolutions/` y
  `governance/architecture.md` / `governance/decisions.md`. No estaba
  en el alcance explícito de los 11 archivos del Sprint 001; se
  registra en lugar de expandir el alcance del sprint en curso.

## Próximo sprint

SPRINT 002 — a definir. No debe iniciarse hasta cerrar validación de
SPRINT 001 (clonado real + Termux real).
