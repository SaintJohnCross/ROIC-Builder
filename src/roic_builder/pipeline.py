from __future__ import annotations

from .adapters.data_providers.capiq import MockCapitalIQProvider
from .adapters.llm.insight_engine import RulesBasedInsightEngine
from .adapters.presentation.thinkcell_ppt import ThinkCellPptInjector
from .adapters.qualitative.scrapers import LicensedResearchCollector, SimpleMemoryBankBuilder
from .config import PipelineConfig
from .services.extraction import FinancialExtractionService
from .services.insight_synthesis import InsightSynthesisService
from .services.qualitative_memory import QualitativeMemoryService
from .services.slide_builder import SlideBuilderService


class RoicPipeline:
    def __init__(self) -> None:
        self.financial_service = FinancialExtractionService(provider=MockCapitalIQProvider())
        self.qualitative_service = QualitativeMemoryService(
            source=LicensedResearchCollector(),
            builder=SimpleMemoryBankBuilder(),
        )
        self.insight_service = InsightSynthesisService(engine=RulesBasedInsightEngine())
        self.slide_service = SlideBuilderService(injector=ThinkCellPptInjector())

    def run(self, config: PipelineConfig) -> str:
        financials = self.financial_service.run(ticker=config.ticker, period=config.period)
        memory_bank = self.qualitative_service.run(ticker=config.ticker, period=config.period)
        insights = self.insight_service.run(financials=financials, memory_bank=memory_bank)

        self.slide_service.run(
            template_path=config.template_path,
            output_path=config.output_path,
            financials=financials,
            insights=insights,
        )
        return config.output_path
