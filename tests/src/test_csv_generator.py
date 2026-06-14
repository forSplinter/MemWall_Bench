from pathlib import Path

import pytest

from src.csv_generator import CSVGenerator


class TestCsvGenerator:
    @pytest.fixture
    def generator(self):
        return CSVGenerator()

    def test_generate(self, generator):
        filepath = generator.generate(name="test", num_rows=10)
        assert filepath.exists()
        assert filepath.suffix == ".csv"

    def test_generate_ctm(self, generator):
        filepath = generator.generate_ctm(num_rows=10, dataset_name="test_ctm")
        assert filepath.exists()
