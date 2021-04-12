import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodulla_kassalla_on_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodulla_kassalla_on_oikea_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

# Edullisen käteistestit #

    def test_edullisen_ostaminen_kateisella_lisaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_ostaminen_kateisella_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_edullisen_ostaminen_kateisella_lisaa_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_ostaminen_kateisella_ei_lisaa_kassaan_jos_liian_pieni_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_ostaminen_kateisella_ei_lisaa_edullisten_maaraa_jos_liian_pieni_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_ostaminen_kateisella_antaa_oikean_vaihtorahan_jos_liian_pieni_maksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

# Maukkaan käteistestit #

    def test_maukkaan_ostaminen_kateisella_lisaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_ostaminen_kateisella_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_maukkaan_ostaminen_kateisella_lisaa_edullisten_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_emaukkaan_ostaminen_kateisella_ei_lisaa_kassaan_jos_liian_pieni_maksu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_ostaminen_kateisella_ei_lisaa_edullisten_maaraa_jos_liian_pieni_maksu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_ostaminen_kateisella_antaa_oikean_vaihtorahan_jos_liian_pieni_maksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

# Edullisen korttitestit #

    def test_edullisen_ostaminen_kortilla_onnistuu_jos_on_saldoa(self):
        self.assertTrue(
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_edullisen_ostaminen_kortilla_lisaa_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_ostaminen_kortilla_ei_lisaa_edullisten_maaraa_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_ostaminen_kortilla_ei_lisaa_kassaan_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_ostaminen_kortilla_ei_onnistu_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.assertFalse(
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_edullisen_ostaminen_kortilla_ei_muuta_kortin_saldoa_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(
            self.maksukortti.saldo, 100)

# Maukkaat korttitestit #

    def test_maukkaan_ostaminen_kortilla_onnistuu_jos_on_saldoa(self):
        self.assertTrue(
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaan_ostaminen_kortilla_lisaa_edullisten_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_ostaminen_kortilla_ei_lisaa_edullisten_maaraa_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_ostaminen_kortilla_ei_lisaa_kassaan_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_ostaminen_kortilla_ei_onnistu_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.assertFalse(
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaan_ostaminen_kortilla_ei_muuta_kortin_saldoa_jos_liian_pieni_maksu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(
            self.maksukortti.saldo, 100)

# Kortin lataamisen testit #

    def test_kortin_lataaminen_muuttaa_kortin_saldoa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_kortin_lataaminen_muuttaa_kassan_saldoa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_lataaminen_negatiivisella_ei_muuta_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
