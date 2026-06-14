import logging
import logging.config
from pathlib import Path

import coloredlogs
import yaml

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOGGING_CONFIG_PATH = ROOT / "config" / "logging.yaml"


def setup_logging(
    default_path=DEFAULT_LOGGING_CONFIG_PATH,
    default_level=logging.INFO,
) -> None:

    if default_path.exists():
        try:
            with default_path.open("r", encoding="utf-8") as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
            coloredlogs.install()

        except Exception as e:
            print(f"Error in Logging configuration. Using default configs: {e}")

            logging.basicConfig(level=default_level)
            coloredlogs.install(level=default_level)

    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print("Failed to load configuration file. Using default configs")
