#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

MODE_CIPHER = 0
MODE_DECIPHER = 1

# Definición de los polinomios A5/1
pol19 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pol22 = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pol23 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

def_clocking_bits = [8, 10, 10]


def lfsr_sequence(polynomial, initial_state, output_bits):
    """
    Returns the output sequence of output_bits bits of an LFSR with a given initial state and connection polynomial.

    :param polynomial: list of integers, with the coefficients of the connection polynomial that define the LFSR.
    :param initial_state: list of integers with the initial state of the LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: a list of output_bits bits
    """
    result = []

    # Damos la vuelta a polynomial y state para operar con ellos
    # Además creamos una variable "polynomial_list" donde se guardarán los índices de polynomial que contengan 1
    state = initial_state[::-1]
    polynomial_reverse = polynomial[::-1]
    polynomial_list = []

    # Guardamos los índices donde se encuentra un 1 en polynomial
    for i in range(len(polynomial_reverse)):
        if polynomial_reverse[i] == 1:
            polynomial_list.append(i)

    # Bucle tantas veces como output_bits hay
    for i in range(output_bits):
        # Añadimos al resultado el último bit de state
        result.append(state[-1])
        # Hacemos una copia de polynomial_list para mantener la original intacta
        plist = polynomial_list.copy()
        # Para sacar el siguiente bit hay que hacer un XOR entre los bits de state en las posiciones que indica el
        # polinomio Es por esto que guardamos en next_bit el primer bit con el que se opera de state
        next_bit = state[polynomial_list[0]]

        # A continuación hacemos un XOR con este primer bit y el resto que haya según el polinomio, tantas veces como
        # se necesite
        for j in range(len(polynomial_list) - 1):
            next_bit = next_bit ^ state[plist[1]]
            # Recortamos plist para, en la siguiente ejecución del bucle, state[plist[1]] sea el siguiente bit que
            # haya que utilizar para la operación
            plist = plist[1:]

        # Eliminamos el último bit de state
        state.pop()
        # Añadimos el siguiente bit calculado a la posición 0 de state
        state.insert(0, next_bit)

    return result


def ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, output_bits):
    """
    Implements extended A5's pseudorandom generator.
    :param params_pol_0: two-element list describing the first LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_1: two-element list describing the second LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_2: two-element list describing the third LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param clocking_bits: three-element list, with the clocking bits of each LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: list of output_bits elements with the pseudo random sequence
    """

    sequence = []

    # Se generan las secuencias pseudoaleatorias de cada uno de los 3 polinomios
    lfsr1 = lfsr_sequence(params_pol_0[0], params_pol_0[1], len(params_pol_0[0]))
    lfsr2 = lfsr_sequence(params_pol_1[0], params_pol_1[1], len(params_pol_1[0]))
    lfsr3 = lfsr_sequence(params_pol_2[0], params_pol_2[1], len(params_pol_2[0]))

    # Se da la vuelta a los LFSR y los polinomios para ajustarlos a cómo funciona nuestro código
    lfsr1 = lfsr1[::-1]
    lfsr2 = lfsr2[::-1]
    lfsr3 = lfsr3[::-1]
    polreversed0 = params_pol_0[0][::-1]
    polreversed1 = params_pol_1[0][::-1]
    polreversed2 = params_pol_2[0][::-1]

    # Comprobación de que los clocking bits son válidos
    if clocking_bits[0] > (len(params_pol_0[1]) - 1) or clocking_bits[1] > (len(params_pol_1[1]) - 1) \
            or clocking_bits[2] > (len(params_pol_2[1]) - 1):
        raise ValueError("bad clocking bits!")

    # Obtención de los índices de cada polinomio:
    pol0 = []
    pol1 = []
    pol2 = []

    for i in range(len(params_pol_0[0])):
        if polreversed0[i] == 1:
            pol0.append(i)

    for i in range(len(params_pol_1[0])):
        if polreversed1[i] == 1:
            pol1.append(i)

    for i in range(len(params_pol_2[0])):
        if polreversed2[i] == 1:
            pol2.append(i)

    # Inicio de la iteración del bucle que añade uno a uno los bits de salida a la secuencia.
    for i in range(output_bits):
        # Se inicializa el primer bit de cada LFSR con el que se va a calcular el siguiente al actualizarlo
        new_bit1 = lfsr1[pol0[0]]
        new_bit2 = lfsr2[pol1[0]]
        new_bit3 = lfsr3[pol2[0]]

        # Creación de una copia de la lista que contiene los índices de cada polinomio, ya que en los bucles donde
        # calculamos el siguiente bit se va a ir recortando. Si se tienen n índices, se calcula el XOR de 0
        # con el 1, el 1 con el 2 y así sucesivamente hasta llegar a n-1 XOR n.
        pol0_copy = pol0.copy()
        pol1_copy = pol1.copy()
        pol2_copy = pol2.copy()

        # Se guarda el XOR entre los 3 últimos bits de los LFSR en la secuencia (hay que tener en cuenta que se hace
        # así ya que se ha invertido previamente los LFSR)
        next_bit = lfsr1[-1] ^ lfsr2[-1] ^ lfsr3[-1]
        sequence.append(next_bit)

        # --- CONDICIONES PARA EL AVANCE DEl LFSR ---#
        # Si los clocking bits lfsr1 == lfsr2 == lfsr3
        if lfsr1[clocking_bits[0]] == lfsr2[clocking_bits[1]] == lfsr3[clocking_bits[2]]:
            # Se hace la operación XOR entre el bit inicializado previamente y el siguiente
            # Se va eliminando el primer índice guardado
            for j in range(len(pol0) - 1):
                new_bit1 = new_bit1 ^ lfsr1[pol0_copy[1]]
                pol0_copy = pol0_copy[1:]

            # Se elimina el último elemento de LFSR1
            lfsr1.pop()
            # Se inserta en el índice 0 el nuevo bit
            lfsr1.insert(0, new_bit1)

            for j in range(len(pol1) - 1):
                new_bit2 = new_bit2 ^ lfsr2[pol1_copy[1]]
                pol1_copy = pol1_copy[1:]

            lfsr2.pop()
            lfsr2.insert(0, new_bit2)

            for j in range(len(pol2) - 1):
                new_bit3 = new_bit3 ^ lfsr3[pol2_copy[1]]
                pol2_copy = pol2_copy[1:]

            lfsr3.pop()
            lfsr3.insert(0, new_bit3)

        # Si los clocking bits lfsr1 == lfsr2
        elif lfsr1[clocking_bits[0]] == lfsr2[clocking_bits[1]]:
            for j in range(len(pol0) - 1):
                new_bit1 = new_bit1 ^ lfsr1[pol0_copy[1]]
                pol0_copy = pol0_copy[1:]

            lfsr1.pop()
            lfsr1.insert(0, new_bit1)

            for j in range(len(pol1) - 1):
                new_bit2 = new_bit2 ^ lfsr2[pol1_copy[1]]
                pol1_copy = pol1_copy[1:]

            lfsr2.pop()
            lfsr2.insert(0, new_bit2)

        # Si los clocking bits lfsr1 == lfsr3
        elif lfsr1[clocking_bits[0]] == lfsr3[clocking_bits[2]]:
            for j in range(len(pol0) - 1):
                new_bit1 = new_bit1 ^ lfsr1[pol0_copy[1]]
                pol0_copy = pol0_copy[1:]

            lfsr1.pop()
            lfsr1.insert(0, new_bit1)

            for j in range(len(pol2) - 1):
                new_bit3 = new_bit3 ^ lfsr3[pol2_copy[1]]
                pol2_copy = pol2_copy[1:]

            lfsr3.pop()
            lfsr3.insert(0, new_bit3)

        # Si los clocking bits lfsr2 == lfsr3
        elif lfsr2[clocking_bits[1]] == lfsr3[clocking_bits[2]]:
            for j in range(len(pol1) - 1):
                new_bit2 = new_bit2 ^ lfsr2[pol1_copy[1]]
                pol1_copy = pol1_copy[1:]

            lfsr2.pop()
            lfsr2.insert(0, new_bit2)

            for j in range(len(pol2) - 1):
                new_bit3 = new_bit3 ^ lfsr3[pol2_copy[1]]
                pol2_copy = pol2_copy[1:]

            lfsr3.pop()
            lfsr3.insert(0, new_bit3)

    return sequence


def a5_cipher(initial_state_0, initial_state_1, initial_state_2, message, mode):
    """
    Implements ciphering/deciphering with the A5 pseudo random generator.

    :param initial_state_0: list, initial state of the first LFSR
    :param initial_state_1: list, initial state of the second LFSR
    :param initial_state_2: list, initial state of the third LFSR
    :param message: string, plaintext to cipher (mode=MODE_CIPHER) or ciphertext to decipher (mode=MODE_DECIPHER)
    :param mode: MODE_CIPHER or MODE_DECIPHER, whether to cipher or decipher
    :return: string, ciphertext (mode=MODE_CIPHER) or plaintext (mode=MODE_DECIPHER)
    """

    output = ""

    params_pol_0 = [pol19, initial_state_0]
    params_pol_1 = [pol22, initial_state_1]
    params_pol_2 = [pol23, initial_state_2]

    if mode == MODE_CIPHER:
        # Conversión del mensaje a una cadena binaria
        binary_text = "".join([format(ord(char), '08b') for char in message])

        # Obtención de la secuencia pseudoaleatoria
        sequence = ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, def_clocking_bits,
                                                len(binary_text))

        # Convertir binary_text a una lista de enteros
        binary_text = [int(char, 2) for char in binary_text]

        # Realizar la operación XOR entre los bits del mensaje y la secuencia pseudoaleatoria
        encrypted_bits = [m ^ p for m, p in zip(binary_text, sequence)]
        output = ''.join([str(bit) for bit in encrypted_bits])

    elif mode == MODE_DECIPHER:
        # Obtención de la secuencia pseudoaleatoria
        sequence = ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, def_clocking_bits,
                                                len(message))

        # Convertir message a una lista de enteros
        message = [int(char, 2) for char in message]

        # Realizar la operación XOR entre los bits cifrados y la secuencia pseudoaleatoria
        decrypted_bits = [m ^ p for m, p in zip(message, sequence)]

        # Convertir decrypted_bits a una cadena de caracteres
        output = "".join(
            [chr(int("".join(map(str, decrypted_bits[i:i + 8])), 2)) for i in range(0, len(decrypted_bits), 8)])
    return output


def aes(message, key):
    """
    Implements 1 block AES enciphering using a 256-bit key.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :param key: string of 1 and 0s with the binary representation of the key, 256 char. long
    :return: string of 1 and 0s with the binary representation of the ciphered message, 128 char. long
    """

    cipher_text = ""

    # Convertir key y message a bytes
    key_bytes = bytes(int(key[i:i + 8], 2) for i in range(0, len(key), 8))
    message_bytes = bytes(int(message[i:i + 8], 2) for i in range(0, len(message), 8))

    # Crear un objeto AES en modo ECB ya que solo se van a cifrar mensajes de 128 bits
    aes = AES.new(key_bytes, AES.MODE_ECB)

    # Cifrar el mensaje
    encrypted_message = aes.encrypt(message_bytes)

    # Convertir el mensaje cifrado de bytes a una cadena de caracteres
    cipher_text = "".join([format(byte, '08b') for byte in encrypted_message])

    return cipher_text


def g(message):
    """
    Implements the g function.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :return: string of 1 and 0s, 256 char. long
    """

    output = ""

    # Encadenar el mensaje consigo mismo
    output = message + message

    return output


def naive_padding(message, block_len):
    """
    Implements a naive padding scheme. As many 0 are appended at the end of the message
    until the desired block length is reached.

    :param message: string with the message
    :param block_len: integer, block length
    :return: string of 1 and 0s with the padded message
    """

    output = ""

    # Convertir el mensaje a binario
    bin_str = "".join(format(ord(c), '08b') for c in message)

    # Calcular el número de bits que faltan para completar el bloque
    remainder = len(bin_str) % block_len

    # Si faltan bits por completar, calculamos cuándos son y los añadimos al final de la cadena:
    if remainder != 0:
        num_zeros = block_len - remainder
        bin_str += "0" * num_zeros

    output = bin_str

    return output


def mmo_hash(message):
    """
    Implements the hash function.

    :param message: a char. string with the message
    :return: string of 1 and 0s with the hash of the message
    """

    h_i = ""

    # Inicializar H0 y block_len
    h0 = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    block_len = 128

    # Añadir el padding al mensaje si es necesario
    padded_msg = naive_padding(message, block_len)

    # Procesamos el mensaje en bloques de longitud block_len
    for i in range(0, len(padded_msg), block_len):
        # Utilizar la función g con h0
        key = g(h0)

        # Cogemos el siguiente bloque del mensaje
        block = padded_msg[i:i + block_len]

        # Ciframos el bloque utilizando la clave recuperada de la función g
        ciphered_block = aes(block, key)

        # Aplicamos la función g al resultado obtenido y hacemos un XOR con el valor actual de h
        g_output = g(ciphered_block)
        h0 = "".join(str(int(a) ^ int(b)) for a, b in zip(h0, g_output))

    # Convertimos el resultado final a una cadena de 1s y 0s
    h_i = h0[-128:].zfill(128)
    # --------------------------------
    return h_i
