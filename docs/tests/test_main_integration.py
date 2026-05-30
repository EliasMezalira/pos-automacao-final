import os
import sys
import unittest
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.main import cep_to_coordinates, get_temperature_celsius, celsius_to_kelvin, celsius_to_fahrenheit


class TestMainIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            urllib.request.urlopen("https://nominatim.openstreetmap.org", timeout=5).close()
            urllib.request.urlopen("https://api.open-meteo.com", timeout=5).close()
        except Exception as exc:
            raise unittest.SkipTest(f"Ignorando testes de integração por falta de rede: {exc}")

    def test_full_temperature_flow_for_cep(self):
        cep = "01001-000"
        lat, lon = cep_to_coordinates(cep)
        self.assertIsInstance(lat, float)
        self.assertIsInstance(lon, float)

        temperatura_c = get_temperature_celsius(lat, lon)
        self.assertIsInstance(temperatura_c, float)

        temperatura_k = celsius_to_kelvin(temperatura_c)
        temperatura_f = celsius_to_fahrenheit(temperatura_c)

        self.assertAlmostEqual(temperatura_k, temperatura_c + 273.15, places=2)
        self.assertAlmostEqual(temperatura_f, (temperatura_c * 9.0 / 5.0) + 32.0, places=2)
        self.assertGreaterEqual(temperatura_k, 0.0)


if __name__ == "__main__":
    unittest.main()