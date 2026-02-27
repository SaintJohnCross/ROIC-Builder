from __future__ import annotations

from ...interfaces import FinancialDataProvider
from ...models import FinancialPacket


class MockCapitalIQProvider(FinancialDataProvider):
    """Drop-in stub for a future Capital IQ API integration."""

    def fetch_financials(self, ticker: str, period: str) -> FinancialPacket:
        return FinancialPacket(
            ticker=ticker,
            period=period,
            balance_sheet={"total_assets": 1_000_000, "total_liabilities": 400_000},
            cash_flow={"operating_cash_flow": 220_000, "capex": -60_000},
            income_statement={"revenue": 850_000, "ebitda": 180_000},
        )
