"""Module entrypoint to run the CLI via `python -m opengov_earlyjapanese`."""

from .cli import app


def main() -> None:
    app()


if __name__ == "__main__":
    main()

