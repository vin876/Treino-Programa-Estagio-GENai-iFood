-- Classificar pedidos por valor
SELECT
    id_pedido,
    valor_total,
    CASE
        WHEN valor_total >= 100 THEN 'alto'
        WHEN valor_total >= 50 THEN 'medio'
        ELSE 'baixo'
    END AS categoria_valor
FROM pedidos;

-- Status de entrega customizado
SELECT
    id_pedido,
    status_entrega,
    CASE
        WHEN status_entrega = 'delivered' THEN 'concluído'
        WHEN status_entrega = 'canceled' THEN 'cancelado'
        ELSE 'em andamento'
    END AS status_traduzido
FROM pedidos;
