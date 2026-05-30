import os
import sys
import unittest
from unittest.mock import patch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.main import (
    normalize_cep,
    celsius_to_kelvin,
    celsius_to_fahrenheit,
    cep_to_coordinates,
    get_temperature_celsius,
)


class TestMainUnit(unittest.TestCase):
    def test_normalize_cep_removes_formatting(self):
        self.assertEqual(normalize_cep("01001-000"), "01001000")
        self.assertEqual(normalize_cep("01001000"), "01001000")

    def test_normalize_cep_rejects_invalid_length(self):
        with self.assertRaises(ValueError):
            normalize_cep("12345")

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0.0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(100.0), 373.15)

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0.0), 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100.0), 212.0)

    @patch("src.main.get_json")
    def test_cep_to_coordinates_calls_api_and_returns_lat_lon(self, mocked_get_json):
        mocked_get_json.return_value = [{"lat": "-23.55052", "lon": "-46.633308"}]
        lat, lon = cep_to_coordinates("01001-000")
        self.assertEqual(lat, -23.55052)
        self.assertEqual(lon, -46.633308)
        mocked_get_json.assert_called_once()

    @patch("src.main.get_json")
    def test_get_temperature_celsius_reads_temperature(self, mocked_get_json):
        mocked_get_json.return_value = {"current_weather": {"temperature": 22.4}}
        temperature = get_temperature_celsius(-23.55052, -46.633308)
        self.assertEqual(temperature, 22.4)
        mocked_get_json.assert_called_once()

    @patch("src.main.get_json")
    def test_get_temperature_celsius_raises_when_missing_temperature(self, mocked_get_json):
        mocked_get_json.return_value = {"current_weather": {}}
        with self.assertRaises(RuntimeError):
            get_temperature_celsius(-23.55, -46.63)


if __name__ == "__main__":
    unittest.main()
