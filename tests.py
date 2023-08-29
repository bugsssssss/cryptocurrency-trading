import unittest
import pandas as pd
import numpy as np
from main import calculate_ema


class TestEMACalculation(unittest.TestCase):
    def test_ema_calculation(self):
        # Test series
        data = pd.Series([10, 12, 15, 20, 18, 22, 25, 30])
        ema = calculate_ema(data, length=3)
        # Expected result
        expected_ema = pd.Series(
            [10.0, 11.0, 12.3333, 15.6667, 17.6667, 20.0, 21.6667, 25.6667])

        # Checking if the non-NaN values are almost equal within a tolerance
        mask = ~ema.isnull()
        np.testing.assert_almost_equal(
            ema[mask].values, expected_ema[mask].values, decimal=4)


if __name__ == '__main__':
    unittest.main()
