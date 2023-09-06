full_sql_query = """
SELECT *
FROM analises.poc_item_deserto_consolidada_v2
WHERE 1=1
    AND valor_estimado IS NOT NULL 
"""

train_sql_query = """
SELECT *
FROM analises.poc_item_deserto_consolidada_v2
WHERE 1=1
    AND valor_estimado IS NOT NULL 
    AND data_hora_prevista_abertura_sp < '2023-08-01 00:00:00.000'
"""

test_sql_query = """
SELECT *
FROM analises.poc_item_deserto_consolidada_v2
WHERE 1=1
    AND valor_estimado IS NOT NULL 
    AND data_hora_prevista_abertura_sp >= '2023-08-01 00:00:00.000'
"""