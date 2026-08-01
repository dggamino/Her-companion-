#!/usr/bin/env bash
# HEREDITARIA-OS — scripts/generate_context_snapshot.sh
# Genera un único archivo consolidado con el estado real del
# repositorio, para iniciar una nueva ventana de contexto sin
# depender del historial de conversación (HER-ADR-0000: el
# repositorio es la fuente canónica, no el chat).
#
# Uso:
#   bash scripts/generate_context_snapshot.sh
#
# Salida:
#   CONTEXT_SNAPSHOT.md en la raíz del repo (no versionado, ver
#   .gitignore — es un artefacto derivado y desactualizable, no
#   fuente de verdad).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${REPO_ROOT}/CONTEXT_SNAPSHOT.md"
TIMESTAMP="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"

cd "${REPO_ROOT}"

if [ ! -d ".git" ]; then
  echo "ERROR: no es un repositorio git. Ejecutar desde la raíz de HEREDITARIA-OS."
  exit 1
fi

LAST_COMMIT="$(git log -1 --format='%h %s (%ad)' --date=short 2>/dev/null || echo 'sin commits')"
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'desconocida')"

{
  echo "# HEREDITARIA-OS — Context Snapshot"
  echo
  echo "Generado: ${TIMESTAMP}"
  echo "Rama: ${BRANCH}"
  echo "Último commit: ${LAST_COMMIT}"
  echo
  echo "> Este archivo se genera automáticamente desde el estado real"
  echo "> del repositorio. No es una fuente de verdad por sí mismo —"
  echo "> es un resumen para arrancar una sesión nueva. Ante cualquier"
  echo "> duda, el repositorio (no este archivo, no el chat) manda."
  echo
  echo "---"
  echo
  echo "## Instrucción para la nueva sesión"
  echo
  echo "1. Usar el Bootstrap Prompt v1.0 como contrato operativo (sin"
  echo "   volver a pegarlo completo salvo que cambie; referenciarlo)."
  echo "2. Este snapshot reemplaza cualquier resumen de conversación."
  echo "3. No aceptar como hecho ningún documento de gobierno (informe"
  echo "   de auditoría, resolución, ADR) que no esté aquí abajo o en"
  echo "   el repositorio real — no reconstruir de memoria."
  echo
  echo "---"
  echo
  echo "## PROJECT_STATE.md"
  echo
  if [ -f "PROJECT_STATE.md" ]; then
    cat "PROJECT_STATE.md"
  else
    echo "_(no encontrado)_"
  fi
  echo
  echo "---"
  echo
  echo "## Issues abiertos (governance/issues/)"
  echo
  if compgen -G "governance/issues/*.md" > /dev/null; then
    for f in governance/issues/*.md; do
      echo "### Archivo: \`${f}\`"
      echo
      cat "${f}"
      echo
    done
  else
    echo "_(ninguno)_"
  fi
  echo "---"
  echo
  echo "## Auditorías (audits/)"
  echo
  if compgen -G "audits/*.md" > /dev/null; then
    for f in audits/*.md; do
      echo "### Archivo: \`${f}\`"
      echo
      cat "${f}"
      echo
    done
  else
    echo "_(ninguna)_"
  fi
  echo "---"
  echo
  echo "## Resoluciones (governance/resolutions/)"
  echo
  RES_FILES=$(find governance/resolutions -maxdepth 1 -name "*.md" 2>/dev/null || true)
  if [ -n "${RES_FILES}" ]; then
    for f in ${RES_FILES}; do
      echo "### Archivo: \`${f}\`"
      echo
      cat "${f}"
      echo
    done
  else
    echo "_(ninguna materializada todavía — ver ISSUE-001)_"
  fi
  echo "---"
  echo
  echo "## Últimos commits (últimos 10)"
  echo
  echo '```'
  git log -10 --oneline 2>/dev/null || echo "sin historial"
  echo '```'
} > "${OUT}"

echo "Snapshot generado: ${OUT}"
echo "Súbelo o pégalo como primer mensaje/adjunto de la nueva sesión."

exit 0
