-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 19/08/2024                                                --
-- Autor(es) ..............: Lucas Macedo                                              --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........: Consulta das tabelas do banco de dados.                        --
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 19/08/2024 | Autor(es): Lucas Macedo e Luana Medeiros            |  --
--                            | Descricao: Inclusão das consultas do banco de dados |  --
-- --------------------------------------------------------------------------------------
BEGIN TRANSACTION;

-- Consulta de Nome e Dano da Tabela Arma
SELECT
    nome,
    dano
FROM
    Arma
WHERE
    id_jogador = 1;

-- Selecionar o id do jogador 
-- Consulta de Nome e Efeito da Tabela Consumivel
SELECT
    nome,
    efeito
FROM
    Consumivel
WHERE
    id_jogador = 1;

-- Selecionar o id do jogador 
-- Consulta Fala da Tabela Dialogo
SELECT
    fala
FROM
    Dialogo
WHERE
    npc = 1;

-- Consulta de atributos da Tabela Habilidade
SELECT
    *
FROM
    Habilidade
WHERE
    id_jogador = 1;

-- Consulta as regiões com a maior quantidade de inimigos instanciados, incluindo o nome da região e o total de inimigos da Tabela Instancia_Inimigo
SELECT
    Regiao.nome AS nome_regiao,
    COUNT(Instancia_Inimigo.inimigo) AS total_inimigos
FROM
    Instancia_Inimigo
    JOIN Regiao ON Instancia_Inimigo.regiao = Regiao.id_regiao
GROUP BY
    Regiao.nome
ORDER BY
    total_inimigos DESC;

-- Consulta todos os itens no inventário de um jogador específico da Tabela Item_inventario
SELECT
    Item.tipo_item,
    Item_inventario.efeito
FROM
    Item_inventario
    JOIN Item ON Item_inventario.item = Item.id_item
WHERE
    Item_inventario.jogador = 1;

-- Consulta todas as missões disponíveis em uma região específica da Tabela Missao
SELECT
    nome,
    descricao,
    qnt_ouro
FROM
    Missao
WHERE
    regiao = 1;

-- Consulta o nome dos NPCs que possuem lojas em uma determinada região e o total de itens disponíveis para venda em suas lojas da Tabela NPC
SELECT
    NPC.nome AS nome_npc,
    COUNT(Venda.id_venda) AS total_itens_venda
FROM
    NPC
    JOIN Loja ON NPC.id_npc = Loja.proprietario
    JOIN Venda ON Loja.id_loja = Venda.loja
WHERE
    Loja.regiao = 1
GROUP BY
    NPC.nome;

-- Consulta o nome dos jogadores que possuem pelo menos uma arma com dano acima de 50 e uma vestimenta com defesa acima de 30 da Tabela Jogador
SELECT
    DISTINCT Jogador.nome
FROM
    Jogador
    JOIN Arma ON Jogador.id_jogador = Arma.id_jogador
    JOIN Vestimenta ON Jogador.id_jogador = Vestimenta.id_jogador
WHERE
    Arma.dano > 50
    AND Vestimenta.defesa > 30;

-- Consulta o nome dos jogadores que possuem itens do tipo "Consumível" em seu inventário e os efeitos desses itens da Tabela Consumivel
SELECT
    Jogador.nome AS nome_jogador,
    Consumivel.nome AS nome_consumivel,
    Consumivel.efeito
FROM
    Consumivel
    JOIN Jogador ON Consumivel.id_jogador = Jogador.id_jogador
    JOIN Item ON Consumivel.id_consumivel = Item.id_item
WHERE
    Item.tipo_item = 'Consumível';

-- Consulta as regiões onde há maior diversidade de tipos de itens droppados por inimigos da Tabela Inimigo
SELECT
    Regiao.nome AS nome_regiao,
    COUNT(DISTINCT Item.tipo_item) AS diversidade_itens
FROM
    Inimigo
    JOIN Item ON Inimigo.drop = Item.id_item
    JOIN Regiao ON Inimigo.regiao = Regiao.id_regiao
GROUP BY
    Regiao.nome
ORDER BY
    diversidade_itens DESC;

-- Consulta uma lista de todos os itens de tipo "Consumível" que estão à venda em uma loja específica, incluindo o nome da loja e o preço dos itens da Tabela Venda
SELECT
    Loja.nome AS nome_loja,
    Venda.nome AS nome_item,
    Venda.preco
FROM
    Venda
    JOIN Loja ON Venda.loja = Loja.id_loja
    JOIN Item ON Venda.item = Item.id_item
WHERE
    Item.tipo_item = 'Consumível'
    AND Loja.id_loja = 1;

COMMIT;