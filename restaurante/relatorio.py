import csv
import json


def salvar_relatorio_txt(relatorio: str, nome_arquivo: str):
    caminho_arquivo = f"relatorios/txt/{nome_arquivo}.txt"

    # write
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)

        print(f"Relatório txt salvo em {caminho_arquivo}")


# comma separated values
def salvar_relatorio_csv(comanda: list[dict], nome_arquivo: str):
    caminho_arquivo = f"relatorios/csv/{nome_arquivo}.csv"
    cabecalho = comanda[0].keys()

    # write
    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()
        escritor.writerows(comanda)

        print(f"Relatório csv salvo em {caminho_arquivo}")


def salvar_relatorio_json(comanda: list[dict], nome_arquivo: str):
    caminho_arquivo = f"relatorios/json/{nome_arquivo}.json"

    # write
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(comanda, arquivo, indent=2, ensure_ascii=False)

        print(f"Relatório json salvo em {caminho_arquivo}")
