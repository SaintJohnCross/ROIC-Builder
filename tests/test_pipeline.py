from __future__ import annotations

from pathlib import Path

from roic_builder.config import PipelineConfig
from roic_builder.pipeline import RoicPipeline


def test_pipeline_writes_output(tmp_path: Path) -> None:
    output = tmp_path / "result.txt"

    config = PipelineConfig(
        ticker="MSFT",
        period="2025Q4",
        template_path="templates/base.pptx",
        output_path=str(output),
    )

    result_path = RoicPipeline().run(config)

    assert result_path == str(output)
    content = output.read_text(encoding="utf-8")
    assert "ticker=MSFT" in content
    assert "slide=industry_outlook" in content
