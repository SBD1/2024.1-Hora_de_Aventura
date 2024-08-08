-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 07/08/2024                                                --
-- Autor(es) ..............: Lucas Macedo                                            --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........: Inclusão de CREATE TABLE de todas as tabelas do banco de dados.--
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 07/08/2024 | Autor(es): Lucas Macedo                       |      --
--                            | Descricao: Inclusão das linhas de CREATE TABLE  |      --
-- --------------------------------------------------------------------------------------
BEGIN TRANSACTION;

CREATE TABLE Arma (
    id_arma SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    dano int NOT NULL,
    descricao char(150),
    durabilidade int NOT NULL,
    FOREIGN KEY (id_arma) REFERENCES Item (id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE Consumivel (
    id_consumivel SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    efeito char(50) NOT NULL,
    FOREIGN KEY (id_consumivel) REFERENCES Item (id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE Dialogo (
    id_dialogo SERIAL PRIMARY KEY,
    nome int NOT NULL,
    fala char(50),
    FOREIGN KEY (nome) REFERENCES NPC (id_npc)
);

CREATE TABLE Habilidade (
    id_habilidade SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    dano int,
    efeito char(50),
    defesa int,
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

CREATE TABLE Inimigo (
    id_inimigo SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    descricao char(50),
    regiao int NOT NULL,
    dano int NOT NULL,
    defesa int NOT NULL,
    vida int NOT NULL,
    drop int,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao),
    FOREIGN KEY (drop) REFERENCES Regiao (id_item)
);

CREATE TABLE Item (
    id_item SERIAL PRIMARY KEY,
    tipo_item char(50) NOT NULL,
);

CREATE TABLE Jogador (
    id_jogador SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
    missao_atual int,
    vida int NOT NULL,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao),
    FOREIGN KEY (missao_atual) REFERENCES Missao (id_missao)
);

CREATE TABLE Loja (
    id_loja SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    descricao char(800),
    proprietario int,
    regiao int,
    FOREIGN KEY (proprietario) REFERENCES NPC (id_npc),
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao)
);

CREATE TABLE Missao (
    id_missao SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
    descricao char(150),
    FOREIGN KEY (regiao) REFERENCES Jogador (id_regiao)
);

CREATE TABLE Mundo (
    id_mundo SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
);

CREATE TABLE NPC (
    id_npc SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
    FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao)
);

CREATE TABLE Regiao (
    id_regiao SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    mundo int NOT NULL,
    FOREIGN KEY (mundo) REFERENCES Mundo (id_mundo)
);

CREATE TABLE Vestimenta (
    id_vestimenta SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    defesa int NOT NULL,
    durabilidade int NOT NULL,
    FOREIGN KEY (id_vestimenta) REFERENCES Item (id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
);

COMMIT;