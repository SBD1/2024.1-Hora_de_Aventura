## Histórico de versões

| Versão |    Data    | Descrição               | Autor                                      |
| :----: | :--------: | ----------------------- | ------------------------------------------ |
| `1.0`  | 21/07/2024 | Criação do documento DD | [Lucas Macedo](https://github.com/Luckx98) |
| `2.0`  | 09/09/2024 | Alteracao de dados      | [Lucas Macedo](https://github.com/Luckx98) |

# DD - Dicionário de Dados

> "Um dicionário de dados é uma coleção de nomes, atributos e definições sobre elementos de dados que estão sendo usados ​​em seu estudo. [...] O objetivo de um dicionário de dados é explicar o que todos os nomes e valores de variáveis ​​em sua planilha realmente significam."(Dados Científicos: como construir metadados, descrição, readme, dicionário-de-dados e mais; Agência de Bibliotecas e Coleções Digitais da Universidade de São Paulo)

## Entidade: Arma

#### Descrição: A entidade Arma armazena as características de arma, como identificador da arma, os dados do jogador, o nome da arma, o quanto de dano que ela causa, descrição e quanto ela dura;

#### Observação: Esta tabela possui chave estrangeira da entidade `Jogador, Item`.

| Nome Variável |     Tipo     |         Descrição         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-----------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|    id_arma    |     int      |   Identificador da arma   |       1-500        |          não           |  PK, FK  |                   |
|  id_jogador   |     int      | Identificador do jogador  |       1-500        |          sim           |    FK    |                   |
|     nome      | varchar[50]  |       Nome da arma        |      a-z, A-Z      |          não           |          |                   |
|     dano      |     int      |    Quantidade de dano     |       1-200        |          não           |          |                   |
|   descricao   | varchar[150] |     Descrição da arma     |      a-z, A-Z      |          sim           |          |                   |
| durabilidade  |     int      | Quanto de uso a arma dura |       1-200        |          não           |          |                   |

## Entidade: Caminhos

#### Descrição: A entidade Caminhos armazena as informações dos caminhos que o jogador pode seguir, como a região de origem e a região de destino.

#### Observação: Esta tabela possui duas chave estrangeira da entidade `Regiao`.

| Nome Variável  | Tipo |    Descrição    | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :------------: | :--: | :-------------: | :----------------: | :--------------------: | :------: | ----------------- |
|     regiao     | int  | Região de saída |       1-500        |          não           |    FK    |                   |
| regiao_destino | int  | Região a seguir |       1-500        |          não           |    FK    |                   |

## Entidade: Consumível

#### Descrição: A entidade Consumível armazena as características do item que é consumível pelo usuário, como identificador de consumível, seu nome, sua descrição e o efeito que possui;

#### Observação: Esta tabela possui chave estrangeira da entidade `Jogador,Item`.

| Nome Variável |     Tipo     |          Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
| id_consumivel |     int      | Identificador do consumível |       1-500        |          não           |  PK, FK  |                   |
|  id_jogador   |     int      |  Identificador do jogador   |       1-500        |          sim           |    FK    |                   |
|     nome      | varchar[50]  |     Nome do consumível      |      a-z, A-Z      |          não           |          |                   |
|   descricao   | varchar[150] |   Descrição do consumível   |      a-z, A-Z      |          sim           |          |                   |
|    efeito     | varchar[50]  |    Qual o efeito que tem    |      a-z, A-Z      |          não           |          |                   |

## Entidade: Diálogo

#### Descrição: A entidade Diálogo armazena as informações dos diálogos que um npc fala, como identificador, o npc que fala e o texto que se refere a fala

#### Observação: Essa tabela possui chave estrangeira das entidades `NPC`.

| Nome Variável |    Tipo     |        Descrição         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :----------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|  id_dialogo   |     int     | Identificador do diálogo |       1-500        |          não           |    PK    |                   |
|      npc      |     int     | Npc que possui o diálogo |       1-500        |          não           |    FK    |                   |
|     fala      | varchar[50] |   Texto que o npc fala   |      a-z, A-Z      |          sim           |          |                   |

## Entidade: Habilidade

#### Descrição: A entidade Habilidade armazena as informações das habilidades que podem ser utilizadas pelo jogador, como o identificador de habilidade, seu nome, sua descrição de como funciona, o dano que possui, o efeito que possui e a defesa que possui.

#### Observação: Essa tabela possui chave estrangeira das entidades `Jogador`.

| Nome Variável |     Tipo     |          Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
| id_habilidade |     int      | Identificador da habilidade |       1-500        |          não           |    PK    |                   |
|  id_jogador   |     int      |  Identificador do jogador   |       1-500        |          sim           |    FK    |                   |
|     nome      | varchar[50]  |     Nome da habilidade      |      a-z, A-Z      |          não           |          |                   |
|   descricao   | varchar[150] |   Descrição da habilidade   |      a-z, A-Z      |          sim           |          |                   |
|     dano      |     int      |     Quantidade de dano      |       1-200        |          sim           |          |                   |
|    efeito     | varchar[50]  |    Efeito da habilidade     |      a-z, A-Z      |          sim           |          |                   |
|    defesa     |     int      |    Quantidade de defesa     |       1-200        |          sim           |          |                   |

## Entidade: Inimigo

#### Descrição: A entidade inimigo armazena as características dos inimigos encontrados, como identificador, seu nome, a descrição de como é, a região que se encontra, o dano que ele possui, a quantidade de defesa, sua vida e se ele ao morrer dropa item

#### Observação: Essa tabela possui chave estrangeira das entidades `Região, Item`.

| Nome Variável |    Tipo     |        Descrição         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :----------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|  id_inimigo   |     int     | Identificador do inimigo |       1-500        |          não           |    PK    |                   |
|     nome      | varchar[50] |     Nome do inimigo      |      a-z, A-Z      |          não           |          |                   |
|   descricao   | varchar[50] |   Descrição do Inimigo   |      a-z, A-Z      |          sim           |          |                   |
|    regiao     |     int     | Identificador da região  |       1-500        |          não           |    FK    |                   |
|     dano      |     int     |    Quantidade de dano    |       1-400        |          não           |          |                   |
|    defesa     |     int     |   Quantidade de defesa   |       1-400        |          não           |          |                   |
|     vida      |     int     |    Quantidade de vida    |       1-500        |          não           |          |                   |
|     drop      |     int     | Item que o inimigo dropa |       1-500        |          sim           |    FK    |                   |

## Entidade: Instancia Inimigo

#### Descrição: A entidade inimigo armazena as características dos inimigos encontrados, como identificador, seu nome, a descrição de como é, a região que se encontra, o dano que ele possui, a quantidade de defesa, sua vida e se ele ao morrer dropa item

#### Observação: Essa tabela possui chave estrangeira das entidades `Região, Item`.

|    Nome Variável     | Tipo |             Descrição              | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :------------------: | :--: | :--------------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
| id_instancia_inimigo | int  | Identificador da instancia inimigo |       1-500        |          não           |  PK, FK  |                   |
|        regiao        | int  |       Regiao que se encontra       |       1-500        |          não           |  PK, FK  |                   |
|        saude         | int  |          Saude do Inimigo          |       1-500        |          nao           |          |                   |

## Entidade: Item

#### Descrição: A entidade Item armazena as informações de identificação do item e seu tipo

#### Observação: Os itens podem ser classificados em 3 tipos, sendo eles: `Arma, Vestimenta, Consumível`.

| Nome Variável |    Tipo     |           Descrição           | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :---------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|    id_item    |     int     |     Identificador da arma     |       1-500        |          não           |    PK    |                   |
|   tipo_item   | varchar[50] | Identificação do tipo de item |      a-z, A-Z      |          não           |          |                   |

## Entidade: Jogador

#### Descrição: A entidade Jogador descreve as características do personagem jogável, como identificador do jogador, o seu nome, a região que ele se encontra, a missão que está atualmente, a quantidade de vida que ele tem e quais itens tem

#### Observação: Essa tabela possui chave estrangeira das entidades `Região, Missão, Item`.

| Nome Variável |    Tipo     |           Descrição           | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :---------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|  id_jogador   |     int     |   Identificador do jogador    |       1-500        |          não           |    PK    |                   |
|     nome      | varchar[50] |        Nome do jogador        |      a-z, A-Z      |          não           |          |                   |
|    regiao     |     int     |    Identificador da região    |       1-500        |          não           |    FK    |                   |
| missao_atual  |     int     | Identificador da missão atual |       1-500        |          sim           |    FK    |                   |
|     vida      |     int     |      Quantidade de vida       |       1-500        |          não           |          |                   |
|   qnt_ouro    |     int     |      Quantidade de ouro       |       min. 0       |          sim           |          |                   |

## Entidade: Loja

#### Descrição: A entidade Loja armazena as informações das lojas, como identificador da loja, o seu nome, descrição do que vende, os dados do proprietário e a região que está localizada

#### Observação: Essa tabela possui chave estrangeira das entidades `NPC, Região`.

| Nome Variável |     Tipo     |       Descrição       | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|    id_loja    |     int      | Identificador da loja |       1-500        |          não           |    PK    |                   |
|     nome      | varchar[50]  |     Nome da loja      |      a-z, A-Z      |          não           |          |                   |
|   descricao   | varchar[150] |   Descrição da loja   |      a-z, A-Z      |          sim           |          |                   |
| proprietario  |     int      | Proprietario da loja  |       1-500        |          não           |    FK    |                   |
|    regiao     |     int      |    Região que está    |       1-500        |          não           |    FK    |                   |

## Entidade: Missão

#### Descrição: A entidade Missão armazena as informações das missões, como o identificador, o seu nome, a região em que a missão se encontra, sua descrição explicando seu funcionamento e sua recompensa

#### Observação: Essa tabela possui chave estrangeira das entidades `Região, Item`.

| Nome Variável |     Tipo     |         Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   id_missao   |     int      |  Identificador da missão   |       1-500        |          não           |    PK    |                   |
|    regiao     |     int      | A região que a missão está |       1-500        |          não           |    FK    |                   |
|  recompensa   |     int      |    Recompensa da missao    |       min. 0       |          sim           |          |                   |
|     nome      | varchar[50]  |       Nome da missão       |      a-z, A-Z      |          não           |          |                   |
|   descricao   | varchar[150] |    Descrição da missão     |      a-z, A-Z      |          nao           |          |                   |
|   qnt_ouro    |     int      |     Quantidade de outo     |       min. 0       |          sim           |          |                   |

## Entidade: Mundo

#### Descrição: A entidade Mundo armazena as características do mundo, como identificador e seu nome

#### Observação: O mundo é formado por diferentes regiões e cada região tem uma missão diferente

| Nome Variável |    Tipo     |       Descrição        | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :--------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   id_mundo    |     int     | Identificador do mundo |       1-500        |          não           |    PK    |                   |
|     nome      | varchar[50] |     Nome do mundo      |      a-z, A-Z      |          não           |          |                   |

## Entidade: NPC

#### Descrição: A entidade NPC armazena as características dos personagens não jogaveis e que pode interagir durante a jornada, como identificador, seu nome e a região que ele se encontra

#### Observação: Essa tabela possui chave estrangeira das entidades `Região`.

| Nome Variável |    Tipo     |       Descrição        | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :--------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|    id_npc     |     int     |  Identificador do npc  |       1-500        |          não           |    PK    |                   |
|     nome      | varchar[50] |      Nome do npc       |      a-z, A-Z      |          não           |          |                   |
|    regiao     |     int     | Região que se encontra |       1-500        |          não           |    FK    |                   |

## Entidade: Região

#### Descrição: A entidade Região armazena as características da região, como o identificador, o seu nome e o mundo que está.

#### Observação: Essa tabela possui chave estrangeira das entidades `Mundo`.

| Nome Variável |    Tipo     |         Descrição         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :-----------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   id_regiao   |     int     |  Identificador da região  |       1-500        |          não           |    PK    |                   |
|     nome      | varchar[50] |      Nome da região       |      a-z, A-Z      |          não           |          |                   |
|     mundo     |     int     | O mundo que a região está |       1-500        |          não           |    FK    |                   |

## Entidade: Vestimenta

#### Descrição: A entidade Vestimenta armazena as características de vestimenta, como o seu identificador, os dados do jogador, o nome da vestimenta, o quanto de dano que defende, descrição e quanto ela dura;

#### Observação: Esta tabela possui chave estrangeira da entidade `Jogador, Item`.

| Nome Variável |     Tipo     |            Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-----------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
| id_vestimenta |     int      |   Identificador da vestimenta   |       1-500        |          não           |  PK, FK  |                   |
|  id_jogador   |     int      |    Identificador do jogador     |       1-500        |          sim           |    FK    |                   |
|     nome      | varchar[50]  |       Nome da vestimenta        |      a-z, A-Z      |          não           |          |                   |
|   descricao   | varchar[150] |     Descrição da vestimenta     |      a-z, A-Z      |          sim           |          |                   |
|    defesa     |     int      |      Quantidade de defesa       |       1-200        |          não           |          |                   |
| durabilidade  |     int      | Quanto de uso a vestimenta dura |       1-200        |          não           |          |                   |

## Entidade: Venda

#### Descrição: A entidade Venda armazena as informações das vendas, como identificador da venda, a loja que está vendendo, o item que está sendo vendido, o nome da loja e o preço do item

#### Observação: Esta tabela possui chave estrangeira da entidade `Loja, Item`.

| Nome Variável |    Tipo     |          Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :-------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   id_venda    |     int     | Identificador da vestimenta |       1-500        |          não           |    PK    |                   |
|     loja      |     int     |    Identificador da loja    |       1-500        |          nao           |    FK    |                   |
|     item      |     int     |    Identificador do item    |       1-500        |          não           |    FK    |                   |
|     nome      | varchar[50] |        Nome da loja         |      a-z, A-Z      |          não           |          |                   |
|     preco     |     int     |        Preço do item        |       1-500        |          nao           |          |                   |
