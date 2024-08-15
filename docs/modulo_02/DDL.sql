-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 07/08/2024                                                --
-- Autor(es) ..............: Lucas Macedo                                            --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........: Inclusão de CREATE TABLE de todas as tabelas do banco de dados.--
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 07/08/2024 | Autor(es): Lucas Macedo                       |      --
--                            | Descricao: Inclusão das linhas de CREATE TABLE  |      --
-- | Atualizacao : 14/08/2024 | Autor(es): Lucas Macedo                       |      --
--                            | Descricao: Atualizaçao das tabelas   |      --
-- --------------------------------------------------------------------------------------
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS Arma (
    id_arma SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    dano int NOT NULL,
    descricao char(150),
    durabilidade int NOT NULL,
    FOREIGN KEY (id_arma) REFERENCES Item (id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE IF NOT EXISTS Consumivel (
    id_consumivel SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    efeito char(50) NOT NULL,
    FOREIGN KEY (id_consumivel) REFERENCES Item (id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE IF NOT EXISTS Dialogo (
    id_dialogo SERIAL PRIMARY KEY,
    npc int NOT NULL,
    fala char(50),
    FOREIGN KEY (npc) REFERENCES NPC (id_npc)
);

CREATE TABLE IF NOT EXISTS Habilidade (
    id_habilidade SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    dano int,
    efeito char(50),
    defesa int,
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE IF NOT EXISTS Inimigo (
    id_inimigo SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    descricao char(50),
    regiao int NOT NULL,
    dano int NOT NULL,
    defesa int NOT NULL,
    vida int NOT NULL,
    drop int,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao),
    FOREIGN KEY (drop) REFERENCES Item (id_item)
);

CREATE TABLE IF NOT EXISTS Item_inventario (
    jogador int NOT NULL,
    item int NOT NULL,
    efeito int NOT NULL,
    FOREIGN KEY (jogador) REFERENCES Jogador (id_jogador),
    FOREIGN KEY (item) REFERENCES Item (id_item)
);

CREATE TABLE IF NOT EXISTS Instancia_Inimigo (
    regiao int NOT NULL,
    inimigo int NOT NULL,
    saude int NOT NULL,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao),
    FOREIGN KEY (inimigo) REFERENCES Inimigo (id_inimigo)
);

CREATE TABLE IF NOT EXISTS Item (
    id_item SERIAL PRIMARY KEY,
    tipo_item char(50) NOT NULL,
);

CREATE TABLE IF NOT EXISTS Jogador (
    id_jogador SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
    missao_atual int,
    vida int NOT NULL,
    qnt_ouro int,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao),
    FOREIGN KEY (missao_atual) REFERENCES Missao (id_missao)
);

CREATE TABLE IF NOT EXISTS Loja (
    id_loja SERIAL PRIMARY KEY,
    proprietario int NOT NULL,
    regiao int NOT NULL,
    nome char(50) NOT NULL,
    descricao char(800),
    FOREIGN KEY (proprietario) REFERENCES NPC (id_npc),
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao)
);

CREATE TABLE IF NOT EXISTS Missao (
    id_missao SERIAL PRIMARY KEY,
    regiao int NOT NULL,
    recompensa int,
    nome char(50) NOT NULL,
    descricao char(150) NOT NULL,
    qnt_ouro int,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao) FOREIGN KEY (recompensa) REFERENCES Item (id_item)
);

CREATE TABLE IF NOT EXISTS Mundo (
    id_mundo SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
);

CREATE TABLE IF NOT EXISTS NPC (
    id_npc SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao)
);

CREATE TABLE IF NOT EXISTS Regiao (
    id_regiao SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    mundo int NOT NULL,
    FOREIGN KEY (mundo) REFERENCES Mundo (id_mundo)
);

CREATE TABLE IF NOT EXISTS Vestimenta (
    id_vestimenta SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    defesa int NOT NULL,
    durabilidade int NOT NULL,
    FOREIGN KEY (id_vestimenta) REFERENCES Item (id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE IF NOT EXISTS Venda (
    id_venda SERIAL PRIMARY KEY,
    loja int NOT NULL,
    item int NOT NULL,
    preco int NOT NULL,
    nome char(50) NOT NULL,
    FOREIGN KEY (loja) REFERENCES Loja (id_loja),
    FOREIGN KEY (item) REFERENCES Item (id_item)
);

COMMIT;