from __future__ import annotations

from ...interfaces import InsightEngine
from ...models import FinancialPacket, InsightPackage, MemoryBank, SlideInsight


class RulesBasedInsightEngine(InsightEngine):
    """Deterministic baseline; replace with an LLM-backed engine later."""

    def synthesize(self, financials: FinancialPacket, memory_bank: MemoryBank) -> InsightPackage:
        revenue = float(financials.income_statement.get("revenue", 0))
        ebitda = float(financials.income_statement.get("ebitda", 0))
        margin = (ebitda / revenue * 100) if revenue else 0.0

        bullets = [
            f"EBITDA margin baseline: {margin:.1f}%",
            "Operating cash flow remains a key funding source.",
        ]

        bullets.extend(memory_bank.extracted_points[:3])

        slide = SlideInsight(
            slide_id="industry_outlook",
            title="Industry Trajectory and Strategic Signal",
            commentary=(
                "Quantitative indicators show positive operating leverage while "
                "qualitative signals suggest a selective demand recovery."
            ),
            bullet_points=bullets,
        )

        return InsightPackage(
            ticker=financials.ticker,
            period=financials.period,
            slide_insights=[slide],
        )
