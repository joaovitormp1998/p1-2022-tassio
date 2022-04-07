#Regras do tenis : Pontuações somadas de 15 em 15 pontos vitoria com 4 sets

class Game:

# testando replace magical literal Definir uma constante para receber os valores q se repetem


#Inicia variaveis
    def __init__(self, player1, player2):
        self.acerto = 0
        self.acerto2 = 0
        self.player1 = player1
        self.player2 = player2
        self.ponto0 = "Love"
        self.ponto1 ="Fifteen"
        self.ponto2 ="Thirty"
        self.ponto3 ="Forty"
#Define nome do jogador
    def jogador (self, nome):
        self.nome = nome
        self.acerto = 0

# A cada novo acerto será acrescentado +15 pontos
    def pontuar(self):
        self.acerto +=15
        return self.acerto

# Define a pontuação do Primeiro Jogador no Set
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

#Define a pontuação do Segundo Jogador no Set
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
     
    def P1Score(self):
        self.acerto +=1

    def P2Score(self):
        self.acerto2 +=1
#Tornar ela mais coesa e deixar so que é para fazer no caso apenas unica função de score
    def score(self):
        result = ""

        if (self.acerto == self.acerto2 and self.acerto < 3):
            if (self.acerto==0):
                result += self.ponto0
            if (self.acerto==1):
                result += self.ponto1
            if (self.acerto==2):
                result = self.ponto2
                result += "-All"
        if (self.acerto==self.acerto2 and self.acerto>2):
            result += "Deuce"

    def placar(self):
        result = ""
        resultado = [{0:0, 1:15, 2:30, 3:40}]
        placar=[{0: self.ponto0, 1: self.ponto1, 2: self.ponto2, 3: self.ponto3}]

        if (self.acerto == self.acerto2 and self.acerto < 3):
            result = placar[self.acerto]
            result += "-All"
        if (self.acerto == self.acerto2 and self.acerto > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.acerto>self.acerto2 and self.acerto2 < 4):

            if (self.acerto==2):
                P1res=placar[self.acerto]
            if (self.acerto==3):
                P1res=placar[self.acerto]
            if (self.acerto2==1):
                P2res=placar[self.acerto2]
            if (self.acerto2==2):
                P2res=placar[self.acerto2]

            result = P1res + "-" + P2res

        if (self.acerto2>self.acerto and self.acerto2 < 4):
            if (self.acerto2==2):
                P2res=placar[self.acerto2]
            if (self.acerto2==3):
                P2res=placar[self.acerto2]
            if (self.acerto==1):
                P1res=placar[self.acerto]
            if (self.acerto==2):
                P1res=self.ponto2
            result = P1res + "-" + P2res

        if (self.acerto > self.acerto2 and self.acerto2 >= 3):
            result = "Advantage " + self.player1
        
        if (self.acerto2 > self.acerto and self.acerto >= 3):
            result = "Advantage " + self.player2
        
        if (self.acerto>=4 and self.acerto2>=0 and (self.acerto-self.acerto2)>=2):
            result = "Win for " + self.player1

        if (self.acerto2>=4 and self.acerto>=0 and (self.acerto2-self.acerto)>=2):
             result = "Win for " + self.player2
        return result
