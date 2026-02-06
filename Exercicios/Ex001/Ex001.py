#Declaração de classes
class Estudante():
    def __init__(self): #Método Construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0
        self.matriculado = False
        self.curso = ""
        self.periodo = 1

    #Métodos de instância
    
    def matricular(self):
        if self.matriculado is False:
            self.matriculado = True
            
    def aprovado(self):
        self.periodo += 1
        
    def mensagem(self):
        return (f"{self.nome} é um(a) Estudante de Graduação, tem {self.idade} anos, está no {self.periodo} periodo da graduação. Sua matricula está como {self.matriculado}")
    



#Declaração de Objetos

aluno1 = Estudante()
aluno1.nome = "Eduardo"
aluno1.idade = 18
aluno1.curso = "Engenharia da Computação"
aluno1.matricular()

print(aluno1.mensagem())

aluno1.aprovado()
aluno1.aprovado()
aluno1.matricular()

print(aluno1.mensagem())

