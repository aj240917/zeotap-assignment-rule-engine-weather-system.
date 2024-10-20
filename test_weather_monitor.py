import unittest
from weather_utils import convert_kelvin_to_celsius

class TestWeatherUtils(unittest.TestCase):
    def test_convert_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert_kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(convert_kelvin_to_celsius(310.15), 37)

if __name__ == '__main__':
    unittest.main()
