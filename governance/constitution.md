# HER-000 — Constitución del Proyecto HEREDITARIA™ OS

## Versión
1.0.0

## Estado
Aprobado

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
| 7 | Time Abstraction | HER-ADR-007 |
| 8 | Open/Closed Rules | HER-ADR-009 |

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

## 6. Supuestos no verificados (registro obligatorio)

Todo supuesto debe listarse aquí con su documento de origen.
Ningún supuesto no listado puede usarse como base de decisión arquitectónica.

| # | Supuesto | Origen | Estado |
|---|----------|--------|--------|
| 1 | WAHA opera continuo en Android sin Doze | HER-RFC-001 | No verificado |
| 2 | GitHub Actions Free Tier suficiente | Bootstrap Prompt | No verificado |
| 3 | Netlify Functions Free Tier suficiente | Bootstrap Prompt | No verificado |
| 4 | Termux instala todas las dependencias sin compilación nativa | Bootstrap Prompt | No verificado |

## Referencias
- HER-001 — Manifiesto
- HER-STD-0001 — Repository Contract
- HER-STD-0002 — Sprint Freeze Rule
- HER-STD-0003 — Convenciones Git
- HER-STD-0004 — Context Snapshot Standard
- AR-2026-07-31-001 — Cierre de fase Architecture & Governance
