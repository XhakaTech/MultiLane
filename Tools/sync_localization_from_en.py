# When a non-English table entry still matches English, replace with the value below.
# Usage: python Tools/sync_localization_from_en.py
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "Assets/Resources/Localization/Text"
LANGS = ["es", "fr", "de", "id", "it", "pl", "pt", "tr", "vi"]
TABLES = ["general", "gameplay"]

OVERRIDES: dict[str, dict[str, str]] = {
    "es": {
        "menu": "Menú",
        "video": "Vídeo",
        "tutorial": "Tutorial guiado",
        "vsync": "Sincronización vertical",
        "version": "Versión",
        "build": "Compilación",
        "credits_text": "Por Mortak con asistentes de IA",
    },
}

def load_en(table: str) -> dict[str, str]:
    path = ROOT / "en" / f"{table}.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return {e["key"]: e["value"] for e in data["entries"]}

def save(lang: str, table: str, entries: list[dict[str, str]]) -> None:
    path = ROOT / lang / f"{table}.json"
    lines = ["{", '  "entries": [']
    for i, e in enumerate(entries):
        key = json.dumps(e["key"], ensure_ascii=False)
        val = json.dumps(e["value"], ensure_ascii=False)
        comma = "," if i < len(entries) - 1 else ""
        lines.append(f'    {{ "key": {key}, "value": {val} }}{comma}')
    lines.append("  ]")
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> None:
    for table in TABLES:
        en_map = load_en(table)
        ovr_table = OVERRIDES
        for lang in LANGS:
            path = ROOT / lang / f"{table}.json"
            with path.open(encoding="utf-8") as f:
                data = json.load(f)
            entries = data["entries"]
            lang_ovr = ovr_table.get(lang, {})
            changed = 0
            new_entries: list[dict[str, str]] = []
            for e in entries:
                key = e["key"]
                val = e["value"]
                en_val = en_map.get(key)
                if en_val is not None and val == en_val and key in lang_ovr:
                    new_entries.append({"key": key, "value": lang_ovr[key]})
                    changed += 1
                else:
                    new_entries.append(dict(e))
            if changed:
                save(lang, table, new_entries)
                print(f"{lang}/{table}.json: {changed} fixes")
    print("Done.")

if __name__ == "__main__":
    main()
