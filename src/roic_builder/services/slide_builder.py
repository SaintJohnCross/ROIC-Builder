from __future__ import annotations

from ..interfaces import SlideInjector
from ..models import FinancialPacket, InsightPackage


class SlideBuilderService:
    def __init__(self, injector: SlideInjector) -> None:
        self.injector = injector

    def run(
        self,
        template_path: str,
        output_path: str,
        financials: FinancialPacket,
        insights: InsightPackage,
    ) -> None:
        self.injector.inject(
            template_path=template_path,
            output_path=output_path,
            financials=financials,
            insights=insights,
        )
