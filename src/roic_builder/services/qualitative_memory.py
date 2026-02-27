from __future__ import annotations

from ..interfaces import MemoryBankBuilder, QualitativeSource
from ..models import MemoryBank


class QualitativeMemoryService:
    def __init__(self, source: QualitativeSource, builder: MemoryBankBuilder) -> None:
        self.source = source
        self.builder = builder

    def run(self, ticker: str, period: str) -> MemoryBank:
        docs = self.source.collect_documents(ticker=ticker, period=period)
        return self.builder.build(ticker=ticker, period=period, docs=docs)
