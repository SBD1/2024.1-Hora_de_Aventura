-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 09/09/2024                                                --
-- Autor(es) ..............: Lucas Macedo                                              --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........: Criando triggers para especialização.                          --
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 09/09/2024 | Autor(es): Lucas Macedo                         |      --
--                            | Descricao: Criando e populando arquivo          |      --
-- --------------------------------------------------------------------------------------
-- TRIGGER Item (Generalização e especialização)
CREATE
OR REPLACE FUNCTION check_item_f() RETURNS trigger AS $ check_item_f $ BEGIN PERFORM *
FROM
    Item
WHERE
    nome = NEW.nome
    AND id_jogador = NEW.id_jogador;

IF FOUND THEN RAISE EXCEPTION 'Este item já pertence ao jogador';

END IF;

RETURN NEW;

END;

$ check_item_f $ LANGUAGE plpgsql;

-- DROP TRIGGER check_arma ON Arma;
CREATE TRIGGER check_arma BEFORE
INSERT
    OR
UPDATE
    ON Arma FOR EACH ROW EXECUTE PROCEDURE check_item_f();

-- DROP TRIGGER check_vestimenta ON Vestimenta;
CREATE TRIGGER check_vestimenta BEFORE
INSERT
    OR
UPDATE
    ON Vestimenta FOR EACH ROW EXECUTE PROCEDURE check_item_f();

-- TRIGGER Npc (Generalização e especialização)
CREATE
OR REPLACE FUNCTION check_dialogo_unique_f() RETURNS trigger AS $ check_dialogo_unique_f $ BEGIN PERFORM *
FROM
    Dialogo
WHERE
    npc = NEW.npc
    AND fala = NEW.fala;

IF FOUND THEN RAISE EXCEPTION 'Este NPC já possui este diálogo.';

END IF;

RETURN NEW;

END;

$ check_dialogo_unique_f $ LANGUAGE plpgsql;

-- DROP TRIGGER check_dialogo ON Vestimenta;
CREATE TRIGGER check_dialogo BEFORE
INSERT
    OR
UPDATE
    ON Dialogo FOR EACH ROW EXECUTE PROCEDURE check_dialogo_unique_f();

-- TRIGGER Jogador (Generalização e especialização)
CREATE
OR REPLACE FUNCTION check_jogador_vida_f() RETURNS trigger AS $ check_jogador_vida_f $ BEGIN IF NEW.vida < 1 THEN RAISE EXCEPTION 'A vida do jogador deve ser pelo menos 1.';

ELSIF NEW.vida = 0 THEN RAISE EXCEPTION 'O jogador está morto.';

END IF;

RETURN NEW;

END;

$ check_jogador_vida_f $ LANGUAGE plpgsql;

-- DROP TRIGGER check_jogador ON Jogador;
CREATE TRIGGER check_jogador BEFORE
INSERT
    OR
UPDATE
    ON Jogador FOR EACH ROW EXECUTE PROCEDURE check_jogador_vida_f();

-- TRIGGER Venda (Generalização e especialização)
CREATE
OR REPLACE FUNCTION check_venda_preco_f() RETURNS trigger AS $ check_venda_preco_f $ BEGIN IF NEW.preco <= 0 THEN RAISE EXCEPTION 'O preço de venda deve ser maior que zero.';

END IF;

RETURN NEW;

END;

$ check_venda_preco_f $ LANGUAGE plpgsql;

-- DROP TRIGGER check_venda ON Venda;
CREATE TRIGGER check_venda BEFORE
INSERT
    OR
UPDATE
    ON Venda FOR EACH ROW EXECUTE PROCEDURE check_venda_preco_f();

-- Trigger para atualizar a quantidade de ouro do jogador após completar uma missão
CREATE
OR REPLACE FUNCTION update_jogador_missao_f() RETURNS trigger AS $ update_jogador_missao_f $ BEGIN IF (TG_OP = 'UPDATE') THEN -- Atualiza o jogador quando a missão atual é alterada
IF (
    NEW.missao_atual IS DISTINCT
    FROM
        OLD.missao_atual
) THEN -- Caso a missão atual tenha sido completada
IF NEW.missao_atual IS NULL THEN -- Aumenta a quantidade de ouro do jogador com a recompensa da missão completada
UPDATE
    Jogador
SET
    qnt_ouro = qnt_ouro + OLD.qnt_ouro
WHERE
    id_jogador = OLD.id_jogador;

END IF;

END IF;

END IF;

RETURN NEW;

END;

$ update_jogador_missao_f $ LANGUAGE plpgsql;

-- DROP TRIGGER update_missao ON Venda;
CREATE TRIGGER update_missao
AFTER
UPDATE
    ON Jogador FOR EACH ROW EXECUTE PROCEDURE update_jogador_missao_f();

SELECT
    event_object_table AS table_name,
    trigger_name
FROM
    information_schema.triggers
GROUP BY
    table_name,
    trigger_name
ORDER BY
    table_name,
    trigger_name