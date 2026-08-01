# HER-000 — Constitución del Proyecto HEREDITARIA™ OS

## Versión
1.0.0-draft

## Estado
Aprobado para Sprint 002 — reevaluar tras Sprint 003

## 1. Propósito

HEREDITARIA™ OS es un sistema operativo de conocimiento legal determinista,
diseñado para operar en Android + Termux, con WhatsApp como interfaz
principal, dentro del Free Tier de todas sus dependencias.

## 2. Principios fundamentales

| # | Principio | Documento |
|---|-----------|-----------|
| 1 | Repository as Product | HER-ADR-0000 |
| 2 | WhatsApp First | HER-RFC-001 |
| 3 | Android + Termux First | HER-RFC-001 |
| 4 | Free Tier únicamente | HER-RFC-001 |
| 5 | Sprint Freeze Rule | HER-STD-0002 |
| 6 | Auditabilidad | HER-STD-0001 |

## 3. Fases del proyecto

| Fase | Estado | Inicio | Cierre |
|------|--------|--------|--------|
| Architecture & Governance | ✅ Cerrada | — | 2026-07-31 |
| Execution | 🔄 En curso | 2026-08-01 | — |

## 4. Estructura de gobierno

- `governance/manifesto.md` — HER-001
- `governance/rfc/` — Requests for Comments
- `governance/adr/` — Architecture Decision Records
- `governance/std/` — Standards
- `governance/resolutions/` — Resoluciones aprobadas
- `governance/issues/` — Issues abiertos/cerrados por sprint

## 5. Modificación de esta constitución

Requiere:
1. Issue en `governance/issues/`
2. Discusión en sprint de gobernanza
3. Aprobación explícita del responsable del proyecto
4. Commit con referencia al issue

## Referencias
- HER-001 — Manifiesto
- HER-STD-0001 — Repository Contract
- HER-STD-0002 — Sprint Freeze Rule
- AR-2026-07-31-001 — Cierre de fase Architecture & Governance
