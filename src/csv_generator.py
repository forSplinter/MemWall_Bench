import csv
import logging
import random
import re
from pathlib import Path

from faker import Faker

from src.utils.faker_provider import CustomProvider
from src.utils.logging_utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

SEED = 42
LOCALE = "fr_FR"
OUTPUT_DIR = Path("./data")
COLUMNS = ["id", "ticker", "quantity", "price", "timestamp", "order_type", "status"]


class CSVGenerator:
    def __init__(self) -> None:
        random.seed(SEED)
        Faker.seed(SEED)
        self.fake = Faker(locale=LOCALE)
        self.fake.add_provider(CustomProvider)
        self.output_dir = OUTPUT_DIR
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

    def _generate_row(self) -> list:
        return [
            self.fake.pyint(),
            self.fake.ticker(),
            self.fake.quantity(),
            self.fake.stock_price(),
            self.fake.iso8601(),
            self.fake.order_type(),
            self.fake.status(),
        ]

    def generate(self, name: str, num_rows: int) -> Path | None:
        filepath = self.output_dir / f"stock_transactions_{name}.csv"
        logger.info(f"Generating {num_rows:,} rows -> {filepath.name}")

        try:
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(COLUMNS)
                for _ in range(num_rows):
                    writer.writerow(self._generate_row())

            size_mb = filepath.stat().st_size / (1024 * 1024)
            logger.info(f"Generated {filepath.name}: {size_mb:.1f} MB")
            return filepath

        except Exception as e:
            logger.error(f"Error generating {filepath.name}: {e}")
            return None

    def generate_ctm(self, num_rows: int, dataset_name: str = "fooBar") -> Path | None:
        return self.generate(dataset_name, num_rows)
