from __future__ import annotations

from ...interfaces import MemoryBankBuilder, QualitativeSource
from ...models import MemoryBank, QualitativeDocument


class LicensedResearchCollector(QualitativeSource):
    """
    Placeholder for ingestion from lawful sources:
    - earnings call transcripts
    - licensed analyst reports
    - public filings/news
    """

    def collect_documents(self, ticker: str, period: str) -> list[QualitativeDocument]:
        return [
            QualitativeDocument(
                source="earnings_call",
                title=f"{ticker} {period} earnings call",
                text="Management highlighted margin stabilization and disciplined capex.",
                metadata={"quarter": period},
            ),
            QualitativeDocument(
                source="licensed_analyst",
                title=f"Street view for {ticker}",
                text="Consensus expects medium-term growth acceleration in core segment.",
                metadata={"confidence": "medium"},
            ),
        ]


class SimpleMemoryBankBuilder(MemoryBankBuilder):
    def build(self, ticker: str, period: str, docs: list[QualitativeDocument]) -> MemoryBank:
        points: list[str] = []
        for doc in docs:
            first_sentence = doc.text.split(".")[0].strip()
            if first_sentence:
                points.append(f"[{doc.source}] {first_sentence}")

        return MemoryBank(
            ticker=ticker,
            period=period,
            documents=docs,
            extracted_points=points,
        )
