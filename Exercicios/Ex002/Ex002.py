#Declaração de classes
class Estudante():
    """
    Docstring para Estudante
    Esta classe tem como objetivo criar um modelo de estudante, com atributos e métodos relacionados a um estudante de graduação.
    
    Atributos:  
    - nome (str): Nome do Estudante
    - idade (int): Idade do estudante
    - matriculado (bool): Atributo para saber se o estudante esta ou não matriculado
    - curso (str): Nome do curso do estudante
    - periodo (int): Periodo em que o estudante está cursando
    
    Métodos:
    - matricular(): Método para matricular o estudante, alterando o atributo 'matriculado' para True.
    - aprovado(): Método para avançar o estudante para o próximo período, incrementando o atributo 'periodo' em 1.
    - __str__(): Método especial para retornar uma string representando o estado atual do estudante.
    """

    def __init__(self, nome = "", idade = 0, matriculado = False, curso = "", periodo = 1): #Método Construtor
        #Documentação 
        """
        Docstring para __init__
        
        :param self: Própria classe
        :param nome: Nome do Estudante
        :param idade: Idade do estudante
        :param matriculado: (True/False) Atributo para saber se o estudante esta ou não matriculado
        :param curso: Nome do curso do estudante
        :param periodo: Periodo em que o estudante está cursando
        """

        #Atributos de instância
        self.nome = nome
        self.idade = idade
        self.matriculado = matriculado
        self.curso = curso
        self.periodo = periodo

    #Métodos de instância
    
    def matricular(self):
        if self.matriculado is False:
            self.matriculado = True
            
    def aprovado(self):
        self.periodo += 1
        
    def __str__ (self):
        return (f"{self.nome} é um(a) Estudante de Graduação, tem {self.idade} anos, está no {self.periodo} periodo da graduação. Sua matricula está como {self.matriculado}")
    



#Declaração de Objetos

aluno1 = Estudante("Eduardo")
aluno1.nome = "Eduardo"
aluno1.idade = 18
aluno1.curso = "Engenharia da Computação"
aluno1.matricular()

print(aluno1)

aluno1.aprovado()
aluno1.aprovado()
aluno1.matricular()

print(aluno1)

print(Estudante.__doc__)