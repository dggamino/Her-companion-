# HER-STD-0005 — Definition of Ready para Sprints de Ejecución

## Versión
1.0.0

## Estado
Aprobado

## Alcance
Criterios que debe cumplir un Sprint de código (no gobernanza) antes
de ser aprobado.

## Criterios de Ready

| # | Criterio | Verificación |
|---|----------|--------------|
| 1 | Alcance definido por responsable | Mensaje explícito con opción o descripción |
| 2 | Dependencias identificadas | Lista de paquetes/componentes previos necesarios |
| 3 | Interfaces congeladas | Si modifica interfaz pública, requiere ADR |
| 4 | Tests definidos | Al menos 1 test por comportamiento nuevo |
| 5 | No deuda técnica nueva | No rompe estándares existentes (STD-0001-0004) |
| 6 | Documentación de gobierno actualizada | PROJECT_STATE.md refleja el sprint |

## Proceso de aprobación

1. Responsable propone alcance (opción o descripción)
2. Arquitecto valida dependencias y criterios
3. Alcance congelado al inicio del sprint
4. No se modifica salvo resolución formal

## Referencias
- HER-STD-0002 — Sprint Freeze Rule
- HER-STD-0001 — Repository Contract
