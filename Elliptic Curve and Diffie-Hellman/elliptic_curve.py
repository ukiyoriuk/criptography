#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import random

P_INFINITY = (None, None)

def isElliptic(curve):
    a, b, p = curve

    return (4 * pow(a, 3) + 27 * pow(b, 2)) % p != 0


# Esta función verifica si un número es primo
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True


# Esta función sirve para obtener todos los puntos de la curva
def GetCurvePoints(curve):
    a, b, p = curve
    points = []

    # Se implementan 2 bucles for para iterar a través de todos los posibles valores de x e y
    # Rango para x: desde -1 hasta p-1
    # Rango para y: desde -(p//2) hasta (p//2)
    for x in range(p):
        for y in range(p):
            # Se verifica si el punto (x, y) satisface la ecuación de la curva elíptica
            if pow(y, 2) % p == (pow(x, 3, p) + a * x + b) % p:
                points.append((x, y))

    return points


def ComputePoints(curve):
    """
    EXERCISE 1.1: Count the points on an elliptic curve
    :curve: a list with the curve values [a, b, p]
    :return: number of points on the curve
    """

    num_points = 0

    # Obtenemos los valores individuales de la curva
    a, b, p = curve

    # Se implementan 2 bucles for para iterar a través de todos los posibles valores de x e y en el rango de 0 a p-1
    for x in range(p):
        for y in range(p):
            # Se verifica si el punto (x, y) satisdace la ecuación de la curva elíptica
            if pow(y, 2) % p == (pow(x, 3) + a * x + b) % p:
                num_points += 1

    # Añadimos un punto más, que es el punto infinito
    num_points += 1

    return num_points


def VerifyNumPoints(curve, n):
    """
    EXERCISE 1.2: Verify group order
    :curve: a list with the curve values [a, b, p]
    :n: number of points
    :return: True if it satisfies the equation or False
    """

    result = False

    # Comprobamos que la curva es elíptica
    if not isElliptic(curve):
        return result

    # Se obtienen los valores individuales de la curva
    a, b, p = curve

    # Se calcula el lazo izquierdo de la desigualdad de la inecuación
    left_side = p + 1 - 2 * math.isqrt(p)

    # Se calcula el lazo derecho de la desigualdad de la inecuación
    right_side = p + 1 + 2 * math.isqrt(p)

    # Se comprueba si se cumple la inecuación
    result = left_side <= n <= right_side

    return result


def AddPoints(curve, P, Q):
    """
    EXERCISE 2.1: Add two points
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :Q: another point as a pair (x, y)
    :return: P+Q
    """

    # Se obtienen los valores individuales de la curva
    a, b, p = curve

    # Descomponemos P y Q
    x1, y1 = P
    x2, y2 = Q

    # Caso P = O (punto infinito)
    if P == P_INFINITY:
        return Q
    # Caso Q = O (punto infinito)
    elif Q == P_INFINITY:
        return P
    # Caso y1 = -y2
    elif x1 == x2 and (y1 == -y2 % p or y2 == -y1):
        return P_INFINITY
    # Caso P = Q
    elif P == Q and y1 != 0:
        st = ((3 * pow(x1, 2) + a) % p) * pow((2 * y1), -1, p)
        x3 = (pow(st, 2) - 2 * x1) % p
        y3 = (st * (x1 - x3) - y1) % p
        suma = (x3, y3)
    # Caso P != Q
    else:
        sc = ((y1 - y2) % p) * pow((x1 - x2), -1, p)
        x3 = (pow(sc, 2) - x1 - x2) % p
        y3 = (sc * (x1 - x3) - y1) % p
        suma = (x3, y3)

    return suma


def SelfProductPoint(curve, n, P):
    """
    EXERCISE 3.1: Multiplication of a scalar by a point
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    # Caso n = 0 o P = O (punto infinito)
    if n == 0 or P == P_INFINITY:
        return P_INFINITY

    # Se inicializa el producto como punto de partida
    current_point = P

    # Se inicializa product al punto infinito
    product = P_INFINITY

    # Caso en el que n sea un entero
    if isinstance(n, int):
        # itera mientras n sea mayor que 0
        while n > 0:
            # Si el bit menos significativo es 1, suma el punto actual al resultado
            if n & 1:
                product = AddPoints(curve, product, current_point)

            # Se duplica el punto actual
            current_point = AddPoints(curve, current_point, current_point)

            # Se desplaza el escalar n un bit hacia la derecha
            n >>= 1
    # Caso n es una tupla de escalares
    elif isinstance(n, tuple):
        for scalar in n:
            product = SelfProductPoint(curve, scalar, product)

    return product


def IsGroup(curve):
    """
    EXERCISE 3.2: xxx
    :curve: check if the curve is a group
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    return isElliptic(curve)


def OrderPoint(curve, P):
    """
    EXERCISE 3.3: Point order
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    point_order = 1
    Q = P

    # Se itera hasta que se llega al punto del infinito
    while Q != P_INFINITY:
        Q = AddPoints(curve, Q, P)
        point_order += 1

    return point_order


def GenKey(curve, P):
    """
    EXERCISE 4.1: Generate a pair of keys
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :return: a pair of keys (pub, priv)
    """

    a, b, p = curve

    # Se genera la clave privada
    priv = random.randint(1, p)

    # Se genera la clave publica
    pub = SelfProductPoint(curve, priv, P)

    key = (pub, priv)
    return key


def SharedKey(curve, priv_user1, pub_user2):
    """
    EXERCISE 4.2: Generate a shared secret
    :curve: a list with the curve values [a, b, p]
    :pub_user1: a public key
    :pub_user2: a private key
    :return: shared secret
    """

    shared = SelfProductPoint(curve, pub_user2, priv_user1)
    return shared
