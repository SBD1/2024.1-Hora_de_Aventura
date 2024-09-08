-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 14/08/2024                                                --
-- Autor(es) ..............: Lucas Macedo                                              --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........:  Carga de todas as tabelas do banco de dados.                  --
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 07/08/2024 | Autor(es): Lucas Macedo                         |      --
--                            | Descricao: Inclusão das linhas de INSERT INTO   |      --
-- --------------------------------------------------------------------------------------

INSERT INTO
    Mundo (nome)
VALUES
    ('Reino doce'),
    ('Palácio de fogo'),
    ('Reino gelado');

INSERT INTO
    Item (id_item, tipo_item)
VALUES
    (1, 'Arma'),
    (2, 'Vestimenta'),
    (3, 'Consumivel');

INSERT INTO
    Caminhos (regiao, regiao_destino)
VALUES
    (1, 2),
    (2, 3),
    (3, 1);

INSERT INTO
    Regiao (nome, mundo)
VALUES
    ('Floresta encantada', 1),
    ('Montanha em cinzas', 2),
    ('Caverna dos congelados', 3),
    ('Deserto salgado', 1);

INSERT INTO
    NPC (nome, regiao)
VALUES
    ('Rei doce', 1),
    ('Princesa Jujuba', 1),
    ('Rei fogo', 2),
    ('Princesa de fogo', 2),
    ('Rei gelado', 3),
    ('Gunther', 3);

INSERT INTO
    Missao (regiao, recompensa, nome, descricao)
VALUES
    (1, NULL, 'Missão 1', 'Invada o castelo do reino doce' ),
    (2, NULL, 'Missão 2', 'Mate 5 orcs'),
    (3, NULL, 'Missão 3', 'Converse com o rei gelado'),
    (4, NULL, 'Missão 4', 'Mate 8 zumbis');

INSERT INTO
    Jogador (nome, regiao, missao_atual, vida, qnt_ouro)
VALUES
    ('Lucas', 1, NULL, 500, 1900),
    ('Ciro', 2, NULL, 500, 0),
    ('Luana', 3, NULL, 500, 0);
