# Complete Criptosystem
Implementación de un criptosistema basado en dos criptosistemas históricos: La rejilla de cardano y el cifrado de desplazamiento.

1. Primero se realiza un primer cifrado del texto usando el cifrado de desplazamiento, con el
desplazamiento que se indique. El criptosistema final usará como valor del desplazamiento el
número de agujeros en la rejilla. Es decir, que si la rejilla tiene 7 agujeros, el desplazamiento
que se usará será de 7 posiciones.

3. A continuación, se aplica la Rejilla de Cardano. Para ello, no vamos a usar una rejilla de
cartulina. En su lugar, se usa una lista de Python que hará de máscara. Así, se pone
un 1 en las posiciones correspondientes a los agujeros y un 0 en el resto de posiciones. Las
posiciones en las que hay un uno se eligen aleatoriamente como parte del proceso de
generación de la clave.

4. Una vez disponemos de la clave de rejilla, se puede cifrar un texto colocándolo en las posiciones
correspondientes a los agujeros (los unos). Si el texto es más largo que la rejilla,
se coloca de nuevo la rejilla a continuación. Así, tantas veces como sea necesario. El resto
de posiciones, las que tienen un cero, son rellenadas con caracteres aleatorios.

5. El cifrado con rejilla se realiza usando como entrada el texto cifrado usando el sistema de
desplazamiento.

6. Para descifrar un mensaje, solo hay que colocar la rejilla tantas veces como sea
necesario, leyendo los carácteres que se corresponden con los agujeros de la rejilla. Después
de aplicar la rejilla para obtener el mensaje, lo que se obtiene es un mensaje cifrado con el
sistema de desplazamiento. Por lo que para terminar de descifrarlo se aplica el
desplazamiento en sentido contrario.

7. En este criptosistema se usa un alfabeto de 41 carácteres, que incluyen las 26 letras del
abecedario en inglés más los 10 dígitos numéricos, del 0 al 9, así como los 4 caracteres siguientes:
“.”,“,”,“:”,“?” y el espacio en blanco. Es decir, un total de 41 carácteres.
