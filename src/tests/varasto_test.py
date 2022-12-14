import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_varastoiminen(self):
        self.varasto.lisaa_varastoon(300)

        self.assertNotAlmostEqual(self.varasto.saldo, 300)

    def test_liikaa_ottaminen(self):
        self.varasto.lisaa_varastoon(3)

        saatu_maara = self.varasto.ota_varastosta(4)

        self.assertNotAlmostEqual(saatu_maara, 4)

    def test_negatiivinen_tilavuus(self):
        varasto2 = Varasto(-3)

        self.assertAlmostEqual(varasto2.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        varasto2 = Varasto(10, -5)

        self.assertAlmostEqual(varasto2.saldo, 0)

    def test_liian_suuri_alkusaldo(self):
        varasto2 = Varasto(10, 15)

        self.assertAlmostEqual(varasto2.tilavuus, varasto2.saldo)

    def test_negatiivisen_maaran_varastointi(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivisen_maaran_ottaminen(self):
        self.varasto.lisaa_varastoon(5)
        
        self.assertAlmostEqual(self.varasto.ota_varastosta(-3), 0)

    def test_str(self):
        self.varasto.lisaa_varastoon(2)

        self.assertEqual("saldo = 2, vielä tilaa 8", self.varasto.__str__())
    