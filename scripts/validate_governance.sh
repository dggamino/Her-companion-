#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "=== HEREDITARIA-OS Governance Validator ==="

FAIL=0

for file in \
  governance/HER-001-Manifiesto.md \
  governance/constitution.md \
  governance/decisions.md \
  governance/adr/HER-ADR-0000.md \
  governance/adr/HER-ADR-0001.md \
  governance/rfc/HER-RFC-001.md \
  governance/rfc/HER-RFC-002.md \
  governance/std/HER-STD-0001.md \
  governance/std/HER-STD-0002.md \
  governance/std/HER-STD-0003.md \
  governance/std/HER-STD-0004.md \
  governance/std/HER-STD-0005.md \
  governance/std/HER-STD-0006.md \
  governance/resolutions/AR-2026-07-31-001.md \
  governance/issues/SPRINT-001.md \
  governance/issues/SPRINT-002.md \
  governance/issues/SPRINT-003.md \
  governance/issues/SPRINT-004.md \
  governance/issues/SPRINT-005.md \
  governance/issues/SPRINT-006.md \
  governance/issues/SPRINT-007.md \
  governance/issues/SPRINT-008.md \
  governance/issues/SPRINT-009.md \
  governance/issues/SPRINT-010.md
do
  if [ -f "$file" ]; then
    echo "  ✅ $file"
  else
    echo "  ❌ MISSING: $file"
    FAIL=1
  fi
done

if [ $FAIL -eq 1 ]; then
  echo "=== VALIDATION FAILED ==="
  exit 1
fi

echo "=== VALIDATION PASSED ==="
