from restaurante.menu import MENU_DISPONIVEL


def capturar_item(id_procurado: int):
    for item in MENU_DISPONIVEL:
        if item["id"] == id_procurado:
            return item


def adicionar_item_para_comanda(id_item: int, quantidade: int, comanda: list[dict]):
    item_para_adicionar = capturar_item(id_item)

    informacoes_do_item_para_adicionar = {
        "id": item_para_adicionar["id"],
        "nome": item_para_adicionar["nome"],
        "preco": item_para_adicionar["preco"],
        "quantidade": quantidade,
        "sub_total": item_para_adicionar["preco"] * quantidade,
    }

    comanda.append(informacoes_do_item_para_adicionar)


def calcular_total_comanda(comanda: list[dict]):
    total = 0

    for item_comanda in comanda:
        # total = total + item_comanda["sub_total"]
        total += item_comanda["sub_total"]

    return total

    # list comprehension
    # total = sum(item_comanda["sub_total"] for item_comanda in comanda)

    # return total
