from django.test import SimpleTestCase

# Create your tests here.


class TestFrontTimes(SimpleTestCase):
    def test_Chocolate_2_times(self):
        response = self.client.get("/warmup-2/font-times?string=Chocolate&n=2")
        self.assertContains(response, "ChoCho")

    def test_word_7_times(self):
        response = self.client.get("/warmup-2/font-times?string=word&n=7")
        self.assertContains(response, "worworworworworworwor")

    def test_word_0_times(self):
        response = self.client.get("/warmup-2/font-times?string=word&n=1")
        self.assertContains(response, "wor")


class TestNoTeen(SimpleTestCase):

    def test_13_14_17(self):
        response = self.client.get("/logic-2/no-teen-sum?a=13&b=14&c=17")
        self.assertContains(response, "0")

    def test_12_1_19(self):
        response = self.client.get("/logic-2/no-teen-sum?a=12&b=1&c=19")
        self.assertContains(response, "13")

    def test_12_15_19(self):
        response = self.client.get("/logic-2/no-teen-sum?a=12&b=15&c=19")
        self.assertContains(response, "27")


class TestXYZ(SimpleTestCase):

    def test_xyz(self):
        response = self.client.get("/string-2/xyz-there?string=abcxyz")
        self.assertContains(response, "True")

    def test_xy(self):
        response = self.client.get("/string-2/xyz-there?string=abcxy")
        self.assertContains(response, "False")

    def test_dotxyz(self):
        response = self.client.get("/string-2/xyz-there?string=.xyz")
        self.assertContains(response, "False")


class TestCenteredAvg(SimpleTestCase):

    def test_15_10_13_12(self):
        response = self.client.get("/list-2/centered-average?a=15&b=10&c=13&d=12")
        self.assertContains(response, "12.5")

    def test_1_2_3_4(self):
        response = self.client.get("/list-2/centered-average?a=1&b=2&c=3&d=4")
        self.assertContains(response, "2.5")

    def test_1_2_3_4_1(self):
        response = self.client.get("/list-2/centered-average?a=1&b=2&c=3&d=4&e=1")
        self.assertContains(response, "2.0")
