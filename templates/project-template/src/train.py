import argparse

from src.utils import load_config, set_seed


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the model.")
    parser.add_argument("--config", default="configs/default.yaml", help="Path to YAML config")
    args = parser.parse_args()

    config = load_config(args.config)
    set_seed(config["seed"])
    print(f"Loaded config: {config}")

    # TODO: build data, model and optimizer; run the training loop; save results to results/


if __name__ == "__main__":
    main()
