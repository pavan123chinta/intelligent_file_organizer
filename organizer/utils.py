import json
import os


def load_config(config_path="config.json"):
    """
    Loads and validates the configuration file.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        dict: Categories dictionary from config file.

    Raises:
        FileNotFoundError: If config file does not exist.
        ValueError: If JSON format is invalid.
        KeyError: If required keys are missing.
    """

    # Check if config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

    try:
        # Open and load JSON
        with open(config_path, "r") as file:
            config_data = json.load(file)

        # Validate required key
        if "categories" not in config_data:
            raise KeyError("Missing 'categories' key in configuration file.")

        return config_data["categories"]

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in configuration file.")

    except Exception as e:
        raise e
