# Knowledge Base — HEREDITARIA™ OS

Esta carpeta contiene la Base de Conocimiento Patrimonial de
HEREDITARIA™.

## Orden obligatorio de fuentes (HER-RFC-001, sección 10)

1. Knowledge Base (esta carpeta)
2. RFC
3. Legislación
4. Observatorio
5. Biblioteca

Las conversaciones nunca se utilizan como fuente permanente de
conocimiento.

## Terminología

Todo contenido de esta carpeta debe ser consistente con:

- `01_Ontology_Blueprint_v1.0` — entidades y relaciones oficiales.
- `02_Glosario_Taxonomia_v1.0` — definiciones oficiales.

Ante cualquier término nuevo, verificar primero si ya existe un
concepto equivalente antes de introducir uno distinto.

## Gobierno de datos (HER-STD-0001, Criterio 9)

Esta carpeta **no debe contener**:

- Datos personales identificables reales.
- Expedientes familiares reales.
- Documentos legales de clientes reales.
- Información patrimonial sensible sin mecanismo explícito de
  protección.

Mientras no exista un módulo específico de gestión de expedientes,
esta carpeta utilizará únicamente:

- datos ficticios;
- ejemplos anonimizados;
- conjuntos de prueba;
- plantillas;
- esquemas.

Los subdirectorios `knowledge/private/` y `knowledge/expedientes/`
están excluidos de versionado (ver `.gitignore`) y no deben usarse
para almacenar información real sin antes definir el mecanismo de
protección correspondiente.

## Estructura prevista (a poblar en sprints futuros)

```
knowledge/
├── README.md          (este archivo)
├── eventos/            Eventos Patrimoniales documentados
├── rutas/               Rutas Patrimoniales
├── programas/           Programas Patrimoniales / beneficios
├── observatorio/        Contenido del módulo Observatorio
└── plantillas/           Kits Documentales reutilizables
```

Estos subdirectorios no se crean en el Sprint 001. Se crearán cuando
un sprint futuro los requiera, evitando infraestructura sin evidencia
de uso inmediato.
