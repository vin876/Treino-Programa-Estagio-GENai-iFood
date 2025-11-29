-- Contar pedidos
SELECT COUNT(*) AS total_pedidos
FROM pedidos;

-- Média do valor dos pedidos
SELECT AVG(valor_total) AS ticket_medio
FROM pedidos;

-- Soma do faturamento
SELECT SUM(valor_total) AS faturamento_total
FROM pedidos;

-- Agrupar por restaurante
SELECT r.nome, SUM(p.valor_total) AS faturamento
FROM pedidos p
JOIN restaurantes r
    ON p.id_restaurante = r.id_restaurante
GROUP BY r.nome
ORDER BY faturamento DESC;
