#!/usr/bin/env python
# coding: utf-8

# In[16]:


nome = ['ruben'] #criação de lista
idade = [20]
def lista(nome, idade):
    dados = [nome, idade]
    print(dados)
lista(nome, idade)
def soma(a, b):
    d = a + b
    print('a soma é {}'.format(d))
soma(3,7)
nota = {'ruben': 'criador', 'idade': 20} #dicionário
print(nota['ruben'])
num = [1,2,3,4,5,6,7,3,8,9,10] #lista
par = []
print(len(num))
print(num.count(3))
print(sum(num))
print(num[:2])
print(num[2:])
for p in num:
    if(p%2==0):
        par.append(p)
print(par)
num.pop(7)
print(num)
outro = [] #tuple
imut = (1,2,3, outro)
tuple(imut)
perg = int(input('digite um número inteiro:\n'))
outro.append(perg)
print(imut)


# In[1]:


pap = [4,4,2,1,5]
gr = [1,2,3,4,5]
r = set(pap)
s = set(gr)
print(r | s)
def diz_oi():
    print('oi')
diz_oi()
for a in range(1,4): #delay
    print(a)
    import time
    time.sleep(1)
import matplotlib
import matplotlib.pyplot as plt
plt.plot(gr, pap, marker='o', color='green')
plt.title('teste')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




