# DICIONÁRIO
cliente = {
    "id": 101,
    "nome": "João",
    "cidade": "Campinas",
    "pedidos": 15
}

print(cliente["nome"])
print(cliente.get("cidade"))

# ALTERANDO
cliente["pedidos"] += 1

# LOOP EM DICIONÁRIO
for chave, valor in cliente.items():
    print(chave, ":", valor)


###########################################

Perante a seguinte lista contendo dicionários, percorre cada condição imprimindo o nome e qual o critério de compra em que o cliente se encaixa:
# DICIONÁRIO
avaliacoes [
{"NOME": "JOAO", "PAGAMENTO": True, "DESCONTO": "POSSUI"},
{"NOME": "MARIA", "PAGAMENTO": True, "DESCONTO": "NAO POSSUI"},
{"NOME": "ABIGAIL", "PAGAMENTO": False, "DESCONTO": "POSSUI"},
{"NOME": "DIJALMA", "PAGAMENTO": False, "DESCONTO": "POSSUI"},
]

for a in avaliacoes:
