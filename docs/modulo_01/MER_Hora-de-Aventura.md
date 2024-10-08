## Histórico de versões

| Versão |    Data    | Descrição                 | Autor                                      |
| :----: | :--------: | ------------------------- | ------------------------------------------ |
| `1.0`  | 18/07/2024 | Criação do documento MER  | [Lucas Macedo](https://github.com/Luckx98) |
| `1.1`  | 21/07/2024 | Adicao de relacionamentos | [Lucas Macedo](https://github.com/Luckx98) |

# MER - Modelo Entidade Relacionamento

O Modelo Entidade Relacionamento de um bancos de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, com seus atributos e seus relacionamentos.

> Entidades: os objetos da realidade a ser modelada.<br>
> Relacionamentos: as associações entre as entidades.<br>
> Atributos: características específicas de uma entidade.<br>

## 1. Entidades

- **Jogador**
- **Itens**
  - **Arma**
  - **Vestimenta**
  - **Consumível**
- **Habilidade**
- **Loja**
- **Missão**
- **Diálogo**
- **Região**
- **Mundo**
- **NPC**
- **Inimigo**

## 2. Atributos

- **Jogador**: <ins>id_jogador</ins>, nome, regiao, missao_atual, vida;
- **Item**: <ins>id_item</ins>, tipo_item;
  - **Arma**: id_arma, id_jogador, nome, dano, descricao, durabilidade;
  - **Vestimenta**: id_vestimenta, id_jogador, nome, descricao, defesa, durabilidade;
  - **Consumível**: id_consumível, id_jogador, nome, descricao, efeito;
- **Habilidade**: <ins>id_habilidade</ins>, id_jogador, nome, descricao, dano, efeito, defesa;
- **Loja**: <ins>id_loja</ins>, nome, descricao, proprietario, regiao;
- **Missão**: <ins>id_missao</ins>, nome, regiao, descricao;
- **Região**: <ins>id_regiao</ins>, nome, mundo
- **Mundo**: <ins>id_mundo</ins>, nome
- **NPC**: <ins>id_npc</ins>, nome, regiao;
- **Diálogo**: <ins>id_dialogo</ins>, npc, fala;
- **Inimigo**: <ins>id_inimigo</ins>, nome, descricao, regiao, dano, defesa, vida, drop;

## 3. Relacionamentos

**Jogador _realiza_ Missão**

- Um jogador pode realizar nenhuma ou mais missões (0,N)
- Uma missão é realizada por apenas um ou vários jogadores (1,N)

**Jogador _possui_ Item-Arma**

- Um jogador possui nenhuma ou várias armas (0,N)
- A arma é de apenas um único jogador (1,1)

**Jogador _está_ em Região**

- O jogador pode apenas estar em um regiao (1,1)
- Uma regiao pode ter nenhum a vários jogadores (0,N)

**Jogador _possui_ Habilidade**

- O jogador possui nenhuma ou várias habilidades (0,N)
- Cada habilidade é única para jogador (1,1)

**Jogador _possui_ Item-Vestimenta**

- O jogador possui nenhuma ou uma vestimenta (0,1)
- A vestimenta é única para jogador (1,1)

**Jogador _interage_ com NPC**

- O jogador interage com nenhum ou vários NPC's (0,N)
- O NPC interage com nenhum ou um jogador (0,1)

**Jogador _compra_ em Loja**

- O jogador compra em nenhuma ou várias lojas (0,N)
- A loja vende para nenhum ou vários jogadores (0,N)

**Jogador _possui_ Itens**

- O jogador possui nenhum ou vários itens (0,N)
- O item é único para jogador (1,1)

**Missão _está_ em Região**

- Uma missão está em um ou várias regiões(1,N)
- Uma região possui apenas uma único missão (1,1)

**Mundo _possui_ Região**

- O mundo possui um ou várias regiões(1,N)
- Uma região possui apenas um mundo(1,1)

**Região _contém_ Inimigo**

- A região contém nenhum ou vários inimigos (0,N)
- O inimigo está em nenhuma ou várias regiões (0,N)

**NPC _fala_ Diálogo**

- Um NPC possui nenhuma a várias falas em um diálogo (0, N)
- Um Dialogo pertence a um único NPC (1, 1)

**NPC _possui_ Loja**

- O NPC possui nenhuma ou uma loja (0,1)
- A loja é de apenas um NPC(1,1)

**Inimigo _dropa_ Item**

- Uma inimigo ou monstro, ao sofrer um ataque, pode "liberar" apenas um único tipo de item (1,1)
- O item pode cair de nenhum ou vários (0, N)

**Item _possui exclusivamente_ tipos**

- Um item pode ser classificado apenas com uma das seguintes categorias: arma, vestimenta, consumível
