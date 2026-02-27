# Architecture and Data Flow

## Purpose
ROIC Builder orchestrates five layers:
1. Financial statement extraction (quantitative)
2. Qualitative document ingestion (transcripts/research)
3. Memory bank construction (normalized evidence)
4. Insight synthesis (quant + qual fusion)
5. Slide injection (template + commentary + bullets)

## Core contracts
Contracts are defined in `src/roic_builder/interfaces.py`.

- `FinancialDataProvider`: fetches financial packets
- `QualitativeSource`: collects documents
- `MemoryBankBuilder`: converts raw docs to extracted points
- `InsightEngine`: synthesizes slide-level insights
- `SlideInjector`: writes final presentation artifacts

Every component depends on interfaces, not concrete adapters, so integrations can be swapped without changing orchestration code.

## Data flow (single run)

1. CLI builds `PipelineConfig`
2. `FinancialExtractionService` fetches financials
3. `QualitativeMemoryService` collects docs and builds memory bank
4. `InsightSynthesisService` produces slide insights
5. `SlideBuilderService` injects content into output artifact

Code path:
- `src/roic_builder/cli.py`
- `src/roic_builder/pipeline.py`
- `src/roic_builder/services/*`
- `src/roic_builder/adapters/*`

## Current implementation status

Operational now:
- End-to-end pipeline orchestration
- Mock financial + qualitative adapters
- Deterministic insight generation baseline
- Output artifact creation (trace file)

Not implemented yet:
- Real Capital IQ API adapter
- Real Selenium ingestion from licensed portals
- Real PowerPoint/think-cell automation
- LLM-based narrative quality/consistency layer

## How to extend safely

1. Add a new adapter implementing one interface.
2. Keep service signatures unchanged.
3. Wire adapter in `pipeline.py` (or dependency-injection factory).
4. Add tests at adapter + pipeline levels.
