---
name: timesfm-forecasting
description: Forecast time series data (sales, demand, metrics, sensor readings, etc.) using Google Research's TimesFM pretrained foundation model. Use this skill when the user asks to forecast, predict future values of, or project a trend from historical time series data, especially when they want a quick zero-shot forecast without training a custom model.
---

# TimesFM Forecasting

Generate point and quantile forecasts for a time series using [TimesFM](https://github.com/google-research/timesfm), Google Research's pretrained time-series foundation model. TimesFM works zero-shot: no training or fine-tuning is required, just historical values and a forecast horizon.

## When to Use This Skill

- The user has a CSV (or similar) of historical values and wants to project it forward — sales, web traffic, demand, sensor readings, prices, etc.
- The user wants uncertainty bounds (quantiles), not just a single-point prediction.
- The user wants a fast baseline forecast without training or fine-tuning a model themselves.

## Quick Start

```bash
python scripts/forecast.py data.csv --horizon 30 -o forecast.csv
```

This reads the `value` column from `data.csv`, forecasts 30 steps ahead using TimesFM 2.5, and writes the point forecast plus quantiles to `forecast.csv`. The script installs the `timesfm` package automatically the first time it runs.

## Options

- `--value-column NAME` — column in the input CSV holding the series values (default: `value`).
- `--horizon N` — required; number of future steps to forecast.
- `--max-context N` — how much history the model attends to (default: 1024; raise for long, slow-moving series).
- `--backend {torch,mlx}` — inference backend; use `mlx` on Apple Silicon without a GPU (default: `torch`).
- `-o, --output PATH` — output CSV path (default: `forecast.csv`).

## Output

The output CSV has one row per forecasted step:

| column | meaning |
|---|---|
| `step` | steps ahead (1 = first forecasted point) |
| `point_forecast` | the model's central forecast |
| `q10`...`q90` | the 10th through 90th percentile forecasts, for uncertainty bands |

## How It Works

The script uses TimesFM 2.5 (the 200M-parameter checkpoint), which is a decoder-only transformer pretrained on a large corpus of real and synthetic time series. It:

1. Installs `timesfm` (with the chosen backend) if not already present.
2. Loads the historical series from the input CSV.
3. Loads the pretrained checkpoint and compiles it for the requested horizon and context length.
4. Runs inference in a single forward pass — no fitting step.

## Important Notes

- **Data requirements**: at least a couple dozen historical points is recommended for a meaningful forecast; the model works with as few as 2, but accuracy improves with more history (up to `--max-context`).
- **Frequency-agnostic**: TimesFM infers patterns directly from the numeric sequence — make sure the input rows are evenly spaced and in chronological order before running.
- **Licensing**: TimesFM 1.0/2.0/2.5 checkpoints (used by this script) are Apache-2.0 and free to use commercially. The newer TimesFM 3.0 checkpoint adds multivariate/covariate support but is distributed under a **non-commercial** license — don't use it for production/commercial forecasts unless that's been cleared.
- **First run is slow**: downloading the checkpoint and compiling the model takes a while the first time; subsequent runs reuse the cached checkpoint.
- **GPU optional**: works on CPU, but a CUDA GPU (or Apple Silicon via the `mlx` backend) is much faster for long series or large horizons.

## Example

**User**: "Forecast the next 14 days of daily_sales.csv"

```bash
python scripts/forecast.py daily_sales.csv --value-column sales --horizon 14 -o sales_forecast.csv
```

**Output**: `sales_forecast.csv` with 14 rows, each giving a point forecast and 10th-90th percentile band for that day.

**Credit:** Built on [TimesFM](https://github.com/google-research/timesfm) by Google Research.
