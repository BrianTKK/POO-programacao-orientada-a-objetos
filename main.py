class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

aluno = Pessoa("Lucas", 20)

print(aluno)
print(repr(aluno))