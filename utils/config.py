import yaml
import numpy as np


def load_config(config_path):
    """
    Load configuration from YAML file.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config


def validate_config(config):
    """
    Validate required configuration keys.
    """

    required_keys = ["seed", "window", "version"]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key: {key}")


def set_seed(seed):
    """
    Set random seed for reproducibility.
    """

    np.random.seed(seed)