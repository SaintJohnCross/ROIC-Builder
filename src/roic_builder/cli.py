from __future__ import annotations

import argparse

from .config import PipelineConfig
from .pipeline import RoicPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ROIC Builder pipeline")
    parser.add_argument("--config", help="Path to YAML config file")
    parser.add_argument("--ticker", help="Ticker symbol, e.g. MSFT")
    parser.add_argument("--period", help="Period key, e.g. 2025Q4")
    parser.add_argument("--template", help="Path to PPT template")
    parser.add_argument("--output", help="Path to generated output")
    return parser


def _build_config(args: argparse.Namespace) -> PipelineConfig:
    if args.config:
        return PipelineConfig.from_yaml(args.config)

    missing = [
        name
        for name, value in (
            ("ticker", args.ticker),
            ("period", args.period),
            ("template", args.template),
            ("output", args.output),
        )
        if not value
    ]
    if missing:
        missing_text = ", ".join(f"--{item}" for item in missing)
        raise ValueError(f"Missing required CLI args when --config is not set: {missing_text}")

    return PipelineConfig(
        ticker=args.ticker,
        period=args.period,
        template_path=args.template,
        output_path=args.output,
    )


def main() -> None:
    args = build_parser().parse_args()
    config = _build_config(args)

    output = RoicPipeline().run(config)
    print(f"Generated output artifact: {output}")


if __name__ == "__main__":
    main()
