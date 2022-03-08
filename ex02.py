##
## EPITECH PROJECT, 2022
## regex
## File description:
## ex02
##
import re

file = open("exo2/exo2.txt", 'r')


reg = re.findall('.*.:', file.read())
str = ''.join(reg)
print(reg)

file.close()