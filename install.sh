#!/usr/bin/env bash
# HEREDITARIA-OS — install.sh
# Instala el entorno del proyecto (Termux o Linux estándar).
# Requiere: termux_setup.sh ya ejecutado en dispositivos Android/Termux.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${REPO_ROOT}/.venv"
LOG_FILE="${REPO_ROOT}/logs/install.log"

mkdir -p "${REPO_ROOT}/logs"

log() {
  echo "[$(date -u +'%Y-%m-%dT%H:%M:%SZ')] $1" | tee -a "${LOG_FILE}"
}

log "Iniciando instalación de HEREDITARIA-OS"

if ! command -v python3 >/dev/null 2>&1; then
  log "ERROR: python3 no está disponible. Ejecuta termux_setup.sh primero si estás en Termux."
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  log "ERROR: git no está disponible. Ejecuta termux_setup.sh primero si estás en Termux."
  exit 1
fi

log "Creando entorno virtual en ${VENV_DIR}"
python3 -m venv "${VENV_DIR}"

# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

log "Actualizando pip"
pip install --upgrade pip >>"${LOG_FILE}" 2>&1

if [ -s "${REPO_ROOT}/requirements.txt" ]; then
  log "Instalando dependencias de requirements.txt"
  pip install -r "${REPO_ROOT}/requirements.txt" >>"${LOG_FILE}" 2>&1
else
  log "requirements.txt vacío (placeholder). Sin dependencias que instalar."
fi

log "Verificando estructura de directorios"
for dir in automation deploy docs governance knowledge runtime scripts templates tests assets logs archive; do
  if [ ! -d "${REPO_ROOT}/${dir}" ]; then
    log "AVISO: directorio esperado no encontrado: ${dir}/"
  fi
done

log "Instalación completada."
log "Para activar el entorno en tu sesión actual: source .venv/bin/activate"

exit 0
