from __future__ import annotations

from abc import ABC, abstractmethod

from .models import FinancialPacket, InsightPackage, MemoryBank, QualitativeDocument


class FinancialDataProvider(ABC):
    @abstractmethod
    def fetch_financials(self, ticker: str, period: str) -> FinancialPacket:
        raise NotImplementedError


class QualitativeSource(ABC):
    @abstractmethod
    def collect_documents(self, ticker: str, period: str) -> list[QualitativeDocument]:
        raise NotImplementedError


class MemoryBankBuilder(ABC):
    @abstractmethod
    def build(self, ticker: str, period: str, docs: list[QualitativeDocument]) -> MemoryBank:
        raise NotImplementedError


class InsightEngine(ABC):
    @abstractmethod
    def synthesize(self, financials: FinancialPacket, memory_bank: MemoryBank) -> InsightPackage:
        raise NotImplementedError


class SlideInjector(ABC):
    @abstractmethod
    def inject(
        self,
        template_path: str,
        output_path: str,
        financials: FinancialPacket,
        insights: InsightPackage,
    ) -> None:
        raise NotImplementedError
