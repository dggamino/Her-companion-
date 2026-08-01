# HER-STD-0006 — Definition of Done para Sprints de Ejecución

## Versión
1.0.0

## Estado
Aprobado

## Alcance
Criterios objetivos que debe cumplir un Sprint de código (no gobernanza)
para considerarse formalmente completado y mergeable a `main`.

## Criterios de Done

| # | Criterio | Verificación |
|---|----------|--------------|
| 1 | Alcance completado | Todo item del alcance congelado está implementado |
| 2 | Tests ejecutados | Suite de tests pasa localmente (`pytest` o equivalente) |
| 3 | CI verde | Pipeline GitHub Actions pasa en la rama del feature |
| 4 | Cobertura mínima | Cobertura de tests no decrece respecto al baseline |
| 5 | Revisión de código | Al menos 1 aprobación o revisión síncrona documentada |
| 6 | Sin regresiones | Validación de gobernanza pasa (`scripts/validate_governance.sh`) |
| 7 | Documentación técnica | README, docstrings o docs actualizados según alcance |
| 8 | Documentación de gobierno | PROJECT_STATE.md e issues reflejan el cierre del sprint |
| 9 | Commit trazable | Commit de cierre referencia el issue: `(resolves ISSUE-XXX)` |
| 10 | Deuda técnica registrada | Todo TODO/FIXME tiene issue asociado o está resuelto |

## Relación con Definition of Ready

| Fase | Estándar | Propósito |
|------|----------|-----------|
| Entrada | HER-STD-0005 | Validar que el sprint puede comenzar |
| Salida | HER-STD-0006 | Validar que el sprint puede cerrarse |

## Proceso de cierre

1. Responsable verifica cada criterio de Done
2. Arquitecto valida criterios 5 (revisión) y 8 (gobierno)
3. Se ejecuta pipeline CI completo en la rama
4. Merge a `main` solo si CI es verde
5. Se actualiza PROJECT_STATE.md y se cierra el issue del sprint

## Referencias
- HER-STD-0001 — Repository Contract
- HER-STD-0002 — Sprint Freeze Rule
- HER-STD-0005 — Definition of Ready
- HER-ADR-0000 — Decision Record Template
