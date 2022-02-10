#Tupla
Tupla = (1,"String",True)
print(Tupla)

""" Diccionarios """
Diccionario = {'a': True, 5:"String", (1,2):False, 'a':100, 'a':False}
Diccionario['c'] = "El chotis"
Diccionario['a'] = False
#valor = Diccionario['c']
valor = Diccionario.get('c', False)
del Diccionario[5]
print(Diccionario)
print(valor)

Llaves = tuple (Diccionario.keys())
valores = tuple (Diccionario.values())
print(valores)