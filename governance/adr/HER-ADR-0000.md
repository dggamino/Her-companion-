# HER-ADR-0000 — Repository as Product

## Versión
1.1

## Estado
Aprobado

## Contexto

Los proyectos de software dependen típicamente de conversaciones,
documentos externos y conocimiento tribal. HEREDITARIA™ OS no puede
permitirse esa dependencia.

## Decisión

El repositorio Git es la fuente única de verdad del proyecto.

## Consecuencias

- Positivo: cualquier colaborador (humano o IA) puede reconstruir el
  estado del proyecto desde `git clone`.
- Positivo: las decisiones arquitectónicas son auditables.
- Negativo: requiere disciplina de commit frecuente y mensajes claros.

## Reglas

1. Todo artefacto versionable vive en el repositorio.
2. El chat es canal de decisión, no de almacenamiento.
3. "Está implementado" no es válido sin commit hash.

## Referencias
- HER-STD-0001 — Repository Contract
- HER-001 — Manifiesto
