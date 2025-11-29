-- Ranking dos restaurantes por faturamento
SELECT 
    r.nome,
    SUM(p.valor_total) AS faturamento,
    RANK() OVER (ORDER BY SUM(p.valor_total) DESC) AS rank_faturamento
FROM pedidos p
JOIN restaurantes r
    ON p.id_restaurante = r.id_restaurante
GROUP BY r.nome;

-- Média móvel (tempo de entrega)
SELECT
    id_pedido,
    tempo_entrega,
    AVG(tempo_entrega) OVER (
        ORDER BY data_pedido
        ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
    ) AS media_movel_5
FROM pedidos;
