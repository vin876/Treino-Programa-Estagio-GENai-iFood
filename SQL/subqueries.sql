-- Clientes com gasto acima da média geral
SELECT nome, gasto_total
FROM (
    SELECT 
        c.nome,
        SUM(p.valor_total) AS gasto_total
    FROM pedidos p
    JOIN clientes c ON p.id_cliente = c.id_cliente
    GROUP BY c.nome
) AS t
WHERE gasto_total > (
    SELECT AVG(valor_total)
    FROM pedidos
);
