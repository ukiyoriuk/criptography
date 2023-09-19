#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

# from P2023_Practica1_Solution_Skeleton import *
from P2023_Practica1_Skeleton import *


def assert_grille(obj, key, ct, pt):
    obj.assertNotEqual(ct, "")
    obj.assertNotEqual(pt, "")
    j = 0
    for i in range(len(ct)):
        if key[i % len(key)] == 1:
            obj.assertEqual(ct[i], pt[j])
            j += 1


class Test_Ex1(unittest.TestCase):

    def test_1(self):
        plaintext = "ABCD"
        expected_ciphertext = "DEFG"
        ciphertext = rotative_encrypt(plaintext, 3)
        self.assertEqual(ciphertext, expected_ciphertext)

    def test_2(self):
        plaintext = "HELLOWORLD"
        expected_ciphertext = "0X447A7 4W"
        ciphertext = rotative_encrypt(plaintext, 19)
        self.assertEqual(ciphertext, expected_ciphertext)

    def test_3(self):
        plaintext = "ESTOESUNMENSAJEUNPOQUITOMASLARGOQUEELANTERIOR"
        expected_ciphertext = "JXYTJXZSRJSXFOJZSUTVZNYTRFXQFWLTVZJJQFSYJWNTW"
        ciphertext = rotative_encrypt(plaintext, 5)
        self.assertEqual(ciphertext, expected_ciphertext)


class Test_Ex2(unittest.TestCase):

    def test_1(self):
        ciphertext = "DEFG"
        expected_plaintext = "ABCD"
        plaintext = rotative_decrypt(ciphertext, 3)
        self.assertEqual(plaintext, expected_plaintext)

    def test_2(self):
        ciphertext = "0X447A7 4W"
        expected_plaintext = "HELLOWORLD"
        plaintext = rotative_decrypt(ciphertext, 19)
        self.assertEqual(plaintext, expected_plaintext)

    def test_3(self):
        ciphertext = "JXYTJXZSRJSXFOJZSUTVZNYTRFXQFWLTVZJJQFSYJWNTW"
        expected_plaintext = "ESTOESUNMENSAJEUNPOQUITOMASLARGOQUEELANTERIOR"
        plaintext = rotative_decrypt(ciphertext, 5)
        self.assertEqual(plaintext, expected_plaintext)


class Test_Ex3(unittest.TestCase):

    def test_1(self):
        grille_len = 10
        num_holes = 5
        key = grille_genkey(grille_len, num_holes)
        self.assertEqual(len(key), grille_len)
        self.assertEqual(sum(key), num_holes)

    def test_2(self):
        grille_len = 50
        num_holes = 5
        key = grille_genkey(grille_len, num_holes)
        self.assertEqual(len(key), grille_len)
        self.assertEqual(sum(key), num_holes)

    def test_3(self):
        grille_len = 100
        num_holes = 25
        key = grille_genkey(grille_len, num_holes)
        self.assertEqual(len(key), grille_len)
        self.assertEqual(sum(key), num_holes)

    def test_4(self):
        grille_len = 50
        num_holes = 10
        key1 = grille_genkey(grille_len, num_holes)
        key2 = grille_genkey(grille_len, num_holes)
        self.assertNotEqual(key1, key2)

    def test_5(self):
        grille_len = 100
        num_holes = 25
        key1 = grille_genkey(grille_len, num_holes)
        key2 = grille_genkey(grille_len, num_holes)
        self.assertNotEqual(key1, key2)


class Test_Ex4(unittest.TestCase):

    def test_1(self):
        key = [0, 0, 0, 1, 1]
        plaintext = "HELLO"
        ciphertext = grille_encrypt(key, plaintext)
        assert_grille(self, key, ciphertext, plaintext)

    def test_2(self):
        key = [1, 0, 1, 0, 1]
        plaintext = "HELLOWORLD"
        ciphertext = grille_encrypt(key, plaintext)
        assert_grille(self, key, ciphertext, plaintext)

    def test_3(self):
        key = [1, 0, 0, 0, 1, 0, 1]
        plaintext = "THIS IS A VERY SECRET MESSAGE"
        ciphertext = grille_encrypt(key, plaintext)
        assert_grille(self, key, ciphertext, plaintext)

    def test_4(self):
        key = grille_genkey(5, 2)
        plaintext = "IS THIS CRYPTOGRAPHY, STEGANOGRAPHY, BOTH OR NEITHER?"
        ciphertext = grille_encrypt(key, plaintext)
        assert_grille(self, key, ciphertext, plaintext)

    def test_5(self):
        key = grille_genkey(20, 10)
        plaintext = "IS THIS CRYPTOGRAPHY, STEGANOGRAPHY, BOTH OR NEITHER?"
        ciphertext = grille_encrypt(key, plaintext)
        assert_grille(self, key, ciphertext, plaintext)


class Test_Ex5(unittest.TestCase):

    def test_1(self):
        key = [0, 0, 0, 1, 1]
        ciphertext = "___HE___LL___O"
        expected_plaintext = "HELLO"
        cleartext = grille_decrypt(key, ciphertext)
        self.assertEqual(cleartext, expected_plaintext)

    def test_2(self):
        key = [1, 0, 1, 0, 1]
        ciphertext = "H_E_LL_O_WO_R_LD"
        expected_plaintext = "HELLOWORLD"
        cleartext = grille_decrypt(key, ciphertext)
        self.assertEqual(cleartext, expected_plaintext)

    def test_3(self):
        key = [1, 0, 0, 0, 1, 0, 1]
        ciphertext = "TGV.HGISRAZ JIS4TX MA T.NV5ERWP7Y4 S8O0E0CRQC1E8T PW8M:ES74OS2AG?ZJE"
        expected_plaintext = "THIS IS A VERY SECRET MESSAGE"
        cleartext = grille_decrypt(key, ciphertext)
        self.assertEqual(cleartext, expected_plaintext)

    def test_4(self):
        key = grille_genkey(5, 2)
        plaintext = "THIS IS A VERY SECRET MESSAGE"
        ciphertext = grille_encrypt(key, plaintext)
        cleartext = grille_decrypt(key, ciphertext)
        self.assertEqual(cleartext, plaintext)


class Test_Ex6(unittest.TestCase):

    def test_1(self):
        key = grille_genkey(5, 2)
        plaintext = "THIS IS A VERY SECRET MESSAGE"
        ciphertext = encrypt(key, plaintext)
        cleartext = decrypt(key, ciphertext)
        self.assertEqual(cleartext, plaintext)


if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [
        Test_Ex1,
        Test_Ex2,
        Test_Ex3,
        Test_Ex4,
        Test_Ex5,
        Test_Ex6,
    ]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)
