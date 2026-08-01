# HEREDITARIA™ OS

Infraestructura documental e inteligencia para el patrimonio familiar.

## Qué es

HEREDITARIA™ OS es el repositorio canónico del proyecto HEREDITARIA™.
Contiene la metodología, el conocimiento patrimonial estructurado y la
automatización necesaria para operar el sistema.

No es una gestoría, despacho jurídico, notaría, papelería ni CRM.

## Principio de gobierno

Este repositorio es el producto principal (ver `governance/decisions.md`,
HER-ADR-0000 — Repository as Product). Todo consumidor externo
(ChatGPT Projects, NotebookLM, AI Studio, Claude, WAHA, Netlify, etc.)
lee de este repositorio; el repositorio no depende de ninguno de ellos.

## Estructura

```
automation/     Automatizaciones (WAHA, workflows)
deploy/         Configuración de despliegue (Netlify, GitHub Actions)
docs/           Documentación técnica no conceptual
governance/     Decisiones, resoluciones e issues arquitectónicos
knowledge/      Base de Conocimiento Patrimonial
runtime/        Componentes en ejecución
scripts/        Scripts operativos
templates/      Plantillas reutilizables
tests/          Pruebas
assets/         Recursos estáticos
logs/           Registros de ejecución
archive/        Material retirado de uso activo
```

## Requisitos mínimos

- Android 14 o 15 con Termux
- Python 3.11+
- Git

## Instalación rápida (Termux)

```bash
bash termux_setup.sh
bash install.sh
```

## Estado del proyecto

Ver [`PROJECT_STATE.md`](PROJECT_STATE.md).

## Gobernanza

Ver [`governance/architecture.md`](governance/architecture.md) y
[`governance/decisions.md`](governance/decisions.md).

## Licencia

Ver [`LICENSE`](LICENSE).
