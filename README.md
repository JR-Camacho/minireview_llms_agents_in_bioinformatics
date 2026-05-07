# Minireview: LLM Applications in Bioinformatics

## Estructura del Proyecto

```text
minireview_llms_aplications_in_bioinformatics/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── LATEX_QUICK_REFERENCE.md
├── requirements.txt
├── references.bib                    (referencias en CSV de PubMed/Scopus)
├── data/
│   └── literature_results.csv        (búsqueda consolidada de PubMed + Scopus)
├── figures/                          (figuras y diagramas finales)
├── scripts/
│   ├── search.py                     (búsqueda en PubMed y Scopus)
│   └── diagrams.py                   (generación de diagrama PRISMA)
├── minireview_example/               (plantilla base - no modificar)
│   ├── main.tex
│   ├── sections/
│   ├── figs/
│   └── README.md
└── manuscript/                       ← TU MANUSCRITO PRINCIPAL
    ├── main.tex                      (archivo raíz con configuración)
    ├── references.bib                (referencias BibTeX de tu review)
    └── sections/
        ├── 01_introduction.tex
        ├── 02_search_methodology.tex
        ├── 03_thematic_synthesis.tex
        └── 04_conclusions.tex
```

## Descripción de Carpetas

### Scripts y Datos
- **`scripts/search.py`**: Búsqueda consolidada en PubMed y Scopus. Resultado → `data/literature_results.csv`
- **`scripts/diagrams.py`**: Genera diagrama PRISMA → `figures/prisma_bioinformatica.pdf`
- **`data/literature_results.csv`**: Resultado consolidado (20 artículos)
- **`figures/`**: Figuras y diagramas finales para el manuscrito

### Configuración
- **`.env`**: Credenciales locales (`ENTREZ_EMAIL`, `SCOPUS_API_KEY`)
- **`.env.example`**: Plantilla para compartir sin datos sensibles
- **`references.bib`**: Referencias en CSV (si exportas desde PubMed)
- **`requirements.txt`**: Dependencias Python

### Manuscrito LaTeX
- **`manuscript/main.tex`**: Archivo raíz con toda la configuración (paquetes, estilos, comandos)
- **`manuscript/sections/`**: 4 secciones del manuscrito (introducción, metodología, síntesis, conclusiones)
- **`manuscript/references.bib`**: Referencias BibTeX para tu mini-review
- **`LATEX_QUICK_REFERENCE.md`**: Guía rápida de comandos y patrones LaTeX

### Referencia
- **`minireview_example/`**: Plantilla base de ejemplo (no modificar, agregada a `.gitignore`)

## Configuracion rapida

1. Crear/activar entorno virtual.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar credenciales en `.env`:

```env
ENTREZ_EMAIL=tuemail@nebrija.es
SCOPUS_API_KEY=tu_api_key_de_scopus
SCOPUS_MAX_RESULTS=25
```

## Como realizar la busqueda

EjeWorkflow de Trabajo

### 1. Búsqueda Bibliográfica
```bash
python scripts/search.py
```
→ Genera `data/literature_results.csv` con resultados de PubMed y Scopus

Ajusta las queries editando `PUBMED_QUERY` y `SCOPUS_QUERY` en `scripts/search.py`.

### 2. Generar Figuras
```bash
python scripts/diagrams.py
```
→ Crea `figures/prisma_bioinformatica.pdf` y otros diagramas

### 3. Redactar Manuscrito
Edita los archivos en `manuscript/sections/`:
- `01_introduction.tex` (400–600 palabras)
- `02_search_methodology.tex` (300–500 palabras)
- `03_thematic_synthesis.tex` (2000–3000 palabras)
- `04_conclusions.tex` (400–600 palabras)

**Referencia rápida**: Revisa `LATEX_QUICK_REFERENCE.md` para comandos, tablas, ecuaciones, código.

### 4. Compilar a PDF
```bash
cd manuscript
pdflatex main
bibtex main
pdflatex main
pdflatex main
```
→ Genera `main.pdf`

O en Overleaf: sube la carpeta `manuscript/`, selecciona pdfLaTeX en Settings.

## Notas Importantes

- **references.bib en raíz**: Contiene datos brutos de la búsqueda (CSV convertido a BibTeX si aplica)
- **manuscript/references.bib**: Tus referencias seleccionadas para el manuscrito (edita aquí)
- **figures/**: Figuras finales para el PDF (generadas automáticamente o manuales)
- **minireview_example/**: Plantilla base educativa (en `.gitignore`)
python scripts/search.py
```

El script:

- Carga `ENTREZ_EMAIL` desde `.env`.
- Carga `SCOPUS_API_KEY` desde `.env`.
- Ejecuta consulta en PubMed y Scopus (via API oficial de Elsevier para Scopus).
- Guarda `data/literature_results.csv` con la columna `source` para indicar la fuente de cada registro.

## Ajustar la ecuacion de busqueda

Modificar `PUBMED_QUERY` y `SCOPUS_QUERY` en `scripts/search.py` para adaptar terminos, operadores y alcance segun tu pregunta de investigacion.
