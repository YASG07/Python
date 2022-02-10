Lista = 'Curso'
Curso = 'POO'

""" Formato """
result ='{a} de {b}'.format(b = Lista, a = Curso)
result = result.title()
print(result)

"""Busqueda"""
pos = result.find('Curso')
print(pos)
count = result.count('C')
New_Lista = result.replace('C', 'X')
New_Lista = result.split(' ')
print(New_Lista)
print(count)
#print(result[7])

"""print(Lista)
#print(Lista[0:10:2])
#print(Lista[::-1])"""

""" Listas """
List = ["String", 15, 15.6, True]
List.append(6)
List.insert(1, "Insert")
List.remove(15)
List.pop()
print(List)