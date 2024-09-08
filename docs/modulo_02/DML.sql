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
    Arma (nome, dano, durabilidade)
VALUES
    ('Espada', 10, 100),
    ('Machado', 15, 100),
    ('Arco', 5, 100),
    ('Flecha', 5, 100),
    ('Cajado', 10, 100),
    ('Varinha', 5, 100),
    ('Adaga', 7, 100),
    ('Lança', 8, 100),
    ('Martelo', 12, 100),
    ('Besta', 10, 100);

INSERT INTO
    Caminhos (regiao, regiao_destino)
VALUES
    (1, 2),
    (2, 3),
    (3, 1);

INSERT INTO
    Consumivel (nome, efeito)
VALUES
    ('Poção de Vida', 'Cura 50 de vida'),
    ('Poção de Mana', 'Recupera 50 de mana'),
    ('Poção de Força', 'Aumenta o dano em 10%'),
    ('Poção de Defesa', 'Aumenta a defesa em 10%'),
    (
        'Poção de Velocidade',
        'Aumenta a velocidade em 10%'
    );

INSERT INTO
    Dialogo (npc, fala)
VALUES
    (1, 'Olá, aventureiro!'),
    (2, 'Você está perdido?'),
    (3, 'Precisa de ajuda?'),
    (4, 'Cuidado com os inimigos!'),
    (5, 'Boa sorte!');

INSERT INTO
    Habilidade (nome, dano, efeito, defesa)
VALUES
    (
        'Ataque Rápido',
        10,
        'Aumenta a velocidade em 10%',
        0
    ),
    ('Defesa', 0, 'Aumenta a defesa em 10%', 10),
    ('Cura', 0, 'Cura 50 de vida', 0),
    ('Ataque Forte', 20, 'Aumenta o dano em 10%', 0),
    (
        'Ataque Mágico',
        15,
        'Aumenta o dano mágico em 10%',
        0
    );

INSERT INTO
    Inimigo (nome, regiao, dano, defesa, vida)
VALUES
    ('Goblin', 1, 5, 2, 20),
    ('Orc', 2, 10, 5, 50),
    ('Esqueleto', 3, 7, 3, 30),
    ('Zumbi', 4, 8, 4, 40);

INSERT INTO
    Item_inventario (id_jogador, id_item, quantidade)
VALUES
    (1, 1, 1),
    (1, 2, 1);

INSERT INTO
    Instancia_Inimigo (regiao, inimigo, vida)
VALUES
    (1, 1, 20),
    (2, 1, 50),
    (3, 1, 30),
    (4, 1, 40);

INSERT INTO
    Item (id_item, tipo_item)
VALUES
    (1, 'Arma'),
    (2, 'Vestimenta'),
    (3, 'Consumivel');

INSERT INTO
    Jogador (nome, regiao, missao_atual, vida, qnt_ouro)
VALUES
    ('Lucas', 1, 1, 500, 1900),
    ('Ciro', 2, 1, 500, 0),
    ('Luana', 3, 1, 500, 0);

INSERT INTO
    Loja (proprietario, regiao, nome)
VALUES
    (1, 1, 'Loja do reino doce'),
    (2, 2, 'Loja do palácio de fogo'),
    (3, 3, 'Loja da reino gelado');

INSERT INTO
    Missao (regiao, recompensa, nome, descricao)
VALUES
    (
        1,
        1,
        'Missão 1',
        'Invada o castelo do reino doce'
    ),
    (2, 2, 'Missão 2', 'Mate 5 orcs'),
    (3, 2, 'Missão 3', 'Converse com o rei gelado'),
    (4, 1, 'Missão 4', 'Mate 8 zumbis');

INSERT INTO
    Mundo (nome)
VALUES
    ('Reino doce'),
    ('Palácio de fogo'),
    ('Reino gelado');

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
    Regiao (nome, mundo)
VALUES
    ('Floresta encantada', 1),
    ('Montanha em cinzas', 2),
    ('Caverna dos congelados', 3),
    ('Deserto salgado', 1);

INSERT INTO
    Vestimenta (
        id_vestimenta,
        id_jogador,
        nome,
        defesa,
        durabilidade
    )
VALUES
    (1, 1, 'Armadura de ferro', 10, 100),
    (2, 1, 'Armadura de couro', 5, 100),
    (3, 2, 'Armadura de ferro', 10, 100),
    (4, 2, 'Armadura de couro', 5, 100),
    (5, 3, 'Armadura de ferro', 10, 100),
    (6, 3, 'Armadura de couro', 5, 100);

INSERT INTO
    Venda (loja, item, preco, nome)
VALUES
    (1, 1, 100, 'Espada doce'),
    (1, 2, 20, 'Armadura de jujuba'),
    (2, 1, 80, 'Escudo de fogo'),
    (2, 2, 90, 'Elmo de brasa'),
    (3, 1, 350, 'Manopla de gelo'),
    (3, 2, 60, 'Botas de neve');