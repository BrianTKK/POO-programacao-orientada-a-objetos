class Pessoa():
    def __init__(self, nome, idade, media):
        self.nome = nome
        self.idade = idade
        self.media = media

    def __eq__(self, outro_objeto):
        return self.nome == outro_objeto.nome
    
    def __repr__(self):
        return f"{self.nome}"
    
    def __gt__(self, outro_objeto):
        return self.media < outro_objeto.media

aluno_00 = Pessoa("Lucas", 20, 8)
aluno_01 = Pessoa("Alice", 22, 7)
aluno_02 = Pessoa("Kreig", 24, 6)

print(sorted([aluno_00, aluno_01, aluno_02]))