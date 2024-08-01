import os
from restaurante.gerenciador import adicionar_item_para_comanda, calcular_total_comanda
from datetime import datetime

from restaurante.relatorio import (
    salvar_relatorio_csv,
    salvar_relatorio_json,
    salvar_relatorio_txt,
)


COMANDA_USUARIO = []


def gerar_relatorio():
    relatorio = ""
    relatorio += "Cafeteria Kenzie - Relatório\n\n"
    horario_agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    relatorio += f"Data e Hora {horario_agora}\n\n"
    relatorio += "Itens consumidos:\n"

    for item in COMANDA_USUARIO:
        relatorio += f"{item['quantidade']}un. - {item['nome']} - Valor unitário: R$ {item['preco']:.2f} - Sub-total: R$ {item['sub_total']:.2f}\n"

    total_comanda = calcular_total_comanda(COMANDA_USUARIO)
    relatorio += f"\nTotal da comanda: R$ {total_comanda:.2f}\n"

    print(relatorio)

    return relatorio


def tela_checkout():
    os.system("cls")

    while True:
        for item in COMANDA_USUARIO:
            print(
                f"{item['quantidade']}un. - {item['nome']} - Valor unitário: R$ {item['preco']:.2f} - Sub-total: R$ {item['sub_total']:.2f}"
            )

        print("\nO que deseja fazer?\n")
        print("  [1]. Voltar ao menu principal")
        print("  [2]. Fechar comanda e salvar relatório\n")

        opcao_selecionada = input("Digite uma opção válida (1 ou 2): ")
        os.system("cls")

        if opcao_selecionada == "1":
            break
        elif opcao_selecionada == "2":
            relatorio = gerar_relatorio()
            timestamp = datetime.now().timestamp()
            nome_arquivo = f"relatorio-{timestamp}"
            salvar_relatorio_txt(relatorio=relatorio, nome_arquivo=nome_arquivo)

            salvar_relatorio_csv(COMANDA_USUARIO, nome_arquivo)
            salvar_relatorio_json(COMANDA_USUARIO, nome_arquivo)
            exit()
        else:
            print("Escolha uma opção válida (1 ou 2)\n")


def tela_adicionar_item():
    os.system("cls")

    while True:
        print("Adicionando item a comanda...\n")
        id_item = input("Digite o ID do item: ")
        quantidade = input("Digite a quantidade: ")

        item_adicionado = adicionar_item_para_comanda(
            id_item=int(id_item), quantidade=int(quantidade), comanda=COMANDA_USUARIO
        )

        os.system("cls")
        print(f"{quantidade} de {item_adicionado['nome']} adicionado(s) a comanda!\n")

        break


def tela_inicial():
    os.system("cls")

    while True:
        print("Cafeteria Kenzie - Gerenciador de Comanda\n")
        print("  [1]. Adicionar item a comanda")
        print("  [2]. Resumo da comanda")
        print("  [3]. Sair\n")

        opcao_selecionada = input("Digite uma opção válida (1, 2 ou 3): ")

        if opcao_selecionada == "1":
            tela_adicionar_item()
        elif opcao_selecionada == "2":
            tela_checkout()
        elif opcao_selecionada == "3":
            print("Saindo...")
            break
        else:
            os.system("cls")
            print("Escolha uma opção válida (1, 2 ou 3)\n")
