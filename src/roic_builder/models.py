from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class FinancialPacket:
    ticker: str
    period: str
    balance_sheet: dict
    cash_flow: dict
    income_statement: dict


@dataclass(slots=True)
class QualitativeDocument:
    source: str
    title: str
    text: str
    metadata: dict = field(default_factory=dict)


@dataclass(slots=True)
class MemoryBank:
    ticker: str
    period: str
    documents: list[QualitativeDocument]
    extracted_points: list[str]


@dataclass(slots=True)
class SlideInsight:
    slide_id: str
    title: str
    commentary: str
    bullet_points: list[str]


@dataclass(slots=True)
class InsightPackage:
    ticker: str
    period: str
    slide_insights: list[SlideInsight]
