import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_ottaminen_pienentaa_saldoa_oikein_jos_on_saldoa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_ottaminen_ei_pienenna_saldoa_jos_ei_ole_saldoa(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ottaminen_palauttaa_false_jos_ei_saldoa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(11))

    def test_ottaminen_palauttaa_true_jos_on_saldoa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))
