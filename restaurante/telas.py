import os
from restaurante.gerenciador import adicionar_item_para_comanda
from datetime import datetime


COMANDA_USUARIO = []


def tela_checkout():
    os.system("cls")

    while True:
        for item in COMANDA_USUARIO:
            print(
                f"{item['quantidade']}un. - {item['nome']} - R$ {item['preco']} - {item['sub_total']}"
            )

        print("\nO que deseja fazer?\n")
        print("  [1]. Voltar ao menu principal")
        print("  [2]. Fechar comanda e salvar relatório\n")

        opcao_selecionada = input("Digite uma opção válida (1 ou 2): ")
        os.system("cls")

        if opcao_selecionada == "1":
            break
        elif opcao_selecionada == "2":
            horario = datetime.now()
            print(f"Horario atual: {horario}")
            print("\nGerar relatório")
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
