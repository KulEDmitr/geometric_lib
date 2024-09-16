import unittest
import circle
import rectangle
import square
import triangle


class circleTestCase(unittest.TestCase):
    def test_normal_data_area(self):
        self.assertEqual(circle.area(65), 13273.228961416877)
        self.assertEqual(circle.area(76), 18145.839167134644)
        self.assertEqual(circle.area(9), 254.46900494077323)
        self.assertEqual(circle.area(99), 30790.74959783356)
        self.assertEqual(circle.area(87), 23778.714795021144)
        self.assertEqual(circle.area(94), 27759.112687119414)
        self.assertEqual(circle.area(21), 1385.4423602330987)
        self.assertEqual(circle.area(11), 380.132711084365)
        self.assertEqual(circle.area(84), 22167.07776372958)
        self.assertEqual(circle.area(76), 18145.839167134644)


    def test_normal_data_perimeter(self):
        self.assertEqual(circle.perimeter(52), 326.7256359733385)
        self.assertEqual(circle.perimeter(89), 559.2034923389832)
        self.assertEqual(circle.perimeter(85), 534.0707511102648)
        self.assertEqual(circle.perimeter(63), 395.84067435231395)
        self.assertEqual(circle.perimeter(17), 106.81415022205297)
        self.assertEqual(circle.perimeter(28), 175.92918860102841)
        self.assertEqual(circle.perimeter(14), 87.96459430051421)
        self.assertEqual(circle.perimeter(53), 333.0088212805181)
        self.assertEqual(circle.perimeter(10), 62.83185307179586)
        self.assertEqual(circle.perimeter(74), 464.9557127312894)


    def test_big_data_area(self):
        self.assertEqual(circle.area(244146374), 1.8726233310557875e+17)
        self.assertEqual(circle.area(399456024), 5.0128859339843565e+17)
        self.assertEqual(circle.area(763739655), 1.8324855304139853e+18)
        self.assertEqual(circle.area(893195285), 2.5063557613965727e+18)
        self.assertEqual(circle.area(549916304), 9.500425671052247e+17)
        self.assertEqual(circle.area(893324198), 2.507079287733983e+18)
        self.assertEqual(circle.area(652091952), 1.3358803239232348e+18)
        self.assertEqual(circle.area(987248866), 3.0619857117963387e+18)
        self.assertEqual(circle.area(746907345), 1.752602122112026e+18)
        self.assertEqual(circle.area(900069502), 2.545083089133981e+18)


    def test_big_data_perimeter(self):
        self.assertEqual(circle.perimeter(405444377), 2547482152.444981)
        self.assertEqual(circle.perimeter(253662646), 1593809410.3274965)
        self.assertEqual(circle.perimeter(602111877), 3783180498.8447223)
        self.assertEqual(circle.perimeter(972038516), 6107498121.743849)
        self.assertEqual(circle.perimeter(715313665), 4494448309.952781)
        self.assertEqual(circle.perimeter(618717341), 3887515706.2684216)
        self.assertEqual(circle.perimeter(145453895), 913913775.9360423)
        self.assertEqual(circle.perimeter(728211486), 4575487709.354613)
        self.assertEqual(circle.perimeter(599877056), 3769138704.373346)
        self.assertEqual(circle.perimeter(541497838), 3402331259.5911117)


    def test_negative_area(self):
        with self.assertRaises(ValueError):
            circle.area(-10)
            circle.area(-69)
            circle.area(-47)
            circle.area(-15)
            circle.area(-37)
            circle.area(-93)
            circle.area(-43)
            circle.area(-43)
            circle.area(-80)
            circle.area(-73)


    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-67)
            circle.perimeter(-51)
            circle.perimeter(-23)
            circle.perimeter(-96)
            circle.perimeter(-55)
            circle.perimeter(-51)
            circle.perimeter(-73)
            circle.perimeter(-63)
            circle.perimeter(-36)
            circle.perimeter(-5)


    def test_string_area(self):
        with self.assertRaises(TypeError):
            circle.area('65')
            circle.area('50')
            circle.area('88')
            circle.area('22')
            circle.area('40')
            circle.area('70')
            circle.area('60')
            circle.area('23')
            circle.area('3')
            circle.area('17')


    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            circle.perimeter('22')
            circle.perimeter('94')
            circle.perimeter('3')
            circle.perimeter('26')
            circle.perimeter('86')
            circle.perimeter('28')
            circle.perimeter('15')
            circle.perimeter('4')
            circle.perimeter('41')
            circle.perimeter('96')


    def test_float_area(self):
        self.assertEqual(circle.area(89.89263093775926), 25386.220936431873)
        self.assertEqual(circle.area(78.98276927436828), 19598.1278402586)
        self.assertEqual(circle.area(71.34040657757339), 15988.99007401501)
        self.assertEqual(circle.area(36.857943092056985), 4267.878655182311)
        self.assertEqual(circle.area(96.4988787384809), 29254.61634077967)
        self.assertEqual(circle.area(85.92178187952842), 23192.973017151617)
        self.assertEqual(circle.area(64.2547037175968), 12970.589758724222)
        self.assertEqual(circle.area(36.9027442583862), 4278.260251752128)
        self.assertEqual(circle.area(69.27380060343843), 15076.06159387116)
        self.assertEqual(circle.area(67.65940828493873), 14381.56880501298)


    def test_float_perimeter(self):
        self.assertEqual(circle.perimeter(79.99220979214947), 502.60587725486056)
        self.assertEqual(circle.perimeter(6.520043541531145), 40.96664178231964)
        self.assertEqual(circle.perimeter(5.652377213524611), 35.514933458654525)
        self.assertEqual(circle.perimeter(54.147278865236885), 340.21738698981216)
        self.assertEqual(circle.perimeter(93.40005057756464), 586.8498254787844)
        self.assertEqual(circle.perimeter(1.2837193936050493), 8.065846832440734)
        self.assertEqual(circle.perimeter(47.087134815206866), 295.85719362809215)
        self.assertEqual(circle.perimeter(13.569694648215357), 85.2609060365802)
        self.assertEqual(circle.perimeter(16.34420439953978), 102.6936649407283)
        self.assertEqual(circle.perimeter(20.95325697077549), 131.65319633633482)


class triangleTestCase(unittest.TestCase):
    def test_normal_data_area(self):
        self.assertEqual(triangle.area(46, 19), 437.0)
        self.assertEqual(triangle.area(68, 27), 918.0)
        self.assertEqual(triangle.area(39, 38), 741.0)
        self.assertEqual(triangle.area(76, 84), 3192.0)
        self.assertEqual(triangle.area(2, 25), 25.0)
        self.assertEqual(triangle.area(2, 92), 92.0)
        self.assertEqual(triangle.area(24, 26), 312.0)
        self.assertEqual(triangle.area(21, 29), 304.5)
        self.assertEqual(triangle.area(52, 50), 1300.0)
        self.assertEqual(triangle.area(32, 26), 416.0)


    def test_normal_data_perimeter(self):
        self.assertEqual(triangle.perimeter(94, 73, 72), 239)
        self.assertEqual(triangle.perimeter(43, 93, 91), 227)
        self.assertEqual(triangle.perimeter(65, 47, 30), 142)
        self.assertEqual(triangle.perimeter(91, 10, 12), 113)
        self.assertEqual(triangle.perimeter(2, 39, 9), 50)
        self.assertEqual(triangle.perimeter(75, 51, 75), 201)
        self.assertEqual(triangle.perimeter(86, 92, 45), 223)
        self.assertEqual(triangle.perimeter(60, 14, 98), 172)
        self.assertEqual(triangle.perimeter(59, 13, 48), 120)
        self.assertEqual(triangle.perimeter(49, 28, 40), 117)


    def test_big_data_area(self):
        self.assertEqual(triangle.area(607884765, 865703229), 2.631239019602031e+17)
        self.assertEqual(triangle.area(401667959, 590247062), 1.1854166634964323e+17)
        self.assertEqual(triangle.area(912266425, 400459785), 1.826630082091093e+17)
        self.assertEqual(triangle.area(444139335, 757190914), 1.681491345060011e+17)
        self.assertEqual(triangle.area(353062714, 250190020), 4.416638373845714e+16)
        self.assertEqual(triangle.area(438587365, 712739519), 1.562992737847887e+17)
        self.assertEqual(triangle.area(361564353, 255942984), 4.626992970742467e+16)
        self.assertEqual(triangle.area(880239694, 226576216), 9.972068951975894e+16)
        self.assertEqual(triangle.area(955386111, 234509489), 1.1202355434415363e+17)
        self.assertEqual(triangle.area(418229310, 275561298), 5.762390576262219e+16)


    def test_big_data_perimeter(self):
        self.assertEqual(triangle.perimeter(500285905, 427267478, 615529565), 1543082948)
        self.assertEqual(triangle.perimeter(743882085, 650722757, 387741608), 1782346450)
        self.assertEqual(triangle.perimeter(990800626, 976136498, 931197729), 2898134853)
        self.assertEqual(triangle.perimeter(548974054, 107231729, 740244935), 1396450718)
        self.assertEqual(triangle.perimeter(384648905, 256265237, 392696013), 1033610155)
        self.assertEqual(triangle.perimeter(330922669, 151034991, 898124130), 1380081790)
        self.assertEqual(triangle.perimeter(846237232, 254006902, 374987017), 1475231151)
        self.assertEqual(triangle.perimeter(845782714, 390509032, 798923992), 2035215738)
        self.assertEqual(triangle.perimeter(732256479, 375741058, 118348407), 1226345944)
        self.assertEqual(triangle.perimeter(700765127, 353064604, 190032479), 1243862210)


    def test_negative_area(self):
        with self.assertRaises(ValueError):
            triangle.area(-19, -27)
            triangle.area(-27, -72)
            triangle.area(-29, -1)
            triangle.area(-82, -17)
            triangle.area(-27, -12)
            triangle.area(-3, -30)
            triangle.area(-55, -10)
            triangle.area(-8, -8)
            triangle.area(-80, -72)
            triangle.area(-58, -51)


    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-96, -43, -67)
            triangle.perimeter(-62, -43, -24)
            triangle.perimeter(-33, -72, -86)
            triangle.perimeter(-31, -68, -44)
            triangle.perimeter(-86, -23, -79)
            triangle.perimeter(-64, -67, -18)
            triangle.perimeter(-83, -96, -54)
            triangle.perimeter(-21, -66, -15)
            triangle.perimeter(-32, -99, -38)
            triangle.perimeter(-45, -17, -30)


    def test_string_area(self):
        with self.assertRaises(TypeError):
            triangle.area('70', '12')
            triangle.area('40', '51')
            triangle.area('87', '78')
            triangle.area('24', '4')
            triangle.area('45', '82')
            triangle.area('40', '93')
            triangle.area('66', '10')
            triangle.area('26', '33')
            triangle.area('44', '13')
            triangle.area('85', '47')


    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter('36', '12', '58')
            triangle.perimeter('59', '59', '19')
            triangle.perimeter('1', '41', '61')
            triangle.perimeter('55', '92', '20')
            triangle.perimeter('27', '99', '85')
            triangle.perimeter('15', '92', '49')
            triangle.perimeter('61', '36', '96')
            triangle.perimeter('68', '26', '81')
            triangle.perimeter('47', '88', '29')
            triangle.perimeter('37', '49', '55')


    def test_float_area(self):
        self.assertEqual(triangle.area(52.793997911468594, 2.5113291266581106), 66.29155233389928)
        self.assertEqual(triangle.area(98.95332578552635, 21.76977687399772), 1077.095911645457)
        self.assertEqual(triangle.area(22.567960503713138, 50.86180603852614), 573.9236149124881)
        self.assertEqual(triangle.area(84.87933162331481, 54.80394252977501), 2325.8610061249296)
        self.assertEqual(triangle.area(11.146337812716963, 80.6079300200469), 449.24160919364573)
        self.assertEqual(triangle.area(74.77937131338989, 16.711889401861978), 624.8522914650711)
        self.assertEqual(triangle.area(95.0895557648501, 94.64013936463436), 4499.644404853292)
        self.assertEqual(triangle.area(55.429544004743896, 43.583506004274845), 1207.906931972486)
        self.assertEqual(triangle.area(99.0382967165392, 86.63336605573066), 4290.0105064900035)
        self.assertEqual(triangle.area(35.237554245518396, 1.6913712434197246), 29.799892969656224)


    def test_float_perimeter(self):
        self.assertEqual(triangle.perimeter(16.2448390453607, 66.0057663055476, 40.26925917532492), 122.51986452623322)
        self.assertEqual(triangle.perimeter(34.69122779225349, 4.845672768768608, 8.067624200642395), 47.60452476166449)
        self.assertEqual(triangle.perimeter(33.2123627050341, 62.43794720193273, 83.57348619946056), 179.22379610642741)
        self.assertEqual(triangle.perimeter(43.540172543193435, 39.38037580607255, 85.81527694489827), 168.73582529416427)
        self.assertEqual(triangle.perimeter(74.73024621186863, 79.99482420997019, 52.75314471312819), 207.47821513496703)
        self.assertEqual(triangle.perimeter(62.26563029138346, 62.783217544815045, 32.716222970806136), 157.76507080700463)
        self.assertEqual(triangle.perimeter(98.5420228797748, 47.74120487992237, 35.63964592602157), 181.92287368571874)
        self.assertEqual(triangle.perimeter(81.51575303054791, 19.84767789088052, 82.41246515448455), 183.77589607591298)
        self.assertEqual(triangle.perimeter(24.34240891658433, 38.42767787590784, 66.88639143659157), 129.65647822908375)
        self.assertEqual(triangle.perimeter(95.10165079956626, 52.35151849257675, 25.48748159824757), 172.94065089039057)


class rectangleTestCase(unittest.TestCase):
    def test_normal_data_area(self):
        self.assertEqual(rectangle.area(18, 32), 576)
        self.assertEqual(rectangle.area(65, 64), 4160)
        self.assertEqual(rectangle.area(84, 14), 1176)
        self.assertEqual(rectangle.area(94, 5), 470)
        self.assertEqual(rectangle.area(58, 100), 5800)
        self.assertEqual(rectangle.area(45, 88), 3960)
        self.assertEqual(rectangle.area(84, 46), 3864)
        self.assertEqual(rectangle.area(2, 35), 70)
        self.assertEqual(rectangle.area(72, 25), 1800)
        self.assertEqual(rectangle.area(93, 13), 1209)


    def test_normal_data_perimeter(self):
        self.assertEqual(rectangle.perimeter(13, 93), 212)
        self.assertEqual(rectangle.perimeter(56, 97), 306)
        self.assertEqual(rectangle.perimeter(17, 68), 170)
        self.assertEqual(rectangle.perimeter(71, 41), 224)
        self.assertEqual(rectangle.perimeter(54, 28), 164)
        self.assertEqual(rectangle.perimeter(1, 69), 140)
        self.assertEqual(rectangle.perimeter(38, 55), 186)
        self.assertEqual(rectangle.perimeter(79, 21), 200)
        self.assertEqual(rectangle.perimeter(38, 12), 100)
        self.assertEqual(rectangle.perimeter(61, 13), 148)


    def test_big_data_area(self):
        self.assertEqual(rectangle.area(928791268, 410558957), 381323574260787476)
        self.assertEqual(rectangle.area(658869355, 381761045), 251530653483275975)
        self.assertEqual(rectangle.area(911251659, 275726557), 251256282496608063)
        self.assertEqual(rectangle.area(260699700, 200950034), 52387613578789800)
        self.assertEqual(rectangle.area(357395257, 739726359), 264374692184479263)
        self.assertEqual(rectangle.area(316791132, 705386277), 223460117188095564)
        self.assertEqual(rectangle.area(917892060, 535599956), 491622946948749360)
        self.assertEqual(rectangle.area(585367843, 183830247), 107608315164547221)
        self.assertEqual(rectangle.area(357585130, 335543671), 119985427215212230)
        self.assertEqual(rectangle.area(878312363, 282463196), 248090917139292148)


    def test_big_data_perimeter(self):
        self.assertEqual(rectangle.perimeter(962259323, 927423965), 3779366576)
        self.assertEqual(rectangle.perimeter(872526379, 672736026), 3090524810)
        self.assertEqual(rectangle.perimeter(521023339, 767571796), 2577190270)
        self.assertEqual(rectangle.perimeter(600778346, 943165104), 3087886900)
        self.assertEqual(rectangle.perimeter(205926835, 915969073), 2243791816)
        self.assertEqual(rectangle.perimeter(966864717, 858250734), 3650230902)
        self.assertEqual(rectangle.perimeter(290743775, 526856147), 1635199844)
        self.assertEqual(rectangle.perimeter(802675722, 237826737), 2081004918)
        self.assertEqual(rectangle.perimeter(429104924, 942980608), 2744171064)
        self.assertEqual(rectangle.perimeter(980812149, 522923926), 3007472150)


    def test_negative_area(self):
        with self.assertRaises(ValueError):
            rectangle.area(-24, -91)
            rectangle.area(-9, -80)
            rectangle.area(-52, -86)
            rectangle.area(-45, -50)
            rectangle.area(-4, -65)
            rectangle.area(-93, -40)
            rectangle.area(-15, -17)
            rectangle.area(-22, -39)
            rectangle.area(-72, -21)
            rectangle.area(-74, -19)


    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-86, -23)
            rectangle.perimeter(-6, -67)
            rectangle.perimeter(-79, -30)
            rectangle.perimeter(-68, -68)
            rectangle.perimeter(-65, -91)
            rectangle.perimeter(-60, -91)
            rectangle.perimeter(-31, -72)
            rectangle.perimeter(-74, -15)
            rectangle.perimeter(-3, -49)
            rectangle.perimeter(-97, -26)


    def test_string_area(self):
        with self.assertRaises(TypeError):
            rectangle.area('36', '35')
            rectangle.area('19', '17')
            rectangle.area('50', '65')
            rectangle.area('41', '26')
            rectangle.area('13', '48')
            rectangle.area('71', '99')
            rectangle.area('17', '23')
            rectangle.area('5', '79')
            rectangle.area('68', '67')
            rectangle.area('7', '77')


    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter('12', '46')
            rectangle.perimeter('80', '21')
            rectangle.perimeter('27', '73')
            rectangle.perimeter('71', '48')
            rectangle.perimeter('5', '27')
            rectangle.perimeter('44', '29')
            rectangle.perimeter('42', '51')
            rectangle.perimeter('53', '58')
            rectangle.perimeter('15', '60')
            rectangle.perimeter('33', '69')


    def test_float_area(self):
        self.assertEqual(rectangle.area(90.19497900740845, 61.88880581550366), 5582.05954132293)
        self.assertEqual(rectangle.area(63.694988373065975, 61.35246140006639), 3907.844315536208)
        self.assertEqual(rectangle.area(15.145324999041918, 47.08021015307457), 713.0450837915074)
        self.assertEqual(rectangle.area(97.25732255151995, 65.63020673176058), 6383.018185233775)
        self.assertEqual(rectangle.area(80.53178454276612, 90.49917272407669), 7288.05987911392)
        self.assertEqual(rectangle.area(10.872316960574723, 5.845384324056344), 63.5528711275154)
        self.assertEqual(rectangle.area(25.424846348140964, 75.81646265034465), 1927.6219135445808)
        self.assertEqual(rectangle.area(95.28319091684781, 24.4987626538077), 2334.3202791693)
        self.assertEqual(rectangle.area(82.45100383790174, 12.503954446738085), 1030.9635960769504)
        self.assertEqual(rectangle.area(43.66923524193527, 25.493340668559927), 1113.2746907581388)


    def test_float_perimeter(self):
        self.assertEqual(rectangle.perimeter(83.71178772657221, 85.6966467405694), 338.8168689342832)
        self.assertEqual(rectangle.perimeter(36.553915641548784, 79.52567822812587), 232.1591877393493)
        self.assertEqual(rectangle.perimeter(28.114486887259037, 84.86647143847534), 225.96191665146875)
        self.assertEqual(rectangle.perimeter(60.453235249030364, 85.41889480464364), 291.744260107348)
        self.assertEqual(rectangle.perimeter(25.481786744583957, 98.93110938907938), 248.82579226732668)
        self.assertEqual(rectangle.perimeter(89.68789990928964, 48.42313781860361), 276.22207545578647)
        self.assertEqual(rectangle.perimeter(11.114521740384031, 42.437233276188), 107.10351003314406)
        self.assertEqual(rectangle.perimeter(26.814723496781674, 75.77089774895258), 205.1712424914685)
        self.assertEqual(rectangle.perimeter(98.08445672361569, 3.214154437296147), 202.59722232182366)
        self.assertEqual(rectangle.perimeter(59.540019848127365, 42.94268192889789), 204.9654035540505)


class squareTestCase(unittest.TestCase):
    def test_normal_data_area(self):
        self.assertEqual(square.area(44), 1936)
        self.assertEqual(square.area(95), 9025)
        self.assertEqual(square.area(40), 1600)
        self.assertEqual(square.area(42), 1764)
        self.assertEqual(square.area(42), 1764)
        self.assertEqual(square.area(51), 2601)
        self.assertEqual(square.area(66), 4356)
        self.assertEqual(square.area(16), 256)
        self.assertEqual(square.area(79), 6241)
        self.assertEqual(square.area(44), 1936)


    def test_normal_data_perimeter(self):
        self.assertEqual(square.perimeter(15), 60)
        self.assertEqual(square.perimeter(44), 176)
        self.assertEqual(square.perimeter(75), 300)
        self.assertEqual(square.perimeter(35), 140)
        self.assertEqual(square.perimeter(74), 296)
        self.assertEqual(square.perimeter(91), 364)
        self.assertEqual(square.perimeter(41), 164)
        self.assertEqual(square.perimeter(45), 180)
        self.assertEqual(square.perimeter(79), 316)
        self.assertEqual(square.perimeter(46), 184)


    def test_big_data_area(self):
        self.assertEqual(square.area(325927055), 106228445180973025)
        self.assertEqual(square.area(638251527), 407365011717831729)
        self.assertEqual(square.area(484512910), 234752759956668100)
        self.assertEqual(square.area(689563802), 475498237028695204)
        self.assertEqual(square.area(265773631), 70635622934924161)
        self.assertEqual(square.area(477458508), 227966626861586064)
        self.assertEqual(square.area(940449700), 884445638230090000)
        self.assertEqual(square.area(608471551), 370237628376345601)
        self.assertEqual(square.area(824049457), 679057507581994849)
        self.assertEqual(square.area(480746186), 231116895353546596)


    def test_big_data_perimeter(self):
        self.assertEqual(square.perimeter(238257463), 953029852)
        self.assertEqual(square.perimeter(125017364), 500069456)
        self.assertEqual(square.perimeter(572536453), 2290145812)
        self.assertEqual(square.perimeter(941990065), 3767960260)
        self.assertEqual(square.perimeter(330970535), 1323882140)
        self.assertEqual(square.perimeter(762830647), 3051322588)
        self.assertEqual(square.perimeter(245815969), 983263876)
        self.assertEqual(square.perimeter(765583040), 3062332160)
        self.assertEqual(square.perimeter(307319464), 1229277856)
        self.assertEqual(square.perimeter(154410391), 617641564)


    def test_negative_area(self):
        with self.assertRaises(ValueError):
            square.area(-72)
            square.area(-88)
            square.area(-7)
            square.area(-44)
            square.area(-30)
            square.area(-48)
            square.area(-72)
            square.area(-17)
            square.area(-66)
            square.area(-14)


    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            square.perimeter(-91)
            square.perimeter(-38)
            square.perimeter(-82)
            square.perimeter(-81)
            square.perimeter(-69)
            square.perimeter(-27)
            square.perimeter(-61)
            square.perimeter(-87)
            square.perimeter(-64)
            square.perimeter(-26)


    def test_string_area(self):
        with self.assertRaises(TypeError):
            square.area('97')
            square.area('86')
            square.area('46')
            square.area('84')
            square.area('79')
            square.area('28')
            square.area('79')
            square.area('36')
            square.area('46')
            square.area('36')


    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            square.perimeter('94')
            square.perimeter('51')
            square.perimeter('81')
            square.perimeter('26')
            square.perimeter('36')
            square.perimeter('35')
            square.perimeter('79')
            square.perimeter('10')
            square.perimeter('2')
            square.perimeter('26')


    def test_float_area(self):
        self.assertEqual(square.area(66.73698255735431), 4453.824840860613)
        self.assertEqual(square.area(90.84008715188621), 8251.921433762282)
        self.assertEqual(square.area(78.52373951843227), 6165.977667958601)
        self.assertEqual(square.area(56.31769425671107), 3171.682686392387)
        self.assertEqual(square.area(21.51868201528743), 463.0536756750546)
        self.assertEqual(square.area(34.498637658482366), 1190.1560002912577)
        self.assertEqual(square.area(23.707303945802057), 562.0362603786417)
        self.assertEqual(square.area(82.2055270462687), 6757.748676954815)
        self.assertEqual(square.area(81.77233267892966), 6686.714391753547)
        self.assertEqual(square.area(54.25056571131141), 2943.123879997317)


    def test_float_perimeter(self):
        self.assertEqual(square.perimeter(57.445254303960105), 229.78101721584042)
        self.assertEqual(square.perimeter(64.2207996815011), 256.8831987260044)
        self.assertEqual(square.perimeter(53.7639624511771), 215.0558498047084)
        self.assertEqual(square.perimeter(39.973591876280544), 159.89436750512218)
        self.assertEqual(square.perimeter(5.4253222623913615), 21.701289049565446)
        self.assertEqual(square.perimeter(39.87966498622469), 159.51865994489876)
        self.assertEqual(square.perimeter(66.80413446018783), 267.2165378407513)
        self.assertEqual(square.perimeter(81.07184514086492), 324.2873805634597)
        self.assertEqual(square.perimeter(15.8897800945936), 63.5591203783744)
        self.assertEqual(square.perimeter(96.53268222398549), 386.13072889594196)
