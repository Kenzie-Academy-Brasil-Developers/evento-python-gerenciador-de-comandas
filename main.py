from restaurante.gerenciador import adicionar_item_para_comanda, calcular_total_comanda

COMANDA_USUARIO = []

adicionar_item_para_comanda(quantidade=2, id_item=50, comanda=COMANDA_USUARIO)
adicionar_item_para_comanda(quantidade=100, id_item=48, comanda=COMANDA_USUARIO)
adicionar_item_para_comanda(quantidade=5, id_item=23, comanda=COMANDA_USUARIO)


total = calcular_total_comanda(COMANDA_USUARIO)
print(total)
