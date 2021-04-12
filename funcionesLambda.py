# Nos importamos el módulo funciones1nivel, pero sólo vamos a importarnos la función sumaTodos

from funciones1nivel import sumaTodos



# Aquí necesitaría crearme la función cubo, pero no me la quiero crear. Entonces utilizo una función anónima que en Python se llama lambda)
print(sumaTodos(3, lambda x: x*2))
#print(sumaTodos(100, lambda x: x*3))