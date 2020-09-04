#!/usr/bin/env python
# coding: utf-8

# Ingresamos el diccionario de la red con las amistades formadas

# In[3]:


red = {'alicia':['monica','carmen','david','carlos','beto'], 'beto':['alicia','jorge'], 'carlos':['alicia','david','monica'], 
       'carmen':['alicia','monica'], 'david':['alicia','carlos'], 'enrique':['irene','jorge','rosa'],
       'irene':['rosa','enrique'], 'jorge':['beto','enrique','rosa'], 'monica':['alicia','carmen'],
       'rosa':['enrique','irene','jorge']}


# Funcion "numero_nodos"

# In[5]:


lista = list()
for i in red:
    lista.append(red)
print('La cantidad de nodos en la red son:',len(lista))


# Funcion "calcula_grados"

# In[7]:


lista2 = list()  
for i in red:
    print('Grado nodal del nodo', i, 'es:', len(red[i]))
    lista2.append(len(red[i]))


# Funcion "grado_maximo"

# In[21]:


print('El grado maximo de la red es:',max(lista2))


# In[ ]:




