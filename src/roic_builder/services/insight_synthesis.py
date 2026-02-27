from __future__ import annotations

from ..interfaces import InsightEngine
from ..models import FinancialPacket, InsightPackage, MemoryBank


class InsightSynthesisService:
    def __init__(self, engine: InsightEngine) -> None:
        self.engine = engine

    def run(self, financials: FinancialPacket, memory_bank: MemoryBank) -> InsightPackage:
        return self.engine.synthesize(financials=financials, memory_bank=memory_bank)
