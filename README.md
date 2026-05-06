# Minireview: LLM Applications in Bioinformatics

## Estructura actual

```text
minireview_llms_aplications_in_bioinformatics/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── references.bib
├── requirements.txt
├── data/
├── doc/
├── figures/
├── scripts/
│   └── search.py
└── sections/
```

## Base del proyecto

- `scripts/search.py`: realiza una busqueda en PubMed con Biopython (Entrez).
- `.env`: define variables locales, en particular `ENTREZ_EMAIL`.
- `.env.example`: plantilla para compartir configuracion sin exponer datos personales.
- `references.bib`: base bibliografica para el manuscrito.
- `sections/`: secciones del texto en LaTeX.
- `figures/`: figuras y diagramas.
- `data/`: exportaciones RIS/BibTeX y archivos derivados.

## Configuracion rapida

1. Crear/activar entorno virtual.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar email para Entrez en `.env`:

```env
ENTREZ_EMAIL=tuemail@nebrija.es
```

## Como realizar la busqueda

Ejecutar:

```bash
python scripts/search.py
```

El script:

- Carga `ENTREZ_EMAIL` desde `.env`.
- Ejecuta la consulta definida en `search_query`.
- Muestra en consola la cantidad de registros encontrados.

## Ajustar la ecuacion de busqueda

Modificar la variable `search_query` en `scripts/search.py` para adaptar terminos, operadores y alcance segun tu pregunta de investigacion.
