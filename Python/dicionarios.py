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

# DICIONÁRIO
avaliacoes [
{"NOME": "JOAO", "PAGAMENTO": True, "DESCONTO": "POSSUI"},
{"NOME": "MARIA", "PAGAMENTO": True, "DESCONTO": "NAO POSSUI"},
{"NOME": "ABIGAIL", "PAGAMENTO": False, "DESCONTO": "POSSUI"},
{"NOME": "DIJALMA", "PAGAMENTO": False, "DESCONTO": "POSSUI"},
]

