from pontuacao import Pontuacao


class Jogador(Pontuacao):


    def __init__(self, nome:str):
        self._nome = nome
        Pontuacao.__init__(self,ponto=0)

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome

p1 = Jogador("Demetrio")
p2 = Jogador("Cleitinho")

print(p1.nome,"Ganhou de", p2.nome)
