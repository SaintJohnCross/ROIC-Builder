from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PipelineConfig:
    ticker: str
    period: str
    template_path: str
    output_path: str

    @classmethod
    def from_yaml(cls, path: str) -> "PipelineConfig":
        try:
            import yaml  # type: ignore
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                "PyYAML is required for --config. Install with: python -m pip install -r requirements.txt"
            ) from exc

        config_path = Path(path)
        data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

        required = ("ticker", "period", "template_path", "output_path")
        missing = [key for key in required if key not in data]
        if missing:
            raise ValueError(f"Missing required config keys in {path}: {', '.join(missing)}")

        return cls(
            ticker=str(data["ticker"]),
            period=str(data["period"]),
            template_path=str(data["template_path"]),
            output_path=str(data["output_path"]),
        )
