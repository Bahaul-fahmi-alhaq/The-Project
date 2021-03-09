# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:59:04 2021

@author: ACE
"""

#max_bil_prima = input()
bil_prima = [2]
x = 1
n = 1
m = 0
g = x/n
while type(g) == float:    
    n += 1
    g = x/n
else:
    m += 1
    if m <= 2:
        n +=1
        g = x/n
    elif n == x:
        bil_prima.append(x)
print('daftar bilangan prima', bil_prima)       
