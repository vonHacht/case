from __future__ import annotations

import csv
import time
from pathlib import Path

import requests

BASE_URL = "https://pokeapi.co/api/v2"
OUT_DIR = Path("../seeds")
OUT_DIR.mkdir(exist_ok=True)

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "dbt-poke-demo/1.0"})


def get_json(url: str) -> dict:
    resp = SESSION.get(url, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_pokemon(limit: int = 20) -> tuple[list[dict], list[dict], list[dict]]:
    """
    Returns:
      pokemon_rows: one row per pokemon
      type_rows: unique type dimension rows
      pokemon_type_rows: one row per pokemon-type relationship
    """
    listing = get_json(f"{BASE_URL}/pokemon?limit={limit}&offset=0")
    pokemon_rows: list[dict] = []
    pokemon_type_rows: list[dict] = []
    type_lookup: dict[int, dict] = {}

    for item in listing["results"]:
        details = get_json(item["url"])

        pokemon_id = details["id"]
        species = details["species"]

        pokemon_rows.append(
            {
                "pokemon_id": pokemon_id,
                "pokemon_name": details["name"],
                "height": details["height"],
                "weight": details["weight"],
                "base_experience": details.get("base_experience"),
                "species_id": species["url"].rstrip("/").split("/")[-1],
                "species_name": species["name"],
            }
        )

        for t in details["types"]:
            slot = t["slot"]
            type_name = t["type"]["name"]
            type_id = int(t["type"]["url"].rstrip("/").split("/")[-1])

            type_lookup[type_id] = {
                "type_id": type_id,
                "type_name": type_name,
            }

            pokemon_type_rows.append(
                {
                    "pokemon_id": pokemon_id,
                    "type_id": type_id,
                    "type_slot": slot,
                }
            )

        # tiny pause to be polite
        time.sleep(0.1)

    type_rows = sorted(type_lookup.values(), key=lambda x: x["type_id"])
    pokemon_rows = sorted(pokemon_rows, key=lambda x: x["pokemon_id"])
    pokemon_type_rows = sorted(
        pokemon_type_rows, key=lambda x: (x["pokemon_id"], x["type_slot"])
    )

    return pokemon_rows, type_rows, pokemon_type_rows


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    pokemon_rows, type_rows, pokemon_type_rows = fetch_pokemon(limit=20)

    write_csv(OUT_DIR / "raw_pokemon.csv", pokemon_rows)
    write_csv(OUT_DIR / "raw_type.csv", type_rows)
    write_csv(OUT_DIR / "raw_pokemon_type.csv", pokemon_type_rows)

    print("Wrote:")
    print(" - seeds/raw_pokemon.csv")
    print(" - seeds/raw_type.csv")
    print(" - seeds/raw_pokemon_type.csv")