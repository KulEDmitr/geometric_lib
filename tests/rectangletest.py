import rectangle
import unittest


class RectangleTestCase(unittest.TestCase):
    def test_area_positive_int_values(self):
        res = rectangle.area(4, 7)
        self.assertEqual(28, res, "Failed for positive int values")

    def test_area_positive_float_values(self):
        res = rectangle.area(3.5, 2.5)
        self.assertAlmostEqual(8.75, res, places=6, msg="Failed for float values")

    def test_area_zero_values(self):
        res = rectangle.area(0, 7)
        self.assertEqual(0, res, "Failed for zero values")

    def test_area_negative_int_values(self):
        with self.assertRaises(ValueError):
            rectangle.area(-4, 7)

    def test_area_negative_int_values(self):
        with self.assertRaises(ValueError):
            rectangle.area(-4.8, 7.1)

    def test_area_string_and_string_values(self):
        with self.assertRaises(TypeError):
            rectangle.area("4", "7")

    def test_area_string_and_int_values(self):
        with self.assertRaises(TypeError):
            rectangle.area("4", 7)

    def test_area_string_and_float_values(self):
        with self.assertRaises(TypeError):
            rectangle.area("4", 7.3)

    def test_perimeter_positive_int_values(self):
        res = rectangle.perimeter(3, 5)
        self.assertEqual(16, res, "Failed for positive int values")

    def test_perimeter_positive_float_values(self):
        res = rectangle.perimeter(3.5, 2.5)
        self.assertAlmostEqual(12.0, res, places=6, msg="Failed for float values")

    def test_perimeter_zero_values(self):
        res = rectangle.perimeter(0, 5)
        self.assertEqual(res, 10, "Failed for zero values")

    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 5)

    def test_perimeter_negative_float_values(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3.5, 2.5)

    def test_perimeter_string_and_string_values(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("3", "5")

    def test_perimeter_string_and_int_values(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("3", 5)

    def test_perimeter_string_and_float_values(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("3", 5.3)




# additional tests
    def test_area_1_1_values(self):
        res = rectangle.area(1, 1)
        self.assertEqual(1, res)

    def test_area_1_2_values(self):
        res = rectangle.area(1, 2)
        self.assertEqual(2, res)

    def test_area_1_3_values(self):
        res = rectangle.area(1, 3)
        self.assertEqual(3, res)

    def test_area_1_4_values(self):
        res = rectangle.area(1, 4)
        self.assertEqual(4, res)

    def test_area_1_5_values(self):
        res = rectangle.area(1, 5)
        self.assertEqual(5, res)

    def test_area_1_6_values(self):
        res = rectangle.area(1, 6)
        self.assertEqual(6, res)

    def test_area_1_7_values(self):
        res = rectangle.area(1, 7)
        self.assertEqual(7, res)

    def test_area_1_8_values(self):
        res = rectangle.area(1, 8)
        self.assertEqual(8, res)

    def test_area_1_9_values(self):
        res = rectangle.area(1, 9)
        self.assertEqual(9, res)

    def test_area_1_10_values(self):
        res = rectangle.area(1, 10)
        self.assertEqual(10, res)

    def test_area_1_11_values(self):
        res = rectangle.area(1, 11)
        self.assertEqual(11, res)

    def test_area_1_12_values(self):
        res = rectangle.area(1, 12)
        self.assertEqual(12, res)

    def test_area_1_13_values(self):
        res = rectangle.area(1, 13)
        self.assertEqual(13, res)

    def test_area_1_14_values(self):
        res = rectangle.area(1, 14)
        self.assertEqual(14, res)

    def test_area_1_15_values(self):
        res = rectangle.area(1, 15)
        self.assertEqual(15, res)

    def test_area_1_16_values(self):
        res = rectangle.area(1, 16)
        self.assertEqual(16, res)

    def test_area_1_17_values(self):
        res = rectangle.area(1, 17)
        self.assertEqual(17, res)

    def test_area_1_18_values(self):
        res = rectangle.area(1, 18)
        self.assertEqual(18, res)

    def test_area_1_19_values(self):
        res = rectangle.area(1, 19)
        self.assertEqual(19, res)

    def test_area_1_20_values(self):
        res = rectangle.area(1, 20)
        self.assertEqual(20, res)

    def test_area_1_21_values(self):
        res = rectangle.area(1, 21)
        self.assertEqual(21, res)

    def test_area_1_22_values(self):
        res = rectangle.area(1, 22)
        self.assertEqual(22, res)

    def test_area_1_23_values(self):
        res = rectangle.area(1, 23)
        self.assertEqual(23, res)

    def test_area_1_24_values(self):
        res = rectangle.area(1, 24)
        self.assertEqual(24, res)

    def test_area_1_25_values(self):
        res = rectangle.area(1, 25)
        self.assertEqual(25, res)

    def test_area_1_26_values(self):
        res = rectangle.area(1, 26)
        self.assertEqual(26, res)

    def test_area_1_27_values(self):
        res = rectangle.area(1, 27)
        self.assertEqual(27, res)

    def test_area_1_28_values(self):
        res = rectangle.area(1, 28)
        self.assertEqual(28, res)

    def test_area_1_29_values(self):
        res = rectangle.area(1, 29)
        self.assertEqual(29, res)

    def test_area_2_1_values(self):
        res = rectangle.area(2, 1)
        self.assertEqual(2, res)

    def test_area_2_2_values(self):
        res = rectangle.area(2, 2)
        self.assertEqual(4, res)

    def test_area_2_3_values(self):
        res = rectangle.area(2, 3)
        self.assertEqual(6, res)

    def test_area_2_4_values(self):
        res = rectangle.area(2, 4)
        self.assertEqual(8, res)

    def test_area_2_5_values(self):
        res = rectangle.area(2, 5)
        self.assertEqual(10, res)

    def test_area_2_6_values(self):
        res = rectangle.area(2, 6)
        self.assertEqual(12, res)

    def test_area_2_7_values(self):
        res = rectangle.area(2, 7)
        self.assertEqual(14, res)

    def test_area_2_8_values(self):
        res = rectangle.area(2, 8)
        self.assertEqual(16, res)

    def test_area_2_9_values(self):
        res = rectangle.area(2, 9)
        self.assertEqual(18, res)

    def test_area_2_10_values(self):
        res = rectangle.area(2, 10)
        self.assertEqual(20, res)

    def test_area_2_11_values(self):
        res = rectangle.area(2, 11)
        self.assertEqual(22, res)

    def test_area_2_12_values(self):
        res = rectangle.area(2, 12)
        self.assertEqual(24, res)

    def test_area_2_13_values(self):
        res = rectangle.area(2, 13)
        self.assertEqual(26, res)

    def test_area_2_14_values(self):
        res = rectangle.area(2, 14)
        self.assertEqual(28, res)

    def test_area_2_15_values(self):
        res = rectangle.area(2, 15)
        self.assertEqual(30, res)

    def test_area_2_16_values(self):
        res = rectangle.area(2, 16)
        self.assertEqual(32, res)

    def test_area_2_17_values(self):
        res = rectangle.area(2, 17)
        self.assertEqual(34, res)

    def test_area_2_18_values(self):
        res = rectangle.area(2, 18)
        self.assertEqual(36, res)

    def test_area_2_19_values(self):
        res = rectangle.area(2, 19)
        self.assertEqual(38, res)

    def test_area_2_20_values(self):
        res = rectangle.area(2, 20)
        self.assertEqual(40, res)

    def test_area_2_21_values(self):
        res = rectangle.area(2, 21)
        self.assertEqual(42, res)

    def test_area_2_22_values(self):
        res = rectangle.area(2, 22)
        self.assertEqual(44, res)

    def test_area_2_23_values(self):
        res = rectangle.area(2, 23)
        self.assertEqual(46, res)

    def test_area_2_24_values(self):
        res = rectangle.area(2, 24)
        self.assertEqual(48, res)

    def test_area_2_25_values(self):
        res = rectangle.area(2, 25)
        self.assertEqual(50, res)

    def test_area_2_26_values(self):
        res = rectangle.area(2, 26)
        self.assertEqual(52, res)

    def test_area_2_27_values(self):
        res = rectangle.area(2, 27)
        self.assertEqual(54, res)

    def test_area_2_28_values(self):
        res = rectangle.area(2, 28)
        self.assertEqual(56, res)

    def test_area_2_29_values(self):
        res = rectangle.area(2, 29)
        self.assertEqual(58, res)

    def test_area_3_1_values(self):
        res = rectangle.area(3, 1)
        self.assertEqual(3, res)

    def test_area_3_2_values(self):
        res = rectangle.area(3, 2)
        self.assertEqual(6, res)

    def test_area_3_3_values(self):
        res = rectangle.area(3, 3)
        self.assertEqual(9, res)

    def test_area_3_4_values(self):
        res = rectangle.area(3, 4)
        self.assertEqual(12, res)

    def test_area_3_5_values(self):
        res = rectangle.area(3, 5)
        self.assertEqual(15, res)

    def test_area_3_6_values(self):
        res = rectangle.area(3, 6)
        self.assertEqual(18, res)

    def test_area_3_7_values(self):
        res = rectangle.area(3, 7)
        self.assertEqual(21, res)

    def test_area_3_8_values(self):
        res = rectangle.area(3, 8)
        self.assertEqual(24, res)

    def test_area_3_9_values(self):
        res = rectangle.area(3, 9)
        self.assertEqual(27, res)

    def test_area_3_10_values(self):
        res = rectangle.area(3, 10)
        self.assertEqual(30, res)

    def test_area_3_11_values(self):
        res = rectangle.area(3, 11)
        self.assertEqual(33, res)

    def test_area_3_12_values(self):
        res = rectangle.area(3, 12)
        self.assertEqual(36, res)

    def test_area_3_13_values(self):
        res = rectangle.area(3, 13)
        self.assertEqual(39, res)

    def test_area_3_14_values(self):
        res = rectangle.area(3, 14)
        self.assertEqual(42, res)

    def test_area_3_15_values(self):
        res = rectangle.area(3, 15)
        self.assertEqual(45, res)

    def test_area_3_16_values(self):
        res = rectangle.area(3, 16)
        self.assertEqual(48, res)

    def test_area_3_17_values(self):
        res = rectangle.area(3, 17)
        self.assertEqual(51, res)

    def test_area_3_18_values(self):
        res = rectangle.area(3, 18)
        self.assertEqual(54, res)

    def test_area_3_19_values(self):
        res = rectangle.area(3, 19)
        self.assertEqual(57, res)

    def test_area_3_20_values(self):
        res = rectangle.area(3, 20)
        self.assertEqual(60, res)

    def test_area_3_21_values(self):
        res = rectangle.area(3, 21)
        self.assertEqual(63, res)

    def test_area_3_22_values(self):
        res = rectangle.area(3, 22)
        self.assertEqual(66, res)

    def test_area_3_23_values(self):
        res = rectangle.area(3, 23)
        self.assertEqual(69, res)

    def test_area_3_24_values(self):
        res = rectangle.area(3, 24)
        self.assertEqual(72, res)

    def test_area_3_25_values(self):
        res = rectangle.area(3, 25)
        self.assertEqual(75, res)

    def test_area_3_26_values(self):
        res = rectangle.area(3, 26)
        self.assertEqual(78, res)

    def test_area_3_27_values(self):
        res = rectangle.area(3, 27)
        self.assertEqual(81, res)

    def test_area_3_28_values(self):
        res = rectangle.area(3, 28)
        self.assertEqual(84, res)

    def test_area_3_29_values(self):
        res = rectangle.area(3, 29)
        self.assertEqual(87, res)

    def test_area_4_1_values(self):
        res = rectangle.area(4, 1)
        self.assertEqual(4, res)

    def test_area_4_2_values(self):
        res = rectangle.area(4, 2)
        self.assertEqual(8, res)

    def test_area_4_3_values(self):
        res = rectangle.area(4, 3)
        self.assertEqual(12, res)

    def test_area_4_4_values(self):
        res = rectangle.area(4, 4)
        self.assertEqual(16, res)

    def test_area_4_5_values(self):
        res = rectangle.area(4, 5)
        self.assertEqual(20, res)

    def test_area_4_6_values(self):
        res = rectangle.area(4, 6)
        self.assertEqual(24, res)

    def test_area_4_7_values(self):
        res = rectangle.area(4, 7)
        self.assertEqual(28, res)

    def test_area_4_8_values(self):
        res = rectangle.area(4, 8)
        self.assertEqual(32, res)

    def test_area_4_9_values(self):
        res = rectangle.area(4, 9)
        self.assertEqual(36, res)

    def test_area_4_10_values(self):
        res = rectangle.area(4, 10)
        self.assertEqual(40, res)

    def test_area_4_11_values(self):
        res = rectangle.area(4, 11)
        self.assertEqual(44, res)

    def test_area_4_12_values(self):
        res = rectangle.area(4, 12)
        self.assertEqual(48, res)

    def test_area_4_13_values(self):
        res = rectangle.area(4, 13)
        self.assertEqual(52, res)

    def test_area_4_14_values(self):
        res = rectangle.area(4, 14)
        self.assertEqual(56, res)

    def test_area_4_15_values(self):
        res = rectangle.area(4, 15)
        self.assertEqual(60, res)

    def test_area_4_16_values(self):
        res = rectangle.area(4, 16)
        self.assertEqual(64, res)

    def test_area_4_17_values(self):
        res = rectangle.area(4, 17)
        self.assertEqual(68, res)

    def test_area_4_18_values(self):
        res = rectangle.area(4, 18)
        self.assertEqual(72, res)

    def test_area_4_19_values(self):
        res = rectangle.area(4, 19)
        self.assertEqual(76, res)

    def test_area_4_20_values(self):
        res = rectangle.area(4, 20)
        self.assertEqual(80, res)

    def test_area_4_21_values(self):
        res = rectangle.area(4, 21)
        self.assertEqual(84, res)

    def test_area_4_22_values(self):
        res = rectangle.area(4, 22)
        self.assertEqual(88, res)

    def test_area_4_23_values(self):
        res = rectangle.area(4, 23)
        self.assertEqual(92, res)

    def test_area_4_24_values(self):
        res = rectangle.area(4, 24)
        self.assertEqual(96, res)

    def test_area_4_25_values(self):
        res = rectangle.area(4, 25)
        self.assertEqual(100, res)

    def test_area_4_26_values(self):
        res = rectangle.area(4, 26)
        self.assertEqual(104, res)

    def test_area_4_27_values(self):
        res = rectangle.area(4, 27)
        self.assertEqual(108, res)

    def test_area_4_28_values(self):
        res = rectangle.area(4, 28)
        self.assertEqual(112, res)

    def test_area_4_29_values(self):
        res = rectangle.area(4, 29)
        self.assertEqual(116, res)

    def test_area_5_1_values(self):
        res = rectangle.area(5, 1)
        self.assertEqual(5, res)

    def test_area_5_2_values(self):
        res = rectangle.area(5, 2)
        self.assertEqual(10, res)

    def test_area_5_3_values(self):
        res = rectangle.area(5, 3)
        self.assertEqual(15, res)

    def test_area_5_4_values(self):
        res = rectangle.area(5, 4)
        self.assertEqual(20, res)

    def test_area_5_5_values(self):
        res = rectangle.area(5, 5)
        self.assertEqual(25, res)

    def test_area_5_6_values(self):
        res = rectangle.area(5, 6)
        self.assertEqual(30, res)

    def test_area_5_7_values(self):
        res = rectangle.area(5, 7)
        self.assertEqual(35, res)

    def test_area_5_8_values(self):
        res = rectangle.area(5, 8)
        self.assertEqual(40, res)

    def test_area_5_9_values(self):
        res = rectangle.area(5, 9)
        self.assertEqual(45, res)

    def test_area_5_10_values(self):
        res = rectangle.area(5, 10)
        self.assertEqual(50, res)

    def test_area_5_11_values(self):
        res = rectangle.area(5, 11)
        self.assertEqual(55, res)

    def test_area_5_12_values(self):
        res = rectangle.area(5, 12)
        self.assertEqual(60, res)

    def test_area_5_13_values(self):
        res = rectangle.area(5, 13)
        self.assertEqual(65, res)

    def test_area_5_14_values(self):
        res = rectangle.area(5, 14)
        self.assertEqual(70, res)

    def test_area_5_15_values(self):
        res = rectangle.area(5, 15)
        self.assertEqual(75, res)

    def test_area_5_16_values(self):
        res = rectangle.area(5, 16)
        self.assertEqual(80, res)

    def test_area_5_17_values(self):
        res = rectangle.area(5, 17)
        self.assertEqual(85, res)

    def test_area_5_18_values(self):
        res = rectangle.area(5, 18)
        self.assertEqual(90, res)

    def test_area_5_19_values(self):
        res = rectangle.area(5, 19)
        self.assertEqual(95, res)

    def test_area_5_20_values(self):
        res = rectangle.area(5, 20)
        self.assertEqual(100, res)

    def test_area_5_21_values(self):
        res = rectangle.area(5, 21)
        self.assertEqual(105, res)

    def test_area_5_22_values(self):
        res = rectangle.area(5, 22)
        self.assertEqual(110, res)

    def test_area_5_23_values(self):
        res = rectangle.area(5, 23)
        self.assertEqual(115, res)

    def test_area_5_24_values(self):
        res = rectangle.area(5, 24)
        self.assertEqual(120, res)

    def test_area_5_25_values(self):
        res = rectangle.area(5, 25)
        self.assertEqual(125, res)

    def test_area_5_26_values(self):
        res = rectangle.area(5, 26)
        self.assertEqual(130, res)

    def test_area_5_27_values(self):
        res = rectangle.area(5, 27)
        self.assertEqual(135, res)

    def test_area_5_28_values(self):
        res = rectangle.area(5, 28)
        self.assertEqual(140, res)

    def test_area_5_29_values(self):
        res = rectangle.area(5, 29)
        self.assertEqual(145, res)

    def test_area_6_1_values(self):
        res = rectangle.area(6, 1)
        self.assertEqual(6, res)

    def test_area_6_2_values(self):
        res = rectangle.area(6, 2)
        self.assertEqual(12, res)

    def test_area_6_3_values(self):
        res = rectangle.area(6, 3)
        self.assertEqual(18, res)

    def test_area_6_4_values(self):
        res = rectangle.area(6, 4)
        self.assertEqual(24, res)

    def test_area_6_5_values(self):
        res = rectangle.area(6, 5)
        self.assertEqual(30, res)

    def test_area_6_6_values(self):
        res = rectangle.area(6, 6)
        self.assertEqual(36, res)

    def test_area_6_7_values(self):
        res = rectangle.area(6, 7)
        self.assertEqual(42, res)

    def test_area_6_8_values(self):
        res = rectangle.area(6, 8)
        self.assertEqual(48, res)

    def test_area_6_9_values(self):
        res = rectangle.area(6, 9)
        self.assertEqual(54, res)

    def test_area_6_10_values(self):
        res = rectangle.area(6, 10)
        self.assertEqual(60, res)

    def test_area_6_11_values(self):
        res = rectangle.area(6, 11)
        self.assertEqual(66, res)

    def test_area_6_12_values(self):
        res = rectangle.area(6, 12)
        self.assertEqual(72, res)

    def test_area_6_13_values(self):
        res = rectangle.area(6, 13)
        self.assertEqual(78, res)

    def test_area_6_14_values(self):
        res = rectangle.area(6, 14)
        self.assertEqual(84, res)

    def test_area_6_15_values(self):
        res = rectangle.area(6, 15)
        self.assertEqual(90, res)

    def test_area_6_16_values(self):
        res = rectangle.area(6, 16)
        self.assertEqual(96, res)

    def test_area_6_17_values(self):
        res = rectangle.area(6, 17)
        self.assertEqual(102, res)

    def test_area_6_18_values(self):
        res = rectangle.area(6, 18)
        self.assertEqual(108, res)

    def test_area_6_19_values(self):
        res = rectangle.area(6, 19)
        self.assertEqual(114, res)

    def test_area_6_20_values(self):
        res = rectangle.area(6, 20)
        self.assertEqual(120, res)

    def test_area_6_21_values(self):
        res = rectangle.area(6, 21)
        self.assertEqual(126, res)

    def test_area_6_22_values(self):
        res = rectangle.area(6, 22)
        self.assertEqual(132, res)

    def test_area_6_23_values(self):
        res = rectangle.area(6, 23)
        self.assertEqual(138, res)

    def test_area_6_24_values(self):
        res = rectangle.area(6, 24)
        self.assertEqual(144, res)

    def test_area_6_25_values(self):
        res = rectangle.area(6, 25)
        self.assertEqual(150, res)

    def test_area_6_26_values(self):
        res = rectangle.area(6, 26)
        self.assertEqual(156, res)

    def test_area_6_27_values(self):
        res = rectangle.area(6, 27)
        self.assertEqual(162, res)

    def test_area_6_28_values(self):
        res = rectangle.area(6, 28)
        self.assertEqual(168, res)

    def test_area_6_29_values(self):
        res = rectangle.area(6, 29)
        self.assertEqual(174, res)

    def test_area_7_1_values(self):
        res = rectangle.area(7, 1)
        self.assertEqual(7, res)

    def test_area_7_2_values(self):
        res = rectangle.area(7, 2)
        self.assertEqual(14, res)

    def test_area_7_3_values(self):
        res = rectangle.area(7, 3)
        self.assertEqual(21, res)

    def test_area_7_4_values(self):
        res = rectangle.area(7, 4)
        self.assertEqual(28, res)

    def test_area_7_5_values(self):
        res = rectangle.area(7, 5)
        self.assertEqual(35, res)

    def test_area_7_6_values(self):
        res = rectangle.area(7, 6)
        self.assertEqual(42, res)

    def test_area_7_7_values(self):
        res = rectangle.area(7, 7)
        self.assertEqual(49, res)

    def test_area_7_8_values(self):
        res = rectangle.area(7, 8)
        self.assertEqual(56, res)

    def test_area_7_9_values(self):
        res = rectangle.area(7, 9)
        self.assertEqual(63, res)

    def test_area_7_10_values(self):
        res = rectangle.area(7, 10)
        self.assertEqual(70, res)

    def test_area_7_11_values(self):
        res = rectangle.area(7, 11)
        self.assertEqual(77, res)

    def test_area_7_12_values(self):
        res = rectangle.area(7, 12)
        self.assertEqual(84, res)

    def test_area_7_13_values(self):
        res = rectangle.area(7, 13)
        self.assertEqual(91, res)

    def test_area_7_14_values(self):
        res = rectangle.area(7, 14)
        self.assertEqual(98, res)

    def test_area_7_15_values(self):
        res = rectangle.area(7, 15)
        self.assertEqual(105, res)

    def test_area_7_16_values(self):
        res = rectangle.area(7, 16)
        self.assertEqual(112, res)

    def test_area_7_17_values(self):
        res = rectangle.area(7, 17)
        self.assertEqual(119, res)

    def test_area_7_18_values(self):
        res = rectangle.area(7, 18)
        self.assertEqual(126, res)

    def test_area_7_19_values(self):
        res = rectangle.area(7, 19)
        self.assertEqual(133, res)

    def test_area_7_20_values(self):
        res = rectangle.area(7, 20)
        self.assertEqual(140, res)

    def test_area_7_21_values(self):
        res = rectangle.area(7, 21)
        self.assertEqual(147, res)

    def test_area_7_22_values(self):
        res = rectangle.area(7, 22)
        self.assertEqual(154, res)

    def test_area_7_23_values(self):
        res = rectangle.area(7, 23)
        self.assertEqual(161, res)

    def test_area_7_24_values(self):
        res = rectangle.area(7, 24)
        self.assertEqual(168, res)

    def test_area_7_25_values(self):
        res = rectangle.area(7, 25)
        self.assertEqual(175, res)

    def test_area_7_26_values(self):
        res = rectangle.area(7, 26)
        self.assertEqual(182, res)

    def test_area_7_27_values(self):
        res = rectangle.area(7, 27)
        self.assertEqual(189, res)

    def test_area_7_28_values(self):
        res = rectangle.area(7, 28)
        self.assertEqual(196, res)

    def test_area_7_29_values(self):
        res = rectangle.area(7, 29)
        self.assertEqual(203, res)

    def test_area_8_1_values(self):
        res = rectangle.area(8, 1)
        self.assertEqual(8, res)

    def test_area_8_2_values(self):
        res = rectangle.area(8, 2)
        self.assertEqual(16, res)

    def test_area_8_3_values(self):
        res = rectangle.area(8, 3)
        self.assertEqual(24, res)

    def test_area_8_4_values(self):
        res = rectangle.area(8, 4)
        self.assertEqual(32, res)

    def test_area_8_5_values(self):
        res = rectangle.area(8, 5)
        self.assertEqual(40, res)

    def test_area_8_6_values(self):
        res = rectangle.area(8, 6)
        self.assertEqual(48, res)

    def test_area_8_7_values(self):
        res = rectangle.area(8, 7)
        self.assertEqual(56, res)

    def test_area_8_8_values(self):
        res = rectangle.area(8, 8)
        self.assertEqual(64, res)

    def test_area_8_9_values(self):
        res = rectangle.area(8, 9)
        self.assertEqual(72, res)

    def test_area_8_10_values(self):
        res = rectangle.area(8, 10)
        self.assertEqual(80, res)

    def test_area_8_11_values(self):
        res = rectangle.area(8, 11)
        self.assertEqual(88, res)

    def test_area_8_12_values(self):
        res = rectangle.area(8, 12)
        self.assertEqual(96, res)

    def test_area_8_13_values(self):
        res = rectangle.area(8, 13)
        self.assertEqual(104, res)

    def test_area_8_14_values(self):
        res = rectangle.area(8, 14)
        self.assertEqual(112, res)

    def test_area_8_15_values(self):
        res = rectangle.area(8, 15)
        self.assertEqual(120, res)

    def test_area_8_16_values(self):
        res = rectangle.area(8, 16)
        self.assertEqual(128, res)

    def test_area_8_17_values(self):
        res = rectangle.area(8, 17)
        self.assertEqual(136, res)

    def test_area_8_18_values(self):
        res = rectangle.area(8, 18)
        self.assertEqual(144, res)

    def test_area_8_19_values(self):
        res = rectangle.area(8, 19)
        self.assertEqual(152, res)

    def test_area_8_20_values(self):
        res = rectangle.area(8, 20)
        self.assertEqual(160, res)

    def test_area_8_21_values(self):
        res = rectangle.area(8, 21)
        self.assertEqual(168, res)

    def test_area_8_22_values(self):
        res = rectangle.area(8, 22)
        self.assertEqual(176, res)

    def test_area_8_23_values(self):
        res = rectangle.area(8, 23)
        self.assertEqual(184, res)

    def test_area_8_24_values(self):
        res = rectangle.area(8, 24)
        self.assertEqual(192, res)

    def test_area_8_25_values(self):
        res = rectangle.area(8, 25)
        self.assertEqual(200, res)

    def test_area_8_26_values(self):
        res = rectangle.area(8, 26)
        self.assertEqual(208, res)

    def test_area_8_27_values(self):
        res = rectangle.area(8, 27)
        self.assertEqual(216, res)

    def test_area_8_28_values(self):
        res = rectangle.area(8, 28)
        self.assertEqual(224, res)

    def test_area_8_29_values(self):
        res = rectangle.area(8, 29)
        self.assertEqual(232, res)

    def test_area_9_1_values(self):
        res = rectangle.area(9, 1)
        self.assertEqual(9, res)

    def test_area_9_2_values(self):
        res = rectangle.area(9, 2)
        self.assertEqual(18, res)

    def test_area_9_3_values(self):
        res = rectangle.area(9, 3)
        self.assertEqual(27, res)

    def test_area_9_4_values(self):
        res = rectangle.area(9, 4)
        self.assertEqual(36, res)

    def test_area_9_5_values(self):
        res = rectangle.area(9, 5)
        self.assertEqual(45, res)

    def test_area_9_6_values(self):
        res = rectangle.area(9, 6)
        self.assertEqual(54, res)

    def test_area_9_7_values(self):
        res = rectangle.area(9, 7)
        self.assertEqual(63, res)

    def test_area_9_8_values(self):
        res = rectangle.area(9, 8)
        self.assertEqual(72, res)

    def test_area_9_9_values(self):
        res = rectangle.area(9, 9)
        self.assertEqual(81, res)

    def test_area_9_10_values(self):
        res = rectangle.area(9, 10)
        self.assertEqual(90, res)

    def test_area_9_11_values(self):
        res = rectangle.area(9, 11)
        self.assertEqual(99, res)

    def test_area_9_12_values(self):
        res = rectangle.area(9, 12)
        self.assertEqual(108, res)

    def test_area_9_13_values(self):
        res = rectangle.area(9, 13)
        self.assertEqual(117, res)

    def test_area_9_14_values(self):
        res = rectangle.area(9, 14)
        self.assertEqual(126, res)

    def test_area_9_15_values(self):
        res = rectangle.area(9, 15)
        self.assertEqual(135, res)

    def test_area_9_16_values(self):
        res = rectangle.area(9, 16)
        self.assertEqual(144, res)

    def test_area_9_17_values(self):
        res = rectangle.area(9, 17)
        self.assertEqual(153, res)

    def test_area_9_18_values(self):
        res = rectangle.area(9, 18)
        self.assertEqual(162, res)

    def test_area_9_19_values(self):
        res = rectangle.area(9, 19)
        self.assertEqual(171, res)

    def test_area_9_20_values(self):
        res = rectangle.area(9, 20)
        self.assertEqual(180, res)

    def test_area_9_21_values(self):
        res = rectangle.area(9, 21)
        self.assertEqual(189, res)

    def test_area_9_22_values(self):
        res = rectangle.area(9, 22)
        self.assertEqual(198, res)

    def test_area_9_23_values(self):
        res = rectangle.area(9, 23)
        self.assertEqual(207, res)

    def test_area_9_24_values(self):
        res = rectangle.area(9, 24)
        self.assertEqual(216, res)

    def test_area_9_25_values(self):
        res = rectangle.area(9, 25)
        self.assertEqual(225, res)

    def test_area_9_26_values(self):
        res = rectangle.area(9, 26)
        self.assertEqual(234, res)

    def test_area_9_27_values(self):
        res = rectangle.area(9, 27)
        self.assertEqual(243, res)

    def test_area_9_28_values(self):
        res = rectangle.area(9, 28)
        self.assertEqual(252, res)

    def test_area_9_29_values(self):
        res = rectangle.area(9, 29)
        self.assertEqual(261, res)

    def test_area_10_1_values(self):
        res = rectangle.area(10, 1)
        self.assertEqual(10, res)

    def test_area_10_2_values(self):
        res = rectangle.area(10, 2)
        self.assertEqual(20, res)

    def test_area_10_3_values(self):
        res = rectangle.area(10, 3)
        self.assertEqual(30, res)

    def test_area_10_4_values(self):
        res = rectangle.area(10, 4)
        self.assertEqual(40, res)

    def test_area_10_5_values(self):
        res = rectangle.area(10, 5)
        self.assertEqual(50, res)

    def test_area_10_6_values(self):
        res = rectangle.area(10, 6)
        self.assertEqual(60, res)

    def test_area_10_7_values(self):
        res = rectangle.area(10, 7)
        self.assertEqual(70, res)

    def test_area_10_8_values(self):
        res = rectangle.area(10, 8)
        self.assertEqual(80, res)

    def test_area_10_9_values(self):
        res = rectangle.area(10, 9)
        self.assertEqual(90, res)

    def test_area_10_10_values(self):
        res = rectangle.area(10, 10)
        self.assertEqual(100, res)

    def test_area_10_11_values(self):
        res = rectangle.area(10, 11)
        self.assertEqual(110, res)

    def test_area_10_12_values(self):
        res = rectangle.area(10, 12)
        self.assertEqual(120, res)

    def test_area_10_13_values(self):
        res = rectangle.area(10, 13)
        self.assertEqual(130, res)

    def test_area_10_14_values(self):
        res = rectangle.area(10, 14)
        self.assertEqual(140, res)

    def test_area_10_15_values(self):
        res = rectangle.area(10, 15)
        self.assertEqual(150, res)

    def test_area_10_16_values(self):
        res = rectangle.area(10, 16)
        self.assertEqual(160, res)

    def test_area_10_17_values(self):
        res = rectangle.area(10, 17)
        self.assertEqual(170, res)

    def test_area_10_18_values(self):
        res = rectangle.area(10, 18)
        self.assertEqual(180, res)

    def test_area_10_19_values(self):
        res = rectangle.area(10, 19)
        self.assertEqual(190, res)

    def test_area_10_20_values(self):
        res = rectangle.area(10, 20)
        self.assertEqual(200, res)

    def test_area_10_21_values(self):
        res = rectangle.area(10, 21)
        self.assertEqual(210, res)

    def test_area_10_22_values(self):
        res = rectangle.area(10, 22)
        self.assertEqual(220, res)

    def test_area_10_23_values(self):
        res = rectangle.area(10, 23)
        self.assertEqual(230, res)

    def test_area_10_24_values(self):
        res = rectangle.area(10, 24)
        self.assertEqual(240, res)

    def test_area_10_25_values(self):
        res = rectangle.area(10, 25)
        self.assertEqual(250, res)

    def test_area_10_26_values(self):
        res = rectangle.area(10, 26)
        self.assertEqual(260, res)

    def test_area_10_27_values(self):
        res = rectangle.area(10, 27)
        self.assertEqual(270, res)

    def test_area_10_28_values(self):
        res = rectangle.area(10, 28)
        self.assertEqual(280, res)

    def test_area_10_29_values(self):
        res = rectangle.area(10, 29)
        self.assertEqual(290, res)

    def test_area_11_1_values(self):
        res = rectangle.area(11, 1)
        self.assertEqual(11, res)

    def test_area_11_2_values(self):
        res = rectangle.area(11, 2)
        self.assertEqual(22, res)

    def test_area_11_3_values(self):
        res = rectangle.area(11, 3)
        self.assertEqual(33, res)

    def test_area_11_4_values(self):
        res = rectangle.area(11, 4)
        self.assertEqual(44, res)

    def test_area_11_5_values(self):
        res = rectangle.area(11, 5)
        self.assertEqual(55, res)

    def test_area_11_6_values(self):
        res = rectangle.area(11, 6)
        self.assertEqual(66, res)

    def test_area_11_7_values(self):
        res = rectangle.area(11, 7)
        self.assertEqual(77, res)

    def test_area_11_8_values(self):
        res = rectangle.area(11, 8)
        self.assertEqual(88, res)

    def test_area_11_9_values(self):
        res = rectangle.area(11, 9)
        self.assertEqual(99, res)

    def test_area_11_10_values(self):
        res = rectangle.area(11, 10)
        self.assertEqual(110, res)

    def test_area_11_11_values(self):
        res = rectangle.area(11, 11)
        self.assertEqual(121, res)

    def test_area_11_12_values(self):
        res = rectangle.area(11, 12)
        self.assertEqual(132, res)

    def test_area_11_13_values(self):
        res = rectangle.area(11, 13)
        self.assertEqual(143, res)

    def test_area_11_14_values(self):
        res = rectangle.area(11, 14)
        self.assertEqual(154, res)

    def test_area_11_15_values(self):
        res = rectangle.area(11, 15)
        self.assertEqual(165, res)

    def test_area_11_16_values(self):
        res = rectangle.area(11, 16)
        self.assertEqual(176, res)

    def test_area_11_17_values(self):
        res = rectangle.area(11, 17)
        self.assertEqual(187, res)

    def test_area_11_18_values(self):
        res = rectangle.area(11, 18)
        self.assertEqual(198, res)

    def test_area_11_19_values(self):
        res = rectangle.area(11, 19)
        self.assertEqual(209, res)

    def test_area_11_20_values(self):
        res = rectangle.area(11, 20)
        self.assertEqual(220, res)

    def test_area_11_21_values(self):
        res = rectangle.area(11, 21)
        self.assertEqual(231, res)

    def test_area_11_22_values(self):
        res = rectangle.area(11, 22)
        self.assertEqual(242, res)

    def test_area_11_23_values(self):
        res = rectangle.area(11, 23)
        self.assertEqual(253, res)

    def test_area_11_24_values(self):
        res = rectangle.area(11, 24)
        self.assertEqual(264, res)

    def test_area_11_25_values(self):
        res = rectangle.area(11, 25)
        self.assertEqual(275, res)

    def test_area_11_26_values(self):
        res = rectangle.area(11, 26)
        self.assertEqual(286, res)

    def test_area_11_27_values(self):
        res = rectangle.area(11, 27)
        self.assertEqual(297, res)

    def test_area_11_28_values(self):
        res = rectangle.area(11, 28)
        self.assertEqual(308, res)

    def test_area_11_29_values(self):
        res = rectangle.area(11, 29)
        self.assertEqual(319, res)

    def test_area_12_1_values(self):
        res = rectangle.area(12, 1)
        self.assertEqual(12, res)

    def test_area_12_2_values(self):
        res = rectangle.area(12, 2)
        self.assertEqual(24, res)

    def test_area_12_3_values(self):
        res = rectangle.area(12, 3)
        self.assertEqual(36, res)

    def test_area_12_4_values(self):
        res = rectangle.area(12, 4)
        self.assertEqual(48, res)

    def test_area_12_5_values(self):
        res = rectangle.area(12, 5)
        self.assertEqual(60, res)

    def test_area_12_6_values(self):
        res = rectangle.area(12, 6)
        self.assertEqual(72, res)

    def test_area_12_7_values(self):
        res = rectangle.area(12, 7)
        self.assertEqual(84, res)

    def test_area_12_8_values(self):
        res = rectangle.area(12, 8)
        self.assertEqual(96, res)

    def test_area_12_9_values(self):
        res = rectangle.area(12, 9)
        self.assertEqual(108, res)

    def test_area_12_10_values(self):
        res = rectangle.area(12, 10)
        self.assertEqual(120, res)

    def test_area_12_11_values(self):
        res = rectangle.area(12, 11)
        self.assertEqual(132, res)

    def test_area_12_12_values(self):
        res = rectangle.area(12, 12)
        self.assertEqual(144, res)

    def test_area_12_13_values(self):
        res = rectangle.area(12, 13)
        self.assertEqual(156, res)

    def test_area_12_14_values(self):
        res = rectangle.area(12, 14)
        self.assertEqual(168, res)

    def test_area_12_15_values(self):
        res = rectangle.area(12, 15)
        self.assertEqual(180, res)

    def test_area_12_16_values(self):
        res = rectangle.area(12, 16)
        self.assertEqual(192, res)

    def test_area_12_17_values(self):
        res = rectangle.area(12, 17)
        self.assertEqual(204, res)

    def test_area_12_18_values(self):
        res = rectangle.area(12, 18)
        self.assertEqual(216, res)

    def test_area_12_19_values(self):
        res = rectangle.area(12, 19)
        self.assertEqual(228, res)

    def test_area_12_20_values(self):
        res = rectangle.area(12, 20)
        self.assertEqual(240, res)

    def test_area_12_21_values(self):
        res = rectangle.area(12, 21)
        self.assertEqual(252, res)

    def test_area_12_22_values(self):
        res = rectangle.area(12, 22)
        self.assertEqual(264, res)

    def test_area_12_23_values(self):
        res = rectangle.area(12, 23)
        self.assertEqual(276, res)

    def test_area_12_24_values(self):
        res = rectangle.area(12, 24)
        self.assertEqual(288, res)

    def test_area_12_25_values(self):
        res = rectangle.area(12, 25)
        self.assertEqual(300, res)

    def test_area_12_26_values(self):
        res = rectangle.area(12, 26)
        self.assertEqual(312, res)

    def test_area_12_27_values(self):
        res = rectangle.area(12, 27)
        self.assertEqual(324, res)

    def test_area_12_28_values(self):
        res = rectangle.area(12, 28)
        self.assertEqual(336, res)

    def test_area_12_29_values(self):
        res = rectangle.area(12, 29)
        self.assertEqual(348, res)

    def test_area_13_1_values(self):
        res = rectangle.area(13, 1)
        self.assertEqual(13, res)

    def test_area_13_2_values(self):
        res = rectangle.area(13, 2)
        self.assertEqual(26, res)

    def test_area_13_3_values(self):
        res = rectangle.area(13, 3)
        self.assertEqual(39, res)

    def test_area_13_4_values(self):
        res = rectangle.area(13, 4)
        self.assertEqual(52, res)

    def test_area_13_5_values(self):
        res = rectangle.area(13, 5)
        self.assertEqual(65, res)

    def test_area_13_6_values(self):
        res = rectangle.area(13, 6)
        self.assertEqual(78, res)

    def test_area_13_7_values(self):
        res = rectangle.area(13, 7)
        self.assertEqual(91, res)

    def test_area_13_8_values(self):
        res = rectangle.area(13, 8)
        self.assertEqual(104, res)

    def test_area_13_9_values(self):
        res = rectangle.area(13, 9)
        self.assertEqual(117, res)

    def test_area_13_10_values(self):
        res = rectangle.area(13, 10)
        self.assertEqual(130, res)

    def test_area_13_11_values(self):
        res = rectangle.area(13, 11)
        self.assertEqual(143, res)

    def test_area_13_12_values(self):
        res = rectangle.area(13, 12)
        self.assertEqual(156, res)

    def test_area_13_13_values(self):
        res = rectangle.area(13, 13)
        self.assertEqual(169, res)

    def test_area_13_14_values(self):
        res = rectangle.area(13, 14)
        self.assertEqual(182, res)

    def test_area_13_15_values(self):
        res = rectangle.area(13, 15)
        self.assertEqual(195, res)

    def test_area_13_16_values(self):
        res = rectangle.area(13, 16)
        self.assertEqual(208, res)

    def test_area_13_17_values(self):
        res = rectangle.area(13, 17)
        self.assertEqual(221, res)

    def test_area_13_18_values(self):
        res = rectangle.area(13, 18)
        self.assertEqual(234, res)

    def test_area_13_19_values(self):
        res = rectangle.area(13, 19)
        self.assertEqual(247, res)

    def test_area_13_20_values(self):
        res = rectangle.area(13, 20)
        self.assertEqual(260, res)

    def test_area_13_21_values(self):
        res = rectangle.area(13, 21)
        self.assertEqual(273, res)

    def test_area_13_22_values(self):
        res = rectangle.area(13, 22)
        self.assertEqual(286, res)

    def test_area_13_23_values(self):
        res = rectangle.area(13, 23)
        self.assertEqual(299, res)

    def test_area_13_24_values(self):
        res = rectangle.area(13, 24)
        self.assertEqual(312, res)

    def test_area_13_25_values(self):
        res = rectangle.area(13, 25)
        self.assertEqual(325, res)

    def test_area_13_26_values(self):
        res = rectangle.area(13, 26)
        self.assertEqual(338, res)

    def test_area_13_27_values(self):
        res = rectangle.area(13, 27)
        self.assertEqual(351, res)

    def test_area_13_28_values(self):
        res = rectangle.area(13, 28)
        self.assertEqual(364, res)

    def test_area_13_29_values(self):
        res = rectangle.area(13, 29)
        self.assertEqual(377, res)

    def test_area_14_1_values(self):
        res = rectangle.area(14, 1)
        self.assertEqual(14, res)

    def test_area_14_2_values(self):
        res = rectangle.area(14, 2)
        self.assertEqual(28, res)

    def test_area_14_3_values(self):
        res = rectangle.area(14, 3)
        self.assertEqual(42, res)

    def test_area_14_4_values(self):
        res = rectangle.area(14, 4)
        self.assertEqual(56, res)

    def test_area_14_5_values(self):
        res = rectangle.area(14, 5)
        self.assertEqual(70, res)

    def test_area_14_6_values(self):
        res = rectangle.area(14, 6)
        self.assertEqual(84, res)

    def test_area_14_7_values(self):
        res = rectangle.area(14, 7)
        self.assertEqual(98, res)

    def test_area_14_8_values(self):
        res = rectangle.area(14, 8)
        self.assertEqual(112, res)

    def test_area_14_9_values(self):
        res = rectangle.area(14, 9)
        self.assertEqual(126, res)

    def test_area_14_10_values(self):
        res = rectangle.area(14, 10)
        self.assertEqual(140, res)

    def test_area_14_11_values(self):
        res = rectangle.area(14, 11)
        self.assertEqual(154, res)

    def test_area_14_12_values(self):
        res = rectangle.area(14, 12)
        self.assertEqual(168, res)

    def test_area_14_13_values(self):
        res = rectangle.area(14, 13)
        self.assertEqual(182, res)

    def test_area_14_14_values(self):
        res = rectangle.area(14, 14)
        self.assertEqual(196, res)

    def test_area_14_15_values(self):
        res = rectangle.area(14, 15)
        self.assertEqual(210, res)

    def test_area_14_16_values(self):
        res = rectangle.area(14, 16)
        self.assertEqual(224, res)

    def test_area_14_17_values(self):
        res = rectangle.area(14, 17)
        self.assertEqual(238, res)

    def test_area_14_18_values(self):
        res = rectangle.area(14, 18)
        self.assertEqual(252, res)

    def test_area_14_19_values(self):
        res = rectangle.area(14, 19)
        self.assertEqual(266, res)

    def test_area_14_20_values(self):
        res = rectangle.area(14, 20)
        self.assertEqual(280, res)

    def test_area_14_21_values(self):
        res = rectangle.area(14, 21)
        self.assertEqual(294, res)

    def test_area_14_22_values(self):
        res = rectangle.area(14, 22)
        self.assertEqual(308, res)

    def test_area_14_23_values(self):
        res = rectangle.area(14, 23)
        self.assertEqual(322, res)

    def test_area_14_24_values(self):
        res = rectangle.area(14, 24)
        self.assertEqual(336, res)

    def test_area_14_25_values(self):
        res = rectangle.area(14, 25)
        self.assertEqual(350, res)

    def test_area_14_26_values(self):
        res = rectangle.area(14, 26)
        self.assertEqual(364, res)

    def test_area_14_27_values(self):
        res = rectangle.area(14, 27)
        self.assertEqual(378, res)

    def test_area_14_28_values(self):
        res = rectangle.area(14, 28)
        self.assertEqual(392, res)

    def test_area_14_29_values(self):
        res = rectangle.area(14, 29)
        self.assertEqual(406, res)

    def test_area_15_1_values(self):
        res = rectangle.area(15, 1)
        self.assertEqual(15, res)

    def test_area_15_2_values(self):
        res = rectangle.area(15, 2)
        self.assertEqual(30, res)

    def test_area_15_3_values(self):
        res = rectangle.area(15, 3)
        self.assertEqual(45, res)

    def test_area_15_4_values(self):
        res = rectangle.area(15, 4)
        self.assertEqual(60, res)

    def test_area_15_5_values(self):
        res = rectangle.area(15, 5)
        self.assertEqual(75, res)

    def test_area_15_6_values(self):
        res = rectangle.area(15, 6)
        self.assertEqual(90, res)

    def test_area_15_7_values(self):
        res = rectangle.area(15, 7)
        self.assertEqual(105, res)

    def test_area_15_8_values(self):
        res = rectangle.area(15, 8)
        self.assertEqual(120, res)

    def test_area_15_9_values(self):
        res = rectangle.area(15, 9)
        self.assertEqual(135, res)

    def test_area_15_10_values(self):
        res = rectangle.area(15, 10)
        self.assertEqual(150, res)

    def test_area_15_11_values(self):
        res = rectangle.area(15, 11)
        self.assertEqual(165, res)

    def test_area_15_12_values(self):
        res = rectangle.area(15, 12)
        self.assertEqual(180, res)

    def test_area_15_13_values(self):
        res = rectangle.area(15, 13)
        self.assertEqual(195, res)

    def test_area_15_14_values(self):
        res = rectangle.area(15, 14)
        self.assertEqual(210, res)

    def test_area_15_15_values(self):
        res = rectangle.area(15, 15)
        self.assertEqual(225, res)

    def test_area_15_16_values(self):
        res = rectangle.area(15, 16)
        self.assertEqual(240, res)

    def test_area_15_17_values(self):
        res = rectangle.area(15, 17)
        self.assertEqual(255, res)

    def test_area_15_18_values(self):
        res = rectangle.area(15, 18)
        self.assertEqual(270, res)

    def test_area_15_19_values(self):
        res = rectangle.area(15, 19)
        self.assertEqual(285, res)

    def test_area_15_20_values(self):
        res = rectangle.area(15, 20)
        self.assertEqual(300, res)

    def test_area_15_21_values(self):
        res = rectangle.area(15, 21)
        self.assertEqual(315, res)

    def test_area_15_22_values(self):
        res = rectangle.area(15, 22)
        self.assertEqual(330, res)

    def test_area_15_23_values(self):
        res = rectangle.area(15, 23)
        self.assertEqual(345, res)

    def test_area_15_24_values(self):
        res = rectangle.area(15, 24)
        self.assertEqual(360, res)

    def test_area_15_25_values(self):
        res = rectangle.area(15, 25)
        self.assertEqual(375, res)

    def test_area_15_26_values(self):
        res = rectangle.area(15, 26)
        self.assertEqual(390, res)

    def test_area_15_27_values(self):
        res = rectangle.area(15, 27)
        self.assertEqual(405, res)

    def test_area_15_28_values(self):
        res = rectangle.area(15, 28)
        self.assertEqual(420, res)

    def test_area_15_29_values(self):
        res = rectangle.area(15, 29)
        self.assertEqual(435, res)

    def test_area_16_1_values(self):
        res = rectangle.area(16, 1)
        self.assertEqual(16, res)

    def test_area_16_2_values(self):
        res = rectangle.area(16, 2)
        self.assertEqual(32, res)

    def test_area_16_3_values(self):
        res = rectangle.area(16, 3)
        self.assertEqual(48, res)

    def test_area_16_4_values(self):
        res = rectangle.area(16, 4)
        self.assertEqual(64, res)

    def test_area_16_5_values(self):
        res = rectangle.area(16, 5)
        self.assertEqual(80, res)

    def test_area_16_6_values(self):
        res = rectangle.area(16, 6)
        self.assertEqual(96, res)

    def test_area_16_7_values(self):
        res = rectangle.area(16, 7)
        self.assertEqual(112, res)

    def test_area_16_8_values(self):
        res = rectangle.area(16, 8)
        self.assertEqual(128, res)

    def test_area_16_9_values(self):
        res = rectangle.area(16, 9)
        self.assertEqual(144, res)

    def test_area_16_10_values(self):
        res = rectangle.area(16, 10)
        self.assertEqual(160, res)

    def test_area_16_11_values(self):
        res = rectangle.area(16, 11)
        self.assertEqual(176, res)

    def test_area_16_12_values(self):
        res = rectangle.area(16, 12)
        self.assertEqual(192, res)

    def test_area_16_13_values(self):
        res = rectangle.area(16, 13)
        self.assertEqual(208, res)

    def test_area_16_14_values(self):
        res = rectangle.area(16, 14)
        self.assertEqual(224, res)

    def test_area_16_15_values(self):
        res = rectangle.area(16, 15)
        self.assertEqual(240, res)

    def test_area_16_16_values(self):
        res = rectangle.area(16, 16)
        self.assertEqual(256, res)

    def test_area_16_17_values(self):
        res = rectangle.area(16, 17)
        self.assertEqual(272, res)

    def test_area_16_18_values(self):
        res = rectangle.area(16, 18)
        self.assertEqual(288, res)

    def test_area_16_19_values(self):
        res = rectangle.area(16, 19)
        self.assertEqual(304, res)

    def test_area_16_20_values(self):
        res = rectangle.area(16, 20)
        self.assertEqual(320, res)

    def test_area_16_21_values(self):
        res = rectangle.area(16, 21)
        self.assertEqual(336, res)

    def test_area_16_22_values(self):
        res = rectangle.area(16, 22)
        self.assertEqual(352, res)

    def test_area_16_23_values(self):
        res = rectangle.area(16, 23)
        self.assertEqual(368, res)

    def test_area_16_24_values(self):
        res = rectangle.area(16, 24)
        self.assertEqual(384, res)

    def test_area_16_25_values(self):
        res = rectangle.area(16, 25)
        self.assertEqual(400, res)

    def test_area_16_26_values(self):
        res = rectangle.area(16, 26)
        self.assertEqual(416, res)

    def test_area_16_27_values(self):
        res = rectangle.area(16, 27)
        self.assertEqual(432, res)

    def test_area_16_28_values(self):
        res = rectangle.area(16, 28)
        self.assertEqual(448, res)

    def test_area_16_29_values(self):
        res = rectangle.area(16, 29)
        self.assertEqual(464, res)

    def test_area_17_1_values(self):
        res = rectangle.area(17, 1)
        self.assertEqual(17, res)

    def test_area_17_2_values(self):
        res = rectangle.area(17, 2)
        self.assertEqual(34, res)

    def test_area_17_3_values(self):
        res = rectangle.area(17, 3)
        self.assertEqual(51, res)

    def test_area_17_4_values(self):
        res = rectangle.area(17, 4)
        self.assertEqual(68, res)

    def test_area_17_5_values(self):
        res = rectangle.area(17, 5)
        self.assertEqual(85, res)

    def test_area_17_6_values(self):
        res = rectangle.area(17, 6)
        self.assertEqual(102, res)

    def test_area_17_7_values(self):
        res = rectangle.area(17, 7)
        self.assertEqual(119, res)

    def test_area_17_8_values(self):
        res = rectangle.area(17, 8)
        self.assertEqual(136, res)

    def test_area_17_9_values(self):
        res = rectangle.area(17, 9)
        self.assertEqual(153, res)

    def test_area_17_10_values(self):
        res = rectangle.area(17, 10)
        self.assertEqual(170, res)

    def test_area_17_11_values(self):
        res = rectangle.area(17, 11)
        self.assertEqual(187, res)

    def test_area_17_12_values(self):
        res = rectangle.area(17, 12)
        self.assertEqual(204, res)

    def test_area_17_13_values(self):
        res = rectangle.area(17, 13)
        self.assertEqual(221, res)

    def test_area_17_14_values(self):
        res = rectangle.area(17, 14)
        self.assertEqual(238, res)

    def test_area_17_15_values(self):
        res = rectangle.area(17, 15)
        self.assertEqual(255, res)

    def test_area_17_16_values(self):
        res = rectangle.area(17, 16)
        self.assertEqual(272, res)

    def test_area_17_17_values(self):
        res = rectangle.area(17, 17)
        self.assertEqual(289, res)

    def test_area_17_18_values(self):
        res = rectangle.area(17, 18)
        self.assertEqual(306, res)

    def test_area_17_19_values(self):
        res = rectangle.area(17, 19)
        self.assertEqual(323, res)

    def test_area_17_20_values(self):
        res = rectangle.area(17, 20)
        self.assertEqual(340, res)

    def test_area_17_21_values(self):
        res = rectangle.area(17, 21)
        self.assertEqual(357, res)

    def test_area_17_22_values(self):
        res = rectangle.area(17, 22)
        self.assertEqual(374, res)

    def test_area_17_23_values(self):
        res = rectangle.area(17, 23)
        self.assertEqual(391, res)

    def test_area_17_24_values(self):
        res = rectangle.area(17, 24)
        self.assertEqual(408, res)

    def test_area_17_25_values(self):
        res = rectangle.area(17, 25)
        self.assertEqual(425, res)

    def test_area_17_26_values(self):
        res = rectangle.area(17, 26)
        self.assertEqual(442, res)

    def test_area_17_27_values(self):
        res = rectangle.area(17, 27)
        self.assertEqual(459, res)

    def test_area_17_28_values(self):
        res = rectangle.area(17, 28)
        self.assertEqual(476, res)

    def test_area_17_29_values(self):
        res = rectangle.area(17, 29)
        self.assertEqual(493, res)

    def test_area_18_1_values(self):
        res = rectangle.area(18, 1)
        self.assertEqual(18, res)

    def test_area_18_2_values(self):
        res = rectangle.area(18, 2)
        self.assertEqual(36, res)

    def test_area_18_3_values(self):
        res = rectangle.area(18, 3)
        self.assertEqual(54, res)

    def test_area_18_4_values(self):
        res = rectangle.area(18, 4)
        self.assertEqual(72, res)

    def test_area_18_5_values(self):
        res = rectangle.area(18, 5)
        self.assertEqual(90, res)

    def test_area_18_6_values(self):
        res = rectangle.area(18, 6)
        self.assertEqual(108, res)

    def test_area_18_7_values(self):
        res = rectangle.area(18, 7)
        self.assertEqual(126, res)

    def test_area_18_8_values(self):
        res = rectangle.area(18, 8)
        self.assertEqual(144, res)

    def test_area_18_9_values(self):
        res = rectangle.area(18, 9)
        self.assertEqual(162, res)

    def test_area_18_10_values(self):
        res = rectangle.area(18, 10)
        self.assertEqual(180, res)

    def test_area_18_11_values(self):
        res = rectangle.area(18, 11)
        self.assertEqual(198, res)

    def test_area_18_12_values(self):
        res = rectangle.area(18, 12)
        self.assertEqual(216, res)

    def test_area_18_13_values(self):
        res = rectangle.area(18, 13)
        self.assertEqual(234, res)

    def test_area_18_14_values(self):
        res = rectangle.area(18, 14)
        self.assertEqual(252, res)

    def test_area_18_15_values(self):
        res = rectangle.area(18, 15)
        self.assertEqual(270, res)

    def test_area_18_16_values(self):
        res = rectangle.area(18, 16)
        self.assertEqual(288, res)

    def test_area_18_17_values(self):
        res = rectangle.area(18, 17)
        self.assertEqual(306, res)

    def test_area_18_18_values(self):
        res = rectangle.area(18, 18)
        self.assertEqual(324, res)

    def test_area_18_19_values(self):
        res = rectangle.area(18, 19)
        self.assertEqual(342, res)

    def test_area_18_20_values(self):
        res = rectangle.area(18, 20)
        self.assertEqual(360, res)

    def test_area_18_21_values(self):
        res = rectangle.area(18, 21)
        self.assertEqual(378, res)

    def test_area_18_22_values(self):
        res = rectangle.area(18, 22)
        self.assertEqual(396, res)

    def test_area_18_23_values(self):
        res = rectangle.area(18, 23)
        self.assertEqual(414, res)

    def test_area_18_24_values(self):
        res = rectangle.area(18, 24)
        self.assertEqual(432, res)

    def test_area_18_25_values(self):
        res = rectangle.area(18, 25)
        self.assertEqual(450, res)

    def test_area_18_26_values(self):
        res = rectangle.area(18, 26)
        self.assertEqual(468, res)

    def test_area_18_27_values(self):
        res = rectangle.area(18, 27)
        self.assertEqual(486, res)

    def test_area_18_28_values(self):
        res = rectangle.area(18, 28)
        self.assertEqual(504, res)

    def test_area_18_29_values(self):
        res = rectangle.area(18, 29)
        self.assertEqual(522, res)

    def test_area_19_1_values(self):
        res = rectangle.area(19, 1)
        self.assertEqual(19, res)

    def test_area_19_2_values(self):
        res = rectangle.area(19, 2)
        self.assertEqual(38, res)

    def test_area_19_3_values(self):
        res = rectangle.area(19, 3)
        self.assertEqual(57, res)

    def test_area_19_4_values(self):
        res = rectangle.area(19, 4)
        self.assertEqual(76, res)

    def test_area_19_5_values(self):
        res = rectangle.area(19, 5)
        self.assertEqual(95, res)

    def test_area_19_6_values(self):
        res = rectangle.area(19, 6)
        self.assertEqual(114, res)

    def test_area_19_7_values(self):
        res = rectangle.area(19, 7)
        self.assertEqual(133, res)

    def test_area_19_8_values(self):
        res = rectangle.area(19, 8)
        self.assertEqual(152, res)

    def test_area_19_9_values(self):
        res = rectangle.area(19, 9)
        self.assertEqual(171, res)

    def test_area_19_10_values(self):
        res = rectangle.area(19, 10)
        self.assertEqual(190, res)

    def test_area_19_11_values(self):
        res = rectangle.area(19, 11)
        self.assertEqual(209, res)

    def test_area_19_12_values(self):
        res = rectangle.area(19, 12)
        self.assertEqual(228, res)

    def test_area_19_13_values(self):
        res = rectangle.area(19, 13)
        self.assertEqual(247, res)

    def test_area_19_14_values(self):
        res = rectangle.area(19, 14)
        self.assertEqual(266, res)

    def test_area_19_15_values(self):
        res = rectangle.area(19, 15)
        self.assertEqual(285, res)

    def test_area_19_16_values(self):
        res = rectangle.area(19, 16)
        self.assertEqual(304, res)

    def test_area_19_17_values(self):
        res = rectangle.area(19, 17)
        self.assertEqual(323, res)

    def test_area_19_18_values(self):
        res = rectangle.area(19, 18)
        self.assertEqual(342, res)

    def test_area_19_19_values(self):
        res = rectangle.area(19, 19)
        self.assertEqual(361, res)

    def test_area_19_20_values(self):
        res = rectangle.area(19, 20)
        self.assertEqual(380, res)

    def test_area_19_21_values(self):
        res = rectangle.area(19, 21)
        self.assertEqual(399, res)

    def test_area_19_22_values(self):
        res = rectangle.area(19, 22)
        self.assertEqual(418, res)

    def test_area_19_23_values(self):
        res = rectangle.area(19, 23)
        self.assertEqual(437, res)

    def test_area_19_24_values(self):
        res = rectangle.area(19, 24)
        self.assertEqual(456, res)

    def test_area_19_25_values(self):
        res = rectangle.area(19, 25)
        self.assertEqual(475, res)

    def test_area_19_26_values(self):
        res = rectangle.area(19, 26)
        self.assertEqual(494, res)

    def test_area_19_27_values(self):
        res = rectangle.area(19, 27)
        self.assertEqual(513, res)

    def test_area_19_28_values(self):
        res = rectangle.area(19, 28)
        self.assertEqual(532, res)

    def test_area_19_29_values(self):
        res = rectangle.area(19, 29)
        self.assertEqual(551, res)

    def test_area_20_1_values(self):
        res = rectangle.area(20, 1)
        self.assertEqual(20, res)

    def test_area_20_2_values(self):
        res = rectangle.area(20, 2)
        self.assertEqual(40, res)

    def test_area_20_3_values(self):
        res = rectangle.area(20, 3)
        self.assertEqual(60, res)

    def test_area_20_4_values(self):
        res = rectangle.area(20, 4)
        self.assertEqual(80, res)

    def test_area_20_5_values(self):
        res = rectangle.area(20, 5)
        self.assertEqual(100, res)

    def test_area_20_6_values(self):
        res = rectangle.area(20, 6)
        self.assertEqual(120, res)

    def test_area_20_7_values(self):
        res = rectangle.area(20, 7)
        self.assertEqual(140, res)

    def test_area_20_8_values(self):
        res = rectangle.area(20, 8)
        self.assertEqual(160, res)

    def test_area_20_9_values(self):
        res = rectangle.area(20, 9)
        self.assertEqual(180, res)

    def test_area_20_10_values(self):
        res = rectangle.area(20, 10)
        self.assertEqual(200, res)

    def test_area_20_11_values(self):
        res = rectangle.area(20, 11)
        self.assertEqual(220, res)

    def test_area_20_12_values(self):
        res = rectangle.area(20, 12)
        self.assertEqual(240, res)

    def test_area_20_13_values(self):
        res = rectangle.area(20, 13)
        self.assertEqual(260, res)

    def test_area_20_14_values(self):
        res = rectangle.area(20, 14)
        self.assertEqual(280, res)

    def test_area_20_15_values(self):
        res = rectangle.area(20, 15)
        self.assertEqual(300, res)

    def test_area_20_16_values(self):
        res = rectangle.area(20, 16)
        self.assertEqual(320, res)

    def test_area_20_17_values(self):
        res = rectangle.area(20, 17)
        self.assertEqual(340, res)

    def test_area_20_18_values(self):
        res = rectangle.area(20, 18)
        self.assertEqual(360, res)

    def test_area_20_19_values(self):
        res = rectangle.area(20, 19)
        self.assertEqual(380, res)

    def test_area_20_20_values(self):
        res = rectangle.area(20, 20)
        self.assertEqual(400, res)

    def test_area_20_21_values(self):
        res = rectangle.area(20, 21)
        self.assertEqual(420, res)

    def test_area_20_22_values(self):
        res = rectangle.area(20, 22)
        self.assertEqual(440, res)

    def test_area_20_23_values(self):
        res = rectangle.area(20, 23)
        self.assertEqual(460, res)

    def test_area_20_24_values(self):
        res = rectangle.area(20, 24)
        self.assertEqual(480, res)

    def test_area_20_25_values(self):
        res = rectangle.area(20, 25)
        self.assertEqual(500, res)

    def test_area_20_26_values(self):
        res = rectangle.area(20, 26)
        self.assertEqual(520, res)

    def test_area_20_27_values(self):
        res = rectangle.area(20, 27)
        self.assertEqual(540, res)

    def test_area_20_28_values(self):
        res = rectangle.area(20, 28)
        self.assertEqual(560, res)

    def test_area_20_29_values(self):
        res = rectangle.area(20, 29)
        self.assertEqual(580, res)

    def test_area_21_1_values(self):
        res = rectangle.area(21, 1)
        self.assertEqual(21, res)

    def test_area_21_2_values(self):
        res = rectangle.area(21, 2)
        self.assertEqual(42, res)

    def test_area_21_3_values(self):
        res = rectangle.area(21, 3)
        self.assertEqual(63, res)

    def test_area_21_4_values(self):
        res = rectangle.area(21, 4)
        self.assertEqual(84, res)

    def test_area_21_5_values(self):
        res = rectangle.area(21, 5)
        self.assertEqual(105, res)

    def test_area_21_6_values(self):
        res = rectangle.area(21, 6)
        self.assertEqual(126, res)

    def test_area_21_7_values(self):
        res = rectangle.area(21, 7)
        self.assertEqual(147, res)

    def test_area_21_8_values(self):
        res = rectangle.area(21, 8)
        self.assertEqual(168, res)

    def test_area_21_9_values(self):
        res = rectangle.area(21, 9)
        self.assertEqual(189, res)

    def test_area_21_10_values(self):
        res = rectangle.area(21, 10)
        self.assertEqual(210, res)

    def test_area_21_11_values(self):
        res = rectangle.area(21, 11)
        self.assertEqual(231, res)

    def test_area_21_12_values(self):
        res = rectangle.area(21, 12)
        self.assertEqual(252, res)

    def test_area_21_13_values(self):
        res = rectangle.area(21, 13)
        self.assertEqual(273, res)

    def test_area_21_14_values(self):
        res = rectangle.area(21, 14)
        self.assertEqual(294, res)

    def test_area_21_15_values(self):
        res = rectangle.area(21, 15)
        self.assertEqual(315, res)

    def test_area_21_16_values(self):
        res = rectangle.area(21, 16)
        self.assertEqual(336, res)

    def test_area_21_17_values(self):
        res = rectangle.area(21, 17)
        self.assertEqual(357, res)

    def test_area_21_18_values(self):
        res = rectangle.area(21, 18)
        self.assertEqual(378, res)

    def test_area_21_19_values(self):
        res = rectangle.area(21, 19)
        self.assertEqual(399, res)

    def test_area_21_20_values(self):
        res = rectangle.area(21, 20)
        self.assertEqual(420, res)

    def test_area_21_21_values(self):
        res = rectangle.area(21, 21)
        self.assertEqual(441, res)

    def test_area_21_22_values(self):
        res = rectangle.area(21, 22)
        self.assertEqual(462, res)

    def test_area_21_23_values(self):
        res = rectangle.area(21, 23)
        self.assertEqual(483, res)

    def test_area_21_24_values(self):
        res = rectangle.area(21, 24)
        self.assertEqual(504, res)

    def test_area_21_25_values(self):
        res = rectangle.area(21, 25)
        self.assertEqual(525, res)

    def test_area_21_26_values(self):
        res = rectangle.area(21, 26)
        self.assertEqual(546, res)

    def test_area_21_27_values(self):
        res = rectangle.area(21, 27)
        self.assertEqual(567, res)

    def test_area_21_28_values(self):
        res = rectangle.area(21, 28)
        self.assertEqual(588, res)

    def test_area_21_29_values(self):
        res = rectangle.area(21, 29)
        self.assertEqual(609, res)

    def test_area_22_1_values(self):
        res = rectangle.area(22, 1)
        self.assertEqual(22, res)

    def test_area_22_2_values(self):
        res = rectangle.area(22, 2)
        self.assertEqual(44, res)

    def test_area_22_3_values(self):
        res = rectangle.area(22, 3)
        self.assertEqual(66, res)

    def test_area_22_4_values(self):
        res = rectangle.area(22, 4)
        self.assertEqual(88, res)

    def test_area_22_5_values(self):
        res = rectangle.area(22, 5)
        self.assertEqual(110, res)

    def test_area_22_6_values(self):
        res = rectangle.area(22, 6)
        self.assertEqual(132, res)

    def test_area_22_7_values(self):
        res = rectangle.area(22, 7)
        self.assertEqual(154, res)

    def test_area_22_8_values(self):
        res = rectangle.area(22, 8)
        self.assertEqual(176, res)

    def test_area_22_9_values(self):
        res = rectangle.area(22, 9)
        self.assertEqual(198, res)

    def test_area_22_10_values(self):
        res = rectangle.area(22, 10)
        self.assertEqual(220, res)

    def test_area_22_11_values(self):
        res = rectangle.area(22, 11)
        self.assertEqual(242, res)

    def test_area_22_12_values(self):
        res = rectangle.area(22, 12)
        self.assertEqual(264, res)

    def test_area_22_13_values(self):
        res = rectangle.area(22, 13)
        self.assertEqual(286, res)

    def test_area_22_14_values(self):
        res = rectangle.area(22, 14)
        self.assertEqual(308, res)

    def test_area_22_15_values(self):
        res = rectangle.area(22, 15)
        self.assertEqual(330, res)

    def test_area_22_16_values(self):
        res = rectangle.area(22, 16)
        self.assertEqual(352, res)

    def test_area_22_17_values(self):
        res = rectangle.area(22, 17)
        self.assertEqual(374, res)

    def test_area_22_18_values(self):
        res = rectangle.area(22, 18)
        self.assertEqual(396, res)

    def test_area_22_19_values(self):
        res = rectangle.area(22, 19)
        self.assertEqual(418, res)

    def test_area_22_20_values(self):
        res = rectangle.area(22, 20)
        self.assertEqual(440, res)

    def test_area_22_21_values(self):
        res = rectangle.area(22, 21)
        self.assertEqual(462, res)

    def test_area_22_22_values(self):
        res = rectangle.area(22, 22)
        self.assertEqual(484, res)

    def test_area_22_23_values(self):
        res = rectangle.area(22, 23)
        self.assertEqual(506, res)

    def test_area_22_24_values(self):
        res = rectangle.area(22, 24)
        self.assertEqual(528, res)

    def test_area_22_25_values(self):
        res = rectangle.area(22, 25)
        self.assertEqual(550, res)

    def test_area_22_26_values(self):
        res = rectangle.area(22, 26)
        self.assertEqual(572, res)

    def test_area_22_27_values(self):
        res = rectangle.area(22, 27)
        self.assertEqual(594, res)

    def test_area_22_28_values(self):
        res = rectangle.area(22, 28)
        self.assertEqual(616, res)

    def test_area_22_29_values(self):
        res = rectangle.area(22, 29)
        self.assertEqual(638, res)

    def test_area_23_1_values(self):
        res = rectangle.area(23, 1)
        self.assertEqual(23, res)

    def test_area_23_2_values(self):
        res = rectangle.area(23, 2)
        self.assertEqual(46, res)

    def test_area_23_3_values(self):
        res = rectangle.area(23, 3)
        self.assertEqual(69, res)

    def test_area_23_4_values(self):
        res = rectangle.area(23, 4)
        self.assertEqual(92, res)

    def test_area_23_5_values(self):
        res = rectangle.area(23, 5)
        self.assertEqual(115, res)

    def test_area_23_6_values(self):
        res = rectangle.area(23, 6)
        self.assertEqual(138, res)

    def test_area_23_7_values(self):
        res = rectangle.area(23, 7)
        self.assertEqual(161, res)

    def test_area_23_8_values(self):
        res = rectangle.area(23, 8)
        self.assertEqual(184, res)

    def test_area_23_9_values(self):
        res = rectangle.area(23, 9)
        self.assertEqual(207, res)

    def test_area_23_10_values(self):
        res = rectangle.area(23, 10)
        self.assertEqual(230, res)

    def test_area_23_11_values(self):
        res = rectangle.area(23, 11)
        self.assertEqual(253, res)

    def test_area_23_12_values(self):
        res = rectangle.area(23, 12)
        self.assertEqual(276, res)

    def test_area_23_13_values(self):
        res = rectangle.area(23, 13)
        self.assertEqual(299, res)

    def test_area_23_14_values(self):
        res = rectangle.area(23, 14)
        self.assertEqual(322, res)

    def test_area_23_15_values(self):
        res = rectangle.area(23, 15)
        self.assertEqual(345, res)

    def test_area_23_16_values(self):
        res = rectangle.area(23, 16)
        self.assertEqual(368, res)

    def test_area_23_17_values(self):
        res = rectangle.area(23, 17)
        self.assertEqual(391, res)

    def test_area_23_18_values(self):
        res = rectangle.area(23, 18)
        self.assertEqual(414, res)

    def test_area_23_19_values(self):
        res = rectangle.area(23, 19)
        self.assertEqual(437, res)

    def test_area_23_20_values(self):
        res = rectangle.area(23, 20)
        self.assertEqual(460, res)

    def test_area_23_21_values(self):
        res = rectangle.area(23, 21)
        self.assertEqual(483, res)

    def test_area_23_22_values(self):
        res = rectangle.area(23, 22)
        self.assertEqual(506, res)

    def test_area_23_23_values(self):
        res = rectangle.area(23, 23)
        self.assertEqual(529, res)

    def test_area_23_24_values(self):
        res = rectangle.area(23, 24)
        self.assertEqual(552, res)

    def test_area_23_25_values(self):
        res = rectangle.area(23, 25)
        self.assertEqual(575, res)

    def test_area_23_26_values(self):
        res = rectangle.area(23, 26)
        self.assertEqual(598, res)

    def test_area_23_27_values(self):
        res = rectangle.area(23, 27)
        self.assertEqual(621, res)

    def test_area_23_28_values(self):
        res = rectangle.area(23, 28)
        self.assertEqual(644, res)

    def test_area_23_29_values(self):
        res = rectangle.area(23, 29)
        self.assertEqual(667, res)

    def test_area_24_1_values(self):
        res = rectangle.area(24, 1)
        self.assertEqual(24, res)

    def test_area_24_2_values(self):
        res = rectangle.area(24, 2)
        self.assertEqual(48, res)

    def test_area_24_3_values(self):
        res = rectangle.area(24, 3)
        self.assertEqual(72, res)

    def test_area_24_4_values(self):
        res = rectangle.area(24, 4)
        self.assertEqual(96, res)

    def test_area_24_5_values(self):
        res = rectangle.area(24, 5)
        self.assertEqual(120, res)

    def test_area_24_6_values(self):
        res = rectangle.area(24, 6)
        self.assertEqual(144, res)

    def test_area_24_7_values(self):
        res = rectangle.area(24, 7)
        self.assertEqual(168, res)

    def test_area_24_8_values(self):
        res = rectangle.area(24, 8)
        self.assertEqual(192, res)

    def test_area_24_9_values(self):
        res = rectangle.area(24, 9)
        self.assertEqual(216, res)

    def test_area_24_10_values(self):
        res = rectangle.area(24, 10)
        self.assertEqual(240, res)

    def test_area_24_11_values(self):
        res = rectangle.area(24, 11)
        self.assertEqual(264, res)

    def test_area_24_12_values(self):
        res = rectangle.area(24, 12)
        self.assertEqual(288, res)

    def test_area_24_13_values(self):
        res = rectangle.area(24, 13)
        self.assertEqual(312, res)

    def test_area_24_14_values(self):
        res = rectangle.area(24, 14)
        self.assertEqual(336, res)

    def test_area_24_15_values(self):
        res = rectangle.area(24, 15)
        self.assertEqual(360, res)

    def test_area_24_16_values(self):
        res = rectangle.area(24, 16)
        self.assertEqual(384, res)

    def test_area_24_17_values(self):
        res = rectangle.area(24, 17)
        self.assertEqual(408, res)

    def test_area_24_18_values(self):
        res = rectangle.area(24, 18)
        self.assertEqual(432, res)

    def test_area_24_19_values(self):
        res = rectangle.area(24, 19)
        self.assertEqual(456, res)

    def test_area_24_20_values(self):
        res = rectangle.area(24, 20)
        self.assertEqual(480, res)

    def test_area_24_21_values(self):
        res = rectangle.area(24, 21)
        self.assertEqual(504, res)

    def test_area_24_22_values(self):
        res = rectangle.area(24, 22)
        self.assertEqual(528, res)

    def test_area_24_23_values(self):
        res = rectangle.area(24, 23)
        self.assertEqual(552, res)

    def test_area_24_24_values(self):
        res = rectangle.area(24, 24)
        self.assertEqual(576, res)

    def test_area_24_25_values(self):
        res = rectangle.area(24, 25)
        self.assertEqual(600, res)

    def test_area_24_26_values(self):
        res = rectangle.area(24, 26)
        self.assertEqual(624, res)

    def test_area_24_27_values(self):
        res = rectangle.area(24, 27)
        self.assertEqual(648, res)

    def test_area_24_28_values(self):
        res = rectangle.area(24, 28)
        self.assertEqual(672, res)

    def test_area_24_29_values(self):
        res = rectangle.area(24, 29)
        self.assertEqual(696, res)

    def test_area_25_1_values(self):
        res = rectangle.area(25, 1)
        self.assertEqual(25, res)

    def test_area_25_2_values(self):
        res = rectangle.area(25, 2)
        self.assertEqual(50, res)

    def test_area_25_3_values(self):
        res = rectangle.area(25, 3)
        self.assertEqual(75, res)

    def test_area_25_4_values(self):
        res = rectangle.area(25, 4)
        self.assertEqual(100, res)

    def test_area_25_5_values(self):
        res = rectangle.area(25, 5)
        self.assertEqual(125, res)

    def test_area_25_6_values(self):
        res = rectangle.area(25, 6)
        self.assertEqual(150, res)

    def test_area_25_7_values(self):
        res = rectangle.area(25, 7)
        self.assertEqual(175, res)

    def test_area_25_8_values(self):
        res = rectangle.area(25, 8)
        self.assertEqual(200, res)

    def test_area_25_9_values(self):
        res = rectangle.area(25, 9)
        self.assertEqual(225, res)

    def test_area_25_10_values(self):
        res = rectangle.area(25, 10)
        self.assertEqual(250, res)

    def test_area_25_11_values(self):
        res = rectangle.area(25, 11)
        self.assertEqual(275, res)

    def test_area_25_12_values(self):
        res = rectangle.area(25, 12)
        self.assertEqual(300, res)

    def test_area_25_13_values(self):
        res = rectangle.area(25, 13)
        self.assertEqual(325, res)

    def test_area_25_14_values(self):
        res = rectangle.area(25, 14)
        self.assertEqual(350, res)

    def test_area_25_15_values(self):
        res = rectangle.area(25, 15)
        self.assertEqual(375, res)

    def test_area_25_16_values(self):
        res = rectangle.area(25, 16)
        self.assertEqual(400, res)

    def test_area_25_17_values(self):
        res = rectangle.area(25, 17)
        self.assertEqual(425, res)

    def test_area_25_18_values(self):
        res = rectangle.area(25, 18)
        self.assertEqual(450, res)

    def test_area_25_19_values(self):
        res = rectangle.area(25, 19)
        self.assertEqual(475, res)

    def test_area_25_20_values(self):
        res = rectangle.area(25, 20)
        self.assertEqual(500, res)

    def test_area_25_21_values(self):
        res = rectangle.area(25, 21)
        self.assertEqual(525, res)

    def test_area_25_22_values(self):
        res = rectangle.area(25, 22)
        self.assertEqual(550, res)

    def test_area_25_23_values(self):
        res = rectangle.area(25, 23)
        self.assertEqual(575, res)

    def test_area_25_24_values(self):
        res = rectangle.area(25, 24)
        self.assertEqual(600, res)

    def test_area_25_25_values(self):
        res = rectangle.area(25, 25)
        self.assertEqual(625, res)

    def test_area_25_26_values(self):
        res = rectangle.area(25, 26)
        self.assertEqual(650, res)

    def test_area_25_27_values(self):
        res = rectangle.area(25, 27)
        self.assertEqual(675, res)

    def test_area_25_28_values(self):
        res = rectangle.area(25, 28)
        self.assertEqual(700, res)

    def test_area_25_29_values(self):
        res = rectangle.area(25, 29)
        self.assertEqual(725, res)

    def test_area_26_1_values(self):
        res = rectangle.area(26, 1)
        self.assertEqual(26, res)

    def test_area_26_2_values(self):
        res = rectangle.area(26, 2)
        self.assertEqual(52, res)

    def test_area_26_3_values(self):
        res = rectangle.area(26, 3)
        self.assertEqual(78, res)

    def test_area_26_4_values(self):
        res = rectangle.area(26, 4)
        self.assertEqual(104, res)

    def test_area_26_5_values(self):
        res = rectangle.area(26, 5)
        self.assertEqual(130, res)

    def test_area_26_6_values(self):
        res = rectangle.area(26, 6)
        self.assertEqual(156, res)

    def test_area_26_7_values(self):
        res = rectangle.area(26, 7)
        self.assertEqual(182, res)

    def test_area_26_8_values(self):
        res = rectangle.area(26, 8)
        self.assertEqual(208, res)

    def test_area_26_9_values(self):
        res = rectangle.area(26, 9)
        self.assertEqual(234, res)

    def test_area_26_10_values(self):
        res = rectangle.area(26, 10)
        self.assertEqual(260, res)

    def test_area_26_11_values(self):
        res = rectangle.area(26, 11)
        self.assertEqual(286, res)

    def test_area_26_12_values(self):
        res = rectangle.area(26, 12)
        self.assertEqual(312, res)

    def test_area_26_13_values(self):
        res = rectangle.area(26, 13)
        self.assertEqual(338, res)

    def test_area_26_14_values(self):
        res = rectangle.area(26, 14)
        self.assertEqual(364, res)

    def test_area_26_15_values(self):
        res = rectangle.area(26, 15)
        self.assertEqual(390, res)

    def test_area_26_16_values(self):
        res = rectangle.area(26, 16)
        self.assertEqual(416, res)

    def test_area_26_17_values(self):
        res = rectangle.area(26, 17)
        self.assertEqual(442, res)

    def test_area_26_18_values(self):
        res = rectangle.area(26, 18)
        self.assertEqual(468, res)

    def test_area_26_19_values(self):
        res = rectangle.area(26, 19)
        self.assertEqual(494, res)

    def test_area_26_20_values(self):
        res = rectangle.area(26, 20)
        self.assertEqual(520, res)

    def test_area_26_21_values(self):
        res = rectangle.area(26, 21)
        self.assertEqual(546, res)

    def test_area_26_22_values(self):
        res = rectangle.area(26, 22)
        self.assertEqual(572, res)

    def test_area_26_23_values(self):
        res = rectangle.area(26, 23)
        self.assertEqual(598, res)

    def test_area_26_24_values(self):
        res = rectangle.area(26, 24)
        self.assertEqual(624, res)

    def test_area_26_25_values(self):
        res = rectangle.area(26, 25)
        self.assertEqual(650, res)

    def test_area_26_26_values(self):
        res = rectangle.area(26, 26)
        self.assertEqual(676, res)

    def test_area_26_27_values(self):
        res = rectangle.area(26, 27)
        self.assertEqual(702, res)

    def test_area_26_28_values(self):
        res = rectangle.area(26, 28)
        self.assertEqual(728, res)

    def test_area_26_29_values(self):
        res = rectangle.area(26, 29)
        self.assertEqual(754, res)

    def test_area_27_1_values(self):
        res = rectangle.area(27, 1)
        self.assertEqual(27, res)

    def test_area_27_2_values(self):
        res = rectangle.area(27, 2)
        self.assertEqual(54, res)

    def test_area_27_3_values(self):
        res = rectangle.area(27, 3)
        self.assertEqual(81, res)

    def test_area_27_4_values(self):
        res = rectangle.area(27, 4)
        self.assertEqual(108, res)

    def test_area_27_5_values(self):
        res = rectangle.area(27, 5)
        self.assertEqual(135, res)

    def test_area_27_6_values(self):
        res = rectangle.area(27, 6)
        self.assertEqual(162, res)

    def test_area_27_7_values(self):
        res = rectangle.area(27, 7)
        self.assertEqual(189, res)

    def test_area_27_8_values(self):
        res = rectangle.area(27, 8)
        self.assertEqual(216, res)

    def test_area_27_9_values(self):
        res = rectangle.area(27, 9)
        self.assertEqual(243, res)

    def test_area_27_10_values(self):
        res = rectangle.area(27, 10)
        self.assertEqual(270, res)

    def test_area_27_11_values(self):
        res = rectangle.area(27, 11)
        self.assertEqual(297, res)

    def test_area_27_12_values(self):
        res = rectangle.area(27, 12)
        self.assertEqual(324, res)

    def test_area_27_13_values(self):
        res = rectangle.area(27, 13)
        self.assertEqual(351, res)

    def test_area_27_14_values(self):
        res = rectangle.area(27, 14)
        self.assertEqual(378, res)

    def test_area_27_15_values(self):
        res = rectangle.area(27, 15)
        self.assertEqual(405, res)

    def test_area_27_16_values(self):
        res = rectangle.area(27, 16)
        self.assertEqual(432, res)

    def test_area_27_17_values(self):
        res = rectangle.area(27, 17)
        self.assertEqual(459, res)

    def test_area_27_18_values(self):
        res = rectangle.area(27, 18)
        self.assertEqual(486, res)

    def test_area_27_19_values(self):
        res = rectangle.area(27, 19)
        self.assertEqual(513, res)

    def test_area_27_20_values(self):
        res = rectangle.area(27, 20)
        self.assertEqual(540, res)

    def test_area_27_21_values(self):
        res = rectangle.area(27, 21)
        self.assertEqual(567, res)

    def test_area_27_22_values(self):
        res = rectangle.area(27, 22)
        self.assertEqual(594, res)

    def test_area_27_23_values(self):
        res = rectangle.area(27, 23)
        self.assertEqual(621, res)

    def test_area_27_24_values(self):
        res = rectangle.area(27, 24)
        self.assertEqual(648, res)

    def test_area_27_25_values(self):
        res = rectangle.area(27, 25)
        self.assertEqual(675, res)

    def test_area_27_26_values(self):
        res = rectangle.area(27, 26)
        self.assertEqual(702, res)

    def test_area_27_27_values(self):
        res = rectangle.area(27, 27)
        self.assertEqual(729, res)

    def test_area_27_28_values(self):
        res = rectangle.area(27, 28)
        self.assertEqual(756, res)

    def test_area_27_29_values(self):
        res = rectangle.area(27, 29)
        self.assertEqual(783, res)

    def test_area_28_1_values(self):
        res = rectangle.area(28, 1)
        self.assertEqual(28, res)

    def test_area_28_2_values(self):
        res = rectangle.area(28, 2)
        self.assertEqual(56, res)

    def test_area_28_3_values(self):
        res = rectangle.area(28, 3)
        self.assertEqual(84, res)

    def test_area_28_4_values(self):
        res = rectangle.area(28, 4)
        self.assertEqual(112, res)

    def test_area_28_5_values(self):
        res = rectangle.area(28, 5)
        self.assertEqual(140, res)

    def test_area_28_6_values(self):
        res = rectangle.area(28, 6)
        self.assertEqual(168, res)

    def test_area_28_7_values(self):
        res = rectangle.area(28, 7)
        self.assertEqual(196, res)

    def test_area_28_8_values(self):
        res = rectangle.area(28, 8)
        self.assertEqual(224, res)

    def test_area_28_9_values(self):
        res = rectangle.area(28, 9)
        self.assertEqual(252, res)

    def test_area_28_10_values(self):
        res = rectangle.area(28, 10)
        self.assertEqual(280, res)

    def test_area_28_11_values(self):
        res = rectangle.area(28, 11)
        self.assertEqual(308, res)

    def test_area_28_12_values(self):
        res = rectangle.area(28, 12)
        self.assertEqual(336, res)

    def test_area_28_13_values(self):
        res = rectangle.area(28, 13)
        self.assertEqual(364, res)

    def test_area_28_14_values(self):
        res = rectangle.area(28, 14)
        self.assertEqual(392, res)

    def test_area_28_15_values(self):
        res = rectangle.area(28, 15)
        self.assertEqual(420, res)

    def test_area_28_16_values(self):
        res = rectangle.area(28, 16)
        self.assertEqual(448, res)

    def test_area_28_17_values(self):
        res = rectangle.area(28, 17)
        self.assertEqual(476, res)

    def test_area_28_18_values(self):
        res = rectangle.area(28, 18)
        self.assertEqual(504, res)

    def test_area_28_19_values(self):
        res = rectangle.area(28, 19)
        self.assertEqual(532, res)

    def test_area_28_20_values(self):
        res = rectangle.area(28, 20)
        self.assertEqual(560, res)

    def test_area_28_21_values(self):
        res = rectangle.area(28, 21)
        self.assertEqual(588, res)

    def test_area_28_22_values(self):
        res = rectangle.area(28, 22)
        self.assertEqual(616, res)

    def test_area_28_23_values(self):
        res = rectangle.area(28, 23)
        self.assertEqual(644, res)

    def test_area_28_24_values(self):
        res = rectangle.area(28, 24)
        self.assertEqual(672, res)

    def test_area_28_25_values(self):
        res = rectangle.area(28, 25)
        self.assertEqual(700, res)

    def test_area_28_26_values(self):
        res = rectangle.area(28, 26)
        self.assertEqual(728, res)

    def test_area_28_27_values(self):
        res = rectangle.area(28, 27)
        self.assertEqual(756, res)

    def test_area_28_28_values(self):
        res = rectangle.area(28, 28)
        self.assertEqual(784, res)

    def test_area_28_29_values(self):
        res = rectangle.area(28, 29)
        self.assertEqual(812, res)

    def test_area_29_1_values(self):
        res = rectangle.area(29, 1)
        self.assertEqual(29, res)

    def test_area_29_2_values(self):
        res = rectangle.area(29, 2)
        self.assertEqual(58, res)

    def test_area_29_3_values(self):
        res = rectangle.area(29, 3)
        self.assertEqual(87, res)

    def test_area_29_4_values(self):
        res = rectangle.area(29, 4)
        self.assertEqual(116, res)

    def test_area_29_5_values(self):
        res = rectangle.area(29, 5)
        self.assertEqual(145, res)

    def test_area_29_6_values(self):
        res = rectangle.area(29, 6)
        self.assertEqual(174, res)

    def test_area_29_7_values(self):
        res = rectangle.area(29, 7)
        self.assertEqual(203, res)

    def test_area_29_8_values(self):
        res = rectangle.area(29, 8)
        self.assertEqual(232, res)

    def test_area_29_9_values(self):
        res = rectangle.area(29, 9)
        self.assertEqual(261, res)

    def test_area_29_10_values(self):
        res = rectangle.area(29, 10)
        self.assertEqual(290, res)

    def test_area_29_11_values(self):
        res = rectangle.area(29, 11)
        self.assertEqual(319, res)

    def test_area_29_12_values(self):
        res = rectangle.area(29, 12)
        self.assertEqual(348, res)

    def test_area_29_13_values(self):
        res = rectangle.area(29, 13)
        self.assertEqual(377, res)

    def test_area_29_14_values(self):
        res = rectangle.area(29, 14)
        self.assertEqual(406, res)

    def test_area_29_15_values(self):
        res = rectangle.area(29, 15)
        self.assertEqual(435, res)

    def test_area_29_16_values(self):
        res = rectangle.area(29, 16)
        self.assertEqual(464, res)

    def test_area_29_17_values(self):
        res = rectangle.area(29, 17)
        self.assertEqual(493, res)

    def test_area_29_18_values(self):
        res = rectangle.area(29, 18)
        self.assertEqual(522, res)

    def test_area_29_19_values(self):
        res = rectangle.area(29, 19)
        self.assertEqual(551, res)

    def test_area_29_20_values(self):
        res = rectangle.area(29, 20)
        self.assertEqual(580, res)

    def test_area_29_21_values(self):
        res = rectangle.area(29, 21)
        self.assertEqual(609, res)

    def test_area_29_22_values(self):
        res = rectangle.area(29, 22)
        self.assertEqual(638, res)

    def test_area_29_23_values(self):
        res = rectangle.area(29, 23)
        self.assertEqual(667, res)

    def test_area_29_24_values(self):
        res = rectangle.area(29, 24)
        self.assertEqual(696, res)

    def test_area_29_25_values(self):
        res = rectangle.area(29, 25)
        self.assertEqual(725, res)

    def test_area_29_26_values(self):
        res = rectangle.area(29, 26)
        self.assertEqual(754, res)

    def test_area_29_27_values(self):
        res = rectangle.area(29, 27)
        self.assertEqual(783, res)

    def test_area_29_28_values(self):
        res = rectangle.area(29, 28)
        self.assertEqual(812, res)

    def test_area_29_29_values(self):
        res = rectangle.area(29, 29)
        self.assertEqual(841, res)

    def test_area_30_1_values(self):
        res = rectangle.area(30, 1)
        self.assertEqual(30, res)

    def test_area_30_2_values(self):
        res = rectangle.area(30, 2)
        self.assertEqual(60, res)

    def test_area_30_3_values(self):
        res = rectangle.area(30, 3)
        self.assertEqual(90, res)

    def test_area_30_4_values(self):
        res = rectangle.area(30, 4)
        self.assertEqual(120, res)

    def test_area_30_5_values(self):
        res = rectangle.area(30, 5)
        self.assertEqual(150, res)

    def test_area_30_6_values(self):
        res = rectangle.area(30, 6)
        self.assertEqual(180, res)

    def test_area_30_7_values(self):
        res = rectangle.area(30, 7)
        self.assertEqual(210, res)

    def test_area_30_8_values(self):
        res = rectangle.area(30, 8)
        self.assertEqual(240, res)

    def test_area_30_9_values(self):
        res = rectangle.area(30, 9)
        self.assertEqual(270, res)

    def test_area_30_10_values(self):
        res = rectangle.area(30, 10)
        self.assertEqual(300, res)

    def test_area_30_11_values(self):
        res = rectangle.area(30, 11)
        self.assertEqual(330, res)

    def test_area_30_12_values(self):
        res = rectangle.area(30, 12)
        self.assertEqual(360, res)

    def test_area_30_13_values(self):
        res = rectangle.area(30, 13)
        self.assertEqual(390, res)

    def test_area_30_14_values(self):
        res = rectangle.area(30, 14)
        self.assertEqual(420, res)

    def test_area_30_15_values(self):
        res = rectangle.area(30, 15)
        self.assertEqual(450, res)

    def test_area_30_16_values(self):
        res = rectangle.area(30, 16)
        self.assertEqual(480, res)

    def test_area_30_17_values(self):
        res = rectangle.area(30, 17)
        self.assertEqual(510, res)

    def test_area_30_18_values(self):
        res = rectangle.area(30, 18)
        self.assertEqual(540, res)

    def test_area_30_19_values(self):
        res = rectangle.area(30, 19)
        self.assertEqual(570, res)

    def test_area_30_20_values(self):
        res = rectangle.area(30, 20)
        self.assertEqual(600, res)

    def test_area_30_21_values(self):
        res = rectangle.area(30, 21)
        self.assertEqual(630, res)

    def test_area_30_22_values(self):
        res = rectangle.area(30, 22)
        self.assertEqual(660, res)

    def test_area_30_23_values(self):
        res = rectangle.area(30, 23)
        self.assertEqual(690, res)

    def test_area_30_24_values(self):
        res = rectangle.area(30, 24)
        self.assertEqual(720, res)

    def test_area_30_25_values(self):
        res = rectangle.area(30, 25)
        self.assertEqual(750, res)

    def test_area_30_26_values(self):
        res = rectangle.area(30, 26)
        self.assertEqual(780, res)

    def test_area_30_27_values(self):
        res = rectangle.area(30, 27)
        self.assertEqual(810, res)

    def test_area_30_28_values(self):
        res = rectangle.area(30, 28)
        self.assertEqual(840, res)

    def test_area_30_29_values(self):
        res = rectangle.area(30, 29)
        self.assertEqual(870, res)

    def test_area_31_1_values(self):
        res = rectangle.area(31, 1)
        self.assertEqual(31, res)

    def test_area_31_2_values(self):
        res = rectangle.area(31, 2)
        self.assertEqual(62, res)

    def test_area_31_3_values(self):
        res = rectangle.area(31, 3)
        self.assertEqual(93, res)

    def test_area_31_4_values(self):
        res = rectangle.area(31, 4)
        self.assertEqual(124, res)

    def test_area_31_5_values(self):
        res = rectangle.area(31, 5)
        self.assertEqual(155, res)

    def test_area_31_6_values(self):
        res = rectangle.area(31, 6)
        self.assertEqual(186, res)

    def test_area_31_7_values(self):
        res = rectangle.area(31, 7)
        self.assertEqual(217, res)

    def test_area_31_8_values(self):
        res = rectangle.area(31, 8)
        self.assertEqual(248, res)

    def test_area_31_9_values(self):
        res = rectangle.area(31, 9)
        self.assertEqual(279, res)

    def test_area_31_10_values(self):
        res = rectangle.area(31, 10)
        self.assertEqual(310, res)

    def test_area_31_11_values(self):
        res = rectangle.area(31, 11)
        self.assertEqual(341, res)

    def test_area_31_12_values(self):
        res = rectangle.area(31, 12)
        self.assertEqual(372, res)

    def test_area_31_13_values(self):
        res = rectangle.area(31, 13)
        self.assertEqual(403, res)

    def test_area_31_14_values(self):
        res = rectangle.area(31, 14)
        self.assertEqual(434, res)

    def test_area_31_15_values(self):
        res = rectangle.area(31, 15)
        self.assertEqual(465, res)

    def test_area_31_16_values(self):
        res = rectangle.area(31, 16)
        self.assertEqual(496, res)

    def test_area_31_17_values(self):
        res = rectangle.area(31, 17)
        self.assertEqual(527, res)

    def test_area_31_18_values(self):
        res = rectangle.area(31, 18)
        self.assertEqual(558, res)

    def test_area_31_19_values(self):
        res = rectangle.area(31, 19)
        self.assertEqual(589, res)

    def test_area_31_20_values(self):
        res = rectangle.area(31, 20)
        self.assertEqual(620, res)

    def test_area_31_21_values(self):
        res = rectangle.area(31, 21)
        self.assertEqual(651, res)

    def test_area_31_22_values(self):
        res = rectangle.area(31, 22)
        self.assertEqual(682, res)

    def test_area_31_23_values(self):
        res = rectangle.area(31, 23)
        self.assertEqual(713, res)

    def test_area_31_24_values(self):
        res = rectangle.area(31, 24)
        self.assertEqual(744, res)

    def test_area_31_25_values(self):
        res = rectangle.area(31, 25)
        self.assertEqual(775, res)

    def test_area_31_26_values(self):
        res = rectangle.area(31, 26)
        self.assertEqual(806, res)

    def test_area_31_27_values(self):
        res = rectangle.area(31, 27)
        self.assertEqual(837, res)

    def test_area_31_28_values(self):
        res = rectangle.area(31, 28)
        self.assertEqual(868, res)

    def test_area_31_29_values(self):
        res = rectangle.area(31, 29)
        self.assertEqual(899, res)

    def test_area_32_1_values(self):
        res = rectangle.area(32, 1)
        self.assertEqual(32, res)

    def test_area_32_2_values(self):
        res = rectangle.area(32, 2)
        self.assertEqual(64, res)

    def test_area_32_3_values(self):
        res = rectangle.area(32, 3)
        self.assertEqual(96, res)

    def test_area_32_4_values(self):
        res = rectangle.area(32, 4)
        self.assertEqual(128, res)

    def test_area_32_5_values(self):
        res = rectangle.area(32, 5)
        self.assertEqual(160, res)

    def test_area_32_6_values(self):
        res = rectangle.area(32, 6)
        self.assertEqual(192, res)

    def test_area_32_7_values(self):
        res = rectangle.area(32, 7)
        self.assertEqual(224, res)

    def test_area_32_8_values(self):
        res = rectangle.area(32, 8)
        self.assertEqual(256, res)

    def test_area_32_9_values(self):
        res = rectangle.area(32, 9)
        self.assertEqual(288, res)

    def test_area_32_10_values(self):
        res = rectangle.area(32, 10)
        self.assertEqual(320, res)

    def test_area_32_11_values(self):
        res = rectangle.area(32, 11)
        self.assertEqual(352, res)

    def test_area_32_12_values(self):
        res = rectangle.area(32, 12)
        self.assertEqual(384, res)

    def test_area_32_13_values(self):
        res = rectangle.area(32, 13)
        self.assertEqual(416, res)

    def test_area_32_14_values(self):
        res = rectangle.area(32, 14)
        self.assertEqual(448, res)

    def test_area_32_15_values(self):
        res = rectangle.area(32, 15)
        self.assertEqual(480, res)

    def test_area_32_16_values(self):
        res = rectangle.area(32, 16)
        self.assertEqual(512, res)

    def test_area_32_17_values(self):
        res = rectangle.area(32, 17)
        self.assertEqual(544, res)

    def test_area_32_18_values(self):
        res = rectangle.area(32, 18)
        self.assertEqual(576, res)

    def test_area_32_19_values(self):
        res = rectangle.area(32, 19)
        self.assertEqual(608, res)

    def test_area_32_20_values(self):
        res = rectangle.area(32, 20)
        self.assertEqual(640, res)

    def test_area_32_21_values(self):
        res = rectangle.area(32, 21)
        self.assertEqual(672, res)

    def test_area_32_22_values(self):
        res = rectangle.area(32, 22)
        self.assertEqual(704, res)

    def test_area_32_23_values(self):
        res = rectangle.area(32, 23)
        self.assertEqual(736, res)

    def test_area_32_24_values(self):
        res = rectangle.area(32, 24)
        self.assertEqual(768, res)

    def test_area_32_25_values(self):
        res = rectangle.area(32, 25)
        self.assertEqual(800, res)

    def test_area_32_26_values(self):
        res = rectangle.area(32, 26)
        self.assertEqual(832, res)

    def test_area_32_27_values(self):
        res = rectangle.area(32, 27)
        self.assertEqual(864, res)

    def test_area_32_28_values(self):
        res = rectangle.area(32, 28)
        self.assertEqual(896, res)

    def test_area_32_29_values(self):
        res = rectangle.area(32, 29)
        self.assertEqual(928, res)

    def test_area_33_1_values(self):
        res = rectangle.area(33, 1)
        self.assertEqual(33, res)

    def test_area_33_2_values(self):
        res = rectangle.area(33, 2)
        self.assertEqual(66, res)

    def test_area_33_3_values(self):
        res = rectangle.area(33, 3)
        self.assertEqual(99, res)

    def test_area_33_4_values(self):
        res = rectangle.area(33, 4)
        self.assertEqual(132, res)

    def test_area_33_5_values(self):
        res = rectangle.area(33, 5)
        self.assertEqual(165, res)

    def test_area_33_6_values(self):
        res = rectangle.area(33, 6)
        self.assertEqual(198, res)

    def test_area_33_7_values(self):
        res = rectangle.area(33, 7)
        self.assertEqual(231, res)

    def test_area_33_8_values(self):
        res = rectangle.area(33, 8)
        self.assertEqual(264, res)

    def test_area_33_9_values(self):
        res = rectangle.area(33, 9)
        self.assertEqual(297, res)

    def test_area_33_10_values(self):
        res = rectangle.area(33, 10)
        self.assertEqual(330, res)

    def test_area_33_11_values(self):
        res = rectangle.area(33, 11)
        self.assertEqual(363, res)

    def test_area_33_12_values(self):
        res = rectangle.area(33, 12)
        self.assertEqual(396, res)

    def test_area_33_13_values(self):
        res = rectangle.area(33, 13)
        self.assertEqual(429, res)

    def test_area_33_14_values(self):
        res = rectangle.area(33, 14)
        self.assertEqual(462, res)

    def test_area_33_15_values(self):
        res = rectangle.area(33, 15)
        self.assertEqual(495, res)

    def test_area_33_16_values(self):
        res = rectangle.area(33, 16)
        self.assertEqual(528, res)

    def test_area_33_17_values(self):
        res = rectangle.area(33, 17)
        self.assertEqual(561, res)

    def test_area_33_18_values(self):
        res = rectangle.area(33, 18)
        self.assertEqual(594, res)

    def test_area_33_19_values(self):
        res = rectangle.area(33, 19)
        self.assertEqual(627, res)

    def test_area_33_20_values(self):
        res = rectangle.area(33, 20)
        self.assertEqual(660, res)

    def test_area_33_21_values(self):
        res = rectangle.area(33, 21)
        self.assertEqual(693, res)

    def test_area_33_22_values(self):
        res = rectangle.area(33, 22)
        self.assertEqual(726, res)

    def test_area_33_23_values(self):
        res = rectangle.area(33, 23)
        self.assertEqual(759, res)

    def test_area_33_24_values(self):
        res = rectangle.area(33, 24)
        self.assertEqual(792, res)

    def test_area_33_25_values(self):
        res = rectangle.area(33, 25)
        self.assertEqual(825, res)

    def test_area_33_26_values(self):
        res = rectangle.area(33, 26)
        self.assertEqual(858, res)

    def test_area_33_27_values(self):
        res = rectangle.area(33, 27)
        self.assertEqual(891, res)

    def test_area_33_28_values(self):
        res = rectangle.area(33, 28)
        self.assertEqual(924, res)

    def test_area_33_29_values(self):
        res = rectangle.area(33, 29)
        self.assertEqual(957, res)

    def test_area_34_1_values(self):
        res = rectangle.area(34, 1)
        self.assertEqual(34, res)

    def test_area_34_2_values(self):
        res = rectangle.area(34, 2)
        self.assertEqual(68, res)

    def test_area_34_3_values(self):
        res = rectangle.area(34, 3)
        self.assertEqual(102, res)

    def test_area_34_4_values(self):
        res = rectangle.area(34, 4)
        self.assertEqual(136, res)

    def test_area_34_5_values(self):
        res = rectangle.area(34, 5)
        self.assertEqual(170, res)

    def test_area_34_6_values(self):
        res = rectangle.area(34, 6)
        self.assertEqual(204, res)

    def test_area_34_7_values(self):
        res = rectangle.area(34, 7)
        self.assertEqual(238, res)

    def test_area_34_8_values(self):
        res = rectangle.area(34, 8)
        self.assertEqual(272, res)

    def test_area_34_9_values(self):
        res = rectangle.area(34, 9)
        self.assertEqual(306, res)

    def test_area_34_10_values(self):
        res = rectangle.area(34, 10)
        self.assertEqual(340, res)

    def test_area_34_11_values(self):
        res = rectangle.area(34, 11)
        self.assertEqual(374, res)

    def test_area_34_12_values(self):
        res = rectangle.area(34, 12)
        self.assertEqual(408, res)

    def test_area_34_13_values(self):
        res = rectangle.area(34, 13)
        self.assertEqual(442, res)

    def test_area_34_14_values(self):
        res = rectangle.area(34, 14)
        self.assertEqual(476, res)

    def test_area_34_15_values(self):
        res = rectangle.area(34, 15)
        self.assertEqual(510, res)

    def test_area_34_16_values(self):
        res = rectangle.area(34, 16)
        self.assertEqual(544, res)

    def test_area_34_17_values(self):
        res = rectangle.area(34, 17)
        self.assertEqual(578, res)

    def test_area_34_18_values(self):
        res = rectangle.area(34, 18)
        self.assertEqual(612, res)

    def test_area_34_19_values(self):
        res = rectangle.area(34, 19)
        self.assertEqual(646, res)

    def test_area_34_20_values(self):
        res = rectangle.area(34, 20)
        self.assertEqual(680, res)

    def test_area_34_21_values(self):
        res = rectangle.area(34, 21)
        self.assertEqual(714, res)

    def test_area_34_22_values(self):
        res = rectangle.area(34, 22)
        self.assertEqual(748, res)

    def test_area_34_23_values(self):
        res = rectangle.area(34, 23)
        self.assertEqual(782, res)

    def test_area_34_24_values(self):
        res = rectangle.area(34, 24)
        self.assertEqual(816, res)

    def test_area_34_25_values(self):
        res = rectangle.area(34, 25)
        self.assertEqual(850, res)

    def test_area_34_26_values(self):
        res = rectangle.area(34, 26)
        self.assertEqual(884, res)

    def test_area_34_27_values(self):
        res = rectangle.area(34, 27)
        self.assertEqual(918, res)

    def test_area_34_28_values(self):
        res = rectangle.area(34, 28)
        self.assertEqual(952, res)

    def test_area_34_29_values(self):
        res = rectangle.area(34, 29)
        self.assertEqual(986, res)

    def test_area_35_1_values(self):
        res = rectangle.area(35, 1)
        self.assertEqual(35, res)

    def test_area_35_2_values(self):
        res = rectangle.area(35, 2)
        self.assertEqual(70, res)

    def test_area_35_3_values(self):
        res = rectangle.area(35, 3)
        self.assertEqual(105, res)

    def test_area_35_4_values(self):
        res = rectangle.area(35, 4)
        self.assertEqual(140, res)

    def test_area_35_5_values(self):
        res = rectangle.area(35, 5)
        self.assertEqual(175, res)

    def test_area_35_6_values(self):
        res = rectangle.area(35, 6)
        self.assertEqual(210, res)

    def test_area_35_7_values(self):
        res = rectangle.area(35, 7)
        self.assertEqual(245, res)

    def test_area_35_8_values(self):
        res = rectangle.area(35, 8)
        self.assertEqual(280, res)

    def test_area_35_9_values(self):
        res = rectangle.area(35, 9)
        self.assertEqual(315, res)

    def test_area_35_10_values(self):
        res = rectangle.area(35, 10)
        self.assertEqual(350, res)

    def test_area_35_11_values(self):
        res = rectangle.area(35, 11)
        self.assertEqual(385, res)

    def test_area_35_12_values(self):
        res = rectangle.area(35, 12)
        self.assertEqual(420, res)

    def test_area_35_13_values(self):
        res = rectangle.area(35, 13)
        self.assertEqual(455, res)

    def test_area_35_14_values(self):
        res = rectangle.area(35, 14)
        self.assertEqual(490, res)

    def test_area_35_15_values(self):
        res = rectangle.area(35, 15)
        self.assertEqual(525, res)

    def test_area_35_16_values(self):
        res = rectangle.area(35, 16)
        self.assertEqual(560, res)

    def test_area_35_17_values(self):
        res = rectangle.area(35, 17)
        self.assertEqual(595, res)

    def test_area_35_18_values(self):
        res = rectangle.area(35, 18)
        self.assertEqual(630, res)

    def test_area_35_19_values(self):
        res = rectangle.area(35, 19)
        self.assertEqual(665, res)

    def test_area_35_20_values(self):
        res = rectangle.area(35, 20)
        self.assertEqual(700, res)

    def test_area_35_21_values(self):
        res = rectangle.area(35, 21)
        self.assertEqual(735, res)

    def test_area_35_22_values(self):
        res = rectangle.area(35, 22)
        self.assertEqual(770, res)

    def test_area_35_23_values(self):
        res = rectangle.area(35, 23)
        self.assertEqual(805, res)

    def test_area_35_24_values(self):
        res = rectangle.area(35, 24)
        self.assertEqual(840, res)

    def test_area_35_25_values(self):
        res = rectangle.area(35, 25)
        self.assertEqual(875, res)

    def test_area_35_26_values(self):
        res = rectangle.area(35, 26)
        self.assertEqual(910, res)

    def test_area_35_27_values(self):
        res = rectangle.area(35, 27)
        self.assertEqual(945, res)

    def test_area_35_28_values(self):
        res = rectangle.area(35, 28)
        self.assertEqual(980, res)

    def test_area_35_29_values(self):
        res = rectangle.area(35, 29)
        self.assertEqual(1015, res)

    def test_area_36_1_values(self):
        res = rectangle.area(36, 1)
        self.assertEqual(36, res)

    def test_area_36_2_values(self):
        res = rectangle.area(36, 2)
        self.assertEqual(72, res)

    def test_area_36_3_values(self):
        res = rectangle.area(36, 3)
        self.assertEqual(108, res)

    def test_area_36_4_values(self):
        res = rectangle.area(36, 4)
        self.assertEqual(144, res)

    def test_area_36_5_values(self):
        res = rectangle.area(36, 5)
        self.assertEqual(180, res)

    def test_area_36_6_values(self):
        res = rectangle.area(36, 6)
        self.assertEqual(216, res)

    def test_area_36_7_values(self):
        res = rectangle.area(36, 7)
        self.assertEqual(252, res)

    def test_area_36_8_values(self):
        res = rectangle.area(36, 8)
        self.assertEqual(288, res)

    def test_area_36_9_values(self):
        res = rectangle.area(36, 9)
        self.assertEqual(324, res)

    def test_area_36_10_values(self):
        res = rectangle.area(36, 10)
        self.assertEqual(360, res)

    def test_area_36_11_values(self):
        res = rectangle.area(36, 11)
        self.assertEqual(396, res)

    def test_area_36_12_values(self):
        res = rectangle.area(36, 12)
        self.assertEqual(432, res)

    def test_area_36_13_values(self):
        res = rectangle.area(36, 13)
        self.assertEqual(468, res)

    def test_area_36_14_values(self):
        res = rectangle.area(36, 14)
        self.assertEqual(504, res)

    def test_area_36_15_values(self):
        res = rectangle.area(36, 15)
        self.assertEqual(540, res)

    def test_area_36_16_values(self):
        res = rectangle.area(36, 16)
        self.assertEqual(576, res)

    def test_area_36_17_values(self):
        res = rectangle.area(36, 17)
        self.assertEqual(612, res)

    def test_area_36_18_values(self):
        res = rectangle.area(36, 18)
        self.assertEqual(648, res)

    def test_area_36_19_values(self):
        res = rectangle.area(36, 19)
        self.assertEqual(684, res)

    def test_area_36_20_values(self):
        res = rectangle.area(36, 20)
        self.assertEqual(720, res)

    def test_area_36_21_values(self):
        res = rectangle.area(36, 21)
        self.assertEqual(756, res)

    def test_area_36_22_values(self):
        res = rectangle.area(36, 22)
        self.assertEqual(792, res)

    def test_area_36_23_values(self):
        res = rectangle.area(36, 23)
        self.assertEqual(828, res)

    def test_area_36_24_values(self):
        res = rectangle.area(36, 24)
        self.assertEqual(864, res)

    def test_area_36_25_values(self):
        res = rectangle.area(36, 25)
        self.assertEqual(900, res)

    def test_area_36_26_values(self):
        res = rectangle.area(36, 26)
        self.assertEqual(936, res)

    def test_area_36_27_values(self):
        res = rectangle.area(36, 27)
        self.assertEqual(972, res)

    def test_area_36_28_values(self):
        res = rectangle.area(36, 28)
        self.assertEqual(1008, res)

    def test_area_36_29_values(self):
        res = rectangle.area(36, 29)
        self.assertEqual(1044, res)

    def test_area_37_1_values(self):
        res = rectangle.area(37, 1)
        self.assertEqual(37, res)

    def test_area_37_2_values(self):
        res = rectangle.area(37, 2)
        self.assertEqual(74, res)

    def test_area_37_3_values(self):
        res = rectangle.area(37, 3)
        self.assertEqual(111, res)

    def test_area_37_4_values(self):
        res = rectangle.area(37, 4)
        self.assertEqual(148, res)

    def test_area_37_5_values(self):
        res = rectangle.area(37, 5)
        self.assertEqual(185, res)

    def test_area_37_6_values(self):
        res = rectangle.area(37, 6)
        self.assertEqual(222, res)

    def test_area_37_7_values(self):
        res = rectangle.area(37, 7)
        self.assertEqual(259, res)

    def test_area_37_8_values(self):
        res = rectangle.area(37, 8)
        self.assertEqual(296, res)

    def test_area_37_9_values(self):
        res = rectangle.area(37, 9)
        self.assertEqual(333, res)

    def test_area_37_10_values(self):
        res = rectangle.area(37, 10)
        self.assertEqual(370, res)

    def test_area_37_11_values(self):
        res = rectangle.area(37, 11)
        self.assertEqual(407, res)

    def test_area_37_12_values(self):
        res = rectangle.area(37, 12)
        self.assertEqual(444, res)

    def test_area_37_13_values(self):
        res = rectangle.area(37, 13)
        self.assertEqual(481, res)

    def test_area_37_14_values(self):
        res = rectangle.area(37, 14)
        self.assertEqual(518, res)

    def test_area_37_15_values(self):
        res = rectangle.area(37, 15)
        self.assertEqual(555, res)

    def test_area_37_16_values(self):
        res = rectangle.area(37, 16)
        self.assertEqual(592, res)

    def test_area_37_17_values(self):
        res = rectangle.area(37, 17)
        self.assertEqual(629, res)

    def test_area_37_18_values(self):
        res = rectangle.area(37, 18)
        self.assertEqual(666, res)

    def test_area_37_19_values(self):
        res = rectangle.area(37, 19)
        self.assertEqual(703, res)

    def test_area_37_20_values(self):
        res = rectangle.area(37, 20)
        self.assertEqual(740, res)

    def test_area_37_21_values(self):
        res = rectangle.area(37, 21)
        self.assertEqual(777, res)

    def test_area_37_22_values(self):
        res = rectangle.area(37, 22)
        self.assertEqual(814, res)

    def test_area_37_23_values(self):
        res = rectangle.area(37, 23)
        self.assertEqual(851, res)

    def test_area_37_24_values(self):
        res = rectangle.area(37, 24)
        self.assertEqual(888, res)

    def test_area_37_25_values(self):
        res = rectangle.area(37, 25)
        self.assertEqual(925, res)

    def test_area_37_26_values(self):
        res = rectangle.area(37, 26)
        self.assertEqual(962, res)

    def test_area_37_27_values(self):
        res = rectangle.area(37, 27)
        self.assertEqual(999, res)

    def test_area_37_28_values(self):
        res = rectangle.area(37, 28)
        self.assertEqual(1036, res)

    def test_area_37_29_values(self):
        res = rectangle.area(37, 29)
        self.assertEqual(1073, res)

    def test_area_38_1_values(self):
        res = rectangle.area(38, 1)
        self.assertEqual(38, res)

    def test_area_38_2_values(self):
        res = rectangle.area(38, 2)
        self.assertEqual(76, res)

    def test_area_38_3_values(self):
        res = rectangle.area(38, 3)
        self.assertEqual(114, res)

    def test_area_38_4_values(self):
        res = rectangle.area(38, 4)
        self.assertEqual(152, res)

    def test_area_38_5_values(self):
        res = rectangle.area(38, 5)
        self.assertEqual(190, res)

    def test_area_38_6_values(self):
        res = rectangle.area(38, 6)
        self.assertEqual(228, res)

    def test_area_38_7_values(self):
        res = rectangle.area(38, 7)
        self.assertEqual(266, res)

    def test_area_38_8_values(self):
        res = rectangle.area(38, 8)
        self.assertEqual(304, res)

    def test_area_38_9_values(self):
        res = rectangle.area(38, 9)
        self.assertEqual(342, res)

    def test_area_38_10_values(self):
        res = rectangle.area(38, 10)
        self.assertEqual(380, res)

    def test_area_38_11_values(self):
        res = rectangle.area(38, 11)
        self.assertEqual(418, res)

    def test_area_38_12_values(self):
        res = rectangle.area(38, 12)
        self.assertEqual(456, res)

    def test_area_38_13_values(self):
        res = rectangle.area(38, 13)
        self.assertEqual(494, res)

    def test_area_38_14_values(self):
        res = rectangle.area(38, 14)
        self.assertEqual(532, res)

    def test_area_38_15_values(self):
        res = rectangle.area(38, 15)
        self.assertEqual(570, res)

    def test_area_38_16_values(self):
        res = rectangle.area(38, 16)
        self.assertEqual(608, res)

    def test_area_38_17_values(self):
        res = rectangle.area(38, 17)
        self.assertEqual(646, res)

    def test_area_38_18_values(self):
        res = rectangle.area(38, 18)
        self.assertEqual(684, res)

    def test_area_38_19_values(self):
        res = rectangle.area(38, 19)
        self.assertEqual(722, res)

    def test_area_38_20_values(self):
        res = rectangle.area(38, 20)
        self.assertEqual(760, res)

    def test_area_38_21_values(self):
        res = rectangle.area(38, 21)
        self.assertEqual(798, res)

    def test_area_38_22_values(self):
        res = rectangle.area(38, 22)
        self.assertEqual(836, res)

    def test_area_38_23_values(self):
        res = rectangle.area(38, 23)
        self.assertEqual(874, res)

    def test_area_38_24_values(self):
        res = rectangle.area(38, 24)
        self.assertEqual(912, res)

    def test_area_38_25_values(self):
        res = rectangle.area(38, 25)
        self.assertEqual(950, res)

    def test_area_38_26_values(self):
        res = rectangle.area(38, 26)
        self.assertEqual(988, res)

    def test_area_38_27_values(self):
        res = rectangle.area(38, 27)
        self.assertEqual(1026, res)

    def test_area_38_28_values(self):
        res = rectangle.area(38, 28)
        self.assertEqual(1064, res)

    def test_area_38_29_values(self):
        res = rectangle.area(38, 29)
        self.assertEqual(1102, res)

    def test_area_39_1_values(self):
        res = rectangle.area(39, 1)
        self.assertEqual(39, res)

    def test_area_39_2_values(self):
        res = rectangle.area(39, 2)
        self.assertEqual(78, res)

    def test_area_39_3_values(self):
        res = rectangle.area(39, 3)
        self.assertEqual(117, res)

    def test_area_39_4_values(self):
        res = rectangle.area(39, 4)
        self.assertEqual(156, res)

    def test_area_39_5_values(self):
        res = rectangle.area(39, 5)
        self.assertEqual(195, res)

    def test_area_39_6_values(self):
        res = rectangle.area(39, 6)
        self.assertEqual(234, res)

    def test_area_39_7_values(self):
        res = rectangle.area(39, 7)
        self.assertEqual(273, res)

    def test_area_39_8_values(self):
        res = rectangle.area(39, 8)
        self.assertEqual(312, res)

    def test_area_39_9_values(self):
        res = rectangle.area(39, 9)
        self.assertEqual(351, res)

    def test_area_39_10_values(self):
        res = rectangle.area(39, 10)
        self.assertEqual(390, res)

    def test_area_39_11_values(self):
        res = rectangle.area(39, 11)
        self.assertEqual(429, res)

    def test_area_39_12_values(self):
        res = rectangle.area(39, 12)
        self.assertEqual(468, res)

    def test_area_39_13_values(self):
        res = rectangle.area(39, 13)
        self.assertEqual(507, res)

    def test_area_39_14_values(self):
        res = rectangle.area(39, 14)
        self.assertEqual(546, res)

    def test_area_39_15_values(self):
        res = rectangle.area(39, 15)
        self.assertEqual(585, res)

    def test_area_39_16_values(self):
        res = rectangle.area(39, 16)
        self.assertEqual(624, res)

    def test_area_39_17_values(self):
        res = rectangle.area(39, 17)
        self.assertEqual(663, res)

    def test_area_39_18_values(self):
        res = rectangle.area(39, 18)
        self.assertEqual(702, res)

    def test_area_39_19_values(self):
        res = rectangle.area(39, 19)
        self.assertEqual(741, res)

    def test_area_39_20_values(self):
        res = rectangle.area(39, 20)
        self.assertEqual(780, res)

    def test_area_39_21_values(self):
        res = rectangle.area(39, 21)
        self.assertEqual(819, res)

    def test_area_39_22_values(self):
        res = rectangle.area(39, 22)
        self.assertEqual(858, res)

    def test_area_39_23_values(self):
        res = rectangle.area(39, 23)
        self.assertEqual(897, res)

    def test_area_39_24_values(self):
        res = rectangle.area(39, 24)
        self.assertEqual(936, res)

    def test_area_39_25_values(self):
        res = rectangle.area(39, 25)
        self.assertEqual(975, res)

    def test_area_39_26_values(self):
        res = rectangle.area(39, 26)
        self.assertEqual(1014, res)

    def test_area_39_27_values(self):
        res = rectangle.area(39, 27)
        self.assertEqual(1053, res)

    def test_area_39_28_values(self):
        res = rectangle.area(39, 28)
        self.assertEqual(1092, res)

    def test_area_39_29_values(self):
        res = rectangle.area(39, 29)
        self.assertEqual(1131, res)

    def test_area_40_1_values(self):
        res = rectangle.area(40, 1)
        self.assertEqual(40, res)

    def test_area_40_2_values(self):
        res = rectangle.area(40, 2)
        self.assertEqual(80, res)

    def test_area_40_3_values(self):
        res = rectangle.area(40, 3)
        self.assertEqual(120, res)

    def test_area_40_4_values(self):
        res = rectangle.area(40, 4)
        self.assertEqual(160, res)

    def test_area_40_5_values(self):
        res = rectangle.area(40, 5)
        self.assertEqual(200, res)

    def test_area_40_6_values(self):
        res = rectangle.area(40, 6)
        self.assertEqual(240, res)

    def test_area_40_7_values(self):
        res = rectangle.area(40, 7)
        self.assertEqual(280, res)

    def test_area_40_8_values(self):
        res = rectangle.area(40, 8)
        self.assertEqual(320, res)

    def test_area_40_9_values(self):
        res = rectangle.area(40, 9)
        self.assertEqual(360, res)

    def test_area_40_10_values(self):
        res = rectangle.area(40, 10)
        self.assertEqual(400, res)

    def test_area_40_11_values(self):
        res = rectangle.area(40, 11)
        self.assertEqual(440, res)

    def test_area_40_12_values(self):
        res = rectangle.area(40, 12)
        self.assertEqual(480, res)

    def test_area_40_13_values(self):
        res = rectangle.area(40, 13)
        self.assertEqual(520, res)

    def test_area_40_14_values(self):
        res = rectangle.area(40, 14)
        self.assertEqual(560, res)

    def test_area_40_15_values(self):
        res = rectangle.area(40, 15)
        self.assertEqual(600, res)

    def test_area_40_16_values(self):
        res = rectangle.area(40, 16)
        self.assertEqual(640, res)

    def test_area_40_17_values(self):
        res = rectangle.area(40, 17)
        self.assertEqual(680, res)

    def test_area_40_18_values(self):
        res = rectangle.area(40, 18)
        self.assertEqual(720, res)

    def test_area_40_19_values(self):
        res = rectangle.area(40, 19)
        self.assertEqual(760, res)

    def test_area_40_20_values(self):
        res = rectangle.area(40, 20)
        self.assertEqual(800, res)

    def test_area_40_21_values(self):
        res = rectangle.area(40, 21)
        self.assertEqual(840, res)

    def test_area_40_22_values(self):
        res = rectangle.area(40, 22)
        self.assertEqual(880, res)

    def test_area_40_23_values(self):
        res = rectangle.area(40, 23)
        self.assertEqual(920, res)

    def test_area_40_24_values(self):
        res = rectangle.area(40, 24)
        self.assertEqual(960, res)

    def test_area_40_25_values(self):
        res = rectangle.area(40, 25)
        self.assertEqual(1000, res)

    def test_area_40_26_values(self):
        res = rectangle.area(40, 26)
        self.assertEqual(1040, res)

    def test_area_40_27_values(self):
        res = rectangle.area(40, 27)
        self.assertEqual(1080, res)

    def test_area_40_28_values(self):
        res = rectangle.area(40, 28)
        self.assertEqual(1120, res)

    def test_area_40_29_values(self):
        res = rectangle.area(40, 29)
        self.assertEqual(1160, res)

    def test_area_41_1_values(self):
        res = rectangle.area(41, 1)
        self.assertEqual(41, res)

    def test_area_41_2_values(self):
        res = rectangle.area(41, 2)
        self.assertEqual(82, res)

    def test_area_41_3_values(self):
        res = rectangle.area(41, 3)
        self.assertEqual(123, res)

    def test_area_41_4_values(self):
        res = rectangle.area(41, 4)
        self.assertEqual(164, res)

    def test_area_41_5_values(self):
        res = rectangle.area(41, 5)
        self.assertEqual(205, res)

    def test_area_41_6_values(self):
        res = rectangle.area(41, 6)
        self.assertEqual(246, res)

    def test_area_41_7_values(self):
        res = rectangle.area(41, 7)
        self.assertEqual(287, res)

    def test_area_41_8_values(self):
        res = rectangle.area(41, 8)
        self.assertEqual(328, res)

    def test_area_41_9_values(self):
        res = rectangle.area(41, 9)
        self.assertEqual(369, res)

    def test_area_41_10_values(self):
        res = rectangle.area(41, 10)
        self.assertEqual(410, res)

    def test_area_41_11_values(self):
        res = rectangle.area(41, 11)
        self.assertEqual(451, res)

    def test_area_41_12_values(self):
        res = rectangle.area(41, 12)
        self.assertEqual(492, res)

    def test_area_41_13_values(self):
        res = rectangle.area(41, 13)
        self.assertEqual(533, res)

    def test_area_41_14_values(self):
        res = rectangle.area(41, 14)
        self.assertEqual(574, res)

    def test_area_41_15_values(self):
        res = rectangle.area(41, 15)
        self.assertEqual(615, res)

    def test_area_41_16_values(self):
        res = rectangle.area(41, 16)
        self.assertEqual(656, res)

    def test_area_41_17_values(self):
        res = rectangle.area(41, 17)
        self.assertEqual(697, res)

    def test_area_41_18_values(self):
        res = rectangle.area(41, 18)
        self.assertEqual(738, res)

    def test_area_41_19_values(self):
        res = rectangle.area(41, 19)
        self.assertEqual(779, res)

    def test_area_41_20_values(self):
        res = rectangle.area(41, 20)
        self.assertEqual(820, res)

    def test_area_41_21_values(self):
        res = rectangle.area(41, 21)
        self.assertEqual(861, res)

    def test_area_41_22_values(self):
        res = rectangle.area(41, 22)
        self.assertEqual(902, res)

    def test_area_41_23_values(self):
        res = rectangle.area(41, 23)
        self.assertEqual(943, res)

    def test_area_41_24_values(self):
        res = rectangle.area(41, 24)
        self.assertEqual(984, res)

    def test_area_41_25_values(self):
        res = rectangle.area(41, 25)
        self.assertEqual(1025, res)

    def test_area_41_26_values(self):
        res = rectangle.area(41, 26)
        self.assertEqual(1066, res)

    def test_area_41_27_values(self):
        res = rectangle.area(41, 27)
        self.assertEqual(1107, res)

    def test_area_41_28_values(self):
        res = rectangle.area(41, 28)
        self.assertEqual(1148, res)

    def test_area_41_29_values(self):
        res = rectangle.area(41, 29)
        self.assertEqual(1189, res)

    def test_area_42_1_values(self):
        res = rectangle.area(42, 1)
        self.assertEqual(42, res)

    def test_area_42_2_values(self):
        res = rectangle.area(42, 2)
        self.assertEqual(84, res)

    def test_area_42_3_values(self):
        res = rectangle.area(42, 3)
        self.assertEqual(126, res)

    def test_area_42_4_values(self):
        res = rectangle.area(42, 4)
        self.assertEqual(168, res)

    def test_area_42_5_values(self):
        res = rectangle.area(42, 5)
        self.assertEqual(210, res)

    def test_area_42_6_values(self):
        res = rectangle.area(42, 6)
        self.assertEqual(252, res)

    def test_area_42_7_values(self):
        res = rectangle.area(42, 7)
        self.assertEqual(294, res)

    def test_area_42_8_values(self):
        res = rectangle.area(42, 8)
        self.assertEqual(336, res)

    def test_area_42_9_values(self):
        res = rectangle.area(42, 9)
        self.assertEqual(378, res)

    def test_area_42_10_values(self):
        res = rectangle.area(42, 10)
        self.assertEqual(420, res)

    def test_area_42_11_values(self):
        res = rectangle.area(42, 11)
        self.assertEqual(462, res)

    def test_area_42_12_values(self):
        res = rectangle.area(42, 12)
        self.assertEqual(504, res)

    def test_area_42_13_values(self):
        res = rectangle.area(42, 13)
        self.assertEqual(546, res)

    def test_area_42_14_values(self):
        res = rectangle.area(42, 14)
        self.assertEqual(588, res)

    def test_area_42_15_values(self):
        res = rectangle.area(42, 15)
        self.assertEqual(630, res)

    def test_area_42_16_values(self):
        res = rectangle.area(42, 16)
        self.assertEqual(672, res)

    def test_area_42_17_values(self):
        res = rectangle.area(42, 17)
        self.assertEqual(714, res)

    def test_area_42_18_values(self):
        res = rectangle.area(42, 18)
        self.assertEqual(756, res)

    def test_area_42_19_values(self):
        res = rectangle.area(42, 19)
        self.assertEqual(798, res)

    def test_area_42_20_values(self):
        res = rectangle.area(42, 20)
        self.assertEqual(840, res)

    def test_area_42_21_values(self):
        res = rectangle.area(42, 21)
        self.assertEqual(882, res)

    def test_area_42_22_values(self):
        res = rectangle.area(42, 22)
        self.assertEqual(924, res)

    def test_area_42_23_values(self):
        res = rectangle.area(42, 23)
        self.assertEqual(966, res)

    def test_area_42_24_values(self):
        res = rectangle.area(42, 24)
        self.assertEqual(1008, res)

    def test_area_42_25_values(self):
        res = rectangle.area(42, 25)
        self.assertEqual(1050, res)

    def test_area_42_26_values(self):
        res = rectangle.area(42, 26)
        self.assertEqual(1092, res)

    def test_area_42_27_values(self):
        res = rectangle.area(42, 27)
        self.assertEqual(1134, res)

    def test_area_42_28_values(self):
        res = rectangle.area(42, 28)
        self.assertEqual(1176, res)

    def test_area_42_29_values(self):
        res = rectangle.area(42, 29)
        self.assertEqual(1218, res)

    def test_area_43_1_values(self):
        res = rectangle.area(43, 1)
        self.assertEqual(43, res)

    def test_area_43_2_values(self):
        res = rectangle.area(43, 2)
        self.assertEqual(86, res)

    def test_area_43_3_values(self):
        res = rectangle.area(43, 3)
        self.assertEqual(129, res)

    def test_area_43_4_values(self):
        res = rectangle.area(43, 4)
        self.assertEqual(172, res)

    def test_area_43_5_values(self):
        res = rectangle.area(43, 5)
        self.assertEqual(215, res)

    def test_area_43_6_values(self):
        res = rectangle.area(43, 6)
        self.assertEqual(258, res)

    def test_area_43_7_values(self):
        res = rectangle.area(43, 7)
        self.assertEqual(301, res)

    def test_area_43_8_values(self):
        res = rectangle.area(43, 8)
        self.assertEqual(344, res)

    def test_area_43_9_values(self):
        res = rectangle.area(43, 9)
        self.assertEqual(387, res)

    def test_area_43_10_values(self):
        res = rectangle.area(43, 10)
        self.assertEqual(430, res)

    def test_area_43_11_values(self):
        res = rectangle.area(43, 11)
        self.assertEqual(473, res)

    def test_area_43_12_values(self):
        res = rectangle.area(43, 12)
        self.assertEqual(516, res)

    def test_area_43_13_values(self):
        res = rectangle.area(43, 13)
        self.assertEqual(559, res)

    def test_area_43_14_values(self):
        res = rectangle.area(43, 14)
        self.assertEqual(602, res)

    def test_area_43_15_values(self):
        res = rectangle.area(43, 15)
        self.assertEqual(645, res)

    def test_area_43_16_values(self):
        res = rectangle.area(43, 16)
        self.assertEqual(688, res)

    def test_area_43_17_values(self):
        res = rectangle.area(43, 17)
        self.assertEqual(731, res)

    def test_area_43_18_values(self):
        res = rectangle.area(43, 18)
        self.assertEqual(774, res)

    def test_area_43_19_values(self):
        res = rectangle.area(43, 19)
        self.assertEqual(817, res)

    def test_area_43_20_values(self):
        res = rectangle.area(43, 20)
        self.assertEqual(860, res)

    def test_area_43_21_values(self):
        res = rectangle.area(43, 21)
        self.assertEqual(903, res)

    def test_area_43_22_values(self):
        res = rectangle.area(43, 22)
        self.assertEqual(946, res)

    def test_area_43_23_values(self):
        res = rectangle.area(43, 23)
        self.assertEqual(989, res)

    def test_area_43_24_values(self):
        res = rectangle.area(43, 24)
        self.assertEqual(1032, res)

    def test_area_43_25_values(self):
        res = rectangle.area(43, 25)
        self.assertEqual(1075, res)

    def test_area_43_26_values(self):
        res = rectangle.area(43, 26)
        self.assertEqual(1118, res)

    def test_area_43_27_values(self):
        res = rectangle.area(43, 27)
        self.assertEqual(1161, res)

    def test_area_43_28_values(self):
        res = rectangle.area(43, 28)
        self.assertEqual(1204, res)

    def test_area_43_29_values(self):
        res = rectangle.area(43, 29)
        self.assertEqual(1247, res)

    def test_area_44_1_values(self):
        res = rectangle.area(44, 1)
        self.assertEqual(44, res)

    def test_area_44_2_values(self):
        res = rectangle.area(44, 2)
        self.assertEqual(88, res)

    def test_area_44_3_values(self):
        res = rectangle.area(44, 3)
        self.assertEqual(132, res)

    def test_area_44_4_values(self):
        res = rectangle.area(44, 4)
        self.assertEqual(176, res)

    def test_area_44_5_values(self):
        res = rectangle.area(44, 5)
        self.assertEqual(220, res)

    def test_area_44_6_values(self):
        res = rectangle.area(44, 6)
        self.assertEqual(264, res)

    def test_area_44_7_values(self):
        res = rectangle.area(44, 7)
        self.assertEqual(308, res)

    def test_area_44_8_values(self):
        res = rectangle.area(44, 8)
        self.assertEqual(352, res)

    def test_area_44_9_values(self):
        res = rectangle.area(44, 9)
        self.assertEqual(396, res)

    def test_area_44_10_values(self):
        res = rectangle.area(44, 10)
        self.assertEqual(440, res)

    def test_area_44_11_values(self):
        res = rectangle.area(44, 11)
        self.assertEqual(484, res)

    def test_area_44_12_values(self):
        res = rectangle.area(44, 12)
        self.assertEqual(528, res)

    def test_area_44_13_values(self):
        res = rectangle.area(44, 13)
        self.assertEqual(572, res)

    def test_area_44_14_values(self):
        res = rectangle.area(44, 14)
        self.assertEqual(616, res)

    def test_area_44_15_values(self):
        res = rectangle.area(44, 15)
        self.assertEqual(660, res)

    def test_area_44_16_values(self):
        res = rectangle.area(44, 16)
        self.assertEqual(704, res)

    def test_area_44_17_values(self):
        res = rectangle.area(44, 17)
        self.assertEqual(748, res)

    def test_area_44_18_values(self):
        res = rectangle.area(44, 18)
        self.assertEqual(792, res)

    def test_area_44_19_values(self):
        res = rectangle.area(44, 19)
        self.assertEqual(836, res)

    def test_area_44_20_values(self):
        res = rectangle.area(44, 20)
        self.assertEqual(880, res)

    def test_area_44_21_values(self):
        res = rectangle.area(44, 21)
        self.assertEqual(924, res)

    def test_area_44_22_values(self):
        res = rectangle.area(44, 22)
        self.assertEqual(968, res)

    def test_area_44_23_values(self):
        res = rectangle.area(44, 23)
        self.assertEqual(1012, res)

    def test_area_44_24_values(self):
        res = rectangle.area(44, 24)
        self.assertEqual(1056, res)

    def test_area_44_25_values(self):
        res = rectangle.area(44, 25)
        self.assertEqual(1100, res)

    def test_area_44_26_values(self):
        res = rectangle.area(44, 26)
        self.assertEqual(1144, res)

    def test_area_44_27_values(self):
        res = rectangle.area(44, 27)
        self.assertEqual(1188, res)

    def test_area_44_28_values(self):
        res = rectangle.area(44, 28)
        self.assertEqual(1232, res)

    def test_area_44_29_values(self):
        res = rectangle.area(44, 29)
        self.assertEqual(1276, res)

    def test_area_45_1_values(self):
        res = rectangle.area(45, 1)
        self.assertEqual(45, res)

    def test_area_45_2_values(self):
        res = rectangle.area(45, 2)
        self.assertEqual(90, res)

    def test_area_45_3_values(self):
        res = rectangle.area(45, 3)
        self.assertEqual(135, res)

    def test_area_45_4_values(self):
        res = rectangle.area(45, 4)
        self.assertEqual(180, res)

    def test_area_45_5_values(self):
        res = rectangle.area(45, 5)
        self.assertEqual(225, res)

    def test_area_45_6_values(self):
        res = rectangle.area(45, 6)
        self.assertEqual(270, res)

    def test_area_45_7_values(self):
        res = rectangle.area(45, 7)
        self.assertEqual(315, res)

    def test_area_45_8_values(self):
        res = rectangle.area(45, 8)
        self.assertEqual(360, res)

    def test_area_45_9_values(self):
        res = rectangle.area(45, 9)
        self.assertEqual(405, res)

    def test_area_45_10_values(self):
        res = rectangle.area(45, 10)
        self.assertEqual(450, res)

    def test_area_45_11_values(self):
        res = rectangle.area(45, 11)
        self.assertEqual(495, res)

    def test_area_45_12_values(self):
        res = rectangle.area(45, 12)
        self.assertEqual(540, res)

    def test_area_45_13_values(self):
        res = rectangle.area(45, 13)
        self.assertEqual(585, res)

    def test_area_45_14_values(self):
        res = rectangle.area(45, 14)
        self.assertEqual(630, res)

    def test_area_45_15_values(self):
        res = rectangle.area(45, 15)
        self.assertEqual(675, res)

    def test_area_45_16_values(self):
        res = rectangle.area(45, 16)
        self.assertEqual(720, res)

    def test_area_45_17_values(self):
        res = rectangle.area(45, 17)
        self.assertEqual(765, res)

    def test_area_45_18_values(self):
        res = rectangle.area(45, 18)
        self.assertEqual(810, res)

    def test_area_45_19_values(self):
        res = rectangle.area(45, 19)
        self.assertEqual(855, res)

    def test_area_45_20_values(self):
        res = rectangle.area(45, 20)
        self.assertEqual(900, res)

    def test_area_45_21_values(self):
        res = rectangle.area(45, 21)
        self.assertEqual(945, res)

    def test_area_45_22_values(self):
        res = rectangle.area(45, 22)
        self.assertEqual(990, res)

    def test_area_45_23_values(self):
        res = rectangle.area(45, 23)
        self.assertEqual(1035, res)

    def test_area_45_24_values(self):
        res = rectangle.area(45, 24)
        self.assertEqual(1080, res)

    def test_area_45_25_values(self):
        res = rectangle.area(45, 25)
        self.assertEqual(1125, res)

    def test_area_45_26_values(self):
        res = rectangle.area(45, 26)
        self.assertEqual(1170, res)

    def test_area_45_27_values(self):
        res = rectangle.area(45, 27)
        self.assertEqual(1215, res)

    def test_area_45_28_values(self):
        res = rectangle.area(45, 28)
        self.assertEqual(1260, res)

    def test_area_45_29_values(self):
        res = rectangle.area(45, 29)
        self.assertEqual(1305, res)

    def test_area_46_1_values(self):
        res = rectangle.area(46, 1)
        self.assertEqual(46, res)

    def test_area_46_2_values(self):
        res = rectangle.area(46, 2)
        self.assertEqual(92, res)

    def test_area_46_3_values(self):
        res = rectangle.area(46, 3)
        self.assertEqual(138, res)

    def test_area_46_4_values(self):
        res = rectangle.area(46, 4)
        self.assertEqual(184, res)

    def test_area_46_5_values(self):
        res = rectangle.area(46, 5)
        self.assertEqual(230, res)

    def test_area_46_6_values(self):
        res = rectangle.area(46, 6)
        self.assertEqual(276, res)

    def test_area_46_7_values(self):
        res = rectangle.area(46, 7)
        self.assertEqual(322, res)

    def test_area_46_8_values(self):
        res = rectangle.area(46, 8)
        self.assertEqual(368, res)

    def test_area_46_9_values(self):
        res = rectangle.area(46, 9)
        self.assertEqual(414, res)

    def test_area_46_10_values(self):
        res = rectangle.area(46, 10)
        self.assertEqual(460, res)

    def test_area_46_11_values(self):
        res = rectangle.area(46, 11)
        self.assertEqual(506, res)

    def test_area_46_12_values(self):
        res = rectangle.area(46, 12)
        self.assertEqual(552, res)

    def test_area_46_13_values(self):
        res = rectangle.area(46, 13)
        self.assertEqual(598, res)

    def test_area_46_14_values(self):
        res = rectangle.area(46, 14)
        self.assertEqual(644, res)

    def test_area_46_15_values(self):
        res = rectangle.area(46, 15)
        self.assertEqual(690, res)

    def test_area_46_16_values(self):
        res = rectangle.area(46, 16)
        self.assertEqual(736, res)

    def test_area_46_17_values(self):
        res = rectangle.area(46, 17)
        self.assertEqual(782, res)

    def test_area_46_18_values(self):
        res = rectangle.area(46, 18)
        self.assertEqual(828, res)

    def test_area_46_19_values(self):
        res = rectangle.area(46, 19)
        self.assertEqual(874, res)

    def test_area_46_20_values(self):
        res = rectangle.area(46, 20)
        self.assertEqual(920, res)

    def test_area_46_21_values(self):
        res = rectangle.area(46, 21)
        self.assertEqual(966, res)

    def test_area_46_22_values(self):
        res = rectangle.area(46, 22)
        self.assertEqual(1012, res)

    def test_area_46_23_values(self):
        res = rectangle.area(46, 23)
        self.assertEqual(1058, res)

    def test_area_46_24_values(self):
        res = rectangle.area(46, 24)
        self.assertEqual(1104, res)

    def test_area_46_25_values(self):
        res = rectangle.area(46, 25)
        self.assertEqual(1150, res)

    def test_area_46_26_values(self):
        res = rectangle.area(46, 26)
        self.assertEqual(1196, res)

    def test_area_46_27_values(self):
        res = rectangle.area(46, 27)
        self.assertEqual(1242, res)

    def test_area_46_28_values(self):
        res = rectangle.area(46, 28)
        self.assertEqual(1288, res)

    def test_area_46_29_values(self):
        res = rectangle.area(46, 29)
        self.assertEqual(1334, res)

    def test_area_47_1_values(self):
        res = rectangle.area(47, 1)
        self.assertEqual(47, res)

    def test_area_47_2_values(self):
        res = rectangle.area(47, 2)
        self.assertEqual(94, res)

    def test_area_47_3_values(self):
        res = rectangle.area(47, 3)
        self.assertEqual(141, res)

    def test_area_47_4_values(self):
        res = rectangle.area(47, 4)
        self.assertEqual(188, res)

    def test_area_47_5_values(self):
        res = rectangle.area(47, 5)
        self.assertEqual(235, res)

    def test_area_47_6_values(self):
        res = rectangle.area(47, 6)
        self.assertEqual(282, res)

    def test_area_47_7_values(self):
        res = rectangle.area(47, 7)
        self.assertEqual(329, res)

    def test_area_47_8_values(self):
        res = rectangle.area(47, 8)
        self.assertEqual(376, res)

    def test_area_47_9_values(self):
        res = rectangle.area(47, 9)
        self.assertEqual(423, res)

    def test_area_47_10_values(self):
        res = rectangle.area(47, 10)
        self.assertEqual(470, res)

    def test_area_47_11_values(self):
        res = rectangle.area(47, 11)
        self.assertEqual(517, res)

    def test_area_47_12_values(self):
        res = rectangle.area(47, 12)
        self.assertEqual(564, res)

    def test_area_47_13_values(self):
        res = rectangle.area(47, 13)
        self.assertEqual(611, res)

    def test_area_47_14_values(self):
        res = rectangle.area(47, 14)
        self.assertEqual(658, res)

    def test_area_47_15_values(self):
        res = rectangle.area(47, 15)
        self.assertEqual(705, res)

    def test_area_47_16_values(self):
        res = rectangle.area(47, 16)
        self.assertEqual(752, res)

    def test_area_47_17_values(self):
        res = rectangle.area(47, 17)
        self.assertEqual(799, res)

    def test_area_47_18_values(self):
        res = rectangle.area(47, 18)
        self.assertEqual(846, res)

    def test_area_47_19_values(self):
        res = rectangle.area(47, 19)
        self.assertEqual(893, res)

    def test_area_47_20_values(self):
        res = rectangle.area(47, 20)
        self.assertEqual(940, res)

    def test_area_47_21_values(self):
        res = rectangle.area(47, 21)
        self.assertEqual(987, res)

    def test_area_47_22_values(self):
        res = rectangle.area(47, 22)
        self.assertEqual(1034, res)

    def test_area_47_23_values(self):
        res = rectangle.area(47, 23)
        self.assertEqual(1081, res)

    def test_area_47_24_values(self):
        res = rectangle.area(47, 24)
        self.assertEqual(1128, res)

    def test_area_47_25_values(self):
        res = rectangle.area(47, 25)
        self.assertEqual(1175, res)

    def test_area_47_26_values(self):
        res = rectangle.area(47, 26)
        self.assertEqual(1222, res)

    def test_area_47_27_values(self):
        res = rectangle.area(47, 27)
        self.assertEqual(1269, res)

    def test_area_47_28_values(self):
        res = rectangle.area(47, 28)
        self.assertEqual(1316, res)

    def test_area_47_29_values(self):
        res = rectangle.area(47, 29)
        self.assertEqual(1363, res)

    def test_area_48_1_values(self):
        res = rectangle.area(48, 1)
        self.assertEqual(48, res)

    def test_area_48_2_values(self):
        res = rectangle.area(48, 2)
        self.assertEqual(96, res)

    def test_area_48_3_values(self):
        res = rectangle.area(48, 3)
        self.assertEqual(144, res)

    def test_area_48_4_values(self):
        res = rectangle.area(48, 4)
        self.assertEqual(192, res)

    def test_area_48_5_values(self):
        res = rectangle.area(48, 5)
        self.assertEqual(240, res)

    def test_area_48_6_values(self):
        res = rectangle.area(48, 6)
        self.assertEqual(288, res)

    def test_area_48_7_values(self):
        res = rectangle.area(48, 7)
        self.assertEqual(336, res)

    def test_area_48_8_values(self):
        res = rectangle.area(48, 8)
        self.assertEqual(384, res)

    def test_area_48_9_values(self):
        res = rectangle.area(48, 9)
        self.assertEqual(432, res)

    def test_area_48_10_values(self):
        res = rectangle.area(48, 10)
        self.assertEqual(480, res)

    def test_area_48_11_values(self):
        res = rectangle.area(48, 11)
        self.assertEqual(528, res)

    def test_area_48_12_values(self):
        res = rectangle.area(48, 12)
        self.assertEqual(576, res)

    def test_area_48_13_values(self):
        res = rectangle.area(48, 13)
        self.assertEqual(624, res)

    def test_area_48_14_values(self):
        res = rectangle.area(48, 14)
        self.assertEqual(672, res)

    def test_area_48_15_values(self):
        res = rectangle.area(48, 15)
        self.assertEqual(720, res)

    def test_area_48_16_values(self):
        res = rectangle.area(48, 16)
        self.assertEqual(768, res)

    def test_area_48_17_values(self):
        res = rectangle.area(48, 17)
        self.assertEqual(816, res)

    def test_area_48_18_values(self):
        res = rectangle.area(48, 18)
        self.assertEqual(864, res)

    def test_area_48_19_values(self):
        res = rectangle.area(48, 19)
        self.assertEqual(912, res)

    def test_area_48_20_values(self):
        res = rectangle.area(48, 20)
        self.assertEqual(960, res)

    def test_area_48_21_values(self):
        res = rectangle.area(48, 21)
        self.assertEqual(1008, res)

    def test_area_48_22_values(self):
        res = rectangle.area(48, 22)
        self.assertEqual(1056, res)

    def test_area_48_23_values(self):
        res = rectangle.area(48, 23)
        self.assertEqual(1104, res)

    def test_area_48_24_values(self):
        res = rectangle.area(48, 24)
        self.assertEqual(1152, res)

    def test_area_48_25_values(self):
        res = rectangle.area(48, 25)
        self.assertEqual(1200, res)

    def test_area_48_26_values(self):
        res = rectangle.area(48, 26)
        self.assertEqual(1248, res)

    def test_area_48_27_values(self):
        res = rectangle.area(48, 27)
        self.assertEqual(1296, res)

    def test_area_48_28_values(self):
        res = rectangle.area(48, 28)
        self.assertEqual(1344, res)

    def test_area_48_29_values(self):
        res = rectangle.area(48, 29)
        self.assertEqual(1392, res)

    def test_area_49_1_values(self):
        res = rectangle.area(49, 1)
        self.assertEqual(49, res)

    def test_area_49_2_values(self):
        res = rectangle.area(49, 2)
        self.assertEqual(98, res)

    def test_area_49_3_values(self):
        res = rectangle.area(49, 3)
        self.assertEqual(147, res)

    def test_area_49_4_values(self):
        res = rectangle.area(49, 4)
        self.assertEqual(196, res)

    def test_area_49_5_values(self):
        res = rectangle.area(49, 5)
        self.assertEqual(245, res)

    def test_area_49_6_values(self):
        res = rectangle.area(49, 6)
        self.assertEqual(294, res)

    def test_area_49_7_values(self):
        res = rectangle.area(49, 7)
        self.assertEqual(343, res)

    def test_area_49_8_values(self):
        res = rectangle.area(49, 8)
        self.assertEqual(392, res)

    def test_area_49_9_values(self):
        res = rectangle.area(49, 9)
        self.assertEqual(441, res)

    def test_area_49_10_values(self):
        res = rectangle.area(49, 10)
        self.assertEqual(490, res)

    def test_area_49_11_values(self):
        res = rectangle.area(49, 11)
        self.assertEqual(539, res)

    def test_area_49_12_values(self):
        res = rectangle.area(49, 12)
        self.assertEqual(588, res)

    def test_area_49_13_values(self):
        res = rectangle.area(49, 13)
        self.assertEqual(637, res)

    def test_area_49_14_values(self):
        res = rectangle.area(49, 14)
        self.assertEqual(686, res)

    def test_area_49_15_values(self):
        res = rectangle.area(49, 15)
        self.assertEqual(735, res)

    def test_area_49_16_values(self):
        res = rectangle.area(49, 16)
        self.assertEqual(784, res)

    def test_area_49_17_values(self):
        res = rectangle.area(49, 17)
        self.assertEqual(833, res)

    def test_area_49_18_values(self):
        res = rectangle.area(49, 18)
        self.assertEqual(882, res)

    def test_area_49_19_values(self):
        res = rectangle.area(49, 19)
        self.assertEqual(931, res)

    def test_area_49_20_values(self):
        res = rectangle.area(49, 20)
        self.assertEqual(980, res)

    def test_area_49_21_values(self):
        res = rectangle.area(49, 21)
        self.assertEqual(1029, res)

    def test_area_49_22_values(self):
        res = rectangle.area(49, 22)
        self.assertEqual(1078, res)

    def test_area_49_23_values(self):
        res = rectangle.area(49, 23)
        self.assertEqual(1127, res)

    def test_area_49_24_values(self):
        res = rectangle.area(49, 24)
        self.assertEqual(1176, res)

    def test_area_49_25_values(self):
        res = rectangle.area(49, 25)
        self.assertEqual(1225, res)

    def test_area_49_26_values(self):
        res = rectangle.area(49, 26)
        self.assertEqual(1274, res)

    def test_area_49_27_values(self):
        res = rectangle.area(49, 27)
        self.assertEqual(1323, res)

    def test_area_49_28_values(self):
        res = rectangle.area(49, 28)
        self.assertEqual(1372, res)

    def test_area_49_29_values(self):
        res = rectangle.area(49, 29)
        self.assertEqual(1421, res)

    def test_area_50_1_values(self):
        res = rectangle.area(50, 1)
        self.assertEqual(50, res)

    def test_area_50_2_values(self):
        res = rectangle.area(50, 2)
        self.assertEqual(100, res)

    def test_area_50_3_values(self):
        res = rectangle.area(50, 3)
        self.assertEqual(150, res)

    def test_area_50_4_values(self):
        res = rectangle.area(50, 4)
        self.assertEqual(200, res)

    def test_area_50_5_values(self):
        res = rectangle.area(50, 5)
        self.assertEqual(250, res)

    def test_area_50_6_values(self):
        res = rectangle.area(50, 6)
        self.assertEqual(300, res)

    def test_area_50_7_values(self):
        res = rectangle.area(50, 7)
        self.assertEqual(350, res)

    def test_area_50_8_values(self):
        res = rectangle.area(50, 8)
        self.assertEqual(400, res)

    def test_area_50_9_values(self):
        res = rectangle.area(50, 9)
        self.assertEqual(450, res)

    def test_area_50_10_values(self):
        res = rectangle.area(50, 10)
        self.assertEqual(500, res)

    def test_area_50_11_values(self):
        res = rectangle.area(50, 11)
        self.assertEqual(550, res)

    def test_area_50_12_values(self):
        res = rectangle.area(50, 12)
        self.assertEqual(600, res)

    def test_area_50_13_values(self):
        res = rectangle.area(50, 13)
        self.assertEqual(650, res)

    def test_area_50_14_values(self):
        res = rectangle.area(50, 14)
        self.assertEqual(700, res)

    def test_area_50_15_values(self):
        res = rectangle.area(50, 15)
        self.assertEqual(750, res)

    def test_area_50_16_values(self):
        res = rectangle.area(50, 16)
        self.assertEqual(800, res)

    def test_area_50_17_values(self):
        res = rectangle.area(50, 17)
        self.assertEqual(850, res)

    def test_area_50_18_values(self):
        res = rectangle.area(50, 18)
        self.assertEqual(900, res)

    def test_area_50_19_values(self):
        res = rectangle.area(50, 19)
        self.assertEqual(950, res)

    def test_area_50_20_values(self):
        res = rectangle.area(50, 20)
        self.assertEqual(1000, res)

    def test_area_50_21_values(self):
        res = rectangle.area(50, 21)
        self.assertEqual(1050, res)

    def test_area_50_22_values(self):
        res = rectangle.area(50, 22)
        self.assertEqual(1100, res)

    def test_area_50_23_values(self):
        res = rectangle.area(50, 23)
        self.assertEqual(1150, res)

    def test_area_50_24_values(self):
        res = rectangle.area(50, 24)
        self.assertEqual(1200, res)

    def test_area_50_25_values(self):
        res = rectangle.area(50, 25)
        self.assertEqual(1250, res)

    def test_area_50_26_values(self):
        res = rectangle.area(50, 26)
        self.assertEqual(1300, res)

    def test_area_50_27_values(self):
        res = rectangle.area(50, 27)
        self.assertEqual(1350, res)

    def test_area_50_28_values(self):
        res = rectangle.area(50, 28)
        self.assertEqual(1400, res)

    def test_area_50_29_values(self):
        res = rectangle.area(50, 29)
        self.assertEqual(1450, res)

    def test_area_51_1_values(self):
        res = rectangle.area(51, 1)
        self.assertEqual(51, res)

    def test_area_51_2_values(self):
        res = rectangle.area(51, 2)
        self.assertEqual(102, res)

    def test_area_51_3_values(self):
        res = rectangle.area(51, 3)
        self.assertEqual(153, res)

    def test_area_51_4_values(self):
        res = rectangle.area(51, 4)
        self.assertEqual(204, res)

    def test_area_51_5_values(self):
        res = rectangle.area(51, 5)
        self.assertEqual(255, res)

    def test_area_51_6_values(self):
        res = rectangle.area(51, 6)
        self.assertEqual(306, res)

    def test_area_51_7_values(self):
        res = rectangle.area(51, 7)
        self.assertEqual(357, res)

    def test_area_51_8_values(self):
        res = rectangle.area(51, 8)
        self.assertEqual(408, res)

    def test_area_51_9_values(self):
        res = rectangle.area(51, 9)
        self.assertEqual(459, res)

    def test_area_51_10_values(self):
        res = rectangle.area(51, 10)
        self.assertEqual(510, res)

    def test_area_51_11_values(self):
        res = rectangle.area(51, 11)
        self.assertEqual(561, res)

    def test_area_51_12_values(self):
        res = rectangle.area(51, 12)
        self.assertEqual(612, res)

    def test_area_51_13_values(self):
        res = rectangle.area(51, 13)
        self.assertEqual(663, res)

    def test_area_51_14_values(self):
        res = rectangle.area(51, 14)
        self.assertEqual(714, res)

    def test_area_51_15_values(self):
        res = rectangle.area(51, 15)
        self.assertEqual(765, res)

    def test_area_51_16_values(self):
        res = rectangle.area(51, 16)
        self.assertEqual(816, res)

    def test_area_51_17_values(self):
        res = rectangle.area(51, 17)
        self.assertEqual(867, res)

    def test_area_51_18_values(self):
        res = rectangle.area(51, 18)
        self.assertEqual(918, res)

    def test_area_51_19_values(self):
        res = rectangle.area(51, 19)
        self.assertEqual(969, res)

    def test_area_51_20_values(self):
        res = rectangle.area(51, 20)
        self.assertEqual(1020, res)

    def test_area_51_21_values(self):
        res = rectangle.area(51, 21)
        self.assertEqual(1071, res)

    def test_area_51_22_values(self):
        res = rectangle.area(51, 22)
        self.assertEqual(1122, res)

    def test_area_51_23_values(self):
        res = rectangle.area(51, 23)
        self.assertEqual(1173, res)

    def test_area_51_24_values(self):
        res = rectangle.area(51, 24)
        self.assertEqual(1224, res)

    def test_area_51_25_values(self):
        res = rectangle.area(51, 25)
        self.assertEqual(1275, res)

    def test_area_51_26_values(self):
        res = rectangle.area(51, 26)
        self.assertEqual(1326, res)

    def test_area_51_27_values(self):
        res = rectangle.area(51, 27)
        self.assertEqual(1377, res)

    def test_area_51_28_values(self):
        res = rectangle.area(51, 28)
        self.assertEqual(1428, res)

    def test_area_51_29_values(self):
        res = rectangle.area(51, 29)
        self.assertEqual(1479, res)

    def test_area_52_1_values(self):
        res = rectangle.area(52, 1)
        self.assertEqual(52, res)

    def test_area_52_2_values(self):
        res = rectangle.area(52, 2)
        self.assertEqual(104, res)

    def test_area_52_3_values(self):
        res = rectangle.area(52, 3)
        self.assertEqual(156, res)

    def test_area_52_4_values(self):
        res = rectangle.area(52, 4)
        self.assertEqual(208, res)

    def test_area_52_5_values(self):
        res = rectangle.area(52, 5)
        self.assertEqual(260, res)

    def test_area_52_6_values(self):
        res = rectangle.area(52, 6)
        self.assertEqual(312, res)

    def test_area_52_7_values(self):
        res = rectangle.area(52, 7)
        self.assertEqual(364, res)

    def test_area_52_8_values(self):
        res = rectangle.area(52, 8)
        self.assertEqual(416, res)

    def test_area_52_9_values(self):
        res = rectangle.area(52, 9)
        self.assertEqual(468, res)

    def test_area_52_10_values(self):
        res = rectangle.area(52, 10)
        self.assertEqual(520, res)

    def test_area_52_11_values(self):
        res = rectangle.area(52, 11)
        self.assertEqual(572, res)

    def test_area_52_12_values(self):
        res = rectangle.area(52, 12)
        self.assertEqual(624, res)

    def test_area_52_13_values(self):
        res = rectangle.area(52, 13)
        self.assertEqual(676, res)

    def test_area_52_14_values(self):
        res = rectangle.area(52, 14)
        self.assertEqual(728, res)

    def test_area_52_15_values(self):
        res = rectangle.area(52, 15)
        self.assertEqual(780, res)

    def test_area_52_16_values(self):
        res = rectangle.area(52, 16)
        self.assertEqual(832, res)

    def test_area_52_17_values(self):
        res = rectangle.area(52, 17)
        self.assertEqual(884, res)

    def test_area_52_18_values(self):
        res = rectangle.area(52, 18)
        self.assertEqual(936, res)

    def test_area_52_19_values(self):
        res = rectangle.area(52, 19)
        self.assertEqual(988, res)

    def test_area_52_20_values(self):
        res = rectangle.area(52, 20)
        self.assertEqual(1040, res)

    def test_area_52_21_values(self):
        res = rectangle.area(52, 21)
        self.assertEqual(1092, res)

    def test_area_52_22_values(self):
        res = rectangle.area(52, 22)
        self.assertEqual(1144, res)

    def test_area_52_23_values(self):
        res = rectangle.area(52, 23)
        self.assertEqual(1196, res)

    def test_area_52_24_values(self):
        res = rectangle.area(52, 24)
        self.assertEqual(1248, res)

    def test_area_52_25_values(self):
        res = rectangle.area(52, 25)
        self.assertEqual(1300, res)

    def test_area_52_26_values(self):
        res = rectangle.area(52, 26)
        self.assertEqual(1352, res)

    def test_area_52_27_values(self):
        res = rectangle.area(52, 27)
        self.assertEqual(1404, res)

    def test_area_52_28_values(self):
        res = rectangle.area(52, 28)
        self.assertEqual(1456, res)

    def test_area_52_29_values(self):
        res = rectangle.area(52, 29)
        self.assertEqual(1508, res)

    def test_area_53_1_values(self):
        res = rectangle.area(53, 1)
        self.assertEqual(53, res)

    def test_area_53_2_values(self):
        res = rectangle.area(53, 2)
        self.assertEqual(106, res)

    def test_area_53_3_values(self):
        res = rectangle.area(53, 3)
        self.assertEqual(159, res)

    def test_area_53_4_values(self):
        res = rectangle.area(53, 4)
        self.assertEqual(212, res)

    def test_area_53_5_values(self):
        res = rectangle.area(53, 5)
        self.assertEqual(265, res)

    def test_area_53_6_values(self):
        res = rectangle.area(53, 6)
        self.assertEqual(318, res)

    def test_area_53_7_values(self):
        res = rectangle.area(53, 7)
        self.assertEqual(371, res)

    def test_area_53_8_values(self):
        res = rectangle.area(53, 8)
        self.assertEqual(424, res)

    def test_area_53_9_values(self):
        res = rectangle.area(53, 9)
        self.assertEqual(477, res)

    def test_area_53_10_values(self):
        res = rectangle.area(53, 10)
        self.assertEqual(530, res)

    def test_area_53_11_values(self):
        res = rectangle.area(53, 11)
        self.assertEqual(583, res)

    def test_area_53_12_values(self):
        res = rectangle.area(53, 12)
        self.assertEqual(636, res)

    def test_area_53_13_values(self):
        res = rectangle.area(53, 13)
        self.assertEqual(689, res)

    def test_area_53_14_values(self):
        res = rectangle.area(53, 14)
        self.assertEqual(742, res)

    def test_area_53_15_values(self):
        res = rectangle.area(53, 15)
        self.assertEqual(795, res)

    def test_area_53_16_values(self):
        res = rectangle.area(53, 16)
        self.assertEqual(848, res)

    def test_area_53_17_values(self):
        res = rectangle.area(53, 17)
        self.assertEqual(901, res)

    def test_area_53_18_values(self):
        res = rectangle.area(53, 18)
        self.assertEqual(954, res)

    def test_area_53_19_values(self):
        res = rectangle.area(53, 19)
        self.assertEqual(1007, res)

    def test_area_53_20_values(self):
        res = rectangle.area(53, 20)
        self.assertEqual(1060, res)

    def test_area_53_21_values(self):
        res = rectangle.area(53, 21)
        self.assertEqual(1113, res)

    def test_area_53_22_values(self):
        res = rectangle.area(53, 22)
        self.assertEqual(1166, res)

    def test_area_53_23_values(self):
        res = rectangle.area(53, 23)
        self.assertEqual(1219, res)

    def test_area_53_24_values(self):
        res = rectangle.area(53, 24)
        self.assertEqual(1272, res)

    def test_area_53_25_values(self):
        res = rectangle.area(53, 25)
        self.assertEqual(1325, res)

    def test_area_53_26_values(self):
        res = rectangle.area(53, 26)
        self.assertEqual(1378, res)

    def test_area_53_27_values(self):
        res = rectangle.area(53, 27)
        self.assertEqual(1431, res)

    def test_area_53_28_values(self):
        res = rectangle.area(53, 28)
        self.assertEqual(1484, res)

    def test_area_53_29_values(self):
        res = rectangle.area(53, 29)
        self.assertEqual(1537, res)

    def test_area_54_1_values(self):
        res = rectangle.area(54, 1)
        self.assertEqual(54, res)

    def test_area_54_2_values(self):
        res = rectangle.area(54, 2)
        self.assertEqual(108, res)

    def test_area_54_3_values(self):
        res = rectangle.area(54, 3)
        self.assertEqual(162, res)

    def test_area_54_4_values(self):
        res = rectangle.area(54, 4)
        self.assertEqual(216, res)

    def test_area_54_5_values(self):
        res = rectangle.area(54, 5)
        self.assertEqual(270, res)

    def test_area_54_6_values(self):
        res = rectangle.area(54, 6)
        self.assertEqual(324, res)

    def test_area_54_7_values(self):
        res = rectangle.area(54, 7)
        self.assertEqual(378, res)

    def test_area_54_8_values(self):
        res = rectangle.area(54, 8)
        self.assertEqual(432, res)

    def test_area_54_9_values(self):
        res = rectangle.area(54, 9)
        self.assertEqual(486, res)

    def test_area_54_10_values(self):
        res = rectangle.area(54, 10)
        self.assertEqual(540, res)

    def test_area_54_11_values(self):
        res = rectangle.area(54, 11)
        self.assertEqual(594, res)

    def test_area_54_12_values(self):
        res = rectangle.area(54, 12)
        self.assertEqual(648, res)

    def test_area_54_13_values(self):
        res = rectangle.area(54, 13)
        self.assertEqual(702, res)

    def test_area_54_14_values(self):
        res = rectangle.area(54, 14)
        self.assertEqual(756, res)

    def test_area_54_15_values(self):
        res = rectangle.area(54, 15)
        self.assertEqual(810, res)

    def test_area_54_16_values(self):
        res = rectangle.area(54, 16)
        self.assertEqual(864, res)

    def test_area_54_17_values(self):
        res = rectangle.area(54, 17)
        self.assertEqual(918, res)

    def test_area_54_18_values(self):
        res = rectangle.area(54, 18)
        self.assertEqual(972, res)

    def test_area_54_19_values(self):
        res = rectangle.area(54, 19)
        self.assertEqual(1026, res)

    def test_area_54_20_values(self):
        res = rectangle.area(54, 20)
        self.assertEqual(1080, res)

    def test_area_54_21_values(self):
        res = rectangle.area(54, 21)
        self.assertEqual(1134, res)

    def test_area_54_22_values(self):
        res = rectangle.area(54, 22)
        self.assertEqual(1188, res)

    def test_area_54_23_values(self):
        res = rectangle.area(54, 23)
        self.assertEqual(1242, res)

    def test_area_54_24_values(self):
        res = rectangle.area(54, 24)
        self.assertEqual(1296, res)

    def test_area_54_25_values(self):
        res = rectangle.area(54, 25)
        self.assertEqual(1350, res)

    def test_area_54_26_values(self):
        res = rectangle.area(54, 26)
        self.assertEqual(1404, res)

    def test_area_54_27_values(self):
        res = rectangle.area(54, 27)
        self.assertEqual(1458, res)

    def test_area_54_28_values(self):
        res = rectangle.area(54, 28)
        self.assertEqual(1512, res)

    def test_area_54_29_values(self):
        res = rectangle.area(54, 29)
        self.assertEqual(1566, res)

    def test_area_55_1_values(self):
        res = rectangle.area(55, 1)
        self.assertEqual(55, res)

    def test_area_55_2_values(self):
        res = rectangle.area(55, 2)
        self.assertEqual(110, res)

    def test_area_55_3_values(self):
        res = rectangle.area(55, 3)
        self.assertEqual(165, res)

    def test_area_55_4_values(self):
        res = rectangle.area(55, 4)
        self.assertEqual(220, res)

    def test_area_55_5_values(self):
        res = rectangle.area(55, 5)
        self.assertEqual(275, res)

    def test_area_55_6_values(self):
        res = rectangle.area(55, 6)
        self.assertEqual(330, res)

    def test_area_55_7_values(self):
        res = rectangle.area(55, 7)
        self.assertEqual(385, res)

    def test_area_55_8_values(self):
        res = rectangle.area(55, 8)
        self.assertEqual(440, res)

    def test_area_55_9_values(self):
        res = rectangle.area(55, 9)
        self.assertEqual(495, res)

    def test_area_55_10_values(self):
        res = rectangle.area(55, 10)
        self.assertEqual(550, res)

    def test_area_55_11_values(self):
        res = rectangle.area(55, 11)
        self.assertEqual(605, res)

    def test_area_55_12_values(self):
        res = rectangle.area(55, 12)
        self.assertEqual(660, res)

    def test_area_55_13_values(self):
        res = rectangle.area(55, 13)
        self.assertEqual(715, res)

    def test_area_55_14_values(self):
        res = rectangle.area(55, 14)
        self.assertEqual(770, res)

    def test_area_55_15_values(self):
        res = rectangle.area(55, 15)
        self.assertEqual(825, res)

    def test_area_55_16_values(self):
        res = rectangle.area(55, 16)
        self.assertEqual(880, res)

    def test_area_55_17_values(self):
        res = rectangle.area(55, 17)
        self.assertEqual(935, res)

    def test_area_55_18_values(self):
        res = rectangle.area(55, 18)
        self.assertEqual(990, res)

    def test_area_55_19_values(self):
        res = rectangle.area(55, 19)
        self.assertEqual(1045, res)

    def test_area_55_20_values(self):
        res = rectangle.area(55, 20)
        self.assertEqual(1100, res)

    def test_area_55_21_values(self):
        res = rectangle.area(55, 21)
        self.assertEqual(1155, res)

    def test_area_55_22_values(self):
        res = rectangle.area(55, 22)
        self.assertEqual(1210, res)

    def test_area_55_23_values(self):
        res = rectangle.area(55, 23)
        self.assertEqual(1265, res)

    def test_area_55_24_values(self):
        res = rectangle.area(55, 24)
        self.assertEqual(1320, res)

    def test_area_55_25_values(self):
        res = rectangle.area(55, 25)
        self.assertEqual(1375, res)

    def test_area_55_26_values(self):
        res = rectangle.area(55, 26)
        self.assertEqual(1430, res)

    def test_area_55_27_values(self):
        res = rectangle.area(55, 27)
        self.assertEqual(1485, res)

    def test_area_55_28_values(self):
        res = rectangle.area(55, 28)
        self.assertEqual(1540, res)

    def test_area_55_29_values(self):
        res = rectangle.area(55, 29)
        self.assertEqual(1595, res)

    def test_area_56_1_values(self):
        res = rectangle.area(56, 1)
        self.assertEqual(56, res)

    def test_area_56_2_values(self):
        res = rectangle.area(56, 2)
        self.assertEqual(112, res)

    def test_area_56_3_values(self):
        res = rectangle.area(56, 3)
        self.assertEqual(168, res)

    def test_area_56_4_values(self):
        res = rectangle.area(56, 4)
        self.assertEqual(224, res)

    def test_area_56_5_values(self):
        res = rectangle.area(56, 5)
        self.assertEqual(280, res)

    def test_area_56_6_values(self):
        res = rectangle.area(56, 6)
        self.assertEqual(336, res)

    def test_area_56_7_values(self):
        res = rectangle.area(56, 7)
        self.assertEqual(392, res)

    def test_area_56_8_values(self):
        res = rectangle.area(56, 8)
        self.assertEqual(448, res)

    def test_area_56_9_values(self):
        res = rectangle.area(56, 9)
        self.assertEqual(504, res)

    def test_area_56_10_values(self):
        res = rectangle.area(56, 10)
        self.assertEqual(560, res)

    def test_area_56_11_values(self):
        res = rectangle.area(56, 11)
        self.assertEqual(616, res)

    def test_area_56_12_values(self):
        res = rectangle.area(56, 12)
        self.assertEqual(672, res)

    def test_area_56_13_values(self):
        res = rectangle.area(56, 13)
        self.assertEqual(728, res)

    def test_area_56_14_values(self):
        res = rectangle.area(56, 14)
        self.assertEqual(784, res)

    def test_area_56_15_values(self):
        res = rectangle.area(56, 15)
        self.assertEqual(840, res)

    def test_area_56_16_values(self):
        res = rectangle.area(56, 16)
        self.assertEqual(896, res)

    def test_area_56_17_values(self):
        res = rectangle.area(56, 17)
        self.assertEqual(952, res)

    def test_area_56_18_values(self):
        res = rectangle.area(56, 18)
        self.assertEqual(1008, res)

    def test_area_56_19_values(self):
        res = rectangle.area(56, 19)
        self.assertEqual(1064, res)

    def test_area_56_20_values(self):
        res = rectangle.area(56, 20)
        self.assertEqual(1120, res)

    def test_area_56_21_values(self):
        res = rectangle.area(56, 21)
        self.assertEqual(1176, res)

    def test_area_56_22_values(self):
        res = rectangle.area(56, 22)
        self.assertEqual(1232, res)

    def test_area_56_23_values(self):
        res = rectangle.area(56, 23)
        self.assertEqual(1288, res)

    def test_area_56_24_values(self):
        res = rectangle.area(56, 24)
        self.assertEqual(1344, res)

    def test_area_56_25_values(self):
        res = rectangle.area(56, 25)
        self.assertEqual(1400, res)

    def test_area_56_26_values(self):
        res = rectangle.area(56, 26)
        self.assertEqual(1456, res)

    def test_area_56_27_values(self):
        res = rectangle.area(56, 27)
        self.assertEqual(1512, res)

    def test_area_56_28_values(self):
        res = rectangle.area(56, 28)
        self.assertEqual(1568, res)

    def test_area_56_29_values(self):
        res = rectangle.area(56, 29)
        self.assertEqual(1624, res)

    def test_area_57_1_values(self):
        res = rectangle.area(57, 1)
        self.assertEqual(57, res)

    def test_area_57_2_values(self):
        res = rectangle.area(57, 2)
        self.assertEqual(114, res)

    def test_area_57_3_values(self):
        res = rectangle.area(57, 3)
        self.assertEqual(171, res)

    def test_area_57_4_values(self):
        res = rectangle.area(57, 4)
        self.assertEqual(228, res)

    def test_area_57_5_values(self):
        res = rectangle.area(57, 5)
        self.assertEqual(285, res)

    def test_area_57_6_values(self):
        res = rectangle.area(57, 6)
        self.assertEqual(342, res)

    def test_area_57_7_values(self):
        res = rectangle.area(57, 7)
        self.assertEqual(399, res)

    def test_area_57_8_values(self):
        res = rectangle.area(57, 8)
        self.assertEqual(456, res)

    def test_area_57_9_values(self):
        res = rectangle.area(57, 9)
        self.assertEqual(513, res)

    def test_area_57_10_values(self):
        res = rectangle.area(57, 10)
        self.assertEqual(570, res)

    def test_area_57_11_values(self):
        res = rectangle.area(57, 11)
        self.assertEqual(627, res)

    def test_area_57_12_values(self):
        res = rectangle.area(57, 12)
        self.assertEqual(684, res)

    def test_area_57_13_values(self):
        res = rectangle.area(57, 13)
        self.assertEqual(741, res)

    def test_area_57_14_values(self):
        res = rectangle.area(57, 14)
        self.assertEqual(798, res)

    def test_area_57_15_values(self):
        res = rectangle.area(57, 15)
        self.assertEqual(855, res)

    def test_area_57_16_values(self):
        res = rectangle.area(57, 16)
        self.assertEqual(912, res)

    def test_area_57_17_values(self):
        res = rectangle.area(57, 17)
        self.assertEqual(969, res)

    def test_area_57_18_values(self):
        res = rectangle.area(57, 18)
        self.assertEqual(1026, res)

    def test_area_57_19_values(self):
        res = rectangle.area(57, 19)
        self.assertEqual(1083, res)

    def test_area_57_20_values(self):
        res = rectangle.area(57, 20)
        self.assertEqual(1140, res)

    def test_area_57_21_values(self):
        res = rectangle.area(57, 21)
        self.assertEqual(1197, res)

    def test_area_57_22_values(self):
        res = rectangle.area(57, 22)
        self.assertEqual(1254, res)

    def test_area_57_23_values(self):
        res = rectangle.area(57, 23)
        self.assertEqual(1311, res)

    def test_area_57_24_values(self):
        res = rectangle.area(57, 24)
        self.assertEqual(1368, res)

    def test_area_57_25_values(self):
        res = rectangle.area(57, 25)
        self.assertEqual(1425, res)

    def test_area_57_26_values(self):
        res = rectangle.area(57, 26)
        self.assertEqual(1482, res)

    def test_area_57_27_values(self):
        res = rectangle.area(57, 27)
        self.assertEqual(1539, res)

    def test_area_57_28_values(self):
        res = rectangle.area(57, 28)
        self.assertEqual(1596, res)

    def test_area_57_29_values(self):
        res = rectangle.area(57, 29)
        self.assertEqual(1653, res)

    def test_area_58_1_values(self):
        res = rectangle.area(58, 1)
        self.assertEqual(58, res)

    def test_area_58_2_values(self):
        res = rectangle.area(58, 2)
        self.assertEqual(116, res)

    def test_area_58_3_values(self):
        res = rectangle.area(58, 3)
        self.assertEqual(174, res)

    def test_area_58_4_values(self):
        res = rectangle.area(58, 4)
        self.assertEqual(232, res)

    def test_area_58_5_values(self):
        res = rectangle.area(58, 5)
        self.assertEqual(290, res)

    def test_area_58_6_values(self):
        res = rectangle.area(58, 6)
        self.assertEqual(348, res)

    def test_area_58_7_values(self):
        res = rectangle.area(58, 7)
        self.assertEqual(406, res)

    def test_area_58_8_values(self):
        res = rectangle.area(58, 8)
        self.assertEqual(464, res)

    def test_area_58_9_values(self):
        res = rectangle.area(58, 9)
        self.assertEqual(522, res)

    def test_area_58_10_values(self):
        res = rectangle.area(58, 10)
        self.assertEqual(580, res)

    def test_area_58_11_values(self):
        res = rectangle.area(58, 11)
        self.assertEqual(638, res)

    def test_area_58_12_values(self):
        res = rectangle.area(58, 12)
        self.assertEqual(696, res)

    def test_area_58_13_values(self):
        res = rectangle.area(58, 13)
        self.assertEqual(754, res)

    def test_area_58_14_values(self):
        res = rectangle.area(58, 14)
        self.assertEqual(812, res)

    def test_area_58_15_values(self):
        res = rectangle.area(58, 15)
        self.assertEqual(870, res)

    def test_area_58_16_values(self):
        res = rectangle.area(58, 16)
        self.assertEqual(928, res)

    def test_area_58_17_values(self):
        res = rectangle.area(58, 17)
        self.assertEqual(986, res)

    def test_area_58_18_values(self):
        res = rectangle.area(58, 18)
        self.assertEqual(1044, res)

    def test_area_58_19_values(self):
        res = rectangle.area(58, 19)
        self.assertEqual(1102, res)

    def test_area_58_20_values(self):
        res = rectangle.area(58, 20)
        self.assertEqual(1160, res)

    def test_area_58_21_values(self):
        res = rectangle.area(58, 21)
        self.assertEqual(1218, res)

    def test_area_58_22_values(self):
        res = rectangle.area(58, 22)
        self.assertEqual(1276, res)

    def test_area_58_23_values(self):
        res = rectangle.area(58, 23)
        self.assertEqual(1334, res)

    def test_area_58_24_values(self):
        res = rectangle.area(58, 24)
        self.assertEqual(1392, res)

    def test_area_58_25_values(self):
        res = rectangle.area(58, 25)
        self.assertEqual(1450, res)

    def test_area_58_26_values(self):
        res = rectangle.area(58, 26)
        self.assertEqual(1508, res)

    def test_area_58_27_values(self):
        res = rectangle.area(58, 27)
        self.assertEqual(1566, res)

    def test_area_58_28_values(self):
        res = rectangle.area(58, 28)
        self.assertEqual(1624, res)

    def test_area_58_29_values(self):
        res = rectangle.area(58, 29)
        self.assertEqual(1682, res)

    def test_area_59_1_values(self):
        res = rectangle.area(59, 1)
        self.assertEqual(59, res)

    def test_area_59_2_values(self):
        res = rectangle.area(59, 2)
        self.assertEqual(118, res)

    def test_area_59_3_values(self):
        res = rectangle.area(59, 3)
        self.assertEqual(177, res)

    def test_area_59_4_values(self):
        res = rectangle.area(59, 4)
        self.assertEqual(236, res)

    def test_area_59_5_values(self):
        res = rectangle.area(59, 5)
        self.assertEqual(295, res)

    def test_area_59_6_values(self):
        res = rectangle.area(59, 6)
        self.assertEqual(354, res)

    def test_area_59_7_values(self):
        res = rectangle.area(59, 7)
        self.assertEqual(413, res)

    def test_area_59_8_values(self):
        res = rectangle.area(59, 8)
        self.assertEqual(472, res)

    def test_area_59_9_values(self):
        res = rectangle.area(59, 9)
        self.assertEqual(531, res)

    def test_area_59_10_values(self):
        res = rectangle.area(59, 10)
        self.assertEqual(590, res)

    def test_area_59_11_values(self):
        res = rectangle.area(59, 11)
        self.assertEqual(649, res)

    def test_area_59_12_values(self):
        res = rectangle.area(59, 12)
        self.assertEqual(708, res)

    def test_area_59_13_values(self):
        res = rectangle.area(59, 13)
        self.assertEqual(767, res)

    def test_area_59_14_values(self):
        res = rectangle.area(59, 14)
        self.assertEqual(826, res)

    def test_area_59_15_values(self):
        res = rectangle.area(59, 15)
        self.assertEqual(885, res)

    def test_area_59_16_values(self):
        res = rectangle.area(59, 16)
        self.assertEqual(944, res)

    def test_area_59_17_values(self):
        res = rectangle.area(59, 17)
        self.assertEqual(1003, res)

    def test_area_59_18_values(self):
        res = rectangle.area(59, 18)
        self.assertEqual(1062, res)

    def test_area_59_19_values(self):
        res = rectangle.area(59, 19)
        self.assertEqual(1121, res)

    def test_area_59_20_values(self):
        res = rectangle.area(59, 20)
        self.assertEqual(1180, res)

    def test_area_59_21_values(self):
        res = rectangle.area(59, 21)
        self.assertEqual(1239, res)

    def test_area_59_22_values(self):
        res = rectangle.area(59, 22)
        self.assertEqual(1298, res)

    def test_area_59_23_values(self):
        res = rectangle.area(59, 23)
        self.assertEqual(1357, res)

    def test_area_59_24_values(self):
        res = rectangle.area(59, 24)
        self.assertEqual(1416, res)

    def test_area_59_25_values(self):
        res = rectangle.area(59, 25)
        self.assertEqual(1475, res)

    def test_area_59_26_values(self):
        res = rectangle.area(59, 26)
        self.assertEqual(1534, res)

    def test_area_59_27_values(self):
        res = rectangle.area(59, 27)
        self.assertEqual(1593, res)

    def test_area_59_28_values(self):
        res = rectangle.area(59, 28)
        self.assertEqual(1652, res)

    def test_area_59_29_values(self):
        res = rectangle.area(59, 29)
        self.assertEqual(1711, res)

    def test_area_1_30_values(self):
        res = rectangle.area(1, 30)
        self.assertEqual(30, res)

    def test_area_1_31_values(self):
        res = rectangle.area(1, 31)
        self.assertEqual(31, res)

    def test_area_1_32_values(self):
        res = rectangle.area(1, 32)
        self.assertEqual(32, res)

    def test_area_1_33_values(self):
        res = rectangle.area(1, 33)
        self.assertEqual(33, res)

    def test_area_1_34_values(self):
        res = rectangle.area(1, 34)
        self.assertEqual(34, res)

    def test_area_1_35_values(self):
        res = rectangle.area(1, 35)
        self.assertEqual(35, res)

    def test_area_1_36_values(self):
        res = rectangle.area(1, 36)
        self.assertEqual(36, res)

    def test_area_1_37_values(self):
        res = rectangle.area(1, 37)
        self.assertEqual(37, res)

    def test_area_1_38_values(self):
        res = rectangle.area(1, 38)
        self.assertEqual(38, res)

    def test_area_1_39_values(self):
        res = rectangle.area(1, 39)
        self.assertEqual(39, res)

    def test_area_1_40_values(self):
        res = rectangle.area(1, 40)
        self.assertEqual(40, res)

    def test_area_1_41_values(self):
        res = rectangle.area(1, 41)
        self.assertEqual(41, res)

    def test_area_1_42_values(self):
        res = rectangle.area(1, 42)
        self.assertEqual(42, res)

    def test_area_1_43_values(self):
        res = rectangle.area(1, 43)
        self.assertEqual(43, res)

    def test_area_1_44_values(self):
        res = rectangle.area(1, 44)
        self.assertEqual(44, res)

    def test_area_1_45_values(self):
        res = rectangle.area(1, 45)
        self.assertEqual(45, res)

    def test_area_1_46_values(self):
        res = rectangle.area(1, 46)
        self.assertEqual(46, res)

    def test_area_1_47_values(self):
        res = rectangle.area(1, 47)
        self.assertEqual(47, res)

    def test_area_1_48_values(self):
        res = rectangle.area(1, 48)
        self.assertEqual(48, res)

    def test_area_1_49_values(self):
        res = rectangle.area(1, 49)
        self.assertEqual(49, res)

    def test_area_1_50_values(self):
        res = rectangle.area(1, 50)
        self.assertEqual(50, res)

    def test_area_1_51_values(self):
        res = rectangle.area(1, 51)
        self.assertEqual(51, res)

    def test_area_1_52_values(self):
        res = rectangle.area(1, 52)
        self.assertEqual(52, res)

    def test_area_1_53_values(self):
        res = rectangle.area(1, 53)
        self.assertEqual(53, res)

    def test_area_1_54_values(self):
        res = rectangle.area(1, 54)
        self.assertEqual(54, res)

    def test_area_1_55_values(self):
        res = rectangle.area(1, 55)
        self.assertEqual(55, res)

    def test_area_1_56_values(self):
        res = rectangle.area(1, 56)
        self.assertEqual(56, res)

    def test_area_1_57_values(self):
        res = rectangle.area(1, 57)
        self.assertEqual(57, res)

    def test_area_1_58_values(self):
        res = rectangle.area(1, 58)
        self.assertEqual(58, res)

    def test_area_1_59_values(self):
        res = rectangle.area(1, 59)
        self.assertEqual(59, res)

    def test_area_2_30_values(self):
        res = rectangle.area(2, 30)
        self.assertEqual(60, res)

    def test_area_2_31_values(self):
        res = rectangle.area(2, 31)
        self.assertEqual(62, res)

    def test_area_2_32_values(self):
        res = rectangle.area(2, 32)
        self.assertEqual(64, res)

    def test_area_2_33_values(self):
        res = rectangle.area(2, 33)
        self.assertEqual(66, res)

    def test_area_2_34_values(self):
        res = rectangle.area(2, 34)
        self.assertEqual(68, res)

    def test_area_2_35_values(self):
        res = rectangle.area(2, 35)
        self.assertEqual(70, res)

    def test_area_2_36_values(self):
        res = rectangle.area(2, 36)
        self.assertEqual(72, res)

    def test_area_2_37_values(self):
        res = rectangle.area(2, 37)
        self.assertEqual(74, res)

    def test_area_2_38_values(self):
        res = rectangle.area(2, 38)
        self.assertEqual(76, res)

    def test_area_2_39_values(self):
        res = rectangle.area(2, 39)
        self.assertEqual(78, res)

    def test_area_2_40_values(self):
        res = rectangle.area(2, 40)
        self.assertEqual(80, res)

    def test_area_2_41_values(self):
        res = rectangle.area(2, 41)
        self.assertEqual(82, res)

    def test_area_2_42_values(self):
        res = rectangle.area(2, 42)
        self.assertEqual(84, res)

    def test_area_2_43_values(self):
        res = rectangle.area(2, 43)
        self.assertEqual(86, res)

    def test_area_2_44_values(self):
        res = rectangle.area(2, 44)
        self.assertEqual(88, res)

    def test_area_2_45_values(self):
        res = rectangle.area(2, 45)
        self.assertEqual(90, res)

    def test_area_2_46_values(self):
        res = rectangle.area(2, 46)
        self.assertEqual(92, res)

    def test_area_2_47_values(self):
        res = rectangle.area(2, 47)
        self.assertEqual(94, res)

    def test_area_2_48_values(self):
        res = rectangle.area(2, 48)
        self.assertEqual(96, res)

    def test_area_2_49_values(self):
        res = rectangle.area(2, 49)
        self.assertEqual(98, res)

    def test_area_2_50_values(self):
        res = rectangle.area(2, 50)
        self.assertEqual(100, res)

    def test_area_2_51_values(self):
        res = rectangle.area(2, 51)
        self.assertEqual(102, res)

    def test_area_2_52_values(self):
        res = rectangle.area(2, 52)
        self.assertEqual(104, res)

    def test_area_2_53_values(self):
        res = rectangle.area(2, 53)
        self.assertEqual(106, res)

    def test_area_2_54_values(self):
        res = rectangle.area(2, 54)
        self.assertEqual(108, res)

    def test_area_2_55_values(self):
        res = rectangle.area(2, 55)
        self.assertEqual(110, res)

    def test_area_2_56_values(self):
        res = rectangle.area(2, 56)
        self.assertEqual(112, res)

    def test_area_2_57_values(self):
        res = rectangle.area(2, 57)
        self.assertEqual(114, res)

    def test_area_2_58_values(self):
        res = rectangle.area(2, 58)
        self.assertEqual(116, res)

    def test_area_2_59_values(self):
        res = rectangle.area(2, 59)
        self.assertEqual(118, res)

    def test_area_3_30_values(self):
        res = rectangle.area(3, 30)
        self.assertEqual(90, res)

    def test_area_3_31_values(self):
        res = rectangle.area(3, 31)
        self.assertEqual(93, res)

    def test_area_3_32_values(self):
        res = rectangle.area(3, 32)
        self.assertEqual(96, res)

    def test_area_3_33_values(self):
        res = rectangle.area(3, 33)
        self.assertEqual(99, res)

    def test_area_3_34_values(self):
        res = rectangle.area(3, 34)
        self.assertEqual(102, res)

    def test_area_3_35_values(self):
        res = rectangle.area(3, 35)
        self.assertEqual(105, res)

    def test_area_3_36_values(self):
        res = rectangle.area(3, 36)
        self.assertEqual(108, res)

    def test_area_3_37_values(self):
        res = rectangle.area(3, 37)
        self.assertEqual(111, res)

    def test_area_3_38_values(self):
        res = rectangle.area(3, 38)
        self.assertEqual(114, res)

    def test_area_3_39_values(self):
        res = rectangle.area(3, 39)
        self.assertEqual(117, res)

    def test_area_3_40_values(self):
        res = rectangle.area(3, 40)
        self.assertEqual(120, res)

    def test_area_3_41_values(self):
        res = rectangle.area(3, 41)
        self.assertEqual(123, res)

    def test_area_3_42_values(self):
        res = rectangle.area(3, 42)
        self.assertEqual(126, res)

    def test_area_3_43_values(self):
        res = rectangle.area(3, 43)
        self.assertEqual(129, res)

    def test_area_3_44_values(self):
        res = rectangle.area(3, 44)
        self.assertEqual(132, res)

    def test_area_3_45_values(self):
        res = rectangle.area(3, 45)
        self.assertEqual(135, res)

    def test_area_3_46_values(self):
        res = rectangle.area(3, 46)
        self.assertEqual(138, res)

    def test_area_3_47_values(self):
        res = rectangle.area(3, 47)
        self.assertEqual(141, res)

    def test_area_3_48_values(self):
        res = rectangle.area(3, 48)
        self.assertEqual(144, res)

    def test_area_3_49_values(self):
        res = rectangle.area(3, 49)
        self.assertEqual(147, res)

    def test_area_3_50_values(self):
        res = rectangle.area(3, 50)
        self.assertEqual(150, res)

    def test_area_3_51_values(self):
        res = rectangle.area(3, 51)
        self.assertEqual(153, res)

    def test_area_3_52_values(self):
        res = rectangle.area(3, 52)
        self.assertEqual(156, res)

    def test_area_3_53_values(self):
        res = rectangle.area(3, 53)
        self.assertEqual(159, res)

    def test_area_3_54_values(self):
        res = rectangle.area(3, 54)
        self.assertEqual(162, res)

    def test_area_3_55_values(self):
        res = rectangle.area(3, 55)
        self.assertEqual(165, res)

    def test_area_3_56_values(self):
        res = rectangle.area(3, 56)
        self.assertEqual(168, res)

    def test_area_3_57_values(self):
        res = rectangle.area(3, 57)
        self.assertEqual(171, res)

    def test_area_3_58_values(self):
        res = rectangle.area(3, 58)
        self.assertEqual(174, res)

    def test_area_3_59_values(self):
        res = rectangle.area(3, 59)
        self.assertEqual(177, res)

    def test_area_4_30_values(self):
        res = rectangle.area(4, 30)
        self.assertEqual(120, res)

    def test_area_4_31_values(self):
        res = rectangle.area(4, 31)
        self.assertEqual(124, res)

    def test_area_4_32_values(self):
        res = rectangle.area(4, 32)
        self.assertEqual(128, res)

    def test_area_4_33_values(self):
        res = rectangle.area(4, 33)
        self.assertEqual(132, res)

    def test_area_4_34_values(self):
        res = rectangle.area(4, 34)
        self.assertEqual(136, res)

    def test_area_4_35_values(self):
        res = rectangle.area(4, 35)
        self.assertEqual(140, res)

    def test_area_4_36_values(self):
        res = rectangle.area(4, 36)
        self.assertEqual(144, res)

    def test_area_4_37_values(self):
        res = rectangle.area(4, 37)
        self.assertEqual(148, res)

    def test_area_4_38_values(self):
        res = rectangle.area(4, 38)
        self.assertEqual(152, res)

    def test_area_4_39_values(self):
        res = rectangle.area(4, 39)
        self.assertEqual(156, res)

    def test_area_4_40_values(self):
        res = rectangle.area(4, 40)
        self.assertEqual(160, res)

    def test_area_4_41_values(self):
        res = rectangle.area(4, 41)
        self.assertEqual(164, res)

    def test_area_4_42_values(self):
        res = rectangle.area(4, 42)
        self.assertEqual(168, res)

    def test_area_4_43_values(self):
        res = rectangle.area(4, 43)
        self.assertEqual(172, res)

    def test_area_4_44_values(self):
        res = rectangle.area(4, 44)
        self.assertEqual(176, res)

    def test_area_4_45_values(self):
        res = rectangle.area(4, 45)
        self.assertEqual(180, res)

    def test_area_4_46_values(self):
        res = rectangle.area(4, 46)
        self.assertEqual(184, res)

    def test_area_4_47_values(self):
        res = rectangle.area(4, 47)
        self.assertEqual(188, res)

    def test_area_4_48_values(self):
        res = rectangle.area(4, 48)
        self.assertEqual(192, res)

    def test_area_4_49_values(self):
        res = rectangle.area(4, 49)
        self.assertEqual(196, res)

    def test_area_4_50_values(self):
        res = rectangle.area(4, 50)
        self.assertEqual(200, res)

    def test_area_4_51_values(self):
        res = rectangle.area(4, 51)
        self.assertEqual(204, res)

    def test_area_4_52_values(self):
        res = rectangle.area(4, 52)
        self.assertEqual(208, res)

    def test_area_4_53_values(self):
        res = rectangle.area(4, 53)
        self.assertEqual(212, res)

    def test_area_4_54_values(self):
        res = rectangle.area(4, 54)
        self.assertEqual(216, res)

    def test_area_4_55_values(self):
        res = rectangle.area(4, 55)
        self.assertEqual(220, res)

    def test_area_4_56_values(self):
        res = rectangle.area(4, 56)
        self.assertEqual(224, res)

    def test_area_4_57_values(self):
        res = rectangle.area(4, 57)
        self.assertEqual(228, res)

    def test_area_4_58_values(self):
        res = rectangle.area(4, 58)
        self.assertEqual(232, res)

    def test_area_4_59_values(self):
        res = rectangle.area(4, 59)
        self.assertEqual(236, res)

    def test_area_5_30_values(self):
        res = rectangle.area(5, 30)
        self.assertEqual(150, res)

    def test_area_5_31_values(self):
        res = rectangle.area(5, 31)
        self.assertEqual(155, res)

    def test_area_5_32_values(self):
        res = rectangle.area(5, 32)
        self.assertEqual(160, res)

    def test_area_5_33_values(self):
        res = rectangle.area(5, 33)
        self.assertEqual(165, res)

    def test_area_5_34_values(self):
        res = rectangle.area(5, 34)
        self.assertEqual(170, res)

    def test_area_5_35_values(self):
        res = rectangle.area(5, 35)
        self.assertEqual(175, res)

    def test_area_5_36_values(self):
        res = rectangle.area(5, 36)
        self.assertEqual(180, res)

    def test_area_5_37_values(self):
        res = rectangle.area(5, 37)
        self.assertEqual(185, res)

    def test_area_5_38_values(self):
        res = rectangle.area(5, 38)
        self.assertEqual(190, res)

    def test_area_5_39_values(self):
        res = rectangle.area(5, 39)
        self.assertEqual(195, res)

    def test_area_5_40_values(self):
        res = rectangle.area(5, 40)
        self.assertEqual(200, res)

    def test_area_5_41_values(self):
        res = rectangle.area(5, 41)
        self.assertEqual(205, res)

    def test_area_5_42_values(self):
        res = rectangle.area(5, 42)
        self.assertEqual(210, res)

    def test_area_5_43_values(self):
        res = rectangle.area(5, 43)
        self.assertEqual(215, res)

    def test_area_5_44_values(self):
        res = rectangle.area(5, 44)
        self.assertEqual(220, res)

    def test_area_5_45_values(self):
        res = rectangle.area(5, 45)
        self.assertEqual(225, res)

    def test_area_5_46_values(self):
        res = rectangle.area(5, 46)
        self.assertEqual(230, res)

    def test_area_5_47_values(self):
        res = rectangle.area(5, 47)
        self.assertEqual(235, res)

    def test_area_5_48_values(self):
        res = rectangle.area(5, 48)
        self.assertEqual(240, res)

    def test_area_5_49_values(self):
        res = rectangle.area(5, 49)
        self.assertEqual(245, res)

    def test_area_5_50_values(self):
        res = rectangle.area(5, 50)
        self.assertEqual(250, res)

    def test_area_5_51_values(self):
        res = rectangle.area(5, 51)
        self.assertEqual(255, res)

    def test_area_5_52_values(self):
        res = rectangle.area(5, 52)
        self.assertEqual(260, res)

    def test_area_5_53_values(self):
        res = rectangle.area(5, 53)
        self.assertEqual(265, res)

    def test_area_5_54_values(self):
        res = rectangle.area(5, 54)
        self.assertEqual(270, res)

    def test_area_5_55_values(self):
        res = rectangle.area(5, 55)
        self.assertEqual(275, res)

    def test_area_5_56_values(self):
        res = rectangle.area(5, 56)
        self.assertEqual(280, res)

    def test_area_5_57_values(self):
        res = rectangle.area(5, 57)
        self.assertEqual(285, res)

    def test_area_5_58_values(self):
        res = rectangle.area(5, 58)
        self.assertEqual(290, res)

    def test_area_5_59_values(self):
        res = rectangle.area(5, 59)
        self.assertEqual(295, res)

    def test_area_6_30_values(self):
        res = rectangle.area(6, 30)
        self.assertEqual(180, res)

    def test_area_6_31_values(self):
        res = rectangle.area(6, 31)
        self.assertEqual(186, res)

    def test_area_6_32_values(self):
        res = rectangle.area(6, 32)
        self.assertEqual(192, res)

    def test_area_6_33_values(self):
        res = rectangle.area(6, 33)
        self.assertEqual(198, res)

    def test_area_6_34_values(self):
        res = rectangle.area(6, 34)
        self.assertEqual(204, res)

    def test_area_6_35_values(self):
        res = rectangle.area(6, 35)
        self.assertEqual(210, res)

    def test_area_6_36_values(self):
        res = rectangle.area(6, 36)
        self.assertEqual(216, res)

    def test_area_6_37_values(self):
        res = rectangle.area(6, 37)
        self.assertEqual(222, res)

    def test_area_6_38_values(self):
        res = rectangle.area(6, 38)
        self.assertEqual(228, res)

    def test_area_6_39_values(self):
        res = rectangle.area(6, 39)
        self.assertEqual(234, res)

    def test_area_6_40_values(self):
        res = rectangle.area(6, 40)
        self.assertEqual(240, res)

    def test_area_6_41_values(self):
        res = rectangle.area(6, 41)
        self.assertEqual(246, res)

    def test_area_6_42_values(self):
        res = rectangle.area(6, 42)
        self.assertEqual(252, res)

    def test_area_6_43_values(self):
        res = rectangle.area(6, 43)
        self.assertEqual(258, res)

    def test_area_6_44_values(self):
        res = rectangle.area(6, 44)
        self.assertEqual(264, res)

    def test_area_6_45_values(self):
        res = rectangle.area(6, 45)
        self.assertEqual(270, res)

    def test_area_6_46_values(self):
        res = rectangle.area(6, 46)
        self.assertEqual(276, res)

    def test_area_6_47_values(self):
        res = rectangle.area(6, 47)
        self.assertEqual(282, res)

    def test_area_6_48_values(self):
        res = rectangle.area(6, 48)
        self.assertEqual(288, res)

    def test_area_6_49_values(self):
        res = rectangle.area(6, 49)
        self.assertEqual(294, res)

    def test_area_6_50_values(self):
        res = rectangle.area(6, 50)
        self.assertEqual(300, res)

    def test_area_6_51_values(self):
        res = rectangle.area(6, 51)
        self.assertEqual(306, res)

    def test_area_6_52_values(self):
        res = rectangle.area(6, 52)
        self.assertEqual(312, res)

    def test_area_6_53_values(self):
        res = rectangle.area(6, 53)
        self.assertEqual(318, res)

    def test_area_6_54_values(self):
        res = rectangle.area(6, 54)
        self.assertEqual(324, res)

    def test_area_6_55_values(self):
        res = rectangle.area(6, 55)
        self.assertEqual(330, res)

    def test_area_6_56_values(self):
        res = rectangle.area(6, 56)
        self.assertEqual(336, res)

    def test_area_6_57_values(self):
        res = rectangle.area(6, 57)
        self.assertEqual(342, res)

    def test_area_6_58_values(self):
        res = rectangle.area(6, 58)
        self.assertEqual(348, res)

    def test_area_6_59_values(self):
        res = rectangle.area(6, 59)
        self.assertEqual(354, res)

    def test_area_7_30_values(self):
        res = rectangle.area(7, 30)
        self.assertEqual(210, res)

    def test_area_7_31_values(self):
        res = rectangle.area(7, 31)
        self.assertEqual(217, res)

    def test_area_7_32_values(self):
        res = rectangle.area(7, 32)
        self.assertEqual(224, res)

    def test_area_7_33_values(self):
        res = rectangle.area(7, 33)
        self.assertEqual(231, res)

    def test_area_7_34_values(self):
        res = rectangle.area(7, 34)
        self.assertEqual(238, res)

    def test_area_7_35_values(self):
        res = rectangle.area(7, 35)
        self.assertEqual(245, res)

    def test_area_7_36_values(self):
        res = rectangle.area(7, 36)
        self.assertEqual(252, res)

    def test_area_7_37_values(self):
        res = rectangle.area(7, 37)
        self.assertEqual(259, res)

    def test_area_7_38_values(self):
        res = rectangle.area(7, 38)
        self.assertEqual(266, res)

    def test_area_7_39_values(self):
        res = rectangle.area(7, 39)
        self.assertEqual(273, res)

    def test_area_7_40_values(self):
        res = rectangle.area(7, 40)
        self.assertEqual(280, res)

    def test_area_7_41_values(self):
        res = rectangle.area(7, 41)
        self.assertEqual(287, res)

    def test_area_7_42_values(self):
        res = rectangle.area(7, 42)
        self.assertEqual(294, res)

    def test_area_7_43_values(self):
        res = rectangle.area(7, 43)
        self.assertEqual(301, res)

    def test_area_7_44_values(self):
        res = rectangle.area(7, 44)
        self.assertEqual(308, res)

    def test_area_7_45_values(self):
        res = rectangle.area(7, 45)
        self.assertEqual(315, res)

    def test_area_7_46_values(self):
        res = rectangle.area(7, 46)
        self.assertEqual(322, res)

    def test_area_7_47_values(self):
        res = rectangle.area(7, 47)
        self.assertEqual(329, res)

    def test_area_7_48_values(self):
        res = rectangle.area(7, 48)
        self.assertEqual(336, res)

    def test_area_7_49_values(self):
        res = rectangle.area(7, 49)
        self.assertEqual(343, res)

    def test_area_7_50_values(self):
        res = rectangle.area(7, 50)
        self.assertEqual(350, res)

    def test_area_7_51_values(self):
        res = rectangle.area(7, 51)
        self.assertEqual(357, res)

    def test_area_7_52_values(self):
        res = rectangle.area(7, 52)
        self.assertEqual(364, res)

    def test_area_7_53_values(self):
        res = rectangle.area(7, 53)
        self.assertEqual(371, res)

    def test_area_7_54_values(self):
        res = rectangle.area(7, 54)
        self.assertEqual(378, res)

    def test_area_7_55_values(self):
        res = rectangle.area(7, 55)
        self.assertEqual(385, res)

    def test_area_7_56_values(self):
        res = rectangle.area(7, 56)
        self.assertEqual(392, res)

    def test_area_7_57_values(self):
        res = rectangle.area(7, 57)
        self.assertEqual(399, res)

    def test_area_7_58_values(self):
        res = rectangle.area(7, 58)
        self.assertEqual(406, res)

    def test_area_7_59_values(self):
        res = rectangle.area(7, 59)
        self.assertEqual(413, res)

    def test_area_8_30_values(self):
        res = rectangle.area(8, 30)
        self.assertEqual(240, res)

    def test_area_8_31_values(self):
        res = rectangle.area(8, 31)
        self.assertEqual(248, res)

    def test_area_8_32_values(self):
        res = rectangle.area(8, 32)
        self.assertEqual(256, res)

    def test_area_8_33_values(self):
        res = rectangle.area(8, 33)
        self.assertEqual(264, res)

    def test_area_8_34_values(self):
        res = rectangle.area(8, 34)
        self.assertEqual(272, res)

    def test_area_8_35_values(self):
        res = rectangle.area(8, 35)
        self.assertEqual(280, res)

    def test_area_8_36_values(self):
        res = rectangle.area(8, 36)
        self.assertEqual(288, res)

    def test_area_8_37_values(self):
        res = rectangle.area(8, 37)
        self.assertEqual(296, res)

    def test_area_8_38_values(self):
        res = rectangle.area(8, 38)
        self.assertEqual(304, res)

    def test_area_8_39_values(self):
        res = rectangle.area(8, 39)
        self.assertEqual(312, res)

    def test_area_8_40_values(self):
        res = rectangle.area(8, 40)
        self.assertEqual(320, res)

    def test_area_8_41_values(self):
        res = rectangle.area(8, 41)
        self.assertEqual(328, res)

    def test_area_8_42_values(self):
        res = rectangle.area(8, 42)
        self.assertEqual(336, res)

    def test_area_8_43_values(self):
        res = rectangle.area(8, 43)
        self.assertEqual(344, res)

    def test_area_8_44_values(self):
        res = rectangle.area(8, 44)
        self.assertEqual(352, res)

    def test_area_8_45_values(self):
        res = rectangle.area(8, 45)
        self.assertEqual(360, res)

    def test_area_8_46_values(self):
        res = rectangle.area(8, 46)
        self.assertEqual(368, res)

    def test_area_8_47_values(self):
        res = rectangle.area(8, 47)
        self.assertEqual(376, res)

    def test_area_8_48_values(self):
        res = rectangle.area(8, 48)
        self.assertEqual(384, res)

    def test_area_8_49_values(self):
        res = rectangle.area(8, 49)
        self.assertEqual(392, res)

    def test_area_8_50_values(self):
        res = rectangle.area(8, 50)
        self.assertEqual(400, res)

    def test_area_8_51_values(self):
        res = rectangle.area(8, 51)
        self.assertEqual(408, res)

    def test_area_8_52_values(self):
        res = rectangle.area(8, 52)
        self.assertEqual(416, res)

    def test_area_8_53_values(self):
        res = rectangle.area(8, 53)
        self.assertEqual(424, res)

    def test_area_8_54_values(self):
        res = rectangle.area(8, 54)
        self.assertEqual(432, res)

    def test_area_8_55_values(self):
        res = rectangle.area(8, 55)
        self.assertEqual(440, res)

    def test_area_8_56_values(self):
        res = rectangle.area(8, 56)
        self.assertEqual(448, res)

    def test_area_8_57_values(self):
        res = rectangle.area(8, 57)
        self.assertEqual(456, res)

    def test_area_8_58_values(self):
        res = rectangle.area(8, 58)
        self.assertEqual(464, res)

    def test_area_8_59_values(self):
        res = rectangle.area(8, 59)
        self.assertEqual(472, res)

    def test_area_9_30_values(self):
        res = rectangle.area(9, 30)
        self.assertEqual(270, res)

    def test_area_9_31_values(self):
        res = rectangle.area(9, 31)
        self.assertEqual(279, res)

    def test_area_9_32_values(self):
        res = rectangle.area(9, 32)
        self.assertEqual(288, res)

    def test_area_9_33_values(self):
        res = rectangle.area(9, 33)
        self.assertEqual(297, res)

    def test_area_9_34_values(self):
        res = rectangle.area(9, 34)
        self.assertEqual(306, res)

    def test_area_9_35_values(self):
        res = rectangle.area(9, 35)
        self.assertEqual(315, res)

    def test_area_9_36_values(self):
        res = rectangle.area(9, 36)
        self.assertEqual(324, res)

    def test_area_9_37_values(self):
        res = rectangle.area(9, 37)
        self.assertEqual(333, res)

    def test_area_9_38_values(self):
        res = rectangle.area(9, 38)
        self.assertEqual(342, res)

    def test_area_9_39_values(self):
        res = rectangle.area(9, 39)
        self.assertEqual(351, res)

    def test_area_9_40_values(self):
        res = rectangle.area(9, 40)
        self.assertEqual(360, res)

    def test_area_9_41_values(self):
        res = rectangle.area(9, 41)
        self.assertEqual(369, res)

    def test_area_9_42_values(self):
        res = rectangle.area(9, 42)
        self.assertEqual(378, res)

    def test_area_9_43_values(self):
        res = rectangle.area(9, 43)
        self.assertEqual(387, res)

    def test_area_9_44_values(self):
        res = rectangle.area(9, 44)
        self.assertEqual(396, res)

    def test_area_9_45_values(self):
        res = rectangle.area(9, 45)
        self.assertEqual(405, res)

    def test_area_9_46_values(self):
        res = rectangle.area(9, 46)
        self.assertEqual(414, res)

    def test_area_9_47_values(self):
        res = rectangle.area(9, 47)
        self.assertEqual(423, res)

    def test_area_9_48_values(self):
        res = rectangle.area(9, 48)
        self.assertEqual(432, res)

    def test_area_9_49_values(self):
        res = rectangle.area(9, 49)
        self.assertEqual(441, res)

    def test_area_9_50_values(self):
        res = rectangle.area(9, 50)
        self.assertEqual(450, res)

    def test_area_9_51_values(self):
        res = rectangle.area(9, 51)
        self.assertEqual(459, res)

    def test_area_9_52_values(self):
        res = rectangle.area(9, 52)
        self.assertEqual(468, res)

    def test_area_9_53_values(self):
        res = rectangle.area(9, 53)
        self.assertEqual(477, res)

    def test_area_9_54_values(self):
        res = rectangle.area(9, 54)
        self.assertEqual(486, res)

    def test_area_9_55_values(self):
        res = rectangle.area(9, 55)
        self.assertEqual(495, res)

    def test_area_9_56_values(self):
        res = rectangle.area(9, 56)
        self.assertEqual(504, res)

    def test_area_9_57_values(self):
        res = rectangle.area(9, 57)
        self.assertEqual(513, res)

    def test_area_9_58_values(self):
        res = rectangle.area(9, 58)
        self.assertEqual(522, res)

    def test_area_9_59_values(self):
        res = rectangle.area(9, 59)
        self.assertEqual(531, res)

    def test_area_10_30_values(self):
        res = rectangle.area(10, 30)
        self.assertEqual(300, res)

    def test_area_10_31_values(self):
        res = rectangle.area(10, 31)
        self.assertEqual(310, res)

    def test_area_10_32_values(self):
        res = rectangle.area(10, 32)
        self.assertEqual(320, res)

    def test_area_10_33_values(self):
        res = rectangle.area(10, 33)
        self.assertEqual(330, res)

    def test_area_10_34_values(self):
        res = rectangle.area(10, 34)
        self.assertEqual(340, res)

    def test_area_10_35_values(self):
        res = rectangle.area(10, 35)
        self.assertEqual(350, res)

    def test_area_10_36_values(self):
        res = rectangle.area(10, 36)
        self.assertEqual(360, res)

    def test_area_10_37_values(self):
        res = rectangle.area(10, 37)
        self.assertEqual(370, res)

    def test_area_10_38_values(self):
        res = rectangle.area(10, 38)
        self.assertEqual(380, res)

    def test_area_10_39_values(self):
        res = rectangle.area(10, 39)
        self.assertEqual(390, res)

    def test_area_10_40_values(self):
        res = rectangle.area(10, 40)
        self.assertEqual(400, res)

    def test_area_10_41_values(self):
        res = rectangle.area(10, 41)
        self.assertEqual(410, res)

    def test_area_10_42_values(self):
        res = rectangle.area(10, 42)
        self.assertEqual(420, res)

    def test_area_10_43_values(self):
        res = rectangle.area(10, 43)
        self.assertEqual(430, res)

    def test_area_10_44_values(self):
        res = rectangle.area(10, 44)
        self.assertEqual(440, res)

    def test_area_10_45_values(self):
        res = rectangle.area(10, 45)
        self.assertEqual(450, res)

    def test_area_10_46_values(self):
        res = rectangle.area(10, 46)
        self.assertEqual(460, res)

    def test_area_10_47_values(self):
        res = rectangle.area(10, 47)
        self.assertEqual(470, res)

    def test_area_10_48_values(self):
        res = rectangle.area(10, 48)
        self.assertEqual(480, res)

    def test_area_10_49_values(self):
        res = rectangle.area(10, 49)
        self.assertEqual(490, res)

    def test_area_10_50_values(self):
        res = rectangle.area(10, 50)
        self.assertEqual(500, res)

    def test_area_10_51_values(self):
        res = rectangle.area(10, 51)
        self.assertEqual(510, res)

    def test_area_10_52_values(self):
        res = rectangle.area(10, 52)
        self.assertEqual(520, res)

    def test_area_10_53_values(self):
        res = rectangle.area(10, 53)
        self.assertEqual(530, res)

    def test_area_10_54_values(self):
        res = rectangle.area(10, 54)
        self.assertEqual(540, res)

    def test_area_10_55_values(self):
        res = rectangle.area(10, 55)
        self.assertEqual(550, res)

    def test_area_10_56_values(self):
        res = rectangle.area(10, 56)
        self.assertEqual(560, res)

    def test_area_10_57_values(self):
        res = rectangle.area(10, 57)
        self.assertEqual(570, res)

    def test_area_10_58_values(self):
        res = rectangle.area(10, 58)
        self.assertEqual(580, res)

    def test_area_10_59_values(self):
        res = rectangle.area(10, 59)
        self.assertEqual(590, res)

    def test_area_11_30_values(self):
        res = rectangle.area(11, 30)
        self.assertEqual(330, res)

    def test_area_11_31_values(self):
        res = rectangle.area(11, 31)
        self.assertEqual(341, res)

    def test_area_11_32_values(self):
        res = rectangle.area(11, 32)
        self.assertEqual(352, res)

    def test_area_11_33_values(self):
        res = rectangle.area(11, 33)
        self.assertEqual(363, res)

    def test_area_11_34_values(self):
        res = rectangle.area(11, 34)
        self.assertEqual(374, res)

    def test_area_11_35_values(self):
        res = rectangle.area(11, 35)
        self.assertEqual(385, res)

    def test_area_11_36_values(self):
        res = rectangle.area(11, 36)
        self.assertEqual(396, res)

    def test_area_11_37_values(self):
        res = rectangle.area(11, 37)
        self.assertEqual(407, res)

    def test_area_11_38_values(self):
        res = rectangle.area(11, 38)
        self.assertEqual(418, res)

    def test_area_11_39_values(self):
        res = rectangle.area(11, 39)
        self.assertEqual(429, res)

    def test_area_11_40_values(self):
        res = rectangle.area(11, 40)
        self.assertEqual(440, res)

    def test_area_11_41_values(self):
        res = rectangle.area(11, 41)
        self.assertEqual(451, res)

    def test_area_11_42_values(self):
        res = rectangle.area(11, 42)
        self.assertEqual(462, res)

    def test_area_11_43_values(self):
        res = rectangle.area(11, 43)
        self.assertEqual(473, res)

    def test_area_11_44_values(self):
        res = rectangle.area(11, 44)
        self.assertEqual(484, res)

    def test_area_11_45_values(self):
        res = rectangle.area(11, 45)
        self.assertEqual(495, res)

    def test_area_11_46_values(self):
        res = rectangle.area(11, 46)
        self.assertEqual(506, res)

    def test_area_11_47_values(self):
        res = rectangle.area(11, 47)
        self.assertEqual(517, res)

    def test_area_11_48_values(self):
        res = rectangle.area(11, 48)
        self.assertEqual(528, res)

    def test_area_11_49_values(self):
        res = rectangle.area(11, 49)
        self.assertEqual(539, res)

    def test_area_11_50_values(self):
        res = rectangle.area(11, 50)
        self.assertEqual(550, res)

    def test_area_11_51_values(self):
        res = rectangle.area(11, 51)
        self.assertEqual(561, res)

    def test_area_11_52_values(self):
        res = rectangle.area(11, 52)
        self.assertEqual(572, res)

    def test_area_11_53_values(self):
        res = rectangle.area(11, 53)
        self.assertEqual(583, res)

    def test_area_11_54_values(self):
        res = rectangle.area(11, 54)
        self.assertEqual(594, res)

    def test_area_11_55_values(self):
        res = rectangle.area(11, 55)
        self.assertEqual(605, res)

    def test_area_11_56_values(self):
        res = rectangle.area(11, 56)
        self.assertEqual(616, res)

    def test_area_11_57_values(self):
        res = rectangle.area(11, 57)
        self.assertEqual(627, res)

    def test_area_11_58_values(self):
        res = rectangle.area(11, 58)
        self.assertEqual(638, res)

    def test_area_11_59_values(self):
        res = rectangle.area(11, 59)
        self.assertEqual(649, res)

    def test_area_12_30_values(self):
        res = rectangle.area(12, 30)
        self.assertEqual(360, res)

    def test_area_12_31_values(self):
        res = rectangle.area(12, 31)
        self.assertEqual(372, res)

    def test_area_12_32_values(self):
        res = rectangle.area(12, 32)
        self.assertEqual(384, res)

    def test_area_12_33_values(self):
        res = rectangle.area(12, 33)
        self.assertEqual(396, res)

    def test_area_12_34_values(self):
        res = rectangle.area(12, 34)
        self.assertEqual(408, res)

    def test_area_12_35_values(self):
        res = rectangle.area(12, 35)
        self.assertEqual(420, res)

    def test_area_12_36_values(self):
        res = rectangle.area(12, 36)
        self.assertEqual(432, res)

    def test_area_12_37_values(self):
        res = rectangle.area(12, 37)
        self.assertEqual(444, res)

    def test_area_12_38_values(self):
        res = rectangle.area(12, 38)
        self.assertEqual(456, res)

    def test_area_12_39_values(self):
        res = rectangle.area(12, 39)
        self.assertEqual(468, res)

    def test_area_12_40_values(self):
        res = rectangle.area(12, 40)
        self.assertEqual(480, res)

    def test_area_12_41_values(self):
        res = rectangle.area(12, 41)
        self.assertEqual(492, res)

    def test_area_12_42_values(self):
        res = rectangle.area(12, 42)
        self.assertEqual(504, res)

    def test_area_12_43_values(self):
        res = rectangle.area(12, 43)
        self.assertEqual(516, res)

    def test_area_12_44_values(self):
        res = rectangle.area(12, 44)
        self.assertEqual(528, res)

    def test_area_12_45_values(self):
        res = rectangle.area(12, 45)
        self.assertEqual(540, res)

    def test_area_12_46_values(self):
        res = rectangle.area(12, 46)
        self.assertEqual(552, res)

    def test_area_12_47_values(self):
        res = rectangle.area(12, 47)
        self.assertEqual(564, res)

    def test_area_12_48_values(self):
        res = rectangle.area(12, 48)
        self.assertEqual(576, res)

    def test_area_12_49_values(self):
        res = rectangle.area(12, 49)
        self.assertEqual(588, res)

    def test_area_12_50_values(self):
        res = rectangle.area(12, 50)
        self.assertEqual(600, res)

    def test_area_12_51_values(self):
        res = rectangle.area(12, 51)
        self.assertEqual(612, res)

    def test_area_12_52_values(self):
        res = rectangle.area(12, 52)
        self.assertEqual(624, res)

    def test_area_12_53_values(self):
        res = rectangle.area(12, 53)
        self.assertEqual(636, res)

    def test_area_12_54_values(self):
        res = rectangle.area(12, 54)
        self.assertEqual(648, res)

    def test_area_12_55_values(self):
        res = rectangle.area(12, 55)
        self.assertEqual(660, res)

    def test_area_12_56_values(self):
        res = rectangle.area(12, 56)
        self.assertEqual(672, res)

    def test_area_12_57_values(self):
        res = rectangle.area(12, 57)
        self.assertEqual(684, res)

    def test_area_12_58_values(self):
        res = rectangle.area(12, 58)
        self.assertEqual(696, res)

    def test_area_12_59_values(self):
        res = rectangle.area(12, 59)
        self.assertEqual(708, res)

    def test_area_13_30_values(self):
        res = rectangle.area(13, 30)
        self.assertEqual(390, res)

    def test_area_13_31_values(self):
        res = rectangle.area(13, 31)
        self.assertEqual(403, res)

    def test_area_13_32_values(self):
        res = rectangle.area(13, 32)
        self.assertEqual(416, res)

    def test_area_13_33_values(self):
        res = rectangle.area(13, 33)
        self.assertEqual(429, res)

    def test_area_13_34_values(self):
        res = rectangle.area(13, 34)
        self.assertEqual(442, res)

    def test_area_13_35_values(self):
        res = rectangle.area(13, 35)
        self.assertEqual(455, res)

    def test_area_13_36_values(self):
        res = rectangle.area(13, 36)
        self.assertEqual(468, res)

    def test_area_13_37_values(self):
        res = rectangle.area(13, 37)
        self.assertEqual(481, res)

    def test_area_13_38_values(self):
        res = rectangle.area(13, 38)
        self.assertEqual(494, res)

    def test_area_13_39_values(self):
        res = rectangle.area(13, 39)
        self.assertEqual(507, res)

    def test_area_13_40_values(self):
        res = rectangle.area(13, 40)
        self.assertEqual(520, res)

    def test_area_13_41_values(self):
        res = rectangle.area(13, 41)
        self.assertEqual(533, res)

    def test_area_13_42_values(self):
        res = rectangle.area(13, 42)
        self.assertEqual(546, res)

    def test_area_13_43_values(self):
        res = rectangle.area(13, 43)
        self.assertEqual(559, res)

    def test_area_13_44_values(self):
        res = rectangle.area(13, 44)
        self.assertEqual(572, res)

    def test_area_13_45_values(self):
        res = rectangle.area(13, 45)
        self.assertEqual(585, res)

    def test_area_13_46_values(self):
        res = rectangle.area(13, 46)
        self.assertEqual(598, res)

    def test_area_13_47_values(self):
        res = rectangle.area(13, 47)
        self.assertEqual(611, res)

    def test_area_13_48_values(self):
        res = rectangle.area(13, 48)
        self.assertEqual(624, res)

    def test_area_13_49_values(self):
        res = rectangle.area(13, 49)
        self.assertEqual(637, res)

    def test_area_13_50_values(self):
        res = rectangle.area(13, 50)
        self.assertEqual(650, res)

    def test_area_13_51_values(self):
        res = rectangle.area(13, 51)
        self.assertEqual(663, res)

    def test_area_13_52_values(self):
        res = rectangle.area(13, 52)
        self.assertEqual(676, res)

    def test_area_13_53_values(self):
        res = rectangle.area(13, 53)
        self.assertEqual(689, res)

    def test_area_13_54_values(self):
        res = rectangle.area(13, 54)
        self.assertEqual(702, res)

    def test_area_13_55_values(self):
        res = rectangle.area(13, 55)
        self.assertEqual(715, res)

    def test_area_13_56_values(self):
        res = rectangle.area(13, 56)
        self.assertEqual(728, res)

    def test_area_13_57_values(self):
        res = rectangle.area(13, 57)
        self.assertEqual(741, res)

    def test_area_13_58_values(self):
        res = rectangle.area(13, 58)
        self.assertEqual(754, res)

    def test_area_13_59_values(self):
        res = rectangle.area(13, 59)
        self.assertEqual(767, res)

    def test_area_14_30_values(self):
        res = rectangle.area(14, 30)
        self.assertEqual(420, res)

    def test_area_14_31_values(self):
        res = rectangle.area(14, 31)
        self.assertEqual(434, res)

    def test_area_14_32_values(self):
        res = rectangle.area(14, 32)
        self.assertEqual(448, res)

    def test_area_14_33_values(self):
        res = rectangle.area(14, 33)
        self.assertEqual(462, res)

    def test_area_14_34_values(self):
        res = rectangle.area(14, 34)
        self.assertEqual(476, res)

    def test_area_14_35_values(self):
        res = rectangle.area(14, 35)
        self.assertEqual(490, res)

    def test_area_14_36_values(self):
        res = rectangle.area(14, 36)
        self.assertEqual(504, res)

    def test_area_14_37_values(self):
        res = rectangle.area(14, 37)
        self.assertEqual(518, res)

    def test_area_14_38_values(self):
        res = rectangle.area(14, 38)
        self.assertEqual(532, res)

    def test_area_14_39_values(self):
        res = rectangle.area(14, 39)
        self.assertEqual(546, res)

    def test_area_14_40_values(self):
        res = rectangle.area(14, 40)
        self.assertEqual(560, res)

    def test_area_14_41_values(self):
        res = rectangle.area(14, 41)
        self.assertEqual(574, res)

    def test_area_14_42_values(self):
        res = rectangle.area(14, 42)
        self.assertEqual(588, res)

    def test_area_14_43_values(self):
        res = rectangle.area(14, 43)
        self.assertEqual(602, res)

    def test_area_14_44_values(self):
        res = rectangle.area(14, 44)
        self.assertEqual(616, res)

    def test_area_14_45_values(self):
        res = rectangle.area(14, 45)
        self.assertEqual(630, res)

    def test_area_14_46_values(self):
        res = rectangle.area(14, 46)
        self.assertEqual(644, res)

    def test_area_14_47_values(self):
        res = rectangle.area(14, 47)
        self.assertEqual(658, res)

    def test_area_14_48_values(self):
        res = rectangle.area(14, 48)
        self.assertEqual(672, res)

    def test_area_14_49_values(self):
        res = rectangle.area(14, 49)
        self.assertEqual(686, res)

    def test_area_14_50_values(self):
        res = rectangle.area(14, 50)
        self.assertEqual(700, res)

    def test_area_14_51_values(self):
        res = rectangle.area(14, 51)
        self.assertEqual(714, res)

    def test_area_14_52_values(self):
        res = rectangle.area(14, 52)
        self.assertEqual(728, res)

    def test_area_14_53_values(self):
        res = rectangle.area(14, 53)
        self.assertEqual(742, res)

    def test_area_14_54_values(self):
        res = rectangle.area(14, 54)
        self.assertEqual(756, res)

    def test_area_14_55_values(self):
        res = rectangle.area(14, 55)
        self.assertEqual(770, res)

    def test_area_14_56_values(self):
        res = rectangle.area(14, 56)
        self.assertEqual(784, res)

    def test_area_14_57_values(self):
        res = rectangle.area(14, 57)
        self.assertEqual(798, res)

    def test_area_14_58_values(self):
        res = rectangle.area(14, 58)
        self.assertEqual(812, res)

    def test_area_14_59_values(self):
        res = rectangle.area(14, 59)
        self.assertEqual(826, res)

    def test_area_15_30_values(self):
        res = rectangle.area(15, 30)
        self.assertEqual(450, res)

    def test_area_15_31_values(self):
        res = rectangle.area(15, 31)
        self.assertEqual(465, res)

    def test_area_15_32_values(self):
        res = rectangle.area(15, 32)
        self.assertEqual(480, res)

    def test_area_15_33_values(self):
        res = rectangle.area(15, 33)
        self.assertEqual(495, res)

    def test_area_15_34_values(self):
        res = rectangle.area(15, 34)
        self.assertEqual(510, res)

    def test_area_15_35_values(self):
        res = rectangle.area(15, 35)
        self.assertEqual(525, res)

    def test_area_15_36_values(self):
        res = rectangle.area(15, 36)
        self.assertEqual(540, res)

    def test_area_15_37_values(self):
        res = rectangle.area(15, 37)
        self.assertEqual(555, res)

    def test_area_15_38_values(self):
        res = rectangle.area(15, 38)
        self.assertEqual(570, res)

    def test_area_15_39_values(self):
        res = rectangle.area(15, 39)
        self.assertEqual(585, res)

    def test_area_15_40_values(self):
        res = rectangle.area(15, 40)
        self.assertEqual(600, res)

    def test_area_15_41_values(self):
        res = rectangle.area(15, 41)
        self.assertEqual(615, res)

    def test_area_15_42_values(self):
        res = rectangle.area(15, 42)
        self.assertEqual(630, res)

    def test_area_15_43_values(self):
        res = rectangle.area(15, 43)
        self.assertEqual(645, res)

    def test_area_15_44_values(self):
        res = rectangle.area(15, 44)
        self.assertEqual(660, res)

    def test_area_15_45_values(self):
        res = rectangle.area(15, 45)
        self.assertEqual(675, res)

    def test_area_15_46_values(self):
        res = rectangle.area(15, 46)
        self.assertEqual(690, res)

    def test_area_15_47_values(self):
        res = rectangle.area(15, 47)
        self.assertEqual(705, res)

    def test_area_15_48_values(self):
        res = rectangle.area(15, 48)
        self.assertEqual(720, res)

    def test_area_15_49_values(self):
        res = rectangle.area(15, 49)
        self.assertEqual(735, res)

    def test_area_15_50_values(self):
        res = rectangle.area(15, 50)
        self.assertEqual(750, res)

    def test_area_15_51_values(self):
        res = rectangle.area(15, 51)
        self.assertEqual(765, res)

    def test_area_15_52_values(self):
        res = rectangle.area(15, 52)
        self.assertEqual(780, res)

    def test_area_15_53_values(self):
        res = rectangle.area(15, 53)
        self.assertEqual(795, res)

    def test_area_15_54_values(self):
        res = rectangle.area(15, 54)
        self.assertEqual(810, res)

    def test_area_15_55_values(self):
        res = rectangle.area(15, 55)
        self.assertEqual(825, res)

    def test_area_15_56_values(self):
        res = rectangle.area(15, 56)
        self.assertEqual(840, res)

    def test_area_15_57_values(self):
        res = rectangle.area(15, 57)
        self.assertEqual(855, res)

    def test_area_15_58_values(self):
        res = rectangle.area(15, 58)
        self.assertEqual(870, res)

    def test_area_15_59_values(self):
        res = rectangle.area(15, 59)
        self.assertEqual(885, res)

    def test_area_16_30_values(self):
        res = rectangle.area(16, 30)
        self.assertEqual(480, res)

    def test_area_16_31_values(self):
        res = rectangle.area(16, 31)
        self.assertEqual(496, res)

    def test_area_16_32_values(self):
        res = rectangle.area(16, 32)
        self.assertEqual(512, res)

    def test_area_16_33_values(self):
        res = rectangle.area(16, 33)
        self.assertEqual(528, res)

    def test_area_16_34_values(self):
        res = rectangle.area(16, 34)
        self.assertEqual(544, res)

    def test_area_16_35_values(self):
        res = rectangle.area(16, 35)
        self.assertEqual(560, res)

    def test_area_16_36_values(self):
        res = rectangle.area(16, 36)
        self.assertEqual(576, res)

    def test_area_16_37_values(self):
        res = rectangle.area(16, 37)
        self.assertEqual(592, res)

    def test_area_16_38_values(self):
        res = rectangle.area(16, 38)
        self.assertEqual(608, res)

    def test_area_16_39_values(self):
        res = rectangle.area(16, 39)
        self.assertEqual(624, res)

    def test_area_16_40_values(self):
        res = rectangle.area(16, 40)
        self.assertEqual(640, res)

    def test_area_16_41_values(self):
        res = rectangle.area(16, 41)
        self.assertEqual(656, res)

    def test_area_16_42_values(self):
        res = rectangle.area(16, 42)
        self.assertEqual(672, res)

    def test_area_16_43_values(self):
        res = rectangle.area(16, 43)
        self.assertEqual(688, res)

    def test_area_16_44_values(self):
        res = rectangle.area(16, 44)
        self.assertEqual(704, res)

    def test_area_16_45_values(self):
        res = rectangle.area(16, 45)
        self.assertEqual(720, res)

    def test_area_16_46_values(self):
        res = rectangle.area(16, 46)
        self.assertEqual(736, res)

    def test_area_16_47_values(self):
        res = rectangle.area(16, 47)
        self.assertEqual(752, res)

    def test_area_16_48_values(self):
        res = rectangle.area(16, 48)
        self.assertEqual(768, res)

    def test_area_16_49_values(self):
        res = rectangle.area(16, 49)
        self.assertEqual(784, res)

    def test_area_16_50_values(self):
        res = rectangle.area(16, 50)
        self.assertEqual(800, res)

    def test_area_16_51_values(self):
        res = rectangle.area(16, 51)
        self.assertEqual(816, res)

    def test_area_16_52_values(self):
        res = rectangle.area(16, 52)
        self.assertEqual(832, res)

    def test_area_16_53_values(self):
        res = rectangle.area(16, 53)
        self.assertEqual(848, res)

    def test_area_16_54_values(self):
        res = rectangle.area(16, 54)
        self.assertEqual(864, res)

    def test_area_16_55_values(self):
        res = rectangle.area(16, 55)
        self.assertEqual(880, res)

    def test_area_16_56_values(self):
        res = rectangle.area(16, 56)
        self.assertEqual(896, res)

    def test_area_16_57_values(self):
        res = rectangle.area(16, 57)
        self.assertEqual(912, res)

    def test_area_16_58_values(self):
        res = rectangle.area(16, 58)
        self.assertEqual(928, res)

    def test_area_16_59_values(self):
        res = rectangle.area(16, 59)
        self.assertEqual(944, res)

    def test_area_17_30_values(self):
        res = rectangle.area(17, 30)
        self.assertEqual(510, res)

    def test_area_17_31_values(self):
        res = rectangle.area(17, 31)
        self.assertEqual(527, res)

    def test_area_17_32_values(self):
        res = rectangle.area(17, 32)
        self.assertEqual(544, res)

    def test_area_17_33_values(self):
        res = rectangle.area(17, 33)
        self.assertEqual(561, res)

    def test_area_17_34_values(self):
        res = rectangle.area(17, 34)
        self.assertEqual(578, res)

    def test_area_17_35_values(self):
        res = rectangle.area(17, 35)
        self.assertEqual(595, res)

    def test_area_17_36_values(self):
        res = rectangle.area(17, 36)
        self.assertEqual(612, res)

    def test_area_17_37_values(self):
        res = rectangle.area(17, 37)
        self.assertEqual(629, res)

    def test_area_17_38_values(self):
        res = rectangle.area(17, 38)
        self.assertEqual(646, res)

    def test_area_17_39_values(self):
        res = rectangle.area(17, 39)
        self.assertEqual(663, res)

    def test_area_17_40_values(self):
        res = rectangle.area(17, 40)
        self.assertEqual(680, res)

    def test_area_17_41_values(self):
        res = rectangle.area(17, 41)
        self.assertEqual(697, res)

    def test_area_17_42_values(self):
        res = rectangle.area(17, 42)
        self.assertEqual(714, res)

    def test_area_17_43_values(self):
        res = rectangle.area(17, 43)
        self.assertEqual(731, res)

    def test_area_17_44_values(self):
        res = rectangle.area(17, 44)
        self.assertEqual(748, res)

    def test_area_17_45_values(self):
        res = rectangle.area(17, 45)
        self.assertEqual(765, res)

    def test_area_17_46_values(self):
        res = rectangle.area(17, 46)
        self.assertEqual(782, res)

    def test_area_17_47_values(self):
        res = rectangle.area(17, 47)
        self.assertEqual(799, res)

    def test_area_17_48_values(self):
        res = rectangle.area(17, 48)
        self.assertEqual(816, res)

    def test_area_17_49_values(self):
        res = rectangle.area(17, 49)
        self.assertEqual(833, res)

    def test_area_17_50_values(self):
        res = rectangle.area(17, 50)
        self.assertEqual(850, res)

    def test_area_17_51_values(self):
        res = rectangle.area(17, 51)
        self.assertEqual(867, res)

    def test_area_17_52_values(self):
        res = rectangle.area(17, 52)
        self.assertEqual(884, res)

    def test_area_17_53_values(self):
        res = rectangle.area(17, 53)
        self.assertEqual(901, res)

    def test_area_17_54_values(self):
        res = rectangle.area(17, 54)
        self.assertEqual(918, res)

    def test_area_17_55_values(self):
        res = rectangle.area(17, 55)
        self.assertEqual(935, res)

    def test_area_17_56_values(self):
        res = rectangle.area(17, 56)
        self.assertEqual(952, res)

    def test_area_17_57_values(self):
        res = rectangle.area(17, 57)
        self.assertEqual(969, res)

    def test_area_17_58_values(self):
        res = rectangle.area(17, 58)
        self.assertEqual(986, res)

    def test_area_17_59_values(self):
        res = rectangle.area(17, 59)
        self.assertEqual(1003, res)

    def test_area_18_30_values(self):
        res = rectangle.area(18, 30)
        self.assertEqual(540, res)

    def test_area_18_31_values(self):
        res = rectangle.area(18, 31)
        self.assertEqual(558, res)

    def test_area_18_32_values(self):
        res = rectangle.area(18, 32)
        self.assertEqual(576, res)

    def test_area_18_33_values(self):
        res = rectangle.area(18, 33)
        self.assertEqual(594, res)

    def test_area_18_34_values(self):
        res = rectangle.area(18, 34)
        self.assertEqual(612, res)

    def test_area_18_35_values(self):
        res = rectangle.area(18, 35)
        self.assertEqual(630, res)

    def test_area_18_36_values(self):
        res = rectangle.area(18, 36)
        self.assertEqual(648, res)

    def test_area_18_37_values(self):
        res = rectangle.area(18, 37)
        self.assertEqual(666, res)

    def test_area_18_38_values(self):
        res = rectangle.area(18, 38)
        self.assertEqual(684, res)

    def test_area_18_39_values(self):
        res = rectangle.area(18, 39)
        self.assertEqual(702, res)

    def test_area_18_40_values(self):
        res = rectangle.area(18, 40)
        self.assertEqual(720, res)

    def test_area_18_41_values(self):
        res = rectangle.area(18, 41)
        self.assertEqual(738, res)

    def test_area_18_42_values(self):
        res = rectangle.area(18, 42)
        self.assertEqual(756, res)

    def test_area_18_43_values(self):
        res = rectangle.area(18, 43)
        self.assertEqual(774, res)

    def test_area_18_44_values(self):
        res = rectangle.area(18, 44)
        self.assertEqual(792, res)

    def test_area_18_45_values(self):
        res = rectangle.area(18, 45)
        self.assertEqual(810, res)

    def test_area_18_46_values(self):
        res = rectangle.area(18, 46)
        self.assertEqual(828, res)

    def test_area_18_47_values(self):
        res = rectangle.area(18, 47)
        self.assertEqual(846, res)

    def test_area_18_48_values(self):
        res = rectangle.area(18, 48)
        self.assertEqual(864, res)

    def test_area_18_49_values(self):
        res = rectangle.area(18, 49)
        self.assertEqual(882, res)

    def test_area_18_50_values(self):
        res = rectangle.area(18, 50)
        self.assertEqual(900, res)

    def test_area_18_51_values(self):
        res = rectangle.area(18, 51)
        self.assertEqual(918, res)

    def test_area_18_52_values(self):
        res = rectangle.area(18, 52)
        self.assertEqual(936, res)

    def test_area_18_53_values(self):
        res = rectangle.area(18, 53)
        self.assertEqual(954, res)

    def test_area_18_54_values(self):
        res = rectangle.area(18, 54)
        self.assertEqual(972, res)

    def test_area_18_55_values(self):
        res = rectangle.area(18, 55)
        self.assertEqual(990, res)

    def test_area_18_56_values(self):
        res = rectangle.area(18, 56)
        self.assertEqual(1008, res)

    def test_area_18_57_values(self):
        res = rectangle.area(18, 57)
        self.assertEqual(1026, res)

    def test_area_18_58_values(self):
        res = rectangle.area(18, 58)
        self.assertEqual(1044, res)

    def test_area_18_59_values(self):
        res = rectangle.area(18, 59)
        self.assertEqual(1062, res)

    def test_area_19_30_values(self):
        res = rectangle.area(19, 30)
        self.assertEqual(570, res)

    def test_area_19_31_values(self):
        res = rectangle.area(19, 31)
        self.assertEqual(589, res)

    def test_area_19_32_values(self):
        res = rectangle.area(19, 32)
        self.assertEqual(608, res)

    def test_area_19_33_values(self):
        res = rectangle.area(19, 33)
        self.assertEqual(627, res)

    def test_area_19_34_values(self):
        res = rectangle.area(19, 34)
        self.assertEqual(646, res)

    def test_area_19_35_values(self):
        res = rectangle.area(19, 35)
        self.assertEqual(665, res)

    def test_area_19_36_values(self):
        res = rectangle.area(19, 36)
        self.assertEqual(684, res)

    def test_area_19_37_values(self):
        res = rectangle.area(19, 37)
        self.assertEqual(703, res)

    def test_area_19_38_values(self):
        res = rectangle.area(19, 38)
        self.assertEqual(722, res)

    def test_area_19_39_values(self):
        res = rectangle.area(19, 39)
        self.assertEqual(741, res)

    def test_area_19_40_values(self):
        res = rectangle.area(19, 40)
        self.assertEqual(760, res)

    def test_area_19_41_values(self):
        res = rectangle.area(19, 41)
        self.assertEqual(779, res)

    def test_area_19_42_values(self):
        res = rectangle.area(19, 42)
        self.assertEqual(798, res)

    def test_area_19_43_values(self):
        res = rectangle.area(19, 43)
        self.assertEqual(817, res)

    def test_area_19_44_values(self):
        res = rectangle.area(19, 44)
        self.assertEqual(836, res)

    def test_area_19_45_values(self):
        res = rectangle.area(19, 45)
        self.assertEqual(855, res)

    def test_area_19_46_values(self):
        res = rectangle.area(19, 46)
        self.assertEqual(874, res)

    def test_area_19_47_values(self):
        res = rectangle.area(19, 47)
        self.assertEqual(893, res)

    def test_area_19_48_values(self):
        res = rectangle.area(19, 48)
        self.assertEqual(912, res)

    def test_area_19_49_values(self):
        res = rectangle.area(19, 49)
        self.assertEqual(931, res)

    def test_area_19_50_values(self):
        res = rectangle.area(19, 50)
        self.assertEqual(950, res)

    def test_area_19_51_values(self):
        res = rectangle.area(19, 51)
        self.assertEqual(969, res)

    def test_area_19_52_values(self):
        res = rectangle.area(19, 52)
        self.assertEqual(988, res)

    def test_area_19_53_values(self):
        res = rectangle.area(19, 53)
        self.assertEqual(1007, res)

    def test_area_19_54_values(self):
        res = rectangle.area(19, 54)
        self.assertEqual(1026, res)

    def test_area_19_55_values(self):
        res = rectangle.area(19, 55)
        self.assertEqual(1045, res)

    def test_area_19_56_values(self):
        res = rectangle.area(19, 56)
        self.assertEqual(1064, res)

    def test_area_19_57_values(self):
        res = rectangle.area(19, 57)
        self.assertEqual(1083, res)

    def test_area_19_58_values(self):
        res = rectangle.area(19, 58)
        self.assertEqual(1102, res)

    def test_area_19_59_values(self):
        res = rectangle.area(19, 59)
        self.assertEqual(1121, res)

    def test_area_20_30_values(self):
        res = rectangle.area(20, 30)
        self.assertEqual(600, res)

    def test_area_20_31_values(self):
        res = rectangle.area(20, 31)
        self.assertEqual(620, res)

    def test_area_20_32_values(self):
        res = rectangle.area(20, 32)
        self.assertEqual(640, res)

    def test_area_20_33_values(self):
        res = rectangle.area(20, 33)
        self.assertEqual(660, res)

    def test_area_20_34_values(self):
        res = rectangle.area(20, 34)
        self.assertEqual(680, res)

    def test_area_20_35_values(self):
        res = rectangle.area(20, 35)
        self.assertEqual(700, res)

    def test_area_20_36_values(self):
        res = rectangle.area(20, 36)
        self.assertEqual(720, res)

    def test_area_20_37_values(self):
        res = rectangle.area(20, 37)
        self.assertEqual(740, res)

    def test_area_20_38_values(self):
        res = rectangle.area(20, 38)
        self.assertEqual(760, res)

    def test_area_20_39_values(self):
        res = rectangle.area(20, 39)
        self.assertEqual(780, res)

    def test_area_20_40_values(self):
        res = rectangle.area(20, 40)
        self.assertEqual(800, res)

    def test_area_20_41_values(self):
        res = rectangle.area(20, 41)
        self.assertEqual(820, res)

    def test_area_20_42_values(self):
        res = rectangle.area(20, 42)
        self.assertEqual(840, res)

    def test_area_20_43_values(self):
        res = rectangle.area(20, 43)
        self.assertEqual(860, res)

    def test_area_20_44_values(self):
        res = rectangle.area(20, 44)
        self.assertEqual(880, res)

    def test_area_20_45_values(self):
        res = rectangle.area(20, 45)
        self.assertEqual(900, res)

    def test_area_20_46_values(self):
        res = rectangle.area(20, 46)
        self.assertEqual(920, res)

    def test_area_20_47_values(self):
        res = rectangle.area(20, 47)
        self.assertEqual(940, res)

    def test_area_20_48_values(self):
        res = rectangle.area(20, 48)
        self.assertEqual(960, res)

    def test_area_20_49_values(self):
        res = rectangle.area(20, 49)
        self.assertEqual(980, res)

    def test_area_20_50_values(self):
        res = rectangle.area(20, 50)
        self.assertEqual(1000, res)

    def test_area_20_51_values(self):
        res = rectangle.area(20, 51)
        self.assertEqual(1020, res)

    def test_area_20_52_values(self):
        res = rectangle.area(20, 52)
        self.assertEqual(1040, res)

    def test_area_20_53_values(self):
        res = rectangle.area(20, 53)
        self.assertEqual(1060, res)

    def test_area_20_54_values(self):
        res = rectangle.area(20, 54)
        self.assertEqual(1080, res)

    def test_area_20_55_values(self):
        res = rectangle.area(20, 55)
        self.assertEqual(1100, res)

    def test_area_20_56_values(self):
        res = rectangle.area(20, 56)
        self.assertEqual(1120, res)

    def test_area_20_57_values(self):
        res = rectangle.area(20, 57)
        self.assertEqual(1140, res)

    def test_area_20_58_values(self):
        res = rectangle.area(20, 58)
        self.assertEqual(1160, res)

    def test_area_20_59_values(self):
        res = rectangle.area(20, 59)
        self.assertEqual(1180, res)

    def test_area_21_30_values(self):
        res = rectangle.area(21, 30)
        self.assertEqual(630, res)

    def test_area_21_31_values(self):
        res = rectangle.area(21, 31)
        self.assertEqual(651, res)

    def test_area_21_32_values(self):
        res = rectangle.area(21, 32)
        self.assertEqual(672, res)

    def test_area_21_33_values(self):
        res = rectangle.area(21, 33)
        self.assertEqual(693, res)

    def test_area_21_34_values(self):
        res = rectangle.area(21, 34)
        self.assertEqual(714, res)

    def test_area_21_35_values(self):
        res = rectangle.area(21, 35)
        self.assertEqual(735, res)

    def test_area_21_36_values(self):
        res = rectangle.area(21, 36)
        self.assertEqual(756, res)

    def test_area_21_37_values(self):
        res = rectangle.area(21, 37)
        self.assertEqual(777, res)

    def test_area_21_38_values(self):
        res = rectangle.area(21, 38)
        self.assertEqual(798, res)

    def test_area_21_39_values(self):
        res = rectangle.area(21, 39)
        self.assertEqual(819, res)

    def test_area_21_40_values(self):
        res = rectangle.area(21, 40)
        self.assertEqual(840, res)

    def test_area_21_41_values(self):
        res = rectangle.area(21, 41)
        self.assertEqual(861, res)

    def test_area_21_42_values(self):
        res = rectangle.area(21, 42)
        self.assertEqual(882, res)

    def test_area_21_43_values(self):
        res = rectangle.area(21, 43)
        self.assertEqual(903, res)

    def test_area_21_44_values(self):
        res = rectangle.area(21, 44)
        self.assertEqual(924, res)

    def test_area_21_45_values(self):
        res = rectangle.area(21, 45)
        self.assertEqual(945, res)

    def test_area_21_46_values(self):
        res = rectangle.area(21, 46)
        self.assertEqual(966, res)

    def test_area_21_47_values(self):
        res = rectangle.area(21, 47)
        self.assertEqual(987, res)

    def test_area_21_48_values(self):
        res = rectangle.area(21, 48)
        self.assertEqual(1008, res)

    def test_area_21_49_values(self):
        res = rectangle.area(21, 49)
        self.assertEqual(1029, res)

    def test_area_21_50_values(self):
        res = rectangle.area(21, 50)
        self.assertEqual(1050, res)

    def test_area_21_51_values(self):
        res = rectangle.area(21, 51)
        self.assertEqual(1071, res)

    def test_area_21_52_values(self):
        res = rectangle.area(21, 52)
        self.assertEqual(1092, res)

    def test_area_21_53_values(self):
        res = rectangle.area(21, 53)
        self.assertEqual(1113, res)

    def test_area_21_54_values(self):
        res = rectangle.area(21, 54)
        self.assertEqual(1134, res)

    def test_area_21_55_values(self):
        res = rectangle.area(21, 55)
        self.assertEqual(1155, res)

    def test_area_21_56_values(self):
        res = rectangle.area(21, 56)
        self.assertEqual(1176, res)

    def test_area_21_57_values(self):
        res = rectangle.area(21, 57)
        self.assertEqual(1197, res)

    def test_area_21_58_values(self):
        res = rectangle.area(21, 58)
        self.assertEqual(1218, res)

    def test_area_21_59_values(self):
        res = rectangle.area(21, 59)
        self.assertEqual(1239, res)

    def test_area_22_30_values(self):
        res = rectangle.area(22, 30)
        self.assertEqual(660, res)

    def test_area_22_31_values(self):
        res = rectangle.area(22, 31)
        self.assertEqual(682, res)

    def test_area_22_32_values(self):
        res = rectangle.area(22, 32)
        self.assertEqual(704, res)

    def test_area_22_33_values(self):
        res = rectangle.area(22, 33)
        self.assertEqual(726, res)

    def test_area_22_34_values(self):
        res = rectangle.area(22, 34)
        self.assertEqual(748, res)

    def test_area_22_35_values(self):
        res = rectangle.area(22, 35)
        self.assertEqual(770, res)

    def test_area_22_36_values(self):
        res = rectangle.area(22, 36)
        self.assertEqual(792, res)

    def test_area_22_37_values(self):
        res = rectangle.area(22, 37)
        self.assertEqual(814, res)

    def test_area_22_38_values(self):
        res = rectangle.area(22, 38)
        self.assertEqual(836, res)

    def test_area_22_39_values(self):
        res = rectangle.area(22, 39)
        self.assertEqual(858, res)

    def test_area_22_40_values(self):
        res = rectangle.area(22, 40)
        self.assertEqual(880, res)

    def test_area_22_41_values(self):
        res = rectangle.area(22, 41)
        self.assertEqual(902, res)

    def test_area_22_42_values(self):
        res = rectangle.area(22, 42)
        self.assertEqual(924, res)

    def test_area_22_43_values(self):
        res = rectangle.area(22, 43)
        self.assertEqual(946, res)

    def test_area_22_44_values(self):
        res = rectangle.area(22, 44)
        self.assertEqual(968, res)

    def test_area_22_45_values(self):
        res = rectangle.area(22, 45)
        self.assertEqual(990, res)

    def test_area_22_46_values(self):
        res = rectangle.area(22, 46)
        self.assertEqual(1012, res)

    def test_area_22_47_values(self):
        res = rectangle.area(22, 47)
        self.assertEqual(1034, res)

    def test_area_22_48_values(self):
        res = rectangle.area(22, 48)
        self.assertEqual(1056, res)

    def test_area_22_49_values(self):
        res = rectangle.area(22, 49)
        self.assertEqual(1078, res)

    def test_area_22_50_values(self):
        res = rectangle.area(22, 50)
        self.assertEqual(1100, res)

    def test_area_22_51_values(self):
        res = rectangle.area(22, 51)
        self.assertEqual(1122, res)

    def test_area_22_52_values(self):
        res = rectangle.area(22, 52)
        self.assertEqual(1144, res)

    def test_area_22_53_values(self):
        res = rectangle.area(22, 53)
        self.assertEqual(1166, res)

    def test_area_22_54_values(self):
        res = rectangle.area(22, 54)
        self.assertEqual(1188, res)

    def test_area_22_55_values(self):
        res = rectangle.area(22, 55)
        self.assertEqual(1210, res)

    def test_area_22_56_values(self):
        res = rectangle.area(22, 56)
        self.assertEqual(1232, res)

    def test_area_22_57_values(self):
        res = rectangle.area(22, 57)
        self.assertEqual(1254, res)

    def test_area_22_58_values(self):
        res = rectangle.area(22, 58)
        self.assertEqual(1276, res)

    def test_area_22_59_values(self):
        res = rectangle.area(22, 59)
        self.assertEqual(1298, res)

    def test_area_23_30_values(self):
        res = rectangle.area(23, 30)
        self.assertEqual(690, res)

    def test_area_23_31_values(self):
        res = rectangle.area(23, 31)
        self.assertEqual(713, res)

    def test_area_23_32_values(self):
        res = rectangle.area(23, 32)
        self.assertEqual(736, res)

    def test_area_23_33_values(self):
        res = rectangle.area(23, 33)
        self.assertEqual(759, res)

    def test_area_23_34_values(self):
        res = rectangle.area(23, 34)
        self.assertEqual(782, res)

    def test_area_23_35_values(self):
        res = rectangle.area(23, 35)
        self.assertEqual(805, res)

    def test_area_23_36_values(self):
        res = rectangle.area(23, 36)
        self.assertEqual(828, res)

    def test_area_23_37_values(self):
        res = rectangle.area(23, 37)
        self.assertEqual(851, res)

    def test_area_23_38_values(self):
        res = rectangle.area(23, 38)
        self.assertEqual(874, res)

    def test_area_23_39_values(self):
        res = rectangle.area(23, 39)
        self.assertEqual(897, res)

    def test_area_23_40_values(self):
        res = rectangle.area(23, 40)
        self.assertEqual(920, res)

    def test_area_23_41_values(self):
        res = rectangle.area(23, 41)
        self.assertEqual(943, res)

    def test_area_23_42_values(self):
        res = rectangle.area(23, 42)
        self.assertEqual(966, res)

    def test_area_23_43_values(self):
        res = rectangle.area(23, 43)
        self.assertEqual(989, res)

    def test_area_23_44_values(self):
        res = rectangle.area(23, 44)
        self.assertEqual(1012, res)

    def test_area_23_45_values(self):
        res = rectangle.area(23, 45)
        self.assertEqual(1035, res)

    def test_area_23_46_values(self):
        res = rectangle.area(23, 46)
        self.assertEqual(1058, res)

    def test_area_23_47_values(self):
        res = rectangle.area(23, 47)
        self.assertEqual(1081, res)

    def test_area_23_48_values(self):
        res = rectangle.area(23, 48)
        self.assertEqual(1104, res)

    def test_area_23_49_values(self):
        res = rectangle.area(23, 49)
        self.assertEqual(1127, res)

    def test_area_23_50_values(self):
        res = rectangle.area(23, 50)
        self.assertEqual(1150, res)

    def test_area_23_51_values(self):
        res = rectangle.area(23, 51)
        self.assertEqual(1173, res)

    def test_area_23_52_values(self):
        res = rectangle.area(23, 52)
        self.assertEqual(1196, res)

    def test_area_23_53_values(self):
        res = rectangle.area(23, 53)
        self.assertEqual(1219, res)

    def test_area_23_54_values(self):
        res = rectangle.area(23, 54)
        self.assertEqual(1242, res)

    def test_area_23_55_values(self):
        res = rectangle.area(23, 55)
        self.assertEqual(1265, res)

    def test_area_23_56_values(self):
        res = rectangle.area(23, 56)
        self.assertEqual(1288, res)

    def test_area_23_57_values(self):
        res = rectangle.area(23, 57)
        self.assertEqual(1311, res)

    def test_area_23_58_values(self):
        res = rectangle.area(23, 58)
        self.assertEqual(1334, res)

    def test_area_23_59_values(self):
        res = rectangle.area(23, 59)
        self.assertEqual(1357, res)

    def test_area_24_30_values(self):
        res = rectangle.area(24, 30)
        self.assertEqual(720, res)

    def test_area_24_31_values(self):
        res = rectangle.area(24, 31)
        self.assertEqual(744, res)

    def test_area_24_32_values(self):
        res = rectangle.area(24, 32)
        self.assertEqual(768, res)

    def test_area_24_33_values(self):
        res = rectangle.area(24, 33)
        self.assertEqual(792, res)

    def test_area_24_34_values(self):
        res = rectangle.area(24, 34)
        self.assertEqual(816, res)

    def test_area_24_35_values(self):
        res = rectangle.area(24, 35)
        self.assertEqual(840, res)

    def test_area_24_36_values(self):
        res = rectangle.area(24, 36)
        self.assertEqual(864, res)

    def test_area_24_37_values(self):
        res = rectangle.area(24, 37)
        self.assertEqual(888, res)

    def test_area_24_38_values(self):
        res = rectangle.area(24, 38)
        self.assertEqual(912, res)

    def test_area_24_39_values(self):
        res = rectangle.area(24, 39)
        self.assertEqual(936, res)

    def test_area_24_40_values(self):
        res = rectangle.area(24, 40)
        self.assertEqual(960, res)

    def test_area_24_41_values(self):
        res = rectangle.area(24, 41)
        self.assertEqual(984, res)

    def test_area_24_42_values(self):
        res = rectangle.area(24, 42)
        self.assertEqual(1008, res)

    def test_area_24_43_values(self):
        res = rectangle.area(24, 43)
        self.assertEqual(1032, res)

    def test_area_24_44_values(self):
        res = rectangle.area(24, 44)
        self.assertEqual(1056, res)

    def test_area_24_45_values(self):
        res = rectangle.area(24, 45)
        self.assertEqual(1080, res)

    def test_area_24_46_values(self):
        res = rectangle.area(24, 46)
        self.assertEqual(1104, res)

    def test_area_24_47_values(self):
        res = rectangle.area(24, 47)
        self.assertEqual(1128, res)

    def test_area_24_48_values(self):
        res = rectangle.area(24, 48)
        self.assertEqual(1152, res)

    def test_area_24_49_values(self):
        res = rectangle.area(24, 49)
        self.assertEqual(1176, res)

    def test_area_24_50_values(self):
        res = rectangle.area(24, 50)
        self.assertEqual(1200, res)

    def test_area_24_51_values(self):
        res = rectangle.area(24, 51)
        self.assertEqual(1224, res)

    def test_area_24_52_values(self):
        res = rectangle.area(24, 52)
        self.assertEqual(1248, res)

    def test_area_24_53_values(self):
        res = rectangle.area(24, 53)
        self.assertEqual(1272, res)

    def test_area_24_54_values(self):
        res = rectangle.area(24, 54)
        self.assertEqual(1296, res)

    def test_area_24_55_values(self):
        res = rectangle.area(24, 55)
        self.assertEqual(1320, res)

    def test_area_24_56_values(self):
        res = rectangle.area(24, 56)
        self.assertEqual(1344, res)

    def test_area_24_57_values(self):
        res = rectangle.area(24, 57)
        self.assertEqual(1368, res)

    def test_area_24_58_values(self):
        res = rectangle.area(24, 58)
        self.assertEqual(1392, res)

    def test_area_24_59_values(self):
        res = rectangle.area(24, 59)
        self.assertEqual(1416, res)

    def test_area_25_30_values(self):
        res = rectangle.area(25, 30)
        self.assertEqual(750, res)

    def test_area_25_31_values(self):
        res = rectangle.area(25, 31)
        self.assertEqual(775, res)

    def test_area_25_32_values(self):
        res = rectangle.area(25, 32)
        self.assertEqual(800, res)

    def test_area_25_33_values(self):
        res = rectangle.area(25, 33)
        self.assertEqual(825, res)

    def test_area_25_34_values(self):
        res = rectangle.area(25, 34)
        self.assertEqual(850, res)

    def test_area_25_35_values(self):
        res = rectangle.area(25, 35)
        self.assertEqual(875, res)

    def test_area_25_36_values(self):
        res = rectangle.area(25, 36)
        self.assertEqual(900, res)

    def test_area_25_37_values(self):
        res = rectangle.area(25, 37)
        self.assertEqual(925, res)

    def test_area_25_38_values(self):
        res = rectangle.area(25, 38)
        self.assertEqual(950, res)

    def test_area_25_39_values(self):
        res = rectangle.area(25, 39)
        self.assertEqual(975, res)

    def test_area_25_40_values(self):
        res = rectangle.area(25, 40)
        self.assertEqual(1000, res)

    def test_area_25_41_values(self):
        res = rectangle.area(25, 41)
        self.assertEqual(1025, res)

    def test_area_25_42_values(self):
        res = rectangle.area(25, 42)
        self.assertEqual(1050, res)

    def test_area_25_43_values(self):
        res = rectangle.area(25, 43)
        self.assertEqual(1075, res)

    def test_area_25_44_values(self):
        res = rectangle.area(25, 44)
        self.assertEqual(1100, res)

    def test_area_25_45_values(self):
        res = rectangle.area(25, 45)
        self.assertEqual(1125, res)

    def test_area_25_46_values(self):
        res = rectangle.area(25, 46)
        self.assertEqual(1150, res)

    def test_area_25_47_values(self):
        res = rectangle.area(25, 47)
        self.assertEqual(1175, res)

    def test_area_25_48_values(self):
        res = rectangle.area(25, 48)
        self.assertEqual(1200, res)

    def test_area_25_49_values(self):
        res = rectangle.area(25, 49)
        self.assertEqual(1225, res)

    def test_area_25_50_values(self):
        res = rectangle.area(25, 50)
        self.assertEqual(1250, res)

    def test_area_25_51_values(self):
        res = rectangle.area(25, 51)
        self.assertEqual(1275, res)

    def test_area_25_52_values(self):
        res = rectangle.area(25, 52)
        self.assertEqual(1300, res)

    def test_area_25_53_values(self):
        res = rectangle.area(25, 53)
        self.assertEqual(1325, res)

    def test_area_25_54_values(self):
        res = rectangle.area(25, 54)
        self.assertEqual(1350, res)

    def test_area_25_55_values(self):
        res = rectangle.area(25, 55)
        self.assertEqual(1375, res)

    def test_area_25_56_values(self):
        res = rectangle.area(25, 56)
        self.assertEqual(1400, res)

    def test_area_25_57_values(self):
        res = rectangle.area(25, 57)
        self.assertEqual(1425, res)

    def test_area_25_58_values(self):
        res = rectangle.area(25, 58)
        self.assertEqual(1450, res)

    def test_area_25_59_values(self):
        res = rectangle.area(25, 59)
        self.assertEqual(1475, res)

    def test_area_26_30_values(self):
        res = rectangle.area(26, 30)
        self.assertEqual(780, res)

    def test_area_26_31_values(self):
        res = rectangle.area(26, 31)
        self.assertEqual(806, res)

    def test_area_26_32_values(self):
        res = rectangle.area(26, 32)
        self.assertEqual(832, res)

    def test_area_26_33_values(self):
        res = rectangle.area(26, 33)
        self.assertEqual(858, res)

    def test_area_26_34_values(self):
        res = rectangle.area(26, 34)
        self.assertEqual(884, res)

    def test_area_26_35_values(self):
        res = rectangle.area(26, 35)
        self.assertEqual(910, res)

    def test_area_26_36_values(self):
        res = rectangle.area(26, 36)
        self.assertEqual(936, res)

    def test_area_26_37_values(self):
        res = rectangle.area(26, 37)
        self.assertEqual(962, res)

    def test_area_26_38_values(self):
        res = rectangle.area(26, 38)
        self.assertEqual(988, res)

    def test_area_26_39_values(self):
        res = rectangle.area(26, 39)
        self.assertEqual(1014, res)

    def test_area_26_40_values(self):
        res = rectangle.area(26, 40)
        self.assertEqual(1040, res)

    def test_area_26_41_values(self):
        res = rectangle.area(26, 41)
        self.assertEqual(1066, res)

    def test_area_26_42_values(self):
        res = rectangle.area(26, 42)
        self.assertEqual(1092, res)

    def test_area_26_43_values(self):
        res = rectangle.area(26, 43)
        self.assertEqual(1118, res)

    def test_area_26_44_values(self):
        res = rectangle.area(26, 44)
        self.assertEqual(1144, res)

    def test_area_26_45_values(self):
        res = rectangle.area(26, 45)
        self.assertEqual(1170, res)

    def test_area_26_46_values(self):
        res = rectangle.area(26, 46)
        self.assertEqual(1196, res)

    def test_area_26_47_values(self):
        res = rectangle.area(26, 47)
        self.assertEqual(1222, res)

    def test_area_26_48_values(self):
        res = rectangle.area(26, 48)
        self.assertEqual(1248, res)

    def test_area_26_49_values(self):
        res = rectangle.area(26, 49)
        self.assertEqual(1274, res)

    def test_area_26_50_values(self):
        res = rectangle.area(26, 50)
        self.assertEqual(1300, res)

    def test_area_26_51_values(self):
        res = rectangle.area(26, 51)
        self.assertEqual(1326, res)

    def test_area_26_52_values(self):
        res = rectangle.area(26, 52)
        self.assertEqual(1352, res)

    def test_area_26_53_values(self):
        res = rectangle.area(26, 53)
        self.assertEqual(1378, res)

    def test_area_26_54_values(self):
        res = rectangle.area(26, 54)
        self.assertEqual(1404, res)

    def test_area_26_55_values(self):
        res = rectangle.area(26, 55)
        self.assertEqual(1430, res)

    def test_area_26_56_values(self):
        res = rectangle.area(26, 56)
        self.assertEqual(1456, res)

    def test_area_26_57_values(self):
        res = rectangle.area(26, 57)
        self.assertEqual(1482, res)

    def test_area_26_58_values(self):
        res = rectangle.area(26, 58)
        self.assertEqual(1508, res)

    def test_area_26_59_values(self):
        res = rectangle.area(26, 59)
        self.assertEqual(1534, res)

    def test_area_27_30_values(self):
        res = rectangle.area(27, 30)
        self.assertEqual(810, res)

    def test_area_27_31_values(self):
        res = rectangle.area(27, 31)
        self.assertEqual(837, res)

    def test_area_27_32_values(self):
        res = rectangle.area(27, 32)
        self.assertEqual(864, res)

    def test_area_27_33_values(self):
        res = rectangle.area(27, 33)
        self.assertEqual(891, res)

    def test_area_27_34_values(self):
        res = rectangle.area(27, 34)
        self.assertEqual(918, res)

    def test_area_27_35_values(self):
        res = rectangle.area(27, 35)
        self.assertEqual(945, res)

    def test_area_27_36_values(self):
        res = rectangle.area(27, 36)
        self.assertEqual(972, res)

    def test_area_27_37_values(self):
        res = rectangle.area(27, 37)
        self.assertEqual(999, res)

    def test_area_27_38_values(self):
        res = rectangle.area(27, 38)
        self.assertEqual(1026, res)

    def test_area_27_39_values(self):
        res = rectangle.area(27, 39)
        self.assertEqual(1053, res)

    def test_area_27_40_values(self):
        res = rectangle.area(27, 40)
        self.assertEqual(1080, res)

    def test_area_27_41_values(self):
        res = rectangle.area(27, 41)
        self.assertEqual(1107, res)

    def test_area_27_42_values(self):
        res = rectangle.area(27, 42)
        self.assertEqual(1134, res)

    def test_area_27_43_values(self):
        res = rectangle.area(27, 43)
        self.assertEqual(1161, res)

    def test_area_27_44_values(self):
        res = rectangle.area(27, 44)
        self.assertEqual(1188, res)

    def test_area_27_45_values(self):
        res = rectangle.area(27, 45)
        self.assertEqual(1215, res)

    def test_area_27_46_values(self):
        res = rectangle.area(27, 46)
        self.assertEqual(1242, res)

    def test_area_27_47_values(self):
        res = rectangle.area(27, 47)
        self.assertEqual(1269, res)

    def test_area_27_48_values(self):
        res = rectangle.area(27, 48)
        self.assertEqual(1296, res)

    def test_area_27_49_values(self):
        res = rectangle.area(27, 49)
        self.assertEqual(1323, res)

    def test_area_27_50_values(self):
        res = rectangle.area(27, 50)
        self.assertEqual(1350, res)

    def test_area_27_51_values(self):
        res = rectangle.area(27, 51)
        self.assertEqual(1377, res)

    def test_area_27_52_values(self):
        res = rectangle.area(27, 52)
        self.assertEqual(1404, res)

    def test_area_27_53_values(self):
        res = rectangle.area(27, 53)
        self.assertEqual(1431, res)

    def test_area_27_54_values(self):
        res = rectangle.area(27, 54)
        self.assertEqual(1458, res)

    def test_area_27_55_values(self):
        res = rectangle.area(27, 55)
        self.assertEqual(1485, res)

    def test_area_27_56_values(self):
        res = rectangle.area(27, 56)
        self.assertEqual(1512, res)

    def test_area_27_57_values(self):
        res = rectangle.area(27, 57)
        self.assertEqual(1539, res)

    def test_area_27_58_values(self):
        res = rectangle.area(27, 58)
        self.assertEqual(1566, res)

    def test_area_27_59_values(self):
        res = rectangle.area(27, 59)
        self.assertEqual(1593, res)

    def test_area_28_30_values(self):
        res = rectangle.area(28, 30)
        self.assertEqual(840, res)

    def test_area_28_31_values(self):
        res = rectangle.area(28, 31)
        self.assertEqual(868, res)

    def test_area_28_32_values(self):
        res = rectangle.area(28, 32)
        self.assertEqual(896, res)

    def test_area_28_33_values(self):
        res = rectangle.area(28, 33)
        self.assertEqual(924, res)

    def test_area_28_34_values(self):
        res = rectangle.area(28, 34)
        self.assertEqual(952, res)

    def test_area_28_35_values(self):
        res = rectangle.area(28, 35)
        self.assertEqual(980, res)

    def test_area_28_36_values(self):
        res = rectangle.area(28, 36)
        self.assertEqual(1008, res)

    def test_area_28_37_values(self):
        res = rectangle.area(28, 37)
        self.assertEqual(1036, res)

    def test_area_28_38_values(self):
        res = rectangle.area(28, 38)
        self.assertEqual(1064, res)

    def test_area_28_39_values(self):
        res = rectangle.area(28, 39)
        self.assertEqual(1092, res)

    def test_area_28_40_values(self):
        res = rectangle.area(28, 40)
        self.assertEqual(1120, res)

    def test_area_28_41_values(self):
        res = rectangle.area(28, 41)
        self.assertEqual(1148, res)

    def test_area_28_42_values(self):
        res = rectangle.area(28, 42)
        self.assertEqual(1176, res)

    def test_area_28_43_values(self):
        res = rectangle.area(28, 43)
        self.assertEqual(1204, res)

    def test_area_28_44_values(self):
        res = rectangle.area(28, 44)
        self.assertEqual(1232, res)

    def test_area_28_45_values(self):
        res = rectangle.area(28, 45)
        self.assertEqual(1260, res)

    def test_area_28_46_values(self):
        res = rectangle.area(28, 46)
        self.assertEqual(1288, res)

    def test_area_28_47_values(self):
        res = rectangle.area(28, 47)
        self.assertEqual(1316, res)

    def test_area_28_48_values(self):
        res = rectangle.area(28, 48)
        self.assertEqual(1344, res)

    def test_area_28_49_values(self):
        res = rectangle.area(28, 49)
        self.assertEqual(1372, res)

    def test_area_28_50_values(self):
        res = rectangle.area(28, 50)
        self.assertEqual(1400, res)

    def test_area_28_51_values(self):
        res = rectangle.area(28, 51)
        self.assertEqual(1428, res)

    def test_area_28_52_values(self):
        res = rectangle.area(28, 52)
        self.assertEqual(1456, res)

    def test_area_28_53_values(self):
        res = rectangle.area(28, 53)
        self.assertEqual(1484, res)

    def test_area_28_54_values(self):
        res = rectangle.area(28, 54)
        self.assertEqual(1512, res)

    def test_area_28_55_values(self):
        res = rectangle.area(28, 55)
        self.assertEqual(1540, res)

    def test_area_28_56_values(self):
        res = rectangle.area(28, 56)
        self.assertEqual(1568, res)

    def test_area_28_57_values(self):
        res = rectangle.area(28, 57)
        self.assertEqual(1596, res)

    def test_area_28_58_values(self):
        res = rectangle.area(28, 58)
        self.assertEqual(1624, res)

    def test_area_28_59_values(self):
        res = rectangle.area(28, 59)
        self.assertEqual(1652, res)

    def test_area_29_30_values(self):
        res = rectangle.area(29, 30)
        self.assertEqual(870, res)

    def test_area_29_31_values(self):
        res = rectangle.area(29, 31)
        self.assertEqual(899, res)

    def test_area_29_32_values(self):
        res = rectangle.area(29, 32)
        self.assertEqual(928, res)

    def test_area_29_33_values(self):
        res = rectangle.area(29, 33)
        self.assertEqual(957, res)

    def test_area_29_34_values(self):
        res = rectangle.area(29, 34)
        self.assertEqual(986, res)

    def test_area_29_35_values(self):
        res = rectangle.area(29, 35)
        self.assertEqual(1015, res)

    def test_area_29_36_values(self):
        res = rectangle.area(29, 36)
        self.assertEqual(1044, res)

    def test_area_29_37_values(self):
        res = rectangle.area(29, 37)
        self.assertEqual(1073, res)

    def test_area_29_38_values(self):
        res = rectangle.area(29, 38)
        self.assertEqual(1102, res)

    def test_area_29_39_values(self):
        res = rectangle.area(29, 39)
        self.assertEqual(1131, res)

    def test_area_29_40_values(self):
        res = rectangle.area(29, 40)
        self.assertEqual(1160, res)

    def test_area_29_41_values(self):
        res = rectangle.area(29, 41)
        self.assertEqual(1189, res)

    def test_area_29_42_values(self):
        res = rectangle.area(29, 42)
        self.assertEqual(1218, res)

    def test_area_29_43_values(self):
        res = rectangle.area(29, 43)
        self.assertEqual(1247, res)

    def test_area_29_44_values(self):
        res = rectangle.area(29, 44)
        self.assertEqual(1276, res)

    def test_area_29_45_values(self):
        res = rectangle.area(29, 45)
        self.assertEqual(1305, res)

    def test_area_29_46_values(self):
        res = rectangle.area(29, 46)
        self.assertEqual(1334, res)

    def test_area_29_47_values(self):
        res = rectangle.area(29, 47)
        self.assertEqual(1363, res)

    def test_area_29_48_values(self):
        res = rectangle.area(29, 48)
        self.assertEqual(1392, res)

    def test_area_29_49_values(self):
        res = rectangle.area(29, 49)
        self.assertEqual(1421, res)

    def test_area_29_50_values(self):
        res = rectangle.area(29, 50)
        self.assertEqual(1450, res)

    def test_area_29_51_values(self):
        res = rectangle.area(29, 51)
        self.assertEqual(1479, res)

    def test_area_29_52_values(self):
        res = rectangle.area(29, 52)
        self.assertEqual(1508, res)

    def test_area_29_53_values(self):
        res = rectangle.area(29, 53)
        self.assertEqual(1537, res)

    def test_area_29_54_values(self):
        res = rectangle.area(29, 54)
        self.assertEqual(1566, res)

    def test_area_29_55_values(self):
        res = rectangle.area(29, 55)
        self.assertEqual(1595, res)

    def test_area_29_56_values(self):
        res = rectangle.area(29, 56)
        self.assertEqual(1624, res)

    def test_area_29_57_values(self):
        res = rectangle.area(29, 57)
        self.assertEqual(1653, res)

    def test_area_29_58_values(self):
        res = rectangle.area(29, 58)
        self.assertEqual(1682, res)

    def test_area_29_59_values(self):
        res = rectangle.area(29, 59)
        self.assertEqual(1711, res)

    def test_area_30_30_values(self):
        res = rectangle.area(30, 30)
        self.assertEqual(900, res)

    def test_area_30_31_values(self):
        res = rectangle.area(30, 31)
        self.assertEqual(930, res)

    def test_area_30_32_values(self):
        res = rectangle.area(30, 32)
        self.assertEqual(960, res)

    def test_area_30_33_values(self):
        res = rectangle.area(30, 33)
        self.assertEqual(990, res)

    def test_area_30_34_values(self):
        res = rectangle.area(30, 34)
        self.assertEqual(1020, res)

    def test_area_30_35_values(self):
        res = rectangle.area(30, 35)
        self.assertEqual(1050, res)

    def test_area_30_36_values(self):
        res = rectangle.area(30, 36)
        self.assertEqual(1080, res)

    def test_area_30_37_values(self):
        res = rectangle.area(30, 37)
        self.assertEqual(1110, res)

    def test_area_30_38_values(self):
        res = rectangle.area(30, 38)
        self.assertEqual(1140, res)

    def test_area_30_39_values(self):
        res = rectangle.area(30, 39)
        self.assertEqual(1170, res)

    def test_area_30_40_values(self):
        res = rectangle.area(30, 40)
        self.assertEqual(1200, res)

    def test_area_30_41_values(self):
        res = rectangle.area(30, 41)
        self.assertEqual(1230, res)

    def test_area_30_42_values(self):
        res = rectangle.area(30, 42)
        self.assertEqual(1260, res)

    def test_area_30_43_values(self):
        res = rectangle.area(30, 43)
        self.assertEqual(1290, res)

    def test_area_30_44_values(self):
        res = rectangle.area(30, 44)
        self.assertEqual(1320, res)

    def test_area_30_45_values(self):
        res = rectangle.area(30, 45)
        self.assertEqual(1350, res)

    def test_area_30_46_values(self):
        res = rectangle.area(30, 46)
        self.assertEqual(1380, res)

    def test_area_30_47_values(self):
        res = rectangle.area(30, 47)
        self.assertEqual(1410, res)

    def test_area_30_48_values(self):
        res = rectangle.area(30, 48)
        self.assertEqual(1440, res)

    def test_area_30_49_values(self):
        res = rectangle.area(30, 49)
        self.assertEqual(1470, res)

    def test_area_30_50_values(self):
        res = rectangle.area(30, 50)
        self.assertEqual(1500, res)

    def test_area_30_51_values(self):
        res = rectangle.area(30, 51)
        self.assertEqual(1530, res)

    def test_area_30_52_values(self):
        res = rectangle.area(30, 52)
        self.assertEqual(1560, res)

    def test_area_30_53_values(self):
        res = rectangle.area(30, 53)
        self.assertEqual(1590, res)

    def test_area_30_54_values(self):
        res = rectangle.area(30, 54)
        self.assertEqual(1620, res)

    def test_area_30_55_values(self):
        res = rectangle.area(30, 55)
        self.assertEqual(1650, res)

    def test_area_30_56_values(self):
        res = rectangle.area(30, 56)
        self.assertEqual(1680, res)

    def test_area_30_57_values(self):
        res = rectangle.area(30, 57)
        self.assertEqual(1710, res)

    def test_area_30_58_values(self):
        res = rectangle.area(30, 58)
        self.assertEqual(1740, res)

    def test_area_30_59_values(self):
        res = rectangle.area(30, 59)
        self.assertEqual(1770, res)

    def test_area_31_30_values(self):
        res = rectangle.area(31, 30)
        self.assertEqual(930, res)

    def test_area_31_31_values(self):
        res = rectangle.area(31, 31)
        self.assertEqual(961, res)

    def test_area_31_32_values(self):
        res = rectangle.area(31, 32)
        self.assertEqual(992, res)

    def test_area_31_33_values(self):
        res = rectangle.area(31, 33)
        self.assertEqual(1023, res)

    def test_area_31_34_values(self):
        res = rectangle.area(31, 34)
        self.assertEqual(1054, res)

    def test_area_31_35_values(self):
        res = rectangle.area(31, 35)
        self.assertEqual(1085, res)

    def test_area_31_36_values(self):
        res = rectangle.area(31, 36)
        self.assertEqual(1116, res)

    def test_area_31_37_values(self):
        res = rectangle.area(31, 37)
        self.assertEqual(1147, res)

    def test_area_31_38_values(self):
        res = rectangle.area(31, 38)
        self.assertEqual(1178, res)

    def test_area_31_39_values(self):
        res = rectangle.area(31, 39)
        self.assertEqual(1209, res)

    def test_area_31_40_values(self):
        res = rectangle.area(31, 40)
        self.assertEqual(1240, res)

    def test_area_31_41_values(self):
        res = rectangle.area(31, 41)
        self.assertEqual(1271, res)

    def test_area_31_42_values(self):
        res = rectangle.area(31, 42)
        self.assertEqual(1302, res)

    def test_area_31_43_values(self):
        res = rectangle.area(31, 43)
        self.assertEqual(1333, res)

    def test_area_31_44_values(self):
        res = rectangle.area(31, 44)
        self.assertEqual(1364, res)

    def test_area_31_45_values(self):
        res = rectangle.area(31, 45)
        self.assertEqual(1395, res)

    def test_area_31_46_values(self):
        res = rectangle.area(31, 46)
        self.assertEqual(1426, res)

    def test_area_31_47_values(self):
        res = rectangle.area(31, 47)
        self.assertEqual(1457, res)

    def test_area_31_48_values(self):
        res = rectangle.area(31, 48)
        self.assertEqual(1488, res)

    def test_area_31_49_values(self):
        res = rectangle.area(31, 49)
        self.assertEqual(1519, res)

    def test_area_31_50_values(self):
        res = rectangle.area(31, 50)
        self.assertEqual(1550, res)

    def test_area_31_51_values(self):
        res = rectangle.area(31, 51)
        self.assertEqual(1581, res)

    def test_area_31_52_values(self):
        res = rectangle.area(31, 52)
        self.assertEqual(1612, res)

    def test_area_31_53_values(self):
        res = rectangle.area(31, 53)
        self.assertEqual(1643, res)

    def test_area_31_54_values(self):
        res = rectangle.area(31, 54)
        self.assertEqual(1674, res)

    def test_area_31_55_values(self):
        res = rectangle.area(31, 55)
        self.assertEqual(1705, res)

    def test_area_31_56_values(self):
        res = rectangle.area(31, 56)
        self.assertEqual(1736, res)

    def test_area_31_57_values(self):
        res = rectangle.area(31, 57)
        self.assertEqual(1767, res)

    def test_area_31_58_values(self):
        res = rectangle.area(31, 58)
        self.assertEqual(1798, res)

    def test_area_31_59_values(self):
        res = rectangle.area(31, 59)
        self.assertEqual(1829, res)

    def test_area_32_30_values(self):
        res = rectangle.area(32, 30)
        self.assertEqual(960, res)

    def test_area_32_31_values(self):
        res = rectangle.area(32, 31)
        self.assertEqual(992, res)

    def test_area_32_32_values(self):
        res = rectangle.area(32, 32)
        self.assertEqual(1024, res)

    def test_area_32_33_values(self):
        res = rectangle.area(32, 33)
        self.assertEqual(1056, res)

    def test_area_32_34_values(self):
        res = rectangle.area(32, 34)
        self.assertEqual(1088, res)

    def test_area_32_35_values(self):
        res = rectangle.area(32, 35)
        self.assertEqual(1120, res)

    def test_area_32_36_values(self):
        res = rectangle.area(32, 36)
        self.assertEqual(1152, res)

    def test_area_32_37_values(self):
        res = rectangle.area(32, 37)
        self.assertEqual(1184, res)

    def test_area_32_38_values(self):
        res = rectangle.area(32, 38)
        self.assertEqual(1216, res)

    def test_area_32_39_values(self):
        res = rectangle.area(32, 39)
        self.assertEqual(1248, res)

    def test_area_32_40_values(self):
        res = rectangle.area(32, 40)
        self.assertEqual(1280, res)

    def test_area_32_41_values(self):
        res = rectangle.area(32, 41)
        self.assertEqual(1312, res)

    def test_area_32_42_values(self):
        res = rectangle.area(32, 42)
        self.assertEqual(1344, res)

    def test_area_32_43_values(self):
        res = rectangle.area(32, 43)
        self.assertEqual(1376, res)

    def test_area_32_44_values(self):
        res = rectangle.area(32, 44)
        self.assertEqual(1408, res)

    def test_area_32_45_values(self):
        res = rectangle.area(32, 45)
        self.assertEqual(1440, res)

    def test_area_32_46_values(self):
        res = rectangle.area(32, 46)
        self.assertEqual(1472, res)

    def test_area_32_47_values(self):
        res = rectangle.area(32, 47)
        self.assertEqual(1504, res)

    def test_area_32_48_values(self):
        res = rectangle.area(32, 48)
        self.assertEqual(1536, res)

    def test_area_32_49_values(self):
        res = rectangle.area(32, 49)
        self.assertEqual(1568, res)

    def test_area_32_50_values(self):
        res = rectangle.area(32, 50)
        self.assertEqual(1600, res)

    def test_area_32_51_values(self):
        res = rectangle.area(32, 51)
        self.assertEqual(1632, res)

    def test_area_32_52_values(self):
        res = rectangle.area(32, 52)
        self.assertEqual(1664, res)

    def test_area_32_53_values(self):
        res = rectangle.area(32, 53)
        self.assertEqual(1696, res)

    def test_area_32_54_values(self):
        res = rectangle.area(32, 54)
        self.assertEqual(1728, res)

    def test_area_32_55_values(self):
        res = rectangle.area(32, 55)
        self.assertEqual(1760, res)

    def test_area_32_56_values(self):
        res = rectangle.area(32, 56)
        self.assertEqual(1792, res)

    def test_area_32_57_values(self):
        res = rectangle.area(32, 57)
        self.assertEqual(1824, res)

    def test_area_32_58_values(self):
        res = rectangle.area(32, 58)
        self.assertEqual(1856, res)

    def test_area_32_59_values(self):
        res = rectangle.area(32, 59)
        self.assertEqual(1888, res)

    def test_area_33_30_values(self):
        res = rectangle.area(33, 30)
        self.assertEqual(990, res)

    def test_area_33_31_values(self):
        res = rectangle.area(33, 31)
        self.assertEqual(1023, res)

    def test_area_33_32_values(self):
        res = rectangle.area(33, 32)
        self.assertEqual(1056, res)

    def test_area_33_33_values(self):
        res = rectangle.area(33, 33)
        self.assertEqual(1089, res)

    def test_area_33_34_values(self):
        res = rectangle.area(33, 34)
        self.assertEqual(1122, res)

    def test_area_33_35_values(self):
        res = rectangle.area(33, 35)
        self.assertEqual(1155, res)

    def test_area_33_36_values(self):
        res = rectangle.area(33, 36)
        self.assertEqual(1188, res)

    def test_area_33_37_values(self):
        res = rectangle.area(33, 37)
        self.assertEqual(1221, res)

    def test_area_33_38_values(self):
        res = rectangle.area(33, 38)
        self.assertEqual(1254, res)

    def test_area_33_39_values(self):
        res = rectangle.area(33, 39)
        self.assertEqual(1287, res)

    def test_area_33_40_values(self):
        res = rectangle.area(33, 40)
        self.assertEqual(1320, res)

    def test_area_33_41_values(self):
        res = rectangle.area(33, 41)
        self.assertEqual(1353, res)

    def test_area_33_42_values(self):
        res = rectangle.area(33, 42)
        self.assertEqual(1386, res)

    def test_area_33_43_values(self):
        res = rectangle.area(33, 43)
        self.assertEqual(1419, res)

    def test_area_33_44_values(self):
        res = rectangle.area(33, 44)
        self.assertEqual(1452, res)

    def test_area_33_45_values(self):
        res = rectangle.area(33, 45)
        self.assertEqual(1485, res)

    def test_area_33_46_values(self):
        res = rectangle.area(33, 46)
        self.assertEqual(1518, res)

    def test_area_33_47_values(self):
        res = rectangle.area(33, 47)
        self.assertEqual(1551, res)

    def test_area_33_48_values(self):
        res = rectangle.area(33, 48)
        self.assertEqual(1584, res)

    def test_area_33_49_values(self):
        res = rectangle.area(33, 49)
        self.assertEqual(1617, res)

    def test_area_33_50_values(self):
        res = rectangle.area(33, 50)
        self.assertEqual(1650, res)

    def test_area_33_51_values(self):
        res = rectangle.area(33, 51)
        self.assertEqual(1683, res)

    def test_area_33_52_values(self):
        res = rectangle.area(33, 52)
        self.assertEqual(1716, res)

    def test_area_33_53_values(self):
        res = rectangle.area(33, 53)
        self.assertEqual(1749, res)

    def test_area_33_54_values(self):
        res = rectangle.area(33, 54)
        self.assertEqual(1782, res)

    def test_area_33_55_values(self):
        res = rectangle.area(33, 55)
        self.assertEqual(1815, res)

    def test_area_33_56_values(self):
        res = rectangle.area(33, 56)
        self.assertEqual(1848, res)

    def test_area_33_57_values(self):
        res = rectangle.area(33, 57)
        self.assertEqual(1881, res)

    def test_area_33_58_values(self):
        res = rectangle.area(33, 58)
        self.assertEqual(1914, res)

    def test_area_33_59_values(self):
        res = rectangle.area(33, 59)
        self.assertEqual(1947, res)

    def test_area_34_30_values(self):
        res = rectangle.area(34, 30)
        self.assertEqual(1020, res)

    def test_area_34_31_values(self):
        res = rectangle.area(34, 31)
        self.assertEqual(1054, res)

    def test_area_34_32_values(self):
        res = rectangle.area(34, 32)
        self.assertEqual(1088, res)

    def test_area_34_33_values(self):
        res = rectangle.area(34, 33)
        self.assertEqual(1122, res)

    def test_area_34_34_values(self):
        res = rectangle.area(34, 34)
        self.assertEqual(1156, res)

    def test_area_34_35_values(self):
        res = rectangle.area(34, 35)
        self.assertEqual(1190, res)

    def test_area_34_36_values(self):
        res = rectangle.area(34, 36)
        self.assertEqual(1224, res)

    def test_area_34_37_values(self):
        res = rectangle.area(34, 37)
        self.assertEqual(1258, res)

    def test_area_34_38_values(self):
        res = rectangle.area(34, 38)
        self.assertEqual(1292, res)

    def test_area_34_39_values(self):
        res = rectangle.area(34, 39)
        self.assertEqual(1326, res)

    def test_area_34_40_values(self):
        res = rectangle.area(34, 40)
        self.assertEqual(1360, res)

    def test_area_34_41_values(self):
        res = rectangle.area(34, 41)
        self.assertEqual(1394, res)

    def test_area_34_42_values(self):
        res = rectangle.area(34, 42)
        self.assertEqual(1428, res)

    def test_area_34_43_values(self):
        res = rectangle.area(34, 43)
        self.assertEqual(1462, res)

    def test_area_34_44_values(self):
        res = rectangle.area(34, 44)
        self.assertEqual(1496, res)

    def test_area_34_45_values(self):
        res = rectangle.area(34, 45)
        self.assertEqual(1530, res)

    def test_area_34_46_values(self):
        res = rectangle.area(34, 46)
        self.assertEqual(1564, res)

    def test_area_34_47_values(self):
        res = rectangle.area(34, 47)
        self.assertEqual(1598, res)

    def test_area_34_48_values(self):
        res = rectangle.area(34, 48)
        self.assertEqual(1632, res)

    def test_area_34_49_values(self):
        res = rectangle.area(34, 49)
        self.assertEqual(1666, res)

    def test_area_34_50_values(self):
        res = rectangle.area(34, 50)
        self.assertEqual(1700, res)

    def test_area_34_51_values(self):
        res = rectangle.area(34, 51)
        self.assertEqual(1734, res)

    def test_area_34_52_values(self):
        res = rectangle.area(34, 52)
        self.assertEqual(1768, res)

    def test_area_34_53_values(self):
        res = rectangle.area(34, 53)
        self.assertEqual(1802, res)

    def test_area_34_54_values(self):
        res = rectangle.area(34, 54)
        self.assertEqual(1836, res)

    def test_area_34_55_values(self):
        res = rectangle.area(34, 55)
        self.assertEqual(1870, res)

    def test_area_34_56_values(self):
        res = rectangle.area(34, 56)
        self.assertEqual(1904, res)

    def test_area_34_57_values(self):
        res = rectangle.area(34, 57)
        self.assertEqual(1938, res)

    def test_area_34_58_values(self):
        res = rectangle.area(34, 58)
        self.assertEqual(1972, res)

    def test_area_34_59_values(self):
        res = rectangle.area(34, 59)
        self.assertEqual(2006, res)

    def test_area_35_30_values(self):
        res = rectangle.area(35, 30)
        self.assertEqual(1050, res)

    def test_area_35_31_values(self):
        res = rectangle.area(35, 31)
        self.assertEqual(1085, res)

    def test_area_35_32_values(self):
        res = rectangle.area(35, 32)
        self.assertEqual(1120, res)

    def test_area_35_33_values(self):
        res = rectangle.area(35, 33)
        self.assertEqual(1155, res)

    def test_area_35_34_values(self):
        res = rectangle.area(35, 34)
        self.assertEqual(1190, res)

    def test_area_35_35_values(self):
        res = rectangle.area(35, 35)
        self.assertEqual(1225, res)

    def test_area_35_36_values(self):
        res = rectangle.area(35, 36)
        self.assertEqual(1260, res)

    def test_area_35_37_values(self):
        res = rectangle.area(35, 37)
        self.assertEqual(1295, res)

    def test_area_35_38_values(self):
        res = rectangle.area(35, 38)
        self.assertEqual(1330, res)

    def test_area_35_39_values(self):
        res = rectangle.area(35, 39)
        self.assertEqual(1365, res)

    def test_area_35_40_values(self):
        res = rectangle.area(35, 40)
        self.assertEqual(1400, res)

    def test_area_35_41_values(self):
        res = rectangle.area(35, 41)
        self.assertEqual(1435, res)

    def test_area_35_42_values(self):
        res = rectangle.area(35, 42)
        self.assertEqual(1470, res)

    def test_area_35_43_values(self):
        res = rectangle.area(35, 43)
        self.assertEqual(1505, res)

    def test_area_35_44_values(self):
        res = rectangle.area(35, 44)
        self.assertEqual(1540, res)

    def test_area_35_45_values(self):
        res = rectangle.area(35, 45)
        self.assertEqual(1575, res)

    def test_area_35_46_values(self):
        res = rectangle.area(35, 46)
        self.assertEqual(1610, res)

    def test_area_35_47_values(self):
        res = rectangle.area(35, 47)
        self.assertEqual(1645, res)

    def test_area_35_48_values(self):
        res = rectangle.area(35, 48)
        self.assertEqual(1680, res)

    def test_area_35_49_values(self):
        res = rectangle.area(35, 49)
        self.assertEqual(1715, res)

    def test_area_35_50_values(self):
        res = rectangle.area(35, 50)
        self.assertEqual(1750, res)

    def test_area_35_51_values(self):
        res = rectangle.area(35, 51)
        self.assertEqual(1785, res)

    def test_area_35_52_values(self):
        res = rectangle.area(35, 52)
        self.assertEqual(1820, res)

    def test_area_35_53_values(self):
        res = rectangle.area(35, 53)
        self.assertEqual(1855, res)

    def test_area_35_54_values(self):
        res = rectangle.area(35, 54)
        self.assertEqual(1890, res)

    def test_area_35_55_values(self):
        res = rectangle.area(35, 55)
        self.assertEqual(1925, res)

    def test_area_35_56_values(self):
        res = rectangle.area(35, 56)
        self.assertEqual(1960, res)

    def test_area_35_57_values(self):
        res = rectangle.area(35, 57)
        self.assertEqual(1995, res)

    def test_area_35_58_values(self):
        res = rectangle.area(35, 58)
        self.assertEqual(2030, res)

    def test_area_35_59_values(self):
        res = rectangle.area(35, 59)
        self.assertEqual(2065, res)

    def test_area_36_30_values(self):
        res = rectangle.area(36, 30)
        self.assertEqual(1080, res)

    def test_area_36_31_values(self):
        res = rectangle.area(36, 31)
        self.assertEqual(1116, res)

    def test_area_36_32_values(self):
        res = rectangle.area(36, 32)
        self.assertEqual(1152, res)

    def test_area_36_33_values(self):
        res = rectangle.area(36, 33)
        self.assertEqual(1188, res)

    def test_area_36_34_values(self):
        res = rectangle.area(36, 34)
        self.assertEqual(1224, res)

    def test_area_36_35_values(self):
        res = rectangle.area(36, 35)
        self.assertEqual(1260, res)

    def test_area_36_36_values(self):
        res = rectangle.area(36, 36)
        self.assertEqual(1296, res)

    def test_area_36_37_values(self):
        res = rectangle.area(36, 37)
        self.assertEqual(1332, res)

    def test_area_36_38_values(self):
        res = rectangle.area(36, 38)
        self.assertEqual(1368, res)

    def test_area_36_39_values(self):
        res = rectangle.area(36, 39)
        self.assertEqual(1404, res)

    def test_area_36_40_values(self):
        res = rectangle.area(36, 40)
        self.assertEqual(1440, res)

    def test_area_36_41_values(self):
        res = rectangle.area(36, 41)
        self.assertEqual(1476, res)

    def test_area_36_42_values(self):
        res = rectangle.area(36, 42)
        self.assertEqual(1512, res)

    def test_area_36_43_values(self):
        res = rectangle.area(36, 43)
        self.assertEqual(1548, res)

    def test_area_36_44_values(self):
        res = rectangle.area(36, 44)
        self.assertEqual(1584, res)

    def test_area_36_45_values(self):
        res = rectangle.area(36, 45)
        self.assertEqual(1620, res)

    def test_area_36_46_values(self):
        res = rectangle.area(36, 46)
        self.assertEqual(1656, res)

    def test_area_36_47_values(self):
        res = rectangle.area(36, 47)
        self.assertEqual(1692, res)

    def test_area_36_48_values(self):
        res = rectangle.area(36, 48)
        self.assertEqual(1728, res)

    def test_area_36_49_values(self):
        res = rectangle.area(36, 49)
        self.assertEqual(1764, res)

    def test_area_36_50_values(self):
        res = rectangle.area(36, 50)
        self.assertEqual(1800, res)

    def test_area_36_51_values(self):
        res = rectangle.area(36, 51)
        self.assertEqual(1836, res)

    def test_area_36_52_values(self):
        res = rectangle.area(36, 52)
        self.assertEqual(1872, res)

    def test_area_36_53_values(self):
        res = rectangle.area(36, 53)
        self.assertEqual(1908, res)

    def test_area_36_54_values(self):
        res = rectangle.area(36, 54)
        self.assertEqual(1944, res)

    def test_area_36_55_values(self):
        res = rectangle.area(36, 55)
        self.assertEqual(1980, res)

    def test_area_36_56_values(self):
        res = rectangle.area(36, 56)
        self.assertEqual(2016, res)

    def test_area_36_57_values(self):
        res = rectangle.area(36, 57)
        self.assertEqual(2052, res)

    def test_area_36_58_values(self):
        res = rectangle.area(36, 58)
        self.assertEqual(2088, res)

    def test_area_36_59_values(self):
        res = rectangle.area(36, 59)
        self.assertEqual(2124, res)

    def test_area_37_30_values(self):
        res = rectangle.area(37, 30)
        self.assertEqual(1110, res)

    def test_area_37_31_values(self):
        res = rectangle.area(37, 31)
        self.assertEqual(1147, res)

    def test_area_37_32_values(self):
        res = rectangle.area(37, 32)
        self.assertEqual(1184, res)

    def test_area_37_33_values(self):
        res = rectangle.area(37, 33)
        self.assertEqual(1221, res)

    def test_area_37_34_values(self):
        res = rectangle.area(37, 34)
        self.assertEqual(1258, res)

    def test_area_37_35_values(self):
        res = rectangle.area(37, 35)
        self.assertEqual(1295, res)

    def test_area_37_36_values(self):
        res = rectangle.area(37, 36)
        self.assertEqual(1332, res)

    def test_area_37_37_values(self):
        res = rectangle.area(37, 37)
        self.assertEqual(1369, res)

    def test_area_37_38_values(self):
        res = rectangle.area(37, 38)
        self.assertEqual(1406, res)

    def test_area_37_39_values(self):
        res = rectangle.area(37, 39)
        self.assertEqual(1443, res)

    def test_area_37_40_values(self):
        res = rectangle.area(37, 40)
        self.assertEqual(1480, res)

    def test_area_37_41_values(self):
        res = rectangle.area(37, 41)
        self.assertEqual(1517, res)

    def test_area_37_42_values(self):
        res = rectangle.area(37, 42)
        self.assertEqual(1554, res)

    def test_area_37_43_values(self):
        res = rectangle.area(37, 43)
        self.assertEqual(1591, res)

    def test_area_37_44_values(self):
        res = rectangle.area(37, 44)
        self.assertEqual(1628, res)

    def test_area_37_45_values(self):
        res = rectangle.area(37, 45)
        self.assertEqual(1665, res)

    def test_area_37_46_values(self):
        res = rectangle.area(37, 46)
        self.assertEqual(1702, res)

    def test_area_37_47_values(self):
        res = rectangle.area(37, 47)
        self.assertEqual(1739, res)

    def test_area_37_48_values(self):
        res = rectangle.area(37, 48)
        self.assertEqual(1776, res)

    def test_area_37_49_values(self):
        res = rectangle.area(37, 49)
        self.assertEqual(1813, res)

    def test_area_37_50_values(self):
        res = rectangle.area(37, 50)
        self.assertEqual(1850, res)

    def test_area_37_51_values(self):
        res = rectangle.area(37, 51)
        self.assertEqual(1887, res)

    def test_area_37_52_values(self):
        res = rectangle.area(37, 52)
        self.assertEqual(1924, res)

    def test_area_37_53_values(self):
        res = rectangle.area(37, 53)
        self.assertEqual(1961, res)

    def test_area_37_54_values(self):
        res = rectangle.area(37, 54)
        self.assertEqual(1998, res)

    def test_area_37_55_values(self):
        res = rectangle.area(37, 55)
        self.assertEqual(2035, res)

    def test_area_37_56_values(self):
        res = rectangle.area(37, 56)
        self.assertEqual(2072, res)

    def test_area_37_57_values(self):
        res = rectangle.area(37, 57)
        self.assertEqual(2109, res)

    def test_area_37_58_values(self):
        res = rectangle.area(37, 58)
        self.assertEqual(2146, res)

    def test_area_37_59_values(self):
        res = rectangle.area(37, 59)
        self.assertEqual(2183, res)

    def test_area_38_30_values(self):
        res = rectangle.area(38, 30)
        self.assertEqual(1140, res)

    def test_area_38_31_values(self):
        res = rectangle.area(38, 31)
        self.assertEqual(1178, res)

    def test_area_38_32_values(self):
        res = rectangle.area(38, 32)
        self.assertEqual(1216, res)

    def test_area_38_33_values(self):
        res = rectangle.area(38, 33)
        self.assertEqual(1254, res)

    def test_area_38_34_values(self):
        res = rectangle.area(38, 34)
        self.assertEqual(1292, res)

    def test_area_38_35_values(self):
        res = rectangle.area(38, 35)
        self.assertEqual(1330, res)

    def test_area_38_36_values(self):
        res = rectangle.area(38, 36)
        self.assertEqual(1368, res)

    def test_area_38_37_values(self):
        res = rectangle.area(38, 37)
        self.assertEqual(1406, res)

    def test_area_38_38_values(self):
        res = rectangle.area(38, 38)
        self.assertEqual(1444, res)

    def test_area_38_39_values(self):
        res = rectangle.area(38, 39)
        self.assertEqual(1482, res)

    def test_area_38_40_values(self):
        res = rectangle.area(38, 40)
        self.assertEqual(1520, res)

    def test_area_38_41_values(self):
        res = rectangle.area(38, 41)
        self.assertEqual(1558, res)

    def test_area_38_42_values(self):
        res = rectangle.area(38, 42)
        self.assertEqual(1596, res)

    def test_area_38_43_values(self):
        res = rectangle.area(38, 43)
        self.assertEqual(1634, res)

    def test_area_38_44_values(self):
        res = rectangle.area(38, 44)
        self.assertEqual(1672, res)

    def test_area_38_45_values(self):
        res = rectangle.area(38, 45)
        self.assertEqual(1710, res)

    def test_area_38_46_values(self):
        res = rectangle.area(38, 46)
        self.assertEqual(1748, res)

    def test_area_38_47_values(self):
        res = rectangle.area(38, 47)
        self.assertEqual(1786, res)

    def test_area_38_48_values(self):
        res = rectangle.area(38, 48)
        self.assertEqual(1824, res)

    def test_area_38_49_values(self):
        res = rectangle.area(38, 49)
        self.assertEqual(1862, res)

    def test_area_38_50_values(self):
        res = rectangle.area(38, 50)
        self.assertEqual(1900, res)

    def test_area_38_51_values(self):
        res = rectangle.area(38, 51)
        self.assertEqual(1938, res)

    def test_area_38_52_values(self):
        res = rectangle.area(38, 52)
        self.assertEqual(1976, res)

    def test_area_38_53_values(self):
        res = rectangle.area(38, 53)
        self.assertEqual(2014, res)

    def test_area_38_54_values(self):
        res = rectangle.area(38, 54)
        self.assertEqual(2052, res)

    def test_area_38_55_values(self):
        res = rectangle.area(38, 55)
        self.assertEqual(2090, res)

    def test_area_38_56_values(self):
        res = rectangle.area(38, 56)
        self.assertEqual(2128, res)

    def test_area_38_57_values(self):
        res = rectangle.area(38, 57)
        self.assertEqual(2166, res)

    def test_area_38_58_values(self):
        res = rectangle.area(38, 58)
        self.assertEqual(2204, res)

    def test_area_38_59_values(self):
        res = rectangle.area(38, 59)
        self.assertEqual(2242, res)

    def test_area_39_30_values(self):
        res = rectangle.area(39, 30)
        self.assertEqual(1170, res)

    def test_area_39_31_values(self):
        res = rectangle.area(39, 31)
        self.assertEqual(1209, res)

    def test_area_39_32_values(self):
        res = rectangle.area(39, 32)
        self.assertEqual(1248, res)

    def test_area_39_33_values(self):
        res = rectangle.area(39, 33)
        self.assertEqual(1287, res)

    def test_area_39_34_values(self):
        res = rectangle.area(39, 34)
        self.assertEqual(1326, res)

    def test_area_39_35_values(self):
        res = rectangle.area(39, 35)
        self.assertEqual(1365, res)

    def test_area_39_36_values(self):
        res = rectangle.area(39, 36)
        self.assertEqual(1404, res)

    def test_area_39_37_values(self):
        res = rectangle.area(39, 37)
        self.assertEqual(1443, res)

    def test_area_39_38_values(self):
        res = rectangle.area(39, 38)
        self.assertEqual(1482, res)

    def test_area_39_39_values(self):
        res = rectangle.area(39, 39)
        self.assertEqual(1521, res)

    def test_area_39_40_values(self):
        res = rectangle.area(39, 40)
        self.assertEqual(1560, res)

    def test_area_39_41_values(self):
        res = rectangle.area(39, 41)
        self.assertEqual(1599, res)

    def test_area_39_42_values(self):
        res = rectangle.area(39, 42)
        self.assertEqual(1638, res)

    def test_area_39_43_values(self):
        res = rectangle.area(39, 43)
        self.assertEqual(1677, res)

    def test_area_39_44_values(self):
        res = rectangle.area(39, 44)
        self.assertEqual(1716, res)

    def test_area_39_45_values(self):
        res = rectangle.area(39, 45)
        self.assertEqual(1755, res)

    def test_area_39_46_values(self):
        res = rectangle.area(39, 46)
        self.assertEqual(1794, res)

    def test_area_39_47_values(self):
        res = rectangle.area(39, 47)
        self.assertEqual(1833, res)

    def test_area_39_48_values(self):
        res = rectangle.area(39, 48)
        self.assertEqual(1872, res)

    def test_area_39_49_values(self):
        res = rectangle.area(39, 49)
        self.assertEqual(1911, res)

    def test_area_39_50_values(self):
        res = rectangle.area(39, 50)
        self.assertEqual(1950, res)

    def test_area_39_51_values(self):
        res = rectangle.area(39, 51)
        self.assertEqual(1989, res)

    def test_area_39_52_values(self):
        res = rectangle.area(39, 52)
        self.assertEqual(2028, res)

    def test_area_39_53_values(self):
        res = rectangle.area(39, 53)
        self.assertEqual(2067, res)

    def test_area_39_54_values(self):
        res = rectangle.area(39, 54)
        self.assertEqual(2106, res)

    def test_area_39_55_values(self):
        res = rectangle.area(39, 55)
        self.assertEqual(2145, res)

    def test_area_39_56_values(self):
        res = rectangle.area(39, 56)
        self.assertEqual(2184, res)

    def test_area_39_57_values(self):
        res = rectangle.area(39, 57)
        self.assertEqual(2223, res)

    def test_area_39_58_values(self):
        res = rectangle.area(39, 58)
        self.assertEqual(2262, res)

    def test_area_39_59_values(self):
        res = rectangle.area(39, 59)
        self.assertEqual(2301, res)

    def test_area_40_30_values(self):
        res = rectangle.area(40, 30)
        self.assertEqual(1200, res)

    def test_area_40_31_values(self):
        res = rectangle.area(40, 31)
        self.assertEqual(1240, res)

    def test_area_40_32_values(self):
        res = rectangle.area(40, 32)
        self.assertEqual(1280, res)

    def test_area_40_33_values(self):
        res = rectangle.area(40, 33)
        self.assertEqual(1320, res)

    def test_area_40_34_values(self):
        res = rectangle.area(40, 34)
        self.assertEqual(1360, res)

    def test_area_40_35_values(self):
        res = rectangle.area(40, 35)
        self.assertEqual(1400, res)

    def test_area_40_36_values(self):
        res = rectangle.area(40, 36)
        self.assertEqual(1440, res)

    def test_area_40_37_values(self):
        res = rectangle.area(40, 37)
        self.assertEqual(1480, res)

    def test_area_40_38_values(self):
        res = rectangle.area(40, 38)
        self.assertEqual(1520, res)

    def test_area_40_39_values(self):
        res = rectangle.area(40, 39)
        self.assertEqual(1560, res)

    def test_area_40_40_values(self):
        res = rectangle.area(40, 40)
        self.assertEqual(1600, res)

    def test_area_40_41_values(self):
        res = rectangle.area(40, 41)
        self.assertEqual(1640, res)

    def test_area_40_42_values(self):
        res = rectangle.area(40, 42)
        self.assertEqual(1680, res)

    def test_area_40_43_values(self):
        res = rectangle.area(40, 43)
        self.assertEqual(1720, res)

    def test_area_40_44_values(self):
        res = rectangle.area(40, 44)
        self.assertEqual(1760, res)

    def test_area_40_45_values(self):
        res = rectangle.area(40, 45)
        self.assertEqual(1800, res)

    def test_area_40_46_values(self):
        res = rectangle.area(40, 46)
        self.assertEqual(1840, res)

    def test_area_40_47_values(self):
        res = rectangle.area(40, 47)
        self.assertEqual(1880, res)

    def test_area_40_48_values(self):
        res = rectangle.area(40, 48)
        self.assertEqual(1920, res)

    def test_area_40_49_values(self):
        res = rectangle.area(40, 49)
        self.assertEqual(1960, res)

    def test_area_40_50_values(self):
        res = rectangle.area(40, 50)
        self.assertEqual(2000, res)

    def test_area_40_51_values(self):
        res = rectangle.area(40, 51)
        self.assertEqual(2040, res)

    def test_area_40_52_values(self):
        res = rectangle.area(40, 52)
        self.assertEqual(2080, res)

    def test_area_40_53_values(self):
        res = rectangle.area(40, 53)
        self.assertEqual(2120, res)

    def test_area_40_54_values(self):
        res = rectangle.area(40, 54)
        self.assertEqual(2160, res)

    def test_area_40_55_values(self):
        res = rectangle.area(40, 55)
        self.assertEqual(2200, res)

    def test_area_40_56_values(self):
        res = rectangle.area(40, 56)
        self.assertEqual(2240, res)

    def test_area_40_57_values(self):
        res = rectangle.area(40, 57)
        self.assertEqual(2280, res)

    def test_area_40_58_values(self):
        res = rectangle.area(40, 58)
        self.assertEqual(2320, res)

    def test_area_40_59_values(self):
        res = rectangle.area(40, 59)
        self.assertEqual(2360, res)

    def test_area_41_30_values(self):
        res = rectangle.area(41, 30)
        self.assertEqual(1230, res)

    def test_area_41_31_values(self):
        res = rectangle.area(41, 31)
        self.assertEqual(1271, res)

    def test_area_41_32_values(self):
        res = rectangle.area(41, 32)
        self.assertEqual(1312, res)

    def test_area_41_33_values(self):
        res = rectangle.area(41, 33)
        self.assertEqual(1353, res)

    def test_area_41_34_values(self):
        res = rectangle.area(41, 34)
        self.assertEqual(1394, res)

    def test_area_41_35_values(self):
        res = rectangle.area(41, 35)
        self.assertEqual(1435, res)

    def test_area_41_36_values(self):
        res = rectangle.area(41, 36)
        self.assertEqual(1476, res)

    def test_area_41_37_values(self):
        res = rectangle.area(41, 37)
        self.assertEqual(1517, res)

    def test_area_41_38_values(self):
        res = rectangle.area(41, 38)
        self.assertEqual(1558, res)

    def test_area_41_39_values(self):
        res = rectangle.area(41, 39)
        self.assertEqual(1599, res)

    def test_area_41_40_values(self):
        res = rectangle.area(41, 40)
        self.assertEqual(1640, res)

    def test_area_41_41_values(self):
        res = rectangle.area(41, 41)
        self.assertEqual(1681, res)

    def test_area_41_42_values(self):
        res = rectangle.area(41, 42)
        self.assertEqual(1722, res)

    def test_area_41_43_values(self):
        res = rectangle.area(41, 43)
        self.assertEqual(1763, res)

    def test_area_41_44_values(self):
        res = rectangle.area(41, 44)
        self.assertEqual(1804, res)

    def test_area_41_45_values(self):
        res = rectangle.area(41, 45)
        self.assertEqual(1845, res)

    def test_area_41_46_values(self):
        res = rectangle.area(41, 46)
        self.assertEqual(1886, res)

    def test_area_41_47_values(self):
        res = rectangle.area(41, 47)
        self.assertEqual(1927, res)

    def test_area_41_48_values(self):
        res = rectangle.area(41, 48)
        self.assertEqual(1968, res)

    def test_area_41_49_values(self):
        res = rectangle.area(41, 49)
        self.assertEqual(2009, res)

    def test_area_41_50_values(self):
        res = rectangle.area(41, 50)
        self.assertEqual(2050, res)

    def test_area_41_51_values(self):
        res = rectangle.area(41, 51)
        self.assertEqual(2091, res)

    def test_area_41_52_values(self):
        res = rectangle.area(41, 52)
        self.assertEqual(2132, res)

    def test_area_41_53_values(self):
        res = rectangle.area(41, 53)
        self.assertEqual(2173, res)

    def test_area_41_54_values(self):
        res = rectangle.area(41, 54)
        self.assertEqual(2214, res)

    def test_area_41_55_values(self):
        res = rectangle.area(41, 55)
        self.assertEqual(2255, res)

    def test_area_41_56_values(self):
        res = rectangle.area(41, 56)
        self.assertEqual(2296, res)

    def test_area_41_57_values(self):
        res = rectangle.area(41, 57)
        self.assertEqual(2337, res)

    def test_area_41_58_values(self):
        res = rectangle.area(41, 58)
        self.assertEqual(2378, res)

    def test_area_41_59_values(self):
        res = rectangle.area(41, 59)
        self.assertEqual(2419, res)

    def test_area_42_30_values(self):
        res = rectangle.area(42, 30)
        self.assertEqual(1260, res)

    def test_area_42_31_values(self):
        res = rectangle.area(42, 31)
        self.assertEqual(1302, res)

    def test_area_42_32_values(self):
        res = rectangle.area(42, 32)
        self.assertEqual(1344, res)

    def test_area_42_33_values(self):
        res = rectangle.area(42, 33)
        self.assertEqual(1386, res)

    def test_area_42_34_values(self):
        res = rectangle.area(42, 34)
        self.assertEqual(1428, res)

    def test_area_42_35_values(self):
        res = rectangle.area(42, 35)
        self.assertEqual(1470, res)

    def test_area_42_36_values(self):
        res = rectangle.area(42, 36)
        self.assertEqual(1512, res)

    def test_area_42_37_values(self):
        res = rectangle.area(42, 37)
        self.assertEqual(1554, res)

    def test_area_42_38_values(self):
        res = rectangle.area(42, 38)
        self.assertEqual(1596, res)

    def test_area_42_39_values(self):
        res = rectangle.area(42, 39)
        self.assertEqual(1638, res)

    def test_area_42_40_values(self):
        res = rectangle.area(42, 40)
        self.assertEqual(1680, res)

    def test_area_42_41_values(self):
        res = rectangle.area(42, 41)
        self.assertEqual(1722, res)

    def test_area_42_42_values(self):
        res = rectangle.area(42, 42)
        self.assertEqual(1764, res)

    def test_area_42_43_values(self):
        res = rectangle.area(42, 43)
        self.assertEqual(1806, res)

    def test_area_42_44_values(self):
        res = rectangle.area(42, 44)
        self.assertEqual(1848, res)

    def test_area_42_45_values(self):
        res = rectangle.area(42, 45)
        self.assertEqual(1890, res)

    def test_area_42_46_values(self):
        res = rectangle.area(42, 46)
        self.assertEqual(1932, res)

    def test_area_42_47_values(self):
        res = rectangle.area(42, 47)
        self.assertEqual(1974, res)

    def test_area_42_48_values(self):
        res = rectangle.area(42, 48)
        self.assertEqual(2016, res)

    def test_area_42_49_values(self):
        res = rectangle.area(42, 49)
        self.assertEqual(2058, res)

    def test_area_42_50_values(self):
        res = rectangle.area(42, 50)
        self.assertEqual(2100, res)

    def test_area_42_51_values(self):
        res = rectangle.area(42, 51)
        self.assertEqual(2142, res)

    def test_area_42_52_values(self):
        res = rectangle.area(42, 52)
        self.assertEqual(2184, res)

    def test_area_42_53_values(self):
        res = rectangle.area(42, 53)
        self.assertEqual(2226, res)

    def test_area_42_54_values(self):
        res = rectangle.area(42, 54)
        self.assertEqual(2268, res)

    def test_area_42_55_values(self):
        res = rectangle.area(42, 55)
        self.assertEqual(2310, res)

    def test_area_42_56_values(self):
        res = rectangle.area(42, 56)
        self.assertEqual(2352, res)

    def test_area_42_57_values(self):
        res = rectangle.area(42, 57)
        self.assertEqual(2394, res)

    def test_area_42_58_values(self):
        res = rectangle.area(42, 58)
        self.assertEqual(2436, res)

    def test_area_42_59_values(self):
        res = rectangle.area(42, 59)
        self.assertEqual(2478, res)

    def test_area_43_30_values(self):
        res = rectangle.area(43, 30)
        self.assertEqual(1290, res)

    def test_area_43_31_values(self):
        res = rectangle.area(43, 31)
        self.assertEqual(1333, res)

    def test_area_43_32_values(self):
        res = rectangle.area(43, 32)
        self.assertEqual(1376, res)

    def test_area_43_33_values(self):
        res = rectangle.area(43, 33)
        self.assertEqual(1419, res)

    def test_area_43_34_values(self):
        res = rectangle.area(43, 34)
        self.assertEqual(1462, res)

    def test_area_43_35_values(self):
        res = rectangle.area(43, 35)
        self.assertEqual(1505, res)

    def test_area_43_36_values(self):
        res = rectangle.area(43, 36)
        self.assertEqual(1548, res)

    def test_area_43_37_values(self):
        res = rectangle.area(43, 37)
        self.assertEqual(1591, res)

    def test_area_43_38_values(self):
        res = rectangle.area(43, 38)
        self.assertEqual(1634, res)

    def test_area_43_39_values(self):
        res = rectangle.area(43, 39)
        self.assertEqual(1677, res)

    def test_area_43_40_values(self):
        res = rectangle.area(43, 40)
        self.assertEqual(1720, res)

    def test_area_43_41_values(self):
        res = rectangle.area(43, 41)
        self.assertEqual(1763, res)

    def test_area_43_42_values(self):
        res = rectangle.area(43, 42)
        self.assertEqual(1806, res)

    def test_area_43_43_values(self):
        res = rectangle.area(43, 43)
        self.assertEqual(1849, res)

    def test_area_43_44_values(self):
        res = rectangle.area(43, 44)
        self.assertEqual(1892, res)

    def test_area_43_45_values(self):
        res = rectangle.area(43, 45)
        self.assertEqual(1935, res)

    def test_area_43_46_values(self):
        res = rectangle.area(43, 46)
        self.assertEqual(1978, res)

    def test_area_43_47_values(self):
        res = rectangle.area(43, 47)
        self.assertEqual(2021, res)

    def test_area_43_48_values(self):
        res = rectangle.area(43, 48)
        self.assertEqual(2064, res)

    def test_area_43_49_values(self):
        res = rectangle.area(43, 49)
        self.assertEqual(2107, res)

    def test_area_43_50_values(self):
        res = rectangle.area(43, 50)
        self.assertEqual(2150, res)

    def test_area_43_51_values(self):
        res = rectangle.area(43, 51)
        self.assertEqual(2193, res)

    def test_area_43_52_values(self):
        res = rectangle.area(43, 52)
        self.assertEqual(2236, res)

    def test_area_43_53_values(self):
        res = rectangle.area(43, 53)
        self.assertEqual(2279, res)

    def test_area_43_54_values(self):
        res = rectangle.area(43, 54)
        self.assertEqual(2322, res)

    def test_area_43_55_values(self):
        res = rectangle.area(43, 55)
        self.assertEqual(2365, res)

    def test_area_43_56_values(self):
        res = rectangle.area(43, 56)
        self.assertEqual(2408, res)

    def test_area_43_57_values(self):
        res = rectangle.area(43, 57)
        self.assertEqual(2451, res)

    def test_area_43_58_values(self):
        res = rectangle.area(43, 58)
        self.assertEqual(2494, res)

    def test_area_43_59_values(self):
        res = rectangle.area(43, 59)
        self.assertEqual(2537, res)

    def test_area_44_30_values(self):
        res = rectangle.area(44, 30)
        self.assertEqual(1320, res)

    def test_area_44_31_values(self):
        res = rectangle.area(44, 31)
        self.assertEqual(1364, res)

    def test_area_44_32_values(self):
        res = rectangle.area(44, 32)
        self.assertEqual(1408, res)

    def test_area_44_33_values(self):
        res = rectangle.area(44, 33)
        self.assertEqual(1452, res)

    def test_area_44_34_values(self):
        res = rectangle.area(44, 34)
        self.assertEqual(1496, res)

    def test_area_44_35_values(self):
        res = rectangle.area(44, 35)
        self.assertEqual(1540, res)

    def test_area_44_36_values(self):
        res = rectangle.area(44, 36)
        self.assertEqual(1584, res)

    def test_area_44_37_values(self):
        res = rectangle.area(44, 37)
        self.assertEqual(1628, res)

    def test_area_44_38_values(self):
        res = rectangle.area(44, 38)
        self.assertEqual(1672, res)

    def test_area_44_39_values(self):
        res = rectangle.area(44, 39)
        self.assertEqual(1716, res)

    def test_area_44_40_values(self):
        res = rectangle.area(44, 40)
        self.assertEqual(1760, res)

    def test_area_44_41_values(self):
        res = rectangle.area(44, 41)
        self.assertEqual(1804, res)

    def test_area_44_42_values(self):
        res = rectangle.area(44, 42)
        self.assertEqual(1848, res)

    def test_area_44_43_values(self):
        res = rectangle.area(44, 43)
        self.assertEqual(1892, res)

    def test_area_44_44_values(self):
        res = rectangle.area(44, 44)
        self.assertEqual(1936, res)

    def test_area_44_45_values(self):
        res = rectangle.area(44, 45)
        self.assertEqual(1980, res)

    def test_area_44_46_values(self):
        res = rectangle.area(44, 46)
        self.assertEqual(2024, res)

    def test_area_44_47_values(self):
        res = rectangle.area(44, 47)
        self.assertEqual(2068, res)

    def test_area_44_48_values(self):
        res = rectangle.area(44, 48)
        self.assertEqual(2112, res)

    def test_area_44_49_values(self):
        res = rectangle.area(44, 49)
        self.assertEqual(2156, res)

    def test_area_44_50_values(self):
        res = rectangle.area(44, 50)
        self.assertEqual(2200, res)

    def test_area_44_51_values(self):
        res = rectangle.area(44, 51)
        self.assertEqual(2244, res)

    def test_area_44_52_values(self):
        res = rectangle.area(44, 52)
        self.assertEqual(2288, res)

    def test_area_44_53_values(self):
        res = rectangle.area(44, 53)
        self.assertEqual(2332, res)

    def test_area_44_54_values(self):
        res = rectangle.area(44, 54)
        self.assertEqual(2376, res)

    def test_area_44_55_values(self):
        res = rectangle.area(44, 55)
        self.assertEqual(2420, res)

    def test_area_44_56_values(self):
        res = rectangle.area(44, 56)
        self.assertEqual(2464, res)

    def test_area_44_57_values(self):
        res = rectangle.area(44, 57)
        self.assertEqual(2508, res)

    def test_area_44_58_values(self):
        res = rectangle.area(44, 58)
        self.assertEqual(2552, res)

    def test_area_44_59_values(self):
        res = rectangle.area(44, 59)
        self.assertEqual(2596, res)

    def test_area_45_30_values(self):
        res = rectangle.area(45, 30)
        self.assertEqual(1350, res)

    def test_area_45_31_values(self):
        res = rectangle.area(45, 31)
        self.assertEqual(1395, res)

    def test_area_45_32_values(self):
        res = rectangle.area(45, 32)
        self.assertEqual(1440, res)

    def test_area_45_33_values(self):
        res = rectangle.area(45, 33)
        self.assertEqual(1485, res)

    def test_area_45_34_values(self):
        res = rectangle.area(45, 34)
        self.assertEqual(1530, res)

    def test_area_45_35_values(self):
        res = rectangle.area(45, 35)
        self.assertEqual(1575, res)

    def test_area_45_36_values(self):
        res = rectangle.area(45, 36)
        self.assertEqual(1620, res)

    def test_area_45_37_values(self):
        res = rectangle.area(45, 37)
        self.assertEqual(1665, res)

    def test_area_45_38_values(self):
        res = rectangle.area(45, 38)
        self.assertEqual(1710, res)

    def test_area_45_39_values(self):
        res = rectangle.area(45, 39)
        self.assertEqual(1755, res)

    def test_area_45_40_values(self):
        res = rectangle.area(45, 40)
        self.assertEqual(1800, res)

    def test_area_45_41_values(self):
        res = rectangle.area(45, 41)
        self.assertEqual(1845, res)

    def test_area_45_42_values(self):
        res = rectangle.area(45, 42)
        self.assertEqual(1890, res)

    def test_area_45_43_values(self):
        res = rectangle.area(45, 43)
        self.assertEqual(1935, res)

    def test_area_45_44_values(self):
        res = rectangle.area(45, 44)
        self.assertEqual(1980, res)

    def test_area_45_45_values(self):
        res = rectangle.area(45, 45)
        self.assertEqual(2025, res)

    def test_area_45_46_values(self):
        res = rectangle.area(45, 46)
        self.assertEqual(2070, res)

    def test_area_45_47_values(self):
        res = rectangle.area(45, 47)
        self.assertEqual(2115, res)

    def test_area_45_48_values(self):
        res = rectangle.area(45, 48)
        self.assertEqual(2160, res)

    def test_area_45_49_values(self):
        res = rectangle.area(45, 49)
        self.assertEqual(2205, res)

    def test_area_45_50_values(self):
        res = rectangle.area(45, 50)
        self.assertEqual(2250, res)

    def test_area_45_51_values(self):
        res = rectangle.area(45, 51)
        self.assertEqual(2295, res)

    def test_area_45_52_values(self):
        res = rectangle.area(45, 52)
        self.assertEqual(2340, res)

    def test_area_45_53_values(self):
        res = rectangle.area(45, 53)
        self.assertEqual(2385, res)

    def test_area_45_54_values(self):
        res = rectangle.area(45, 54)
        self.assertEqual(2430, res)

    def test_area_45_55_values(self):
        res = rectangle.area(45, 55)
        self.assertEqual(2475, res)

    def test_area_45_56_values(self):
        res = rectangle.area(45, 56)
        self.assertEqual(2520, res)

    def test_area_45_57_values(self):
        res = rectangle.area(45, 57)
        self.assertEqual(2565, res)

    def test_area_45_58_values(self):
        res = rectangle.area(45, 58)
        self.assertEqual(2610, res)

    def test_area_45_59_values(self):
        res = rectangle.area(45, 59)
        self.assertEqual(2655, res)

    def test_area_46_30_values(self):
        res = rectangle.area(46, 30)
        self.assertEqual(1380, res)

    def test_area_46_31_values(self):
        res = rectangle.area(46, 31)
        self.assertEqual(1426, res)

    def test_area_46_32_values(self):
        res = rectangle.area(46, 32)
        self.assertEqual(1472, res)

    def test_area_46_33_values(self):
        res = rectangle.area(46, 33)
        self.assertEqual(1518, res)

    def test_area_46_34_values(self):
        res = rectangle.area(46, 34)
        self.assertEqual(1564, res)

    def test_area_46_35_values(self):
        res = rectangle.area(46, 35)
        self.assertEqual(1610, res)

    def test_area_46_36_values(self):
        res = rectangle.area(46, 36)
        self.assertEqual(1656, res)

    def test_area_46_37_values(self):
        res = rectangle.area(46, 37)
        self.assertEqual(1702, res)

    def test_area_46_38_values(self):
        res = rectangle.area(46, 38)
        self.assertEqual(1748, res)

    def test_area_46_39_values(self):
        res = rectangle.area(46, 39)
        self.assertEqual(1794, res)

    def test_area_46_40_values(self):
        res = rectangle.area(46, 40)
        self.assertEqual(1840, res)

    def test_area_46_41_values(self):
        res = rectangle.area(46, 41)
        self.assertEqual(1886, res)

    def test_area_46_42_values(self):
        res = rectangle.area(46, 42)
        self.assertEqual(1932, res)

    def test_area_46_43_values(self):
        res = rectangle.area(46, 43)
        self.assertEqual(1978, res)

    def test_area_46_44_values(self):
        res = rectangle.area(46, 44)
        self.assertEqual(2024, res)

    def test_area_46_45_values(self):
        res = rectangle.area(46, 45)
        self.assertEqual(2070, res)

    def test_area_46_46_values(self):
        res = rectangle.area(46, 46)
        self.assertEqual(2116, res)

    def test_area_46_47_values(self):
        res = rectangle.area(46, 47)
        self.assertEqual(2162, res)

    def test_area_46_48_values(self):
        res = rectangle.area(46, 48)
        self.assertEqual(2208, res)

    def test_area_46_49_values(self):
        res = rectangle.area(46, 49)
        self.assertEqual(2254, res)

    def test_area_46_50_values(self):
        res = rectangle.area(46, 50)
        self.assertEqual(2300, res)

    def test_area_46_51_values(self):
        res = rectangle.area(46, 51)
        self.assertEqual(2346, res)

    def test_area_46_52_values(self):
        res = rectangle.area(46, 52)
        self.assertEqual(2392, res)

    def test_area_46_53_values(self):
        res = rectangle.area(46, 53)
        self.assertEqual(2438, res)

    def test_area_46_54_values(self):
        res = rectangle.area(46, 54)
        self.assertEqual(2484, res)

    def test_area_46_55_values(self):
        res = rectangle.area(46, 55)
        self.assertEqual(2530, res)

    def test_area_46_56_values(self):
        res = rectangle.area(46, 56)
        self.assertEqual(2576, res)

    def test_area_46_57_values(self):
        res = rectangle.area(46, 57)
        self.assertEqual(2622, res)

    def test_area_46_58_values(self):
        res = rectangle.area(46, 58)
        self.assertEqual(2668, res)

    def test_area_46_59_values(self):
        res = rectangle.area(46, 59)
        self.assertEqual(2714, res)

    def test_area_47_30_values(self):
        res = rectangle.area(47, 30)
        self.assertEqual(1410, res)

    def test_area_47_31_values(self):
        res = rectangle.area(47, 31)
        self.assertEqual(1457, res)

    def test_area_47_32_values(self):
        res = rectangle.area(47, 32)
        self.assertEqual(1504, res)

    def test_area_47_33_values(self):
        res = rectangle.area(47, 33)
        self.assertEqual(1551, res)

    def test_area_47_34_values(self):
        res = rectangle.area(47, 34)
        self.assertEqual(1598, res)

    def test_area_47_35_values(self):
        res = rectangle.area(47, 35)
        self.assertEqual(1645, res)

    def test_area_47_36_values(self):
        res = rectangle.area(47, 36)
        self.assertEqual(1692, res)

    def test_area_47_37_values(self):
        res = rectangle.area(47, 37)
        self.assertEqual(1739, res)

    def test_area_47_38_values(self):
        res = rectangle.area(47, 38)
        self.assertEqual(1786, res)

    def test_area_47_39_values(self):
        res = rectangle.area(47, 39)
        self.assertEqual(1833, res)

    def test_area_47_40_values(self):
        res = rectangle.area(47, 40)
        self.assertEqual(1880, res)

    def test_area_47_41_values(self):
        res = rectangle.area(47, 41)
        self.assertEqual(1927, res)

    def test_area_47_42_values(self):
        res = rectangle.area(47, 42)
        self.assertEqual(1974, res)

    def test_area_47_43_values(self):
        res = rectangle.area(47, 43)
        self.assertEqual(2021, res)

    def test_area_47_44_values(self):
        res = rectangle.area(47, 44)
        self.assertEqual(2068, res)

    def test_area_47_45_values(self):
        res = rectangle.area(47, 45)
        self.assertEqual(2115, res)

    def test_area_47_46_values(self):
        res = rectangle.area(47, 46)
        self.assertEqual(2162, res)

    def test_area_47_47_values(self):
        res = rectangle.area(47, 47)
        self.assertEqual(2209, res)

    def test_area_47_48_values(self):
        res = rectangle.area(47, 48)
        self.assertEqual(2256, res)

    def test_area_47_49_values(self):
        res = rectangle.area(47, 49)
        self.assertEqual(2303, res)

    def test_area_47_50_values(self):
        res = rectangle.area(47, 50)
        self.assertEqual(2350, res)

    def test_area_47_51_values(self):
        res = rectangle.area(47, 51)
        self.assertEqual(2397, res)

    def test_area_47_52_values(self):
        res = rectangle.area(47, 52)
        self.assertEqual(2444, res)

    def test_area_47_53_values(self):
        res = rectangle.area(47, 53)
        self.assertEqual(2491, res)

    def test_area_47_54_values(self):
        res = rectangle.area(47, 54)
        self.assertEqual(2538, res)

    def test_area_47_55_values(self):
        res = rectangle.area(47, 55)
        self.assertEqual(2585, res)

    def test_area_47_56_values(self):
        res = rectangle.area(47, 56)
        self.assertEqual(2632, res)

    def test_area_47_57_values(self):
        res = rectangle.area(47, 57)
        self.assertEqual(2679, res)

    def test_area_47_58_values(self):
        res = rectangle.area(47, 58)
        self.assertEqual(2726, res)

    def test_area_47_59_values(self):
        res = rectangle.area(47, 59)
        self.assertEqual(2773, res)

    def test_area_48_30_values(self):
        res = rectangle.area(48, 30)
        self.assertEqual(1440, res)

    def test_area_48_31_values(self):
        res = rectangle.area(48, 31)
        self.assertEqual(1488, res)

    def test_area_48_32_values(self):
        res = rectangle.area(48, 32)
        self.assertEqual(1536, res)

    def test_area_48_33_values(self):
        res = rectangle.area(48, 33)
        self.assertEqual(1584, res)

    def test_area_48_34_values(self):
        res = rectangle.area(48, 34)
        self.assertEqual(1632, res)

    def test_area_48_35_values(self):
        res = rectangle.area(48, 35)
        self.assertEqual(1680, res)

    def test_area_48_36_values(self):
        res = rectangle.area(48, 36)
        self.assertEqual(1728, res)

    def test_area_48_37_values(self):
        res = rectangle.area(48, 37)
        self.assertEqual(1776, res)

    def test_area_48_38_values(self):
        res = rectangle.area(48, 38)
        self.assertEqual(1824, res)

    def test_area_48_39_values(self):
        res = rectangle.area(48, 39)
        self.assertEqual(1872, res)

    def test_area_48_40_values(self):
        res = rectangle.area(48, 40)
        self.assertEqual(1920, res)

    def test_area_48_41_values(self):
        res = rectangle.area(48, 41)
        self.assertEqual(1968, res)

    def test_area_48_42_values(self):
        res = rectangle.area(48, 42)
        self.assertEqual(2016, res)

    def test_area_48_43_values(self):
        res = rectangle.area(48, 43)
        self.assertEqual(2064, res)

    def test_area_48_44_values(self):
        res = rectangle.area(48, 44)
        self.assertEqual(2112, res)

    def test_area_48_45_values(self):
        res = rectangle.area(48, 45)
        self.assertEqual(2160, res)

    def test_area_48_46_values(self):
        res = rectangle.area(48, 46)
        self.assertEqual(2208, res)

    def test_area_48_47_values(self):
        res = rectangle.area(48, 47)
        self.assertEqual(2256, res)

    def test_area_48_48_values(self):
        res = rectangle.area(48, 48)
        self.assertEqual(2304, res)

    def test_area_48_49_values(self):
        res = rectangle.area(48, 49)
        self.assertEqual(2352, res)

    def test_area_48_50_values(self):
        res = rectangle.area(48, 50)
        self.assertEqual(2400, res)

    def test_area_48_51_values(self):
        res = rectangle.area(48, 51)
        self.assertEqual(2448, res)

    def test_area_48_52_values(self):
        res = rectangle.area(48, 52)
        self.assertEqual(2496, res)

    def test_area_48_53_values(self):
        res = rectangle.area(48, 53)
        self.assertEqual(2544, res)

    def test_area_48_54_values(self):
        res = rectangle.area(48, 54)
        self.assertEqual(2592, res)

    def test_area_48_55_values(self):
        res = rectangle.area(48, 55)
        self.assertEqual(2640, res)

    def test_area_48_56_values(self):
        res = rectangle.area(48, 56)
        self.assertEqual(2688, res)

    def test_area_48_57_values(self):
        res = rectangle.area(48, 57)
        self.assertEqual(2736, res)

    def test_area_48_58_values(self):
        res = rectangle.area(48, 58)
        self.assertEqual(2784, res)

    def test_area_48_59_values(self):
        res = rectangle.area(48, 59)
        self.assertEqual(2832, res)

    def test_area_49_30_values(self):
        res = rectangle.area(49, 30)
        self.assertEqual(1470, res)

    def test_area_49_31_values(self):
        res = rectangle.area(49, 31)
        self.assertEqual(1519, res)

    def test_area_49_32_values(self):
        res = rectangle.area(49, 32)
        self.assertEqual(1568, res)

    def test_area_49_33_values(self):
        res = rectangle.area(49, 33)
        self.assertEqual(1617, res)

    def test_area_49_34_values(self):
        res = rectangle.area(49, 34)
        self.assertEqual(1666, res)

    def test_area_49_35_values(self):
        res = rectangle.area(49, 35)
        self.assertEqual(1715, res)

    def test_area_49_36_values(self):
        res = rectangle.area(49, 36)
        self.assertEqual(1764, res)

    def test_area_49_37_values(self):
        res = rectangle.area(49, 37)
        self.assertEqual(1813, res)

    def test_area_49_38_values(self):
        res = rectangle.area(49, 38)
        self.assertEqual(1862, res)

    def test_area_49_39_values(self):
        res = rectangle.area(49, 39)
        self.assertEqual(1911, res)

    def test_area_49_40_values(self):
        res = rectangle.area(49, 40)
        self.assertEqual(1960, res)

    def test_area_49_41_values(self):
        res = rectangle.area(49, 41)
        self.assertEqual(2009, res)

    def test_area_49_42_values(self):
        res = rectangle.area(49, 42)
        self.assertEqual(2058, res)

    def test_area_49_43_values(self):
        res = rectangle.area(49, 43)
        self.assertEqual(2107, res)

    def test_area_49_44_values(self):
        res = rectangle.area(49, 44)
        self.assertEqual(2156, res)

    def test_area_49_45_values(self):
        res = rectangle.area(49, 45)
        self.assertEqual(2205, res)

    def test_area_49_46_values(self):
        res = rectangle.area(49, 46)
        self.assertEqual(2254, res)

    def test_area_49_47_values(self):
        res = rectangle.area(49, 47)
        self.assertEqual(2303, res)

    def test_area_49_48_values(self):
        res = rectangle.area(49, 48)
        self.assertEqual(2352, res)

    def test_area_49_49_values(self):
        res = rectangle.area(49, 49)
        self.assertEqual(2401, res)

    def test_area_49_50_values(self):
        res = rectangle.area(49, 50)
        self.assertEqual(2450, res)

    def test_area_49_51_values(self):
        res = rectangle.area(49, 51)
        self.assertEqual(2499, res)

    def test_area_49_52_values(self):
        res = rectangle.area(49, 52)
        self.assertEqual(2548, res)

    def test_area_49_53_values(self):
        res = rectangle.area(49, 53)
        self.assertEqual(2597, res)

    def test_area_49_54_values(self):
        res = rectangle.area(49, 54)
        self.assertEqual(2646, res)

    def test_area_49_55_values(self):
        res = rectangle.area(49, 55)
        self.assertEqual(2695, res)

    def test_area_49_56_values(self):
        res = rectangle.area(49, 56)
        self.assertEqual(2744, res)

    def test_area_49_57_values(self):
        res = rectangle.area(49, 57)
        self.assertEqual(2793, res)

    def test_area_49_58_values(self):
        res = rectangle.area(49, 58)
        self.assertEqual(2842, res)

    def test_area_49_59_values(self):
        res = rectangle.area(49, 59)
        self.assertEqual(2891, res)

    def test_area_50_30_values(self):
        res = rectangle.area(50, 30)
        self.assertEqual(1500, res)

    def test_area_50_31_values(self):
        res = rectangle.area(50, 31)
        self.assertEqual(1550, res)

    def test_area_50_32_values(self):
        res = rectangle.area(50, 32)
        self.assertEqual(1600, res)

    def test_area_50_33_values(self):
        res = rectangle.area(50, 33)
        self.assertEqual(1650, res)

    def test_area_50_34_values(self):
        res = rectangle.area(50, 34)
        self.assertEqual(1700, res)

    def test_area_50_35_values(self):
        res = rectangle.area(50, 35)
        self.assertEqual(1750, res)

    def test_area_50_36_values(self):
        res = rectangle.area(50, 36)
        self.assertEqual(1800, res)

    def test_area_50_37_values(self):
        res = rectangle.area(50, 37)
        self.assertEqual(1850, res)

    def test_area_50_38_values(self):
        res = rectangle.area(50, 38)
        self.assertEqual(1900, res)

    def test_area_50_39_values(self):
        res = rectangle.area(50, 39)
        self.assertEqual(1950, res)

    def test_area_50_40_values(self):
        res = rectangle.area(50, 40)
        self.assertEqual(2000, res)

    def test_area_50_41_values(self):
        res = rectangle.area(50, 41)
        self.assertEqual(2050, res)

    def test_area_50_42_values(self):
        res = rectangle.area(50, 42)
        self.assertEqual(2100, res)

    def test_area_50_43_values(self):
        res = rectangle.area(50, 43)
        self.assertEqual(2150, res)

    def test_area_50_44_values(self):
        res = rectangle.area(50, 44)
        self.assertEqual(2200, res)

    def test_area_50_45_values(self):
        res = rectangle.area(50, 45)
        self.assertEqual(2250, res)

    def test_area_50_46_values(self):
        res = rectangle.area(50, 46)
        self.assertEqual(2300, res)

    def test_area_50_47_values(self):
        res = rectangle.area(50, 47)
        self.assertEqual(2350, res)

    def test_area_50_48_values(self):
        res = rectangle.area(50, 48)
        self.assertEqual(2400, res)

    def test_area_50_49_values(self):
        res = rectangle.area(50, 49)
        self.assertEqual(2450, res)

    def test_area_50_50_values(self):
        res = rectangle.area(50, 50)
        self.assertEqual(2500, res)

    def test_area_50_51_values(self):
        res = rectangle.area(50, 51)
        self.assertEqual(2550, res)

    def test_area_50_52_values(self):
        res = rectangle.area(50, 52)
        self.assertEqual(2600, res)

    def test_area_50_53_values(self):
        res = rectangle.area(50, 53)
        self.assertEqual(2650, res)

    def test_area_50_54_values(self):
        res = rectangle.area(50, 54)
        self.assertEqual(2700, res)

    def test_area_50_55_values(self):
        res = rectangle.area(50, 55)
        self.assertEqual(2750, res)

    def test_area_50_56_values(self):
        res = rectangle.area(50, 56)
        self.assertEqual(2800, res)

    def test_area_50_57_values(self):
        res = rectangle.area(50, 57)
        self.assertEqual(2850, res)

    def test_area_50_58_values(self):
        res = rectangle.area(50, 58)
        self.assertEqual(2900, res)

    def test_area_50_59_values(self):
        res = rectangle.area(50, 59)
        self.assertEqual(2950, res)

    def test_area_51_30_values(self):
        res = rectangle.area(51, 30)
        self.assertEqual(1530, res)

    def test_area_51_31_values(self):
        res = rectangle.area(51, 31)
        self.assertEqual(1581, res)

    def test_area_51_32_values(self):
        res = rectangle.area(51, 32)
        self.assertEqual(1632, res)

    def test_area_51_33_values(self):
        res = rectangle.area(51, 33)
        self.assertEqual(1683, res)

    def test_area_51_34_values(self):
        res = rectangle.area(51, 34)
        self.assertEqual(1734, res)

    def test_area_51_35_values(self):
        res = rectangle.area(51, 35)
        self.assertEqual(1785, res)

    def test_area_51_36_values(self):
        res = rectangle.area(51, 36)
        self.assertEqual(1836, res)

    def test_area_51_37_values(self):
        res = rectangle.area(51, 37)
        self.assertEqual(1887, res)

    def test_area_51_38_values(self):
        res = rectangle.area(51, 38)
        self.assertEqual(1938, res)

    def test_area_51_39_values(self):
        res = rectangle.area(51, 39)
        self.assertEqual(1989, res)

    def test_area_51_40_values(self):
        res = rectangle.area(51, 40)
        self.assertEqual(2040, res)

    def test_area_51_41_values(self):
        res = rectangle.area(51, 41)
        self.assertEqual(2091, res)

    def test_area_51_42_values(self):
        res = rectangle.area(51, 42)
        self.assertEqual(2142, res)

    def test_area_51_43_values(self):
        res = rectangle.area(51, 43)
        self.assertEqual(2193, res)

    def test_area_51_44_values(self):
        res = rectangle.area(51, 44)
        self.assertEqual(2244, res)

    def test_area_51_45_values(self):
        res = rectangle.area(51, 45)
        self.assertEqual(2295, res)

    def test_area_51_46_values(self):
        res = rectangle.area(51, 46)
        self.assertEqual(2346, res)

    def test_area_51_47_values(self):
        res = rectangle.area(51, 47)
        self.assertEqual(2397, res)

    def test_area_51_48_values(self):
        res = rectangle.area(51, 48)
        self.assertEqual(2448, res)

    def test_area_51_49_values(self):
        res = rectangle.area(51, 49)
        self.assertEqual(2499, res)

    def test_area_51_50_values(self):
        res = rectangle.area(51, 50)
        self.assertEqual(2550, res)

    def test_area_51_51_values(self):
        res = rectangle.area(51, 51)
        self.assertEqual(2601, res)

    def test_area_51_52_values(self):
        res = rectangle.area(51, 52)
        self.assertEqual(2652, res)

    def test_area_51_53_values(self):
        res = rectangle.area(51, 53)
        self.assertEqual(2703, res)

    def test_area_51_54_values(self):
        res = rectangle.area(51, 54)
        self.assertEqual(2754, res)

    def test_area_51_55_values(self):
        res = rectangle.area(51, 55)
        self.assertEqual(2805, res)

    def test_area_51_56_values(self):
        res = rectangle.area(51, 56)
        self.assertEqual(2856, res)

    def test_area_51_57_values(self):
        res = rectangle.area(51, 57)
        self.assertEqual(2907, res)

    def test_area_51_58_values(self):
        res = rectangle.area(51, 58)
        self.assertEqual(2958, res)

    def test_area_51_59_values(self):
        res = rectangle.area(51, 59)
        self.assertEqual(3009, res)

    def test_area_52_30_values(self):
        res = rectangle.area(52, 30)
        self.assertEqual(1560, res)

    def test_area_52_31_values(self):
        res = rectangle.area(52, 31)
        self.assertEqual(1612, res)

    def test_area_52_32_values(self):
        res = rectangle.area(52, 32)
        self.assertEqual(1664, res)

    def test_area_52_33_values(self):
        res = rectangle.area(52, 33)
        self.assertEqual(1716, res)

    def test_area_52_34_values(self):
        res = rectangle.area(52, 34)
        self.assertEqual(1768, res)

    def test_area_52_35_values(self):
        res = rectangle.area(52, 35)
        self.assertEqual(1820, res)

    def test_area_52_36_values(self):
        res = rectangle.area(52, 36)
        self.assertEqual(1872, res)

    def test_area_52_37_values(self):
        res = rectangle.area(52, 37)
        self.assertEqual(1924, res)

    def test_area_52_38_values(self):
        res = rectangle.area(52, 38)
        self.assertEqual(1976, res)

    def test_area_52_39_values(self):
        res = rectangle.area(52, 39)
        self.assertEqual(2028, res)

    def test_area_52_40_values(self):
        res = rectangle.area(52, 40)
        self.assertEqual(2080, res)

    def test_area_52_41_values(self):
        res = rectangle.area(52, 41)
        self.assertEqual(2132, res)

    def test_area_52_42_values(self):
        res = rectangle.area(52, 42)
        self.assertEqual(2184, res)

    def test_area_52_43_values(self):
        res = rectangle.area(52, 43)
        self.assertEqual(2236, res)

    def test_area_52_44_values(self):
        res = rectangle.area(52, 44)
        self.assertEqual(2288, res)

    def test_area_52_45_values(self):
        res = rectangle.area(52, 45)
        self.assertEqual(2340, res)

    def test_area_52_46_values(self):
        res = rectangle.area(52, 46)
        self.assertEqual(2392, res)

    def test_area_52_47_values(self):
        res = rectangle.area(52, 47)
        self.assertEqual(2444, res)

    def test_area_52_48_values(self):
        res = rectangle.area(52, 48)
        self.assertEqual(2496, res)

    def test_area_52_49_values(self):
        res = rectangle.area(52, 49)
        self.assertEqual(2548, res)

    def test_area_52_50_values(self):
        res = rectangle.area(52, 50)
        self.assertEqual(2600, res)

    def test_area_52_51_values(self):
        res = rectangle.area(52, 51)
        self.assertEqual(2652, res)

    def test_area_52_52_values(self):
        res = rectangle.area(52, 52)
        self.assertEqual(2704, res)

    def test_area_52_53_values(self):
        res = rectangle.area(52, 53)
        self.assertEqual(2756, res)

    def test_area_52_54_values(self):
        res = rectangle.area(52, 54)
        self.assertEqual(2808, res)

    def test_area_52_55_values(self):
        res = rectangle.area(52, 55)
        self.assertEqual(2860, res)

    def test_area_52_56_values(self):
        res = rectangle.area(52, 56)
        self.assertEqual(2912, res)

    def test_area_52_57_values(self):
        res = rectangle.area(52, 57)
        self.assertEqual(2964, res)

    def test_area_52_58_values(self):
        res = rectangle.area(52, 58)
        self.assertEqual(3016, res)

    def test_area_52_59_values(self):
        res = rectangle.area(52, 59)
        self.assertEqual(3068, res)

    def test_area_53_30_values(self):
        res = rectangle.area(53, 30)
        self.assertEqual(1590, res)

    def test_area_53_31_values(self):
        res = rectangle.area(53, 31)
        self.assertEqual(1643, res)

    def test_area_53_32_values(self):
        res = rectangle.area(53, 32)
        self.assertEqual(1696, res)

    def test_area_53_33_values(self):
        res = rectangle.area(53, 33)
        self.assertEqual(1749, res)

    def test_area_53_34_values(self):
        res = rectangle.area(53, 34)
        self.assertEqual(1802, res)

    def test_area_53_35_values(self):
        res = rectangle.area(53, 35)
        self.assertEqual(1855, res)

    def test_area_53_36_values(self):
        res = rectangle.area(53, 36)
        self.assertEqual(1908, res)

    def test_area_53_37_values(self):
        res = rectangle.area(53, 37)
        self.assertEqual(1961, res)

    def test_area_53_38_values(self):
        res = rectangle.area(53, 38)
        self.assertEqual(2014, res)

    def test_area_53_39_values(self):
        res = rectangle.area(53, 39)
        self.assertEqual(2067, res)

    def test_area_53_40_values(self):
        res = rectangle.area(53, 40)
        self.assertEqual(2120, res)

    def test_area_53_41_values(self):
        res = rectangle.area(53, 41)
        self.assertEqual(2173, res)

    def test_area_53_42_values(self):
        res = rectangle.area(53, 42)
        self.assertEqual(2226, res)

    def test_area_53_43_values(self):
        res = rectangle.area(53, 43)
        self.assertEqual(2279, res)

    def test_area_53_44_values(self):
        res = rectangle.area(53, 44)
        self.assertEqual(2332, res)

    def test_area_53_45_values(self):
        res = rectangle.area(53, 45)
        self.assertEqual(2385, res)

    def test_area_53_46_values(self):
        res = rectangle.area(53, 46)
        self.assertEqual(2438, res)

    def test_area_53_47_values(self):
        res = rectangle.area(53, 47)
        self.assertEqual(2491, res)

    def test_area_53_48_values(self):
        res = rectangle.area(53, 48)
        self.assertEqual(2544, res)

    def test_area_53_49_values(self):
        res = rectangle.area(53, 49)
        self.assertEqual(2597, res)

    def test_area_53_50_values(self):
        res = rectangle.area(53, 50)
        self.assertEqual(2650, res)

    def test_area_53_51_values(self):
        res = rectangle.area(53, 51)
        self.assertEqual(2703, res)

    def test_area_53_52_values(self):
        res = rectangle.area(53, 52)
        self.assertEqual(2756, res)

    def test_area_53_53_values(self):
        res = rectangle.area(53, 53)
        self.assertEqual(2809, res)

    def test_area_53_54_values(self):
        res = rectangle.area(53, 54)
        self.assertEqual(2862, res)

    def test_area_53_55_values(self):
        res = rectangle.area(53, 55)
        self.assertEqual(2915, res)

    def test_area_53_56_values(self):
        res = rectangle.area(53, 56)
        self.assertEqual(2968, res)

    def test_area_53_57_values(self):
        res = rectangle.area(53, 57)
        self.assertEqual(3021, res)

    def test_area_53_58_values(self):
        res = rectangle.area(53, 58)
        self.assertEqual(3074, res)

    def test_area_53_59_values(self):
        res = rectangle.area(53, 59)
        self.assertEqual(3127, res)

    def test_area_54_30_values(self):
        res = rectangle.area(54, 30)
        self.assertEqual(1620, res)

    def test_area_54_31_values(self):
        res = rectangle.area(54, 31)
        self.assertEqual(1674, res)

    def test_area_54_32_values(self):
        res = rectangle.area(54, 32)
        self.assertEqual(1728, res)

    def test_area_54_33_values(self):
        res = rectangle.area(54, 33)
        self.assertEqual(1782, res)

    def test_area_54_34_values(self):
        res = rectangle.area(54, 34)
        self.assertEqual(1836, res)

    def test_area_54_35_values(self):
        res = rectangle.area(54, 35)
        self.assertEqual(1890, res)

    def test_area_54_36_values(self):
        res = rectangle.area(54, 36)
        self.assertEqual(1944, res)

    def test_area_54_37_values(self):
        res = rectangle.area(54, 37)
        self.assertEqual(1998, res)

    def test_area_54_38_values(self):
        res = rectangle.area(54, 38)
        self.assertEqual(2052, res)

    def test_area_54_39_values(self):
        res = rectangle.area(54, 39)
        self.assertEqual(2106, res)

    def test_area_54_40_values(self):
        res = rectangle.area(54, 40)
        self.assertEqual(2160, res)

    def test_area_54_41_values(self):
        res = rectangle.area(54, 41)
        self.assertEqual(2214, res)

    def test_area_54_42_values(self):
        res = rectangle.area(54, 42)
        self.assertEqual(2268, res)

    def test_area_54_43_values(self):
        res = rectangle.area(54, 43)
        self.assertEqual(2322, res)

    def test_area_54_44_values(self):
        res = rectangle.area(54, 44)
        self.assertEqual(2376, res)

    def test_area_54_45_values(self):
        res = rectangle.area(54, 45)
        self.assertEqual(2430, res)

    def test_area_54_46_values(self):
        res = rectangle.area(54, 46)
        self.assertEqual(2484, res)

    def test_area_54_47_values(self):
        res = rectangle.area(54, 47)
        self.assertEqual(2538, res)

    def test_area_54_48_values(self):
        res = rectangle.area(54, 48)
        self.assertEqual(2592, res)

    def test_area_54_49_values(self):
        res = rectangle.area(54, 49)
        self.assertEqual(2646, res)

    def test_area_54_50_values(self):
        res = rectangle.area(54, 50)
        self.assertEqual(2700, res)

    def test_area_54_51_values(self):
        res = rectangle.area(54, 51)
        self.assertEqual(2754, res)

    def test_area_54_52_values(self):
        res = rectangle.area(54, 52)
        self.assertEqual(2808, res)

    def test_area_54_53_values(self):
        res = rectangle.area(54, 53)
        self.assertEqual(2862, res)

    def test_area_54_54_values(self):
        res = rectangle.area(54, 54)
        self.assertEqual(2916, res)

    def test_area_54_55_values(self):
        res = rectangle.area(54, 55)
        self.assertEqual(2970, res)

    def test_area_54_56_values(self):
        res = rectangle.area(54, 56)
        self.assertEqual(3024, res)

    def test_area_54_57_values(self):
        res = rectangle.area(54, 57)
        self.assertEqual(3078, res)

    def test_area_54_58_values(self):
        res = rectangle.area(54, 58)
        self.assertEqual(3132, res)

    def test_area_54_59_values(self):
        res = rectangle.area(54, 59)
        self.assertEqual(3186, res)

    def test_area_55_30_values(self):
        res = rectangle.area(55, 30)
        self.assertEqual(1650, res)

    def test_area_55_31_values(self):
        res = rectangle.area(55, 31)
        self.assertEqual(1705, res)

    def test_area_55_32_values(self):
        res = rectangle.area(55, 32)
        self.assertEqual(1760, res)

    def test_area_55_33_values(self):
        res = rectangle.area(55, 33)
        self.assertEqual(1815, res)

    def test_area_55_34_values(self):
        res = rectangle.area(55, 34)
        self.assertEqual(1870, res)

    def test_area_55_35_values(self):
        res = rectangle.area(55, 35)
        self.assertEqual(1925, res)

    def test_area_55_36_values(self):
        res = rectangle.area(55, 36)
        self.assertEqual(1980, res)

    def test_area_55_37_values(self):
        res = rectangle.area(55, 37)
        self.assertEqual(2035, res)

    def test_area_55_38_values(self):
        res = rectangle.area(55, 38)
        self.assertEqual(2090, res)

    def test_area_55_39_values(self):
        res = rectangle.area(55, 39)
        self.assertEqual(2145, res)

    def test_area_55_40_values(self):
        res = rectangle.area(55, 40)
        self.assertEqual(2200, res)

    def test_area_55_41_values(self):
        res = rectangle.area(55, 41)
        self.assertEqual(2255, res)

    def test_area_55_42_values(self):
        res = rectangle.area(55, 42)
        self.assertEqual(2310, res)

    def test_area_55_43_values(self):
        res = rectangle.area(55, 43)
        self.assertEqual(2365, res)

    def test_area_55_44_values(self):
        res = rectangle.area(55, 44)
        self.assertEqual(2420, res)

    def test_area_55_45_values(self):
        res = rectangle.area(55, 45)
        self.assertEqual(2475, res)

    def test_area_55_46_values(self):
        res = rectangle.area(55, 46)
        self.assertEqual(2530, res)

    def test_area_55_47_values(self):
        res = rectangle.area(55, 47)
        self.assertEqual(2585, res)

    def test_area_55_48_values(self):
        res = rectangle.area(55, 48)
        self.assertEqual(2640, res)

    def test_area_55_49_values(self):
        res = rectangle.area(55, 49)
        self.assertEqual(2695, res)

    def test_area_55_50_values(self):
        res = rectangle.area(55, 50)
        self.assertEqual(2750, res)

    def test_area_55_51_values(self):
        res = rectangle.area(55, 51)
        self.assertEqual(2805, res)

    def test_area_55_52_values(self):
        res = rectangle.area(55, 52)
        self.assertEqual(2860, res)

    def test_area_55_53_values(self):
        res = rectangle.area(55, 53)
        self.assertEqual(2915, res)

    def test_area_55_54_values(self):
        res = rectangle.area(55, 54)
        self.assertEqual(2970, res)

    def test_area_55_55_values(self):
        res = rectangle.area(55, 55)
        self.assertEqual(3025, res)

    def test_area_55_56_values(self):
        res = rectangle.area(55, 56)
        self.assertEqual(3080, res)

    def test_area_55_57_values(self):
        res = rectangle.area(55, 57)
        self.assertEqual(3135, res)

    def test_area_55_58_values(self):
        res = rectangle.area(55, 58)
        self.assertEqual(3190, res)

    def test_area_55_59_values(self):
        res = rectangle.area(55, 59)
        self.assertEqual(3245, res)

    def test_area_56_30_values(self):
        res = rectangle.area(56, 30)
        self.assertEqual(1680, res)

    def test_area_56_31_values(self):
        res = rectangle.area(56, 31)
        self.assertEqual(1736, res)

    def test_area_56_32_values(self):
        res = rectangle.area(56, 32)
        self.assertEqual(1792, res)

    def test_area_56_33_values(self):
        res = rectangle.area(56, 33)
        self.assertEqual(1848, res)

    def test_area_56_34_values(self):
        res = rectangle.area(56, 34)
        self.assertEqual(1904, res)

    def test_area_56_35_values(self):
        res = rectangle.area(56, 35)
        self.assertEqual(1960, res)

    def test_area_56_36_values(self):
        res = rectangle.area(56, 36)
        self.assertEqual(2016, res)

    def test_area_56_37_values(self):
        res = rectangle.area(56, 37)
        self.assertEqual(2072, res)

    def test_area_56_38_values(self):
        res = rectangle.area(56, 38)
        self.assertEqual(2128, res)

    def test_area_56_39_values(self):
        res = rectangle.area(56, 39)
        self.assertEqual(2184, res)

    def test_area_56_40_values(self):
        res = rectangle.area(56, 40)
        self.assertEqual(2240, res)

    def test_area_56_41_values(self):
        res = rectangle.area(56, 41)
        self.assertEqual(2296, res)

    def test_area_56_42_values(self):
        res = rectangle.area(56, 42)
        self.assertEqual(2352, res)

    def test_area_56_43_values(self):
        res = rectangle.area(56, 43)
        self.assertEqual(2408, res)

    def test_area_56_44_values(self):
        res = rectangle.area(56, 44)
        self.assertEqual(2464, res)

    def test_area_56_45_values(self):
        res = rectangle.area(56, 45)
        self.assertEqual(2520, res)

    def test_area_56_46_values(self):
        res = rectangle.area(56, 46)
        self.assertEqual(2576, res)

    def test_area_56_47_values(self):
        res = rectangle.area(56, 47)
        self.assertEqual(2632, res)

    def test_area_56_48_values(self):
        res = rectangle.area(56, 48)
        self.assertEqual(2688, res)

    def test_area_56_49_values(self):
        res = rectangle.area(56, 49)
        self.assertEqual(2744, res)

    def test_area_56_50_values(self):
        res = rectangle.area(56, 50)
        self.assertEqual(2800, res)

    def test_area_56_51_values(self):
        res = rectangle.area(56, 51)
        self.assertEqual(2856, res)

    def test_area_56_52_values(self):
        res = rectangle.area(56, 52)
        self.assertEqual(2912, res)

    def test_area_56_53_values(self):
        res = rectangle.area(56, 53)
        self.assertEqual(2968, res)

    def test_area_56_54_values(self):
        res = rectangle.area(56, 54)
        self.assertEqual(3024, res)

    def test_area_56_55_values(self):
        res = rectangle.area(56, 55)
        self.assertEqual(3080, res)

    def test_area_56_56_values(self):
        res = rectangle.area(56, 56)
        self.assertEqual(3136, res)

    def test_area_56_57_values(self):
        res = rectangle.area(56, 57)
        self.assertEqual(3192, res)

    def test_area_56_58_values(self):
        res = rectangle.area(56, 58)
        self.assertEqual(3248, res)

    def test_area_56_59_values(self):
        res = rectangle.area(56, 59)
        self.assertEqual(3304, res)

    def test_area_57_30_values(self):
        res = rectangle.area(57, 30)
        self.assertEqual(1710, res)

    def test_area_57_31_values(self):
        res = rectangle.area(57, 31)
        self.assertEqual(1767, res)

    def test_area_57_32_values(self):
        res = rectangle.area(57, 32)
        self.assertEqual(1824, res)

    def test_area_57_33_values(self):
        res = rectangle.area(57, 33)
        self.assertEqual(1881, res)

    def test_area_57_34_values(self):
        res = rectangle.area(57, 34)
        self.assertEqual(1938, res)

    def test_area_57_35_values(self):
        res = rectangle.area(57, 35)
        self.assertEqual(1995, res)

    def test_area_57_36_values(self):
        res = rectangle.area(57, 36)
        self.assertEqual(2052, res)

    def test_area_57_37_values(self):
        res = rectangle.area(57, 37)
        self.assertEqual(2109, res)

    def test_area_57_38_values(self):
        res = rectangle.area(57, 38)
        self.assertEqual(2166, res)

    def test_area_57_39_values(self):
        res = rectangle.area(57, 39)
        self.assertEqual(2223, res)

    def test_area_57_40_values(self):
        res = rectangle.area(57, 40)
        self.assertEqual(2280, res)

    def test_area_57_41_values(self):
        res = rectangle.area(57, 41)
        self.assertEqual(2337, res)

    def test_area_57_42_values(self):
        res = rectangle.area(57, 42)
        self.assertEqual(2394, res)

    def test_area_57_43_values(self):
        res = rectangle.area(57, 43)
        self.assertEqual(2451, res)

    def test_area_57_44_values(self):
        res = rectangle.area(57, 44)
        self.assertEqual(2508, res)

    def test_area_57_45_values(self):
        res = rectangle.area(57, 45)
        self.assertEqual(2565, res)

    def test_area_57_46_values(self):
        res = rectangle.area(57, 46)
        self.assertEqual(2622, res)

    def test_area_57_47_values(self):
        res = rectangle.area(57, 47)
        self.assertEqual(2679, res)

    def test_area_57_48_values(self):
        res = rectangle.area(57, 48)
        self.assertEqual(2736, res)

    def test_area_57_49_values(self):
        res = rectangle.area(57, 49)
        self.assertEqual(2793, res)

    def test_area_57_50_values(self):
        res = rectangle.area(57, 50)
        self.assertEqual(2850, res)

    def test_area_57_51_values(self):
        res = rectangle.area(57, 51)
        self.assertEqual(2907, res)

    def test_area_57_52_values(self):
        res = rectangle.area(57, 52)
        self.assertEqual(2964, res)

    def test_area_57_53_values(self):
        res = rectangle.area(57, 53)
        self.assertEqual(3021, res)

    def test_area_57_54_values(self):
        res = rectangle.area(57, 54)
        self.assertEqual(3078, res)

    def test_area_57_55_values(self):
        res = rectangle.area(57, 55)
        self.assertEqual(3135, res)

    def test_area_57_56_values(self):
        res = rectangle.area(57, 56)
        self.assertEqual(3192, res)

    def test_area_57_57_values(self):
        res = rectangle.area(57, 57)
        self.assertEqual(3249, res)

    def test_area_57_58_values(self):
        res = rectangle.area(57, 58)
        self.assertEqual(3306, res)

    def test_area_57_59_values(self):
        res = rectangle.area(57, 59)
        self.assertEqual(3363, res)

    def test_area_58_30_values(self):
        res = rectangle.area(58, 30)
        self.assertEqual(1740, res)

    def test_area_58_31_values(self):
        res = rectangle.area(58, 31)
        self.assertEqual(1798, res)

    def test_area_58_32_values(self):
        res = rectangle.area(58, 32)
        self.assertEqual(1856, res)

    def test_area_58_33_values(self):
        res = rectangle.area(58, 33)
        self.assertEqual(1914, res)

    def test_area_58_34_values(self):
        res = rectangle.area(58, 34)
        self.assertEqual(1972, res)

    def test_area_58_35_values(self):
        res = rectangle.area(58, 35)
        self.assertEqual(2030, res)

    def test_area_58_36_values(self):
        res = rectangle.area(58, 36)
        self.assertEqual(2088, res)

    def test_area_58_37_values(self):
        res = rectangle.area(58, 37)
        self.assertEqual(2146, res)

    def test_area_58_38_values(self):
        res = rectangle.area(58, 38)
        self.assertEqual(2204, res)

    def test_area_58_39_values(self):
        res = rectangle.area(58, 39)
        self.assertEqual(2262, res)

    def test_area_58_40_values(self):
        res = rectangle.area(58, 40)
        self.assertEqual(2320, res)

    def test_area_58_41_values(self):
        res = rectangle.area(58, 41)
        self.assertEqual(2378, res)

    def test_area_58_42_values(self):
        res = rectangle.area(58, 42)
        self.assertEqual(2436, res)

    def test_area_58_43_values(self):
        res = rectangle.area(58, 43)
        self.assertEqual(2494, res)

    def test_area_58_44_values(self):
        res = rectangle.area(58, 44)
        self.assertEqual(2552, res)

    def test_area_58_45_values(self):
        res = rectangle.area(58, 45)
        self.assertEqual(2610, res)

    def test_area_58_46_values(self):
        res = rectangle.area(58, 46)
        self.assertEqual(2668, res)

    def test_area_58_47_values(self):
        res = rectangle.area(58, 47)
        self.assertEqual(2726, res)

    def test_area_58_48_values(self):
        res = rectangle.area(58, 48)
        self.assertEqual(2784, res)

    def test_area_58_49_values(self):
        res = rectangle.area(58, 49)
        self.assertEqual(2842, res)

    def test_area_58_50_values(self):
        res = rectangle.area(58, 50)
        self.assertEqual(2900, res)

    def test_area_58_51_values(self):
        res = rectangle.area(58, 51)
        self.assertEqual(2958, res)

    def test_area_58_52_values(self):
        res = rectangle.area(58, 52)
        self.assertEqual(3016, res)

    def test_area_58_53_values(self):
        res = rectangle.area(58, 53)
        self.assertEqual(3074, res)

    def test_area_58_54_values(self):
        res = rectangle.area(58, 54)
        self.assertEqual(3132, res)

    def test_area_58_55_values(self):
        res = rectangle.area(58, 55)
        self.assertEqual(3190, res)

    def test_area_58_56_values(self):
        res = rectangle.area(58, 56)
        self.assertEqual(3248, res)

    def test_area_58_57_values(self):
        res = rectangle.area(58, 57)
        self.assertEqual(3306, res)

    def test_area_58_58_values(self):
        res = rectangle.area(58, 58)
        self.assertEqual(3364, res)

    def test_area_58_59_values(self):
        res = rectangle.area(58, 59)
        self.assertEqual(3422, res)

    def test_area_59_30_values(self):
        res = rectangle.area(59, 30)
        self.assertEqual(1770, res)

    def test_area_59_31_values(self):
        res = rectangle.area(59, 31)
        self.assertEqual(1829, res)

    def test_area_59_32_values(self):
        res = rectangle.area(59, 32)
        self.assertEqual(1888, res)

    def test_area_59_33_values(self):
        res = rectangle.area(59, 33)
        self.assertEqual(1947, res)

    def test_area_59_34_values(self):
        res = rectangle.area(59, 34)
        self.assertEqual(2006, res)

    def test_area_59_35_values(self):
        res = rectangle.area(59, 35)
        self.assertEqual(2065, res)

    def test_area_59_36_values(self):
        res = rectangle.area(59, 36)
        self.assertEqual(2124, res)

    def test_area_59_37_values(self):
        res = rectangle.area(59, 37)
        self.assertEqual(2183, res)

    def test_area_59_38_values(self):
        res = rectangle.area(59, 38)
        self.assertEqual(2242, res)

    def test_area_59_39_values(self):
        res = rectangle.area(59, 39)
        self.assertEqual(2301, res)

    def test_area_59_40_values(self):
        res = rectangle.area(59, 40)
        self.assertEqual(2360, res)

    def test_area_59_41_values(self):
        res = rectangle.area(59, 41)
        self.assertEqual(2419, res)

    def test_area_59_42_values(self):
        res = rectangle.area(59, 42)
        self.assertEqual(2478, res)

    def test_area_59_43_values(self):
        res = rectangle.area(59, 43)
        self.assertEqual(2537, res)

    def test_area_59_44_values(self):
        res = rectangle.area(59, 44)
        self.assertEqual(2596, res)

    def test_area_59_45_values(self):
        res = rectangle.area(59, 45)
        self.assertEqual(2655, res)

    def test_area_59_46_values(self):
        res = rectangle.area(59, 46)
        self.assertEqual(2714, res)

    def test_area_59_47_values(self):
        res = rectangle.area(59, 47)
        self.assertEqual(2773, res)

    def test_area_59_48_values(self):
        res = rectangle.area(59, 48)
        self.assertEqual(2832, res)

    def test_area_59_49_values(self):
        res = rectangle.area(59, 49)
        self.assertEqual(2891, res)

    def test_area_59_50_values(self):
        res = rectangle.area(59, 50)
        self.assertEqual(2950, res)

    def test_area_59_51_values(self):
        res = rectangle.area(59, 51)
        self.assertEqual(3009, res)

    def test_area_59_52_values(self):
        res = rectangle.area(59, 52)
        self.assertEqual(3068, res)

    def test_area_59_53_values(self):
        res = rectangle.area(59, 53)
        self.assertEqual(3127, res)

    def test_area_59_54_values(self):
        res = rectangle.area(59, 54)
        self.assertEqual(3186, res)

    def test_area_59_55_values(self):
        res = rectangle.area(59, 55)
        self.assertEqual(3245, res)

    def test_area_59_56_values(self):
        res = rectangle.area(59, 56)
        self.assertEqual(3304, res)

    def test_area_59_57_values(self):
        res = rectangle.area(59, 57)
        self.assertEqual(3363, res)

    def test_area_59_58_values(self):
        res = rectangle.area(59, 58)
        self.assertEqual(3422, res)

    def test_area_59_59_values(self):
        res = rectangle.area(59, 59)
        self.assertEqual(3481, res)

