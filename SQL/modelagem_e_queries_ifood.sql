-- Top 5 restaurantes por NPS (exemplo estilo iFood)
SELECT 
    r.nome,
    AVG(a.nota) AS nps_medio
FROM avaliacao_pedidos a
JOIN pedidos p ON a.id_pedido = p.id_pedido
JOIN restaurantes r ON p.id_restaurante = r.id_restaurante
GROUP BY r.nome
ORDER BY nps_medio DESC
LIMIT 5;

-- Retenção de clientes (clientes que compraram mês após mês)
SELECT 
    id_cliente,
    COUNT(DISTINCT DATE_TRUNC('month', data_pedido)) AS meses_ativos
FROM pedidos
GROUP BY id_cliente
HAVING COUNT(DISTINCT DATE_TRUNC('month', data_pedido)) >= 3;

-- Tempo médio de entrega por cidade
SELECT 
    c.cidade,
    AVG(p.tempo_entrega) AS tempo_medio
FROM pedidos p
JOIN clientes c 
    ON p.id_cliente = c.id_cliente
GROUP BY cidade
ORDER BY tempo_medio;
