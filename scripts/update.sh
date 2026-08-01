#!/usr/bin/env bash
# HEREDITARIA-OS — scripts/update.sh
# Actualiza el repositorio local desde el remoto canónico (GitHub)
# y deja evidencia en logs/update.log (HER-STD-0001, Criterio 10 —
# Auditabilidad).
#
# Uso:
#   bash scripts/update.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_FILE="${REPO_ROOT}/logs/update.log"

mkdir -p "${REPO_ROOT}/logs"

log() {
  echo "[$(date -u +'%Y-%m-%dT%H:%M:%SZ')] $1" | tee -a "${LOG_FILE}"
}

cd "${REPO_ROOT}"

if [ ! -d ".git" ]; then
  log "ERROR: este directorio no es un repositorio git."
  exit 1
fi

log "Iniciando actualización del repositorio"

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
log "Rama actual: ${CURRENT_BRANCH}"

if ! git diff --quiet || ! git diff --cached --quiet; then
  log "AVISO: hay cambios locales sin commitear. Se aborta el pull para evitar pérdida de datos."
  git status --short | tee -a "${LOG_FILE}"
  exit 1
fi

log "Ejecutando git fetch"
git fetch origin >>"${LOG_FILE}" 2>&1

log "Ejecutando git pull --ff-only"
if git pull --ff-only origin "${CURRENT_BRANCH}" >>"${LOG_FILE}" 2>&1; then
  log "Actualización completada sin conflictos."
else
  log "ERROR: no fue posible hacer fast-forward. Revisión manual requerida."
  exit 1
fi

NEW_COMMIT="$(git rev-parse --short HEAD)"
log "HEAD actual: ${NEW_COMMIT}"

exit 0
