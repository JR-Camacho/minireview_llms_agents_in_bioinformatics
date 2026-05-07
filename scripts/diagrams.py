"""
Generacion de diagramas para la minireview (Graphviz).

Requiere el paquete `graphviz` y el binario `dot` instalado en el sistema.
"""

from pathlib import Path

from graphviz import Digraph


def generate_prisma_diagram(
    figures_dir=None,
    basename: str = "prisma_bioinformatica",
    *,
    diagram_format: str = "pdf",
) -> Path:
    """
    Diagrama PRISMA (flujo de seleccion bibliografica).
    Guarda PDF en figures/<basename>.pdf por defecto.
    """
    root = Path(__file__).resolve().parent.parent
    out_dir = Path(figures_dir) if figures_dir is not None else root / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    outfile = str(out_dir / basename)

    graph = Digraph("PRISMA", filename=outfile, format=diagram_format)
    graph.attr(rankdir="TB", size="8,10")
    graph.attr(
        "node",
        shape="box",
        style="filled",
        fillcolor="white",
        fontname="Helvetica",
        fontsize="12",
    )

    graph.node("A", "Identificación:\nArtículos identificados en PubMed\n(n = 40)")
    graph.node("B", "Cribado:\nTítulo y resumen\n(n = 40)")
    graph.node("C", "Elegibilidad:\nEvaluación a texto completo\n(n = 15)")
    graph.node("D", "Inclusión:\nEstudios incluidos en la síntesis\n(n = 15)")
    graph.node(
        "E",
        (
            "Artículos excluidos (n = 25):\n"
            "• Aplicaciones clínicas de imágenes\n"
            "• Estudios de prompting simple\n"
            "• No relacionados con bioinformática\n"
            "• Sin arquitecturas de agentes"
        ),
        fillcolor="#fff4f4",
    )

    graph.edge("A", "B")
    graph.edge("B", "C")
    graph.edge("C", "D")
    graph.edge("B", "E")

    rendered = graph.render(cleanup=True)
    return Path(rendered).resolve()


def export_all_diagrams(figures_dir=None) -> dict[str, Path]:
    """Genera todos los diagramas definidos en este modulo (extensible)."""
    return {
        "prisma_bioinformatica": generate_prisma_diagram(figures_dir=figures_dir),
    }


if __name__ == "__main__":
    for name, path in export_all_diagrams().items():
        print(f"{name}: {path}")
