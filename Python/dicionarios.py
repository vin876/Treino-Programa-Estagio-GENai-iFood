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

Perante a seguinte lista contendo dicionários, percorre cada item para que se encaixa na devida condição, imprimindo o nome e qual o critério de compra em que o cliente se encaixa:
# DICIONÁRIO
avaliacoes [
{"NOME": "JOAO", "PAGAMENTO": True, "DESCONTO": "POSSUI"},
{"NOME": "MARIA", "PAGAMENTO": True, "DESCONTO": "NAO POSSUI"},
{"NOME": "ABIGAIL", "PAGAMENTO": False, "DESCONTO": "POSSUI"},
{"NOME": "DIJALMA", "PAGAMENTO": False, "DESCONTO": "POSSUI"},
]

for a in avaliacoes:
 if a["PAGAMENTO"] == False and a["DESCONTO"] == "NAO POSSUI":
   print(a["NOME"], "Está com a avaliação para aprovar compras baixas")
   
 elif a["PAGAMENTO"] == True and a["DESCONTO"] == "NAO POSSUI":
   print(a["NOME"], "Está com a avaliação para aprovar compras moderadas")
   
 elif a["PAGAMENTO"] == False and a["DESCONTO"] == "POSSUI":
   print(a["NOME"], "Está com a avaliação para aprovar compras medianas")
   
 else:
   print(a["NOME"], "Está com a avaliação para aprovar compras altas")

#####AlGORITMO PENSADO PASSO A PASSO QUE FOI PENSADO#########
//uma lista de dicionarios foi concedida.
//A questão pede que percorra cada item, para verificar cada estrutura condicional e imprimir o nome dentro da lista dicionário que se encaixa no devido critério.
//Primeiro um atribuir a para a lista dicionario avaliacoes.
//Segundo criar estruturas condicionais em que os critérios de cada cliente se encaixe, para que imprima resultado para todos.
//Terceiro imprimir resultado com o nome do cliente que se encaixa em determinado critério com uma mensagem relacionada à sua permissão de compra.
