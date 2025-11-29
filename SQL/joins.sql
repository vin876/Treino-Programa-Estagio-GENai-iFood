-- INNER JOIN entre pedidos e clientes
SELECT p.id_pedido, c.nome, p.valor_total
FROM pedidos p
INNER JOIN clientes c
    ON p.id_cliente = c.id_cliente;

-- LEFT JOIN para pegar clientes sem pedidos
SELECT c.nome, p.id_pedido
FROM clientes c
LEFT JOIN pedidos p
    ON c.id_cliente = p.id_cliente;

-- JOIN triplo (muito estilo iFood)
SELECT p.id_pedido, c.nome AS cliente, r.nome AS restaurante
FROM pedidos p
JOIN clientes c
    ON p.id_cliente = c.id_cliente
JOIN restaurantes r
    ON p.id_restaurante = r.id_restaurante;

