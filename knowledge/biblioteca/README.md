# knowledge/biblioteca/ — Serie HEREDITARIA™ troceada

Fuente: `SERIE_HEREDITARIA_COMPLETA.md` (6 libros, Daniel Gómez Gamiño,
2026), troceada en 53 unidades individuales por capítulo/sección.

## Nivel en el orden de fuentes (HER-RFC-001 §10)

Esta carpeta es **Biblioteca**, prioridad 5 de 5. El bot debe consultar
Knowledge Base estructurada, RFC, y Legislación antes que estos
capítulos si hay conflicto de información.

## Estructura

```
biblioteca/
├── INDEX.md                                    Índice completo generado
├── libro-1-la-casa-no-se-toca-por-quien/       7 capítulos + epílogo + nota legal
├── libro-2-el-cuadrante-del-patrimonio-familiar/  Marco de 4 cuadrantes
├── libro-3-el-cuidador-que-nadie-documento/    Validador
├── libro-4-herencia-calculada/                 Calculador
├── libro-5-82-como-tu-pension-deja-de-ser-insuficiente/  Planeador
└── libro-6-cuentaselo-a-tus-padres/            Formato regalo, guiones de conversación
```

Cada archivo tiene frontmatter YAML con: libro, sección, tipo
(capitulo/epilogo/nota-legal/intro/ultima-pagina), cuadrante asociado,
keywords de RFC-001 detectadas por coincidencia de texto, y el
fundamento legal (Decreto 87).

## Uso previsto

- **Router de keywords**: cruzar la keyword detectada en el mensaje de
  WhatsApp contra `keywords_rfc001` de cada archivo para servir el
  fragmento correcto.
- **Clasificador de Cuadrante**: los capítulos 2-5 de "El Cuadrante del
  Patrimonio Familiar" son la base directa de un árbol de decisión
  conversacional (Congelado/Calculador/Validador/Planeador).
- **Plantillas de mensaje**: `libro-6.../04-capitulo-lo-que-puedes-decir-palabra-por-palabra.md`
  contiene las tres aperturas de conversación listas para usar como
  mensajes pre-armados.

## ⚠️ Inconsistencia de canon sin resolver

Esta serie usa **"Don Refugio"** y **"Tío Efraín"** como personajes
recurrentes. `ONTOLOGIA.md` (corpus de gobernanza de marca, HARD_CANON
§1.5) define **"Don Severo Villanueva"** como la ficha fija del
personaje, "no editable sin nueva versión de ontología".

No se resolvió antes de trocear este contenido — se trocea tal cual
está, sin alterar el texto original del autor. Antes de que el bot
cite cualquiera de estos personajes en producción, debe decidirse cuál
es el canon vigente. Ver también: título "Coordinador de Registro
Patrimonial Familiar" en la portada de la serie, marcado como
DEPRECATED en `ONTOLOGIA.md` §4 salvo disclaimer con igual peso visual
(no presente en la portada tal como está escrita).

## Nota de datos

Los ejemplos y perfiles ("el padre de 74 años en Ecatepec", etc.) están
marcados por el propio autor como composites anónimos en cada Nota
Legal — consistente con la categoría COUNTERFACTUAL de `ONTOLOGIA.md`
§5. No son expedientes reales; no aplica HER-STD-0001 Criterio 9 sobre
esta carpeta.
