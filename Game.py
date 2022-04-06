#Regras do tenis : Pontuações somadas de 15 em 15 pontos vitoria com 4 sets

class Game:

# testando replace magical literal Definir uma constante para receber os valores q se repetem


#Inicia variaveis
    def __init__(self, player1, player2):
        self.points = 0
        self.points2 = 0
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
        self.points +=15
        return self.points

# Define a pontuação do Primeiro Jogador no Set
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

#Define a pontuação do Segundo Jogador no Set
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
     
    def P1Score(self):
        self.points +=1
    
    
    def P2Score(self):
        self.points2 +=1
#Tornar ela mais coesa e deixar so que é para fazer no caso apenas unica função de score
    def score(self):
        result = ""
        if (self.points == self.points2 and self.points < 3):
            if (self.points==0):
                result = self.ponto0
            if (self.points==1):
                result = self.ponto1
            if (self.points==2):
                result = self.ponto2
            result += "-All"
        if (self.points==self.points2 and self.points>2):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.points > 0 and self.points2==0):
            if (self.points==1):
                P1res = self.ponto1
            if (self.points==2):
                P1res = self.ponto2
            if (self.points==3):
                P1res = self.ponto3
            
            P2res = self.ponto0
            result = P1res + "-" + P2res
        if (self.points2 > 0 and self.points==0):
            if (self.points2==1):
                P2res = "Fifteen"
            if (self.points2==2):
                P2res = "Thirty"
            if (self.points2==3):
                P2res = "Forty"
            
            P1res = self.ponto0
            result = P1res + "-" + P2res
        
        
        if (self.points>self.points2 and self.points2 < 4):
            if (self.points==2):
                P1res=self.ponto2
            if (self.points==3):
                P1res=self.ponto3
            if (self.points2==1):
                P2res=self.ponto1
            if (self.points2==2):
                P2res=self.ponto2
            result = P1res + "-" + P2res

        if (self.points2>self.points and self.points2 < 4):
            if (self.points2==2):
                P2res=self.ponto2
            if (self.points2==3):
                P2res=self.ponto3
            if (self.points==1):
                P1res=self.ponto1
            if (self.points2==2):
                P1res=self.ponto2
            result = P1res + "-" + P2res

        if (self.points > self.points2 and self.points2 >= 3):
            result = "Advantage " + self.player1
        
        if (self.points2 > self.points and self.points >= 3):
            result = "Advantage " + self.player2
        
        if (self.points>=4 and self.points2>=0 and (self.points-self.points2)>=2):
            result = "Win for " + self.player1

        if (self.points2>=4 and self.points>=0 and (self.points2-self.points)>=2):
             result = "Win for " + self.player2
        return result