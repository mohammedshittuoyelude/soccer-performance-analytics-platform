# Soccer Performance Analytics Platform ⚽

A data + analytics project that ingests soccer datasets, cleans and normalizes them, and produces player/team performance insights.

## MVP Goals
- Ingest a public soccer dataset
- Clean/normalize data into analysis-ready tables
- Compute core performance metrics (minutes, trends, consistency)
- Produce a simple notebook with insights

## Repo Structure
- `data/raw/` - raw downloaded data
- `data/processed/` - cleaned outputs (CSV/Parquet)
- `notebooks/` - analysis + charts
- `src/` - ingestion, transforms, analytics modules
- `reports/` - exported charts / summaries

## Early Insights (StatsBomb Sample)

### Top Players by Total Events
![Top Players by Events](reports/top_players_by_events.png)

### Top Players by Pass Events
![Top Players by Passes](reports/top_players_by_passes.png)
