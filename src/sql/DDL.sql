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
CREATE TABLE IF NOT EXISTS Arma (
    id_arma SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    dano int NOT NULL,
    descricao char(150),
    durabilidade int NOT NULL
);

CREATE TABLE IF NOT EXISTS Caminhos (
    regiao int NOT NULL,
    regiao_destino int NOT NULL
);

CREATE TABLE IF NOT EXISTS Consumivel (
    id_consumivel SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    efeito char(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Dialogo (
    id_dialogo SERIAL PRIMARY KEY,
    npc int NOT NULL,
    fala char(50)
);

CREATE TABLE IF NOT EXISTS Habilidade (
    id_habilidade SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    dano int,
    efeito char(50),
    defesa int
);

CREATE TABLE IF NOT EXISTS Inimigo (
    id_inimigo SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    descricao char(50),
    regiao int NOT NULL,
    dano int NOT NULL,
    defesa int NOT NULL,
    vida int NOT NULL,
    "drop" int
);

CREATE TABLE IF NOT EXISTS Item_inventario (
    jogador int NOT NULL,
    item int NOT NULL,
    efeito int NOT NULL
);

CREATE TABLE IF NOT EXISTS Instancia_Inimigo (
    regiao int NOT NULL,
    inimigo int NOT NULL,
    saude int NOT NULL
);

CREATE TABLE IF NOT EXISTS Item (
    id_item SERIAL PRIMARY KEY,
    tipo_item char(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Jogador (
    id_jogador SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
    missao_atual int,
    vida int NOT NULL,
    qnt_ouro int
);

CREATE TABLE IF NOT EXISTS Loja (
    id_loja SERIAL PRIMARY KEY,
    proprietario int NOT NULL,
    regiao int NOT NULL,
    nome char(50) NOT NULL,
    descricao char(800)
);

CREATE TABLE IF NOT EXISTS Missao (
    id_missao SERIAL PRIMARY KEY,
    regiao int NOT NULL,
    recompensa int,
    nome char(50) NOT NULL,
    descricao char(150) NOT NULL,
    qnt_ouro int
);

CREATE TABLE IF NOT EXISTS Mundo (
    id_mundo SERIAL PRIMARY KEY,
    nome char(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS NPC (
    id_npc SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    regiao int NOT NULL,
);

CREATE TABLE IF NOT EXISTS Regiao (
    id_regiao SERIAL PRIMARY KEY,
    nome char(50) NOT NULL,
    mundo int NOT NULL,
);

CREATE TABLE IF NOT EXISTS Vestimenta (
    id_vestimenta SERIAL PRIMARY KEY,
    id_jogador int,
    nome char(50) NOT NULL,
    descricao char(150),
    defesa int NOT NULL,
    durabilidade int NOT NULL
);

CREATE TABLE IF NOT EXISTS Venda (
    id_venda SERIAL PRIMARY KEY,
    loja int NOT NULL,
    item int NOT NULL,
    preco int NOT NULL,
    nome char(50) NOT NULL
);

ALTER TABLE
    Arma
ADD
    CONSTRAINT "FK_01" FOREIGN KEY (id_arma) REFERENCES Item (id_item);

ALTER TABLE
    Arma
ADD
    CONSTRAINT "FK_02" FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador);

ALTER TABLE
    Caminhos
ADD
    CONSTRAINT "FK_03" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Caminhos
ADD
    CONSTRAINT "FK_04" FOREIGN KEY (regiao_destino) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Consumivel
ADD
    CONSTRAINT "FK_05" FOREIGN KEY (id_consumivel) REFERENCES Item (id_item);

ALTER TABLE
    Consumivel
ADD
    CONSTRAINT "FK_06" FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador);

ALTER TABLE
    Dialogo
ADD
    CONSTRAINT "FK_07" FOREIGN KEY (npc) REFERENCES NPC (id_npc);

ALTER TABLE
    Habilidade
ADD
    CONSTRAINT "FK_08" FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador);

ALTER TABLE
    Inimigo
ADD
    CONSTRAINT "FK_09" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Inimigo
ADD
    CONSTRAINT "FK_10" FOREIGN KEY ("drop") REFERENCES Item (id_item);

ALTER TABLE
    Item_inventario
ADD
    CONSTRAINT "FK_11" FOREIGN KEY (jogador) REFERENCES Jogador (id_jogador);

ALTER TABLE
    Item_inventario
ADD
    CONSTRAINT "FK_12" FOREIGN KEY (item) REFERENCES Item (id_item);

ALTER TABLE
    Instancia_Inimigo
ADD
    CONSTRAINT "FK_13" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Instancia_Inimigo
ADD
    CONSTRAINT "FK_14" FOREIGN KEY (inimigo) REFERENCES Inimigo (id_inimigo);

ALTER TABLE
    Jogador
ADD
    CONSTRAINT "FK_15" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Jogador
ADD
    CONSTRAINT "FK_16" FOREIGN KEY (missao_atual) REFERENCES Missao (id_missao);

ALTER TABLE
    Loja
ADD
    CONSTRAINT "FK_17" FOREIGN KEY (proprietario) REFERENCES NPC (id_npc);

ALTER TABLE
    Loja
ADD
    CONSTRAINT "FK_18" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    NPC
ADD
    CONSTRAINT "FK_19" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Missao
ADD
    CONSTRAINT "FK_20" FOREIGN KEY (regiao) REFERENCES Regiao (id_regiao);

ALTER TABLE
    Missao
ADD
    CONSTRAINT "FK_21" FOREIGN KEY (recompensa) REFERENCES Item (id_item);

ALTER TABLE
    Vestimenta
ADD
    CONSTRAINT "FK_22" FOREIGN KEY (id_vestimenta) REFERENCES Item (id_item);

ALTER TABLE
    Vestimenta
ADD
    CONSTRAINT "FK_23" FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador);

ALTER TABLE
    Venda
ADD
    CONSTRAINT "FK_24" FOREIGN KEY (loja) REFERENCES Loja (id_loja);

ALTER TABLE
    Venda
ADD
    CONSTRAINT "FK_25" FOREIGN KEY (item) REFERENCES Item (id_item);

ALTER TABLE
    Regiao
ADD
    CONSTRAINT "FK_26" FOREIGN KEY (mundo) REFERENCES Mundo (id_mundo);