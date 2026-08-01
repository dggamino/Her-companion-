#!/usr/bin/env bash
# HEREDITARIA-OS — termux_setup.sh
# Prepara un entorno Termux (Android 14/15) para clonar y ejecutar
# HEREDITARIA-OS. Ejecutar antes de install.sh.
#
# Uso:
#   bash termux_setup.sh

set -euo pipefail

echo "== HEREDITARIA-OS :: Termux Setup =="

if [ -z "${PREFIX:-}" ] || [[ "${PREFIX}" != *"com.termux"* ]]; then
  echo "AVISO: este script está diseñado para Termux."
  echo "No se detectó la variable de entorno PREFIX de Termux."
  echo "Continuando de todas formas (puede fallar en otros entornos)."
fi

echo "-> Actualizando paquetes base"
pkg update -y
pkg upgrade -y

echo "-> Instalando dependencias base: git, python, openssh, clang, make"
pkg install -y git python openssh clang make

echo "-> Verificando versiones instaladas"
python3 --version
git --version

echo "-> Configurando almacenamiento compartido (opcional, requiere confirmación manual)"
if command -v termux-setup-storage >/dev/null 2>&1; then
  echo "Ejecuta manualmente 'termux-setup-storage' si necesitas acceso a almacenamiento compartido."
fi

echo "-> Setup de Termux completado."
echo "Siguiente paso: clonar el repositorio y ejecutar install.sh"
echo
echo "  git clone <URL_DEL_REPOSITORIO> HEREDITARIA-OS"
echo "  cd HEREDITARIA-OS"
echo "  bash install.sh"

exit 0
