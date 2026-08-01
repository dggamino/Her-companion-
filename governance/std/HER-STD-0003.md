# HER-STD-0003 — Convenciones de Control de Versiones

## Versión
1.0.0

## Estado
Aprobado

## Alcance
Todas las operaciones Git en HEREDITARIA™ OS.

## 1. Rama principal

- **Nombre:** `main`
- **Razón:** Consistencia con GitHub defaults y convención moderna.
- **Migración:** Los repositorios locales con `master` deben renombrarse
  vía `git branch -M main` antes del primer push.

## 2. Ramas de trabajo

| Prefijo | Uso | Ejemplo |
|---------|-----|---------|
| `feature/` | Nuevas funcionalidades | `feature/HER-006-score-engine` |
| `fix/` | Correcciones | `fix/ISSUE-002-branch-name` |
| `docs/` | Documentación | `docs/ADR-007-time-abstraction` |
| `sprint/` | Integración de sprint | `sprint/002-governance` |

## 3. Commits

Formato: `tipo(alcance): descripción (HER-XXX)`

Tipos permitidos:
- `feat` — nueva funcionalidad
- `fix` — corrección
- `docs` — documentación
- `chore` — mantenimiento
- `merge` — fusión de historiales

## 4. Flujo de trabajo

1. Crear rama desde `main`: `git checkout -b feature/xxx`
2. Commitear con mensaje estándar
3. Push a remoto: `git push -u origin feature/xxx`
4. Merge vía Pull Request (cuando GitHub Actions esté activo) o merge local
5. Borrar rama remota post-merge

## 5. Autenticación

- Repositorio privado: requiere Personal Access Token (PAT) con scope `repo`.
- Almacenamiento: `git config --global credential.helper store`.
- El token nunca se commiteará en el repositorio.

## Referencias
- ISSUE-002 (resuelto por este estándar)
- HER-STD-0001 (Repository Contract)
