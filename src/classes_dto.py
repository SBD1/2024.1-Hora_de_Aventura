
class CurrentPlayer:
    def __init__(self, id_jogador, nome, regiao, missao_atual, vida, qnt_ouro):
        self.id_jogador = id_jogador
        self.nome = nome
        self.regiao = regiao
        self.missao_atual = missao_atual
        self.vida = vida
        self.qnt_ouro = qnt_ouro

class Enemy:
    def __init__(self, id_instancia_inimigo, id_inimigo, nome, descricao,regiao,dano,defesa,vida, drop):
        self.id_instancia_inimigo = id_instancia_inimigo
        self.id_inimigo = id_inimigo
        self.nome = nome 
        self.descricao = descricao 
        self.regiao = regiao  
        self.dano = dano  
        self.defesa = defesa  
        self.vida = vida  
        self.drop = drop
