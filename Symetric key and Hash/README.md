# symetrickeyandhash
Trabajo sobre LFSR a través de la implementación del criptosistema A5/1 y función de has basada en un criptosistema de bloque.

1. Implementación de la cifra de flujo A5/1.
   Este apartado trata sobre el criptosistema de flujo que utiliza una combinaciñon no lineal de la salida de tres LFSR. Su funcionamiento es el siguiente:
   LFSR1:
   - Tamaño: 19
   - Polinomio de conexiones: x^19 + x^18 + x^17 + x^14 + 1
   - clocking bit: 8
  LFSR2:
   - Tamaño: 22
   - Polinomio de conexiones: x^22 + x^21 + 1
   - clocking bit: 10
  LFSR3:
   - Tamaño: 23
   - Polinomio de conexiones: x^23 + x^22 + x^21 + x^8 + 1
   - clocking bit: 10

  2. Implementación de una función hash.
     Esta función hash utiliza como criptosistema de bloque AES, que cifra mensajes en bloques de 128 bits, con una clave de 256 bits. Así, la función de hash
     tratarña los mensajes en bloques de b = 128 bits y tendrá un tamaño de 128 bits.
     Dado que el tamaño de la clave del criptosistema de bloque y el tamaño de los bloques que ciframos no son iguales, se define la función g() tal que g(x) = x||x,
     donde el símbolo || denota la concatenación.
     Por otra parte, el valor inicial de H0 es 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF.
