class Persona:
    def __init__(self, edad):
        self.edad = edad
        
    def hablar(self, mensaje):
        print(mensaje)
        
class Ingeniero(Persona):
    def __init__(self):
        print('Hola')
        
    def programar(self, lenguaje):
        print ('Voy a programar en', lenguaje)

class Licenciado(Persona):
    def estudiar(self, de):
        print ('Debo estudiar el caso de', de)

pedro = Ingeniero()
raul = Licenciado(18)

pedro.programar('Python')
raul.estudiar('Pedro')

pedro.hablar('Hola')
raul.hablar('Hola, Pedro!')