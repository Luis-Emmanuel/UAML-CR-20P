#!/usr/bin/env python
# coding: utf-8

# Primero simplemente pedimos la cantidad de nodos que tendra la red y creamos una lista en base a estos haciendo uso de range en el bucle for.

# In[1]:


#######################################FUNCION: CREA_UN_GRAFO_COMPLETO###############################################

n = int(input('Ingresa el tamaño de la red: '))

lst_nodos = list()
for i in range(1,n+1):
    lst_nodos.append(i)


# Luego declaramos un diccionario vacio en este caso llamado red. hacemos otro bucle for con la función range. creamos una lista temporal que copiara los datos de la lista de nodos. removeremos un valor de la lista temporal, esto para que la key no se inclulla en los valores del diccionario. en la variable up ponemos lo que sera la key con el valor del contador i y los valores los de la lista temporal. finalmente con .update ingresamos la llave y valores al diccionario. asi hasta tener los n nodos.

# In[2]:


red = {}

for i in range(1,n+1):
    lst_temp = list(lst_nodos)
    lst_temp.remove(i)
    up = {i:lst_temp}
    red.update(up)

print(red)


# calcula_grados_de_entrada.
# Damos el diccionario dirigido con sus valores todos dados como listas por conveniencia mas que nada.
# bucle for para recorrer el diccionario.
# variable up que ira colocando el nodo como llave y el tamaño del valor como el nuevo valor.
# ingresamos los datos al nuevo diccionario.
# imprimimos el resultado.

# In[3]:


################################################CALCULA_GRADOS_DE_ENTRADA######################################################
d_grafica = {1:[2], 2:[4], 3:[2], 4:[1,3,5], 5:[2,4,6], 6:[1]}

grado_e = {}

for i in d_grafica:
    up = {i:len(d_grafica[i])}
    grado_e.update(up)

print(grado_e)


# primero creamos una lista con los valores del diccionario de grado_e previamente realizado.
# ordenamos dicha lista por conveniencia.
# en otro bucle for iremos contando en la variable llaves la cantidad de nodos con el mismo grado.
# finalmente procedemos a agregar los datos al nuevo diccionario.
# si bien no es la forma mas eficiente de hacer esto es lo mejor que se me ocurrio por el momento.

# In[4]:


###############################################DIST_GRADOS_DE_ENTRADA#########################################################
distr = {}
values = 1
lst_temp2 = list()

for values in grado_e.values():
    lst_temp2.append(values)
    lst_temp2.sort()
    
for i in lst_temp2:
    llave = lst_temp2.count(i)
    up2 = {llave:i}
    distr.update(up2)
print(distr)


# declaramos el diccionario de distribución normal
# hacemos un bucle que recorra el diccionario distr obtenido en la funcion anterior
# como la distribucion normal es basicamente representar los grados de entrada pero a la inversa solamente hacemos ese cambio
# con ayuda de un par de variable y simplemente las agregamos al nuevo diccionario.

# In[5]:


#################################################DIST_NORMALIZADA#############################################################
distr_norm = {}

for i in distr:
    llave = distr[i]
    valor = i
    up3 = {llave:valor}
    distr_norm.update(up3)
print(distr_norm)


# Importamos la libreria de matplotlib con la variable de plt.
# creamos una lista para el eje x y el eje y para la grafica.
# llenamos dichas listas con un bucle for y los datos solicitados.
# finalmente solo creamos la grafica, etiquetas de esta y la imprimimos.

# In[6]:


###################################################GRAFICA_DISTR#############################################################
get_ipython().run_line_magic('matplotlib', 'notebook')

import matplotlib.pyplot as plt

x = list()
y = list()

for i in distr:
    x.append(distr[i])
    y.append(i)
plt.plot(x,y)
plt.title('Distribución de Grados de Entrada')
plt.xlabel('grado nodal')
plt.ylabel('numero de nodos')
plt.show()


# Repetimos lo mismo que en la función anterior nada mas que haciendo uso del diccionario ditr_norm y que en el eje y
# se representara la proporción de nodos.

# In[7]:


################################################GRAFICA_DISTR_NORM############################################################
x2 = list()
y2 = list()

suma = sum(distr_norm.values())

for i in distr_norm:
    x2.append(distr_norm[i])
    valor = i/suma
    y2.append(valor)
plt.plot(x2,y2)
plt.title('Distribución Normalizada de Grados de Entrada')
plt.xlabel('grado nodal')
plt.ylabel('proporción de nodos')
plt.show()


# In[ ]:




