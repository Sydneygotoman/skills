#!/usr/bin/env python3
"""Forecast a time series with Google Research's TimesFM foundation model.

Repo: https://github.com/google-research/timesfm
"""

import argparse
import csv
import subprocess
import sys

QUANTILE_LEVELS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def ensure_timesfm(backend: str) -> None:
    try:
        import timesfm  # noqa: F401
        return
    except ImportError:
        pass
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"timesfm[{backend}]"])


def load_series(csv_path: str, value_column: str) -> list[float]:
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or value_column not in reader.fieldnames:
            raise SystemExit(
                f"Column '{value_column}' not found. Available columns: {reader.fieldnames}"
            )
        return [
            float(row[value_column])
            for row in reader
            if row[value_column] not in ("", None)
        ]


def run_forecast(series: list[float], horizon: int, max_context: int):
    import numpy as np
    import timesfm

    model = timesfm.TimesFM_2p5_200M_torch()
    model.load_checkpoint()
    model.compile(
        timesfm.ForecastConfig(
            max_context=max_context,
            max_horizon=horizon,
            normalize_inputs=True,
            use_continuous_quantile_head=True,
            force_flip_invariance=True,
            infer_is_positive=True,
            fix_quantile_crossing=True,
        )
    )
    point_forecast, quantile_forecast = model.forecast(
        horizon=horizon, inputs=[np.array(series, dtype=np.float32)]
    )
    return point_forecast[0], quantile_forecast[0]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Forecast a time series with the TimesFM 2.5 foundation model."
    )
    parser.add_argument("csv_path", help="CSV file containing the historical series")
    parser.add_argument(
        "--value-column",
        default="value",
        help="Column holding the series values (default: value)",
    )
    parser.add_argument(
        "--horizon", type=int, required=True, help="Number of future steps to forecast"
    )
    parser.add_argument(
        "--max-context",
        type=int,
        default=1024,
        help="Max history length the model attends to (default: 1024)",
    )
    parser.add_argument(
        "--backend",
        choices=["torch", "mlx"],
        default="torch",
        help="Inference backend to install/use (default: torch)",
    )
    parser.add_argument(
        "-o", "--output", default="forecast.csv", help="Where to write the forecast CSV"
    )
    args = parser.parse_args()

    ensure_timesfm(args.backend)
    series = load_series(args.csv_path, args.value_column)
    if len(series) < 2:
        raise SystemExit("Need at least 2 historical points to forecast.")

    point_forecast, quantile_forecast = run_forecast(series, args.horizon, args.max_context)

    with open(args.output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["step", "point_forecast"] + [f"q{int(q * 100)}" for q in QUANTILE_LEVELS])
        for step, (point, quantiles) in enumerate(zip(point_forecast, quantile_forecast), start=1):
            # quantiles[0] is the mean; quantiles[1:] are the 10th-90th percentiles
            writer.writerow([step, float(point)] + [float(q) for q in quantiles[1:]])

    print(f"Wrote {args.horizon}-step forecast to {args.output}")


if __name__ == "__main__":
    main()
