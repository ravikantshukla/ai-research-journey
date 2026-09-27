from pathlib import Path

from src.utils import load_config, set_seed

CONFIG = Path(__file__).resolve().parents[1] / "configs" / "default.yaml"


def test_config_loads():
    config = load_config(CONFIG)
    for key in ("seed", "batch_size", "hidden_dim", "lr", "epochs"):
        assert key in config


def test_set_seed_runs():
    set_seed(0)
