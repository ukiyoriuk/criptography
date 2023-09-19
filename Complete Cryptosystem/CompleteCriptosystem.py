#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:?"

def rotative_encrypt(message, shift):
    """
    Simple substitution cipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    # Para no tener problemas con el mensaje y comparando carácteres, se ponen todos los carácteres en mayúsculas
    message = message.upper()

    # Por cada carácter en el mensaje, comprueba si el carácter está en el alfabeto ABC.
    for char in message:
        # Si el carácter está en el alfabeto, se determina su posición en ABC para después calcular
        # el nuevo carácter por el que hay que sustituirlo (con una suma, ya que estamos encriptando).
        # Como el diccionario tiene que ser cíclico (es decir, si el carácter original es 9 y usamos
        # un shift 7, la cadena no tiene tantos carácteres por lo que tiene que seguir contando desde el inicio de la cadena).
        if char in ABC:
            char_index = ABC.index(char)
            encrypted_index = (char_index + shift) % len(ABC)
            encrypted_char = ABC[encrypted_index]
            ciphertext += encrypted_char
        # Si el carácter no está en el diccionario, entonces simplemente lo agrega a ciphertext.
        else:
            ciphertext += char

    return ciphertext


def rotative_decrypt(message, shift):
    """
    Simple substitution decipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    plaintext = ""

    # Para no tener problemas con el mensaje y comparando carácteres, se ponen todos los carácteres en mayúsculas
    message = message.upper()

    # Por cada carácter en el mensaje, comprueba si el carácter está en el alfabeto ABC.
    for char in message:
        # Si el carácter está en el alfabeto, se determina su posición en ABC para después calcular
        # el nuevo carácter por el que hay que sustituirlo (con una resta, ya que estamos desencriptando).
        # Como el diccionario tiene que ser cíclico (es decir, si el carácter original es A y usamos un shift
        # 4, la cadena no tiene carácteres antes de A por lo que tiene que seguir contando desde el final de la cadena).
        if char in ABC:
            char_index = ABC.index(char)
            decrypted_index = (char_index - shift) % len(ABC)
            decrypted_char = ABC[decrypted_index]
            plaintext += decrypted_char
        # Si el carácter no está en el diccionario, entonces simplemente lo agrega a plaintext.
        else:
            plaintext += char

    return plaintext


def grille_genkey(grille_len, num_holes):
    """
    Key generation
    :gruille_len: total grille length in symbols
    :num_holes: Number of holes in the grille
    :return: key as list of 0 and 1
    """

    key = []

    # Crear una lista de ceros con la longitud grille_len
    key = [0] * grille_len
    # Elegir los índices aleatorios donde poner los agujeros
    indexes = random.sample(range(grille_len), num_holes)
    # Poner un uno en cada índice aleatoriamente seleccionado
    for i in indexes:
        key[i] = 1
    # --------------------------------

    return key


def grille_encrypt(key, plaintext):
    """
    Encrypt a text using the key
    :message: message to grille_encrypt
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    j = 0
    finished = False

    # Inicializamos un bucle con las condiciones de que sigan quedando carácteres en plaintext
    # que aún no hemos puesto en ciphertext. (Esto hace que si la lista key termina y aún quedan
    # carácteres en plaintext, vuelva a empezar de cero.
    while j < len(plaintext) or not finished:
        # Bucle con la longitud de la clave.
        for i in range(len(key)):
            # Si quedan carácteres en plaintext, sigue añadiendo en función de si el valor de la clave
            # en cada iteración sea 0 o 1.
            if not finished:
                if key[i] == 0:
                    # Escoge un valor aleatorio de la variable ABC si en la posición i de key hay un 0.
                    ciphertext += random.choice(ABC)
                else:
                    # Escoge la letra correspondiente de plaintext si aún queda texto y la añade a ciphertext.
                    if j == len(plaintext):
                        finished = True
                    else:
                        char = plaintext[j]
                        ciphertext += char
                        j += 1
    return ciphertext


def grille_decrypt(key, ciphertext):
    """
    Decrypt a text using the key
    :message: message to grille_decrypt
    :subs_alphabet: substitution alphabet
    :return: ciphered text
    """

    plaintext = ""

    j = 0
    finished = False

    # Inicializamos un bucle con las condiciones de que sigan quedando carácteres en ciphertext
    # que aún no hemos puesto en plaintext. (Esto hace que si la lista key termina y aún quedan
    # carácteres en ciphertext, vuelva a empezar de cero).
    while j < len(ciphertext) or not finished:
        # Bucle con la longitud de la clave.
        for i in range(len(key)):
            # Si quedan carácteres en ciphertext, sigue añadiendo en función de si el valor de la clave
            # en cada iteración sea 0 o 1.
            if not finished:
                if key[i] == 1:
                    # Escoge la letra correspondiente de ciphertext si aún queda texto y la añade a plaintext.
                    if j >= len(ciphertext):
                        finished = True
                    else:
                        char = ciphertext[j]
                        plaintext += char
                j += 1

    return plaintext


def encrypt(key, plaintext):
    """
    Complete cryptosystem (encrypt)
    :key: grille key
    :plaintext: message to encrypt
    :return: encrypted text
    """
    # Variable que define el número de agujeros en la clave
    num_holes = 0

    # Se cuenta el número de agujeros en la clave
    for i in range(len(key)):
        if key[i] == 1:
            num_holes += 1

    # Se llama a la función de desplazamiento, pasándole el texto en claro y el shift (número de agujeros en la clave)
    # El resultado se guarda en rotativetext
    rotativetext = rotative_encrypt(plaintext, num_holes)

    # Se manda el texto desplazado (ciphertext) a la función que encripta con la rejilla
    ciphertext = grille_encrypt(key, rotativetext)

    return ciphertext


def decrypt(key, ciphertext):
    """
    Complete cryptosystem (decrypt)
    :key: grille key
    :ciphertext: message to decrypt
    :return: plaintext
    """

    plaintext = ""

    # Se desencripta el texto con la función de rejilla
    grilletext = grille_decrypt(key, ciphertext)

    # Variable que define el número de agujeros en la clave
    num_holes = 0

    # Se cuenta el número de agujeros en la clave
    for i in range(len(key)):
        if key[i] == 1:
            num_holes += 1

    # Se desencripta el texto con la función de desplazamiento
    plaintext = rotative_decrypt(grilletext, num_holes)

    return plaintext
