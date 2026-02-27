from __future__ import annotations

from pathlib import Path

from ...interfaces import SlideInjector
from ...models import FinancialPacket, InsightPackage


class ThinkCellPptInjector(SlideInjector):
    """
    Stub for PowerPoint/think-cell automation.

    For now, it writes a trace file at output_path so the pipeline is testable.
    Replace with one of:
    - python-pptx + think-cell placeholders
    - COM automation on Windows for direct think-cell interaction
    """

    def inject(
        self,
        template_path: str,
        output_path: str,
        financials: FinancialPacket,
        insights: InsightPackage,
    ) -> None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            f"template={template_path}",
            f"ticker={financials.ticker}",
            f"period={financials.period}",
        ]

        for insight in insights.slide_insights:
            lines.append(f"slide={insight.slide_id}:{insight.title}")
            lines.append(f"commentary={insight.commentary}")
            lines.extend(f"bullet={point}" for point in insight.bullet_points)

        path.write_text("\n".join(lines), encoding="utf-8")
