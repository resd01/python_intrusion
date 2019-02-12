#!/env/python
# -*- coding: utf-8 -*-

# tuple
fruits_tuple = ('Cerise', 'Banane', 'Poire', 'Pomme', 'Orange')
print "=== TUPLE ==="
print fruits_tuple

# liste
fruits_list = ['Cerise', 'Banane', 'Poire', 'Pomme', 'Orange']
print "=== LIST ==="
print fruits_list[-2] # partant de la fin
print fruits_list[2:] # a partir de
print fruits_list[:2] # avant

# changement de valeur
fruits_list[2] = 'Melon'
print fruits_list

# Ajout d'un nouvel élément
fruits_list.append("Poire")
print fruits_list

# Itération sur la list
## For
print "=== FOR ==="
for fruit in fruits_list:
	print fruit
	pass
# Executer si la boucle s'est bien passée
else:
	print "Done"

## While
print "=== WHILE ==="
i = 0
while len(fruits_list) > i:
	print fruits_list[i]
	i += 1
	pass