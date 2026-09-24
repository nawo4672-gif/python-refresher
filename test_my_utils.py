import math
import random
import tempfile
import unittest
from pathlib import Path
from statistics import StatisticsError

import my_utils


class TestStatisticsFunctions(unittest.TestCase):
    def setUp(self):
        self.random_generator = random.Random(2026)

    def test_mean_with_random_integers(self):
        numbers = [self.random_generator.randint(-100, 100) for _ in range(25)]

        expected = sum(numbers) / len(numbers)

        self.assertEqual(my_utils.mean(numbers), expected)

    def test_mean_with_empty_array(self):
        with self.assertRaises(StatisticsError):
            my_utils.mean([])

    def test_median_with_random_odd_length_array(self):
        numbers = [self.random_generator.randint(-100, 100) for _ in range(11)]

        expected = sorted(numbers)[len(numbers) // 2]

        self.assertEqual(my_utils.median(numbers), expected)

    def test_median_with_empty_array(self):
        with self.assertRaises(StatisticsError):
            my_utils.median([])

    def test_standard_deviation_with_random_integers(self):
        numbers = [self.random_generator.randint(-100, 100) for _ in range(25)]
        expected_mean = sum(numbers) / len(numbers)
        expected = math.sqrt(
            sum((number - expected_mean) ** 2 for number in numbers)
            / len(numbers)
        )

        self.assertAlmostEqual(my_utils.standard_deviation(numbers), expected)

    def test_standard_deviation_with_empty_array(self):
        with self.assertRaises(StatisticsError):
            my_utils.standard_deviation([])


class TestGetColumn(unittest.TestCase):
    def test_get_column_with_random_csv_values(self):
        random_generator = random.Random(2026)
        rows = [
            (f"country_{index}", random_generator.randint(1, 1000))
            for index in range(10)
        ]

        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "data.csv"
            file_path.write_text(
                "".join(f"{country},{value}\n" for country, value in rows)
            )

            result = my_utils.get_column(
                str(file_path), 0, rows[4][0], result_column=1
            )

        self.assertEqual(result, [rows[4][1]])

    def test_get_column_with_missing_file(self):
        result = my_utils.get_column("missing.csv", 0, "country")

        self.assertEqual(result, [])

    def test_get_column_with_unmatched_query(self):
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "data.csv"
            file_path.write_text("country_1,10\n")

            result = my_utils.get_column(
                str(file_path), 0, "missing_country", result_column=1
            )

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
