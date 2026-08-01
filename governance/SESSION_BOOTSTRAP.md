# SESSION_BOOTSTRAP — Protocolo de continuidad entre sesiones

## Problema que resuelve

Una ventana de contexto de chat tiene límite. Cuando se agota o se
abre una sesión nueva, el riesgo es reconstruir el estado del
proyecto "de memoria" — lo cual ya produjo un incidente real: un
informe de auditoría completo fue presentado como aprobado sin haber
sido generado por comparación real de documentos (ver
`audits/AUDIT-001-Ontology.md`, nota de integridad).

Este protocolo existe para que ese tipo de error sea estructuralmente
más difícil: el repositorio, no el historial de conversación, es la
fuente de verdad (HER-ADR-0000).

## Protocolo

### Antes de cerrar la sesión actual (si aplica)

Si hay cambios sin commitear, commitearlos o descartarlos
explícitamente. No dejar estado "solo en el chat".

### Para iniciar la sesión nueva

1. Ejecutar en Termux:

   ```bash
   cd HEREDITARIA-OS
   bash scripts/generate_context_snapshot.sh
   ```

2. Subir o pegar el archivo `CONTEXT_SNAPSHOT.md` generado como
   primer mensaje de la sesión nueva, junto con el comando de sprint
   correspondiente (ej. `SPRINT 002`).

3. La sesión nueva debe tratar todo dato de `CONTEXT_SNAPSHOT.md`
   como hecho verificado (viene del repositorio real), y todo lo que
   no esté ahí como desconocido — no reconstruir por inferencia ni
   por lo que "probablemente" se decidió antes.

4. El Bootstrap Prompt v1.0 no se repega completo salvo que haya
   cambiado; se referencia como contrato ya vigente.

### Qué NO hacer

- No pedir a la IA que "recuerde" o "resuma" la conversación anterior
  como fuente de continuidad — el snapshot del repositorio reemplaza
  esa función.
- No aceptar documentos de gobierno (auditorías, resoluciones, ADR)
  pegados en el chat como ya aprobados si no están en el repositorio
  o no se generan mediante verificación real dentro de la sesión.

## Limitación conocida

`CONTEXT_SNAPSHOT.md` no se versiona (ver `.gitignore`) porque es un
artefacto derivado que se regenera en cada arranque — versionarlo
generaría ruido de commits sin valor de auditoría real. La fuente de
verdad sigue siendo `PROJECT_STATE.md`, `governance/issues/`,
`audits/` y `governance/resolutions/` por separado.
