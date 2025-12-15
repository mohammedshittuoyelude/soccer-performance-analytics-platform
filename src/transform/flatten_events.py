import json
from pathlib import Path

import pandas as pd

RAW_EVENTS_DIR = Path("data/raw/statsbomb/events")
OUT_DIR = Path("data/processed/statsbomb")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def flatten_event(e: dict) -> dict:
    loc = e.get("location") or [None, None]
    return {
        "match_id": None,  # we'll fill this from the filename
        "event_id": e.get("id"),
        "index": e.get("index"),
        "period": e.get("period"),
        "minute": e.get("minute"),
        "second": e.get("second"),
        "team": (e.get("team") or {}).get("name"),
        "player": (e.get("player") or {}).get("name"),
        "possession": e.get("possession"),
        "type": (e.get("type") or {}).get("name"),
        "play_pattern": (e.get("play_pattern") or {}).get("name"),
        "x": loc[0],
        "y": loc[1],
    }


def main():
    if not RAW_EVENTS_DIR.exists():
        raise SystemExit("No events found. Run the download script first.")

    rows = []

    for p in RAW_EVENTS_DIR.rglob("*.json"):
        match_id_from_file = p.stem  # e.g. "3895292" from "3895292.json"

        with p.open("r", encoding="utf-8") as f:
            events = json.load(f)

        for e in events:
            row = flatten_event(e)
            row["match_id"] = match_id_from_file
            rows.append(row)

    df = pd.DataFrame(rows)

    df.to_csv(OUT_DIR / "events_flat.csv", index=False)
    df.to_parquet(OUT_DIR / "events_flat.parquet", index=False)

    print(f"Wrote {len(df):,} rows to {OUT_DIR}")


if __name__ == "__main__":
    main()
