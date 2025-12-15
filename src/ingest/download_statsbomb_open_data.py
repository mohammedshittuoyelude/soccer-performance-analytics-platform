import json
from pathlib import Path
import requests

BASE = "https://raw.githubusercontent.com/statsbomb/open-data/master/data"
RAW_DIR = Path("data/raw/statsbomb")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def fetch_json(url: str):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()

def save_json(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f)

def main():
    competitions = fetch_json(f"{BASE}/competitions.json")
    save_json(competitions, RAW_DIR / "competitions.json")

    comp = competitions[0]
    comp_id, season_id = comp["competition_id"], comp["season_id"]

    matches = fetch_json(f"{BASE}/matches/{comp_id}/{season_id}.json")
    save_json(matches, RAW_DIR / f"matches_{comp_id}_{season_id}.json")

    N = min(5, len(matches))
    for m in matches[:N]:
        match_id = m["match_id"]
        events = fetch_json(f"{BASE}/events/{match_id}.json")
        save_json(events, RAW_DIR / "events" / f"{match_id}.json")

    print(f"Saved competitions + matches + {N} match event files into {RAW_DIR}")

if __name__ == "__main__":
    main()
