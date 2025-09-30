"""Typer CLI for common tasks."""

import json
from typing import Optional

import typer

from opengov_earlyjapanese import __version__
from opengov_earlyjapanese.core.hiragana import HiraganaTeacher
from opengov_earlyjapanese.core.katakana import KatakanaTeacher
from opengov_earlyjapanese.core.kanji import KanjiMaster

# Global settings
COLOR_OUTPUT = True

app = typer.Typer(add_completion=False, help="OpenGov-EarlyJapanese CLI")
kanji_app = typer.Typer(help="Kanji utilities")
katakana_app = typer.Typer(help="Katakana utilities")


@app.callback(invoke_without_command=True)
def version_callback(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None, "--version", help="Show version", is_eager=True
    ),
    color: bool = typer.Option(True, "--color/--no-color", help="Colorize table output"),
):
    # Update color preference early
    # Typer doesn't pass boolean options here unless defined, so handle via env later if needed
    # For now, keep default True and allow override via a dedicated option on commands that print tables.
    # Persist color setting
    global COLOR_OUTPUT
    COLOR_OUTPUT = bool(color)
    if version:
        typer.echo(__version__)
        raise typer.Exit()
    # If no subcommand and no version, show help
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit(code=0)


def _print_table(rows, headers):
    # Basic table renderer without external deps
    widths = [len(h) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(str(cell)))
    def fmt(r):
        return " | ".join(str(c).ljust(widths[i]) for i, c in enumerate(r))
    sep = "-+-".join("-" * w for w in widths)
    header = fmt(headers)
    # Colorize header and separator when supported
    if COLOR_OUTPUT:
        typer.secho(header, bold=True)
        typer.secho(sep, dim=True)
        for r in rows:
            typer.echo(fmt(r))
    else:
        lines = [header, sep]
        for r in rows:
            lines.append(fmt(r))
        typer.echo("\n".join(lines))


@app.command()
def hiragana(
    row: str = typer.Argument("a_row"),
    fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table"),
):
    """Show hiragana for a given row (e.g., a_row)."""
    t = HiraganaTeacher()
    try:
        lesson = t.get_lesson(row)
    except ValueError as e:
        typer.secho(str(e), err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if fmt == "table":
        rows = [
            [
                c,
                t.characters[c].romaji,
                t.characters[c].unicode,
                (t.characters[c].mnemonic or "")[:40],
            ]
            for c in lesson.characters
        ]
        _print_table(rows, ["char", "romaji", "unicode", "mnemonic"])
    else:
        typer.echo(json.dumps(lesson.model_dump(), ensure_ascii=False, indent=2))


@app.command()
def rows(fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table")):
    """List available hiragana rows."""
    t = HiraganaTeacher()
    items = sorted(list(t.rows.keys()))
    if fmt == "table":
        _print_table([[r] for r in items], ["row"])
    else:
        typer.echo(json.dumps(items, ensure_ascii=False))


@app.command()
def mnemonic(character: str = typer.Argument(..., help="A single hiragana character")):
    """Show mnemonic for a given hiragana character."""
    if len(character) != 1:
        typer.secho("Please provide a single hiragana character.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    t = HiraganaTeacher()
    m = t.get_mnemonic(character)
    if m is None:
        typer.secho("Character not found.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    typer.echo(m)


@kanji_app.command("analyze")
def kanji_analyze(
    character: str = typer.Argument(..., help="A single kanji character"),
    fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table"),
):
    """Analyze a kanji and print meanings and readings."""
    if len(character) != 1:
        typer.secho("Please provide a single kanji character.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    km = KanjiMaster()
    analysis = km.analyze(character)
    if fmt == "table":
        rows = [[
            analysis.character,
            ", ".join(analysis.meanings),
            ", ".join(analysis.on_reading),
            ", ".join(analysis.kun_reading),
            ", ".join(analysis.radicals),
        ]]
        _print_table(rows, ["char", "meanings", "on", "kun", "radicals"])
    else:
        typer.echo(json.dumps(analysis.model_dump(), ensure_ascii=False, indent=2))


@app.command()
def characters(
    row: str = typer.Argument("a_row", help="Row name like a_row, ka_row"),
    fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table"),
):
    """List detailed character info for a row."""
    t = HiraganaTeacher()
    try:
        lesson = t.get_lesson(row)
    except ValueError as e:
        typer.secho(str(e), err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if fmt == "table":
        rows = [
            [
                c,
                t.characters[c].romaji,
                t.characters[c].unicode,
                (t.characters[c].mnemonic or "")[:40],
            ]
            for c in lesson.characters
        ]
        _print_table(rows, ["char", "romaji", "unicode", "mnemonic"])
    else:
        details = [t.characters[c].model_dump() for c in lesson.characters]
        typer.echo(json.dumps(details, ensure_ascii=False, indent=2))


@kanji_app.command("sentences")
def kanji_sentences(
    character: str = typer.Argument(..., help="A single kanji character"),
    level: str = typer.Option("N5", "--level", "-l", help="JLPT level N5..N1"),
    fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table"),
):
    """Generate example sentences for a kanji at a JLPT level."""
    if len(character) != 1:
        typer.secho("Please provide a single kanji character.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if level not in {"N5", "N4", "N3", "N2", "N1"}:
        typer.secho("Level must be one of N5, N4, N3, N2, N1.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    km = KanjiMaster()
    sentences = km.generate_sentences(character, level=level)
    if fmt == "table":
        _print_table([[i + 1, s] for i, s in enumerate(sentences)], ["#", "sentence"])
    else:
        typer.echo(json.dumps(sentences, ensure_ascii=False, indent=2))


app.add_typer(kanji_app, name="kanji")
app.add_typer(katakana_app, name="katakana")


@katakana_app.command("rows")
def katakana_rows(fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table")):
    """List available katakana rows."""
    t = KatakanaTeacher()
    items = sorted(list(t.rows.keys()))
    if fmt == "table":
        _print_table([[r] for r in items], ["row"])
    else:
        typer.echo(json.dumps(items, ensure_ascii=False))


@katakana_app.command("characters")
def katakana_characters(
    row: str = typer.Argument("a_row"),
    fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table"),
):
    """List katakana characters for a row."""
    t = KatakanaTeacher()
    if row not in t.rows:
        typer.secho(f"Unknown row: {row}", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if fmt == "table":
        rows = [
            [
                c,
                t.characters[c].romaji,
                t.characters[c].unicode,
                (t.characters[c].mnemonic or "")[:40],
            ]
            for c in t.rows[row]
        ]
        _print_table(rows, ["char", "romaji", "unicode", "mnemonic"])
    else:
        details = [t.characters[c].model_dump() for c in t.rows[row]]
        typer.echo(json.dumps(details, ensure_ascii=False, indent=2))


@katakana_app.command("mnemonic")
def katakana_mnemonic(character: str = typer.Argument(..., help="A single katakana character")):
    """Show mnemonic for a given katakana character."""
    if len(character) != 1:
        typer.secho("Please provide a single katakana character.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    t = KatakanaTeacher()
    ch = t.characters.get(character)
    if not ch or not ch.mnemonic:
        typer.secho("Character not found.", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    typer.echo(ch.mnemonic)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search string for character, romaji, or mnemonic"),
    kind: str = typer.Option("all", "--kind", "-k", help="Content kind", case_sensitive=False),
    fmt: str = typer.Option("json", "--format", "-f", "-F", help="json or table"),
):
    """Search hiragana/katakana by character, romaji, or mnemonic."""
    kind = kind.lower()
    if kind not in {"all", "hiragana", "katakana"}:
        typer.secho("--kind must be one of: all, hiragana, katakana", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)

    query_lower = query.lower()
    results = []

    def match_char(obj):
        romaji = (obj.romaji or "").lower()
        mnemonic = (obj.mnemonic or "").lower()
        return (
            query in obj.character
            or query_lower in romaji
            or (mnemonic and query_lower in mnemonic)
        )

    if kind in {"all", "hiragana"}:
        ht = HiraganaTeacher()
        for ch in ht.characters.values():
            if match_char(ch):
                results.append({
                    "type": "hiragana",
                    "row": ch.row,
                    "character": ch.character,
                    "romaji": ch.romaji,
                    "mnemonic": ch.mnemonic,
                })

    if kind in {"all", "katakana"}:
        kt = KatakanaTeacher()
        for ch in kt.characters.values():
            if match_char(ch):
                results.append({
                    "type": "katakana",
                    "row": ch.row,
                    "character": ch.character,
                    "romaji": ch.romaji,
                    "mnemonic": ch.mnemonic,
                })

    if fmt == "table":
        table_rows = [[r["type"], r["row"], r["character"], r["romaji"], (r["mnemonic"] or "")[:40]] for r in results]
        _print_table(table_rows, ["type", "row", "char", "romaji", "mnemonic"])
    else:
        typer.echo(json.dumps(results, ensure_ascii=False, indent=2))



if __name__ == "__main__":
    app()
