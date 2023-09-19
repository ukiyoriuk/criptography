#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

# from P2023_Practica3_Solution_Skeleton import *
from elliptic_curve import *


class Test_Ex1_1(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        expected_num_points = 12
        num_points = ComputePoints(curve)
        self.assertEqual(num_points, expected_num_points)

    def test_2(self):
        curve = [3, 7, 23]
        expected_num_points = 20
        num_points = ComputePoints(curve)
        self.assertEqual(num_points, expected_num_points)

    def test_3(self):
        curve = [3, 7, 101]
        expected_num_points = 91
        num_points = ComputePoints(curve)
        self.assertEqual(num_points, expected_num_points)

    def test_4(self):
        curve = [5, 31, 17]
        expected_num_points = 14
        num_points = ComputePoints(curve)
        self.assertEqual(num_points, expected_num_points)

    def test_5(self):
        curve = [9, 6, 19]
        expected_num_points = 19
        num_points = ComputePoints(curve)
        self.assertEqual(num_points, expected_num_points)


class Test_Ex1_2(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        num_points = 12
        r = VerifyNumPoints(curve, num_points)
        self.assertEqual(r, True)

        r = VerifyNumPoints(curve, num_points + 15)
        self.assertEqual(r, False)

        r = VerifyNumPoints(curve, num_points - 15)
        self.assertEqual(r, False)

    def test_2(self):
        curve = [3, 7, 23]
        num_points = 20
        r = VerifyNumPoints(curve, num_points)
        self.assertEqual(r, True)

        r = VerifyNumPoints(curve, num_points + 15)
        self.assertEqual(r, False)

        r = VerifyNumPoints(curve, num_points - 15)
        self.assertEqual(r, False)

    def test_3(self):
        curve = [3, 7, 101]
        num_points = 91
        r = VerifyNumPoints(curve, num_points)
        self.assertEqual(r, True)

        r = VerifyNumPoints(curve, num_points + 40)
        self.assertEqual(r, False)

        r = VerifyNumPoints(curve, num_points - 40)
        self.assertEqual(r, False)

    def test_4(self):
        curve = [5, 31, 17]
        num_points = 14
        r = VerifyNumPoints(curve, num_points)
        self.assertEqual(r, True)

        r = VerifyNumPoints(curve, num_points + 15)
        self.assertEqual(r, False)

        r = VerifyNumPoints(curve, num_points - 15)
        self.assertEqual(r, False)

    def test_5(self):
        curve = [9, 6, 19]
        num_points = 19
        r = VerifyNumPoints(curve, num_points)
        self.assertEqual(r, True)

        r = VerifyNumPoints(curve, num_points + 15)
        self.assertEqual(r, False)

        r = VerifyNumPoints(curve, num_points - 15)
        self.assertEqual(r, False)


class Test_Ex2_1(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        P = (10, 0)
        Q = (9, 2)
        R = AddPoints(curve, P, Q)
        expected_R = (7, 5)
        self.assertEqual(R, expected_R)

    def test_2(self):
        curve = [0, 1, 11]
        P = (10, 0)
        R = AddPoints(curve, P, P)
        expected_R = P_INFINITY
        self.assertEqual(R, expected_R)

    def test_3(self):
        curve = [0, 1, 11]
        P = (9, 2)
        R = AddPoints(curve, P, P)
        expected_R = (2, 8)
        self.assertEqual(R, expected_R)

    def test_4(self):
        curve = [3, 7, 101]
        P = (87, 94)
        Q = (51, 81)
        R = AddPoints(curve, P, Q)
        expected_R = (60, 42)
        self.assertEqual(R, expected_R)

    def test_5(self):
        curve = [3, 7, 101]
        P = (87, 94)
        R = AddPoints(curve, P, P)
        expected_R = (41, 13)
        self.assertEqual(R, expected_R)

    def test_6(self):
        curve = [3, 7, 101]
        P = (51, 81)
        R = AddPoints(curve, P, P)
        expected_R = (79, 10)
        self.assertEqual(R, expected_R)

    def test_7(self):
        curve = [3, 7, 101]
        P = (51, 81)
        R = AddPoints(curve, P, P_INFINITY)
        expected_R = P
        self.assertEqual(R, expected_R)

    def test_8(self):
        curve = [3, 7, 101]
        P = (51, 81)
        R = AddPoints(curve, P_INFINITY, P)
        expected_R = P
        self.assertEqual(R, expected_R)


class Test_Ex3_1(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        n = 1
        P = (0, 10)
        R = SelfProductPoint(curve, n, P)
        expected_R = (0, 10)
        self.assertEqual(R, expected_R)

    def test_2(self):
        curve = [0, 1, 11]
        n = 2
        P = (0, 10)
        R = SelfProductPoint(curve, n, P)
        expected_R = (0, 1)
        self.assertEqual(R, expected_R)

    def test_3(self):
        curve = [0, 1, 11]
        n = 5
        P = (0, 10)
        R = SelfProductPoint(curve, n, P)
        expected_R = (0, 1)
        self.assertEqual(R, expected_R)

    def test_4(self):
        curve = [3, 7, 101]
        n = 31
        P = (61, 74)
        R = SelfProductPoint(curve, n, P)
        expected_R = (34, 15)
        self.assertEqual(R, expected_R)

    def test_5(self):
        curve = [3, 7, 13435686514322281333]
        n = 111111111111111
        P = (7045079013845402941, 10452172095203059543)
        R = SelfProductPoint(curve, n, P)
        expected_R = (10708246960187464146, 13140430156227645527)
        self.assertEqual(R, expected_R)


class Test_Ex3_2(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        expected = True
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_2(self):
        curve = [3, 7, 101]
        expected = True
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_3(self):
        curve = [9, 6, 19]
        expected = True
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_4(self):
        curve = [3, 7, 23]
        expected = True
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_5(self):
        curve = [7, 4, 11]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_6(self):
        curve = [0, 0, 19]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_7(self):
        curve = [1, 3, 19]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_8(self):
        curve = [1, 16, 19]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_9(self):
        curve = [7, 16, 19]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_10(self):
        curve = [73, 79, 101]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)

    def test_11(self):
        curve = [83, 64, 101]
        expected = False
        result = IsGroup(curve)
        self.assertEqual(result, expected)


class Test_Ex3_3(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        P = (10, 0)
        point_order = OrderPoint(curve, P)
        expected_OrderPoint = 2
        self.assertEqual(point_order, expected_OrderPoint)

    def test_2(self):
        curve = [3, 7, 101]
        P = (85, 2)
        point_order = OrderPoint(curve, P)
        expected_OrderPoint = 91
        self.assertEqual(point_order, expected_OrderPoint)

    def test_3(self):
        curve = [8, 11, 101]
        P = (66, 65)
        point_order = OrderPoint(curve, P)
        expected_OrderPoint = 43
        self.assertEqual(point_order, expected_OrderPoint)


class Test_Ex4(unittest.TestCase):

    def test_1(self):
        curve = [0, 1, 11]
        P = (10, 0)
        pub_A, priv_A = GenKey(curve, P)
        pub_B, priv_B = GenKey(curve, P)
        shared_A = SharedKey(curve, priv_A, pub_B)
        shared_B = SharedKey(curve, priv_B, pub_A)
        self.assertEqual(shared_A, shared_B)
        self.assertNotEqual(shared_A, None)
        self.assertNotEqual(shared_B, None)

    def test_2(self):
        curve = [0, 1, 11]
        P = (9, 2)
        pub_A, priv_A = GenKey(curve, P)
        pub_B, priv_B = GenKey(curve, P)
        shared_A = SharedKey(curve, priv_A, pub_B)
        shared_B = SharedKey(curve, priv_B, pub_A)
        self.assertEqual(shared_A, shared_B)
        self.assertNotEqual(shared_A, None)
        self.assertNotEqual(shared_B, None)

    def test_3(self):
        curve = [3, 7, 101]
        P = (61, 74)
        pub_A, priv_A = GenKey(curve, P)
        pub_B, priv_B = GenKey(curve, P)
        shared_A = SharedKey(curve, priv_A, pub_B)
        shared_B = SharedKey(curve, priv_B, pub_A)
        self.assertEqual(shared_A, shared_B)
        self.assertNotEqual(shared_A, None)
        self.assertNotEqual(shared_B, None)

    def test_4(self):
        curve = [3, 7, 101]
        P = (51, 81)
        pub_A, priv_A = GenKey(curve, P)
        pub_B, priv_B = GenKey(curve, P)
        shared_A = SharedKey(curve, priv_A, pub_B)
        shared_B = SharedKey(curve, priv_B, pub_A)
        self.assertEqual(shared_A, shared_B)
        self.assertNotEqual(shared_A, None)
        self.assertNotEqual(shared_B, None)


if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [
        Test_Ex1_1,
        Test_Ex1_2,
        Test_Ex2_1,
        Test_Ex3_1,
        Test_Ex3_2,
        Test_Ex3_3,
        Test_Ex4,
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
