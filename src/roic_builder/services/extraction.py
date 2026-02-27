from __future__ import annotations

from ..interfaces import FinancialDataProvider
from ..models import FinancialPacket


class FinancialExtractionService:
    def __init__(self, provider: FinancialDataProvider) -> None:
        self.provider = provider

    def run(self, ticker: str, period: str) -> FinancialPacket:
        return self.provider.fetch_financials(ticker=ticker, period=period)
