from Bio import Entrez
import os
import ssl
import csv
from pathlib import Path
from urllib.error import URLError
from dotenv import load_dotenv


load_dotenv()
Entrez.email = os.getenv("ENTREZ_EMAIL", "")
ssl._create_default_https_context = ssl._create_unverified_context

if not Entrez.email:
    raise ValueError("Missing ENTREZ_EMAIL. Set it in .env or environment variables.")

def search_articles(query, max_results=20):
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()
    except URLError as exc:
        raise RuntimeError(
            "Could not connect to PubMed due to SSL/network settings."
        ) from exc

    id_list = record["IdList"]

    if not id_list:
        print("No results found.")
        return []

    return id_list


def save_results(pmids, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["pmid", "url"])
        for pmid in pmids:
            writer.writerow([pmid, f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"])

search_query = '("large language models"[TIAB] OR "LLM"[TIAB] OR "AI agents"[TIAB]) AND ("bioinformatics"[TIAB] OR "workflow"[TIAB] OR "automation"[TIAB])'

print(f"Searching PubMed for: {search_query}")
results = search_articles(search_query)
print(f"Found {len(results)} records.")
output_file = Path("data/pubmed_results.csv")
save_results(results, output_file)
print(f"Results saved to: {output_file}")