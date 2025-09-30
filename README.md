# OpenGov-EarlyJapanese

Simple Japanese learning toolkit focusing on core features implemented in this repository.

## Features

- Hiragana lessons with mnemonics
- Minimal Kanji analysis (offline sample)
- Spaced repetition scheduler
- FastAPI API, Typer CLI, Streamlit UI

## Quick Start

### Install (uv)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
cp .env.example .env
```

### Run
```bash
# API
uv run uvicorn opengov_earlyjapanese.api.main:app --reload

# UI
uv run streamlit run opengov_earlyjapanese/ui/app.py

# CLI
uv run python -m opengov_earlyjapanese --help
```

## Usage

```python
from opengov_earlyjapanese import HiraganaTeacher, KanjiMaster

print(HiraganaTeacher().get_lesson("a_row").characters)
print(KanjiMaster().analyze("愛").meanings)
```

### CLI Usage

Run via module (no install required):
```bash
python3 -m opengov_earlyjapanese --help
python3 -m opengov_earlyjapanese --version
python3 -m opengov_earlyjapanese rows
python3 -m opengov_earlyjapanese mnemonic あ
python3 -m opengov_earlyjapanese hiragana a_row
python3 -m opengov_earlyjapanese characters ka_row
python3 -m opengov_earlyjapanese search ko --kind hiragana
python3 -m opengov_earlyjapanese characters a_row --format table
python3 -m opengov_earlyjapanese search Apple --format table
python3 -m opengov_earlyjapanese katakana rows
python3 -m opengov_earlyjapanese katakana rows --format table
python3 -m opengov_earlyjapanese katakana characters ka_row --format table
python3 -m opengov_earlyjapanese katakana mnemonic ア
python3 -m opengov_earlyjapanese kanji analyze 愛
python3 -m opengov_earlyjapanese kanji sentences 愛 --level N4

# Color control
python3 -m opengov_earlyjapanese --no-color katakana rows --format table
```

After installing the package, the `nihongo` entry point is available:
```bash
nihongo --help
nihongo rows
nihongo kanji analyze 愛
```

## Configuration

Environment variables in `.env` (optional):
- `API_HOST`, `API_PORT`
- `DATABASE_URL`, `REDIS_URL` (not required for current features)
- `MECAB_DICT_PATH` (unused in this build)

## Testing

```bash
uv run pytest -q
```

## License

MIT
