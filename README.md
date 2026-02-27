# ROIC Builder

A modular Python system for:

1. Structured financial data extraction (e.g., Capital IQ-style providers)
2. Data injection into slide templates / think-cell-ready structures
3. Qualitative ingestion (earnings calls, analyst commentary, licensed research)
4. Insight synthesis from quantitative + qualitative evidence
5. Slide-level commentary and key dot-point insertion

## Important scope note

This scaffold only supports lawful and licensed data/report sources. Connectors for unauthorized or pirated content are intentionally out of scope.

## Quick start

```bash
python -m pip install -r requirements-dev.txt
python -m roic_builder.cli --config configs/run.example.yaml
```

## Documentation

- Architecture and end-to-end flow: `docs/ARCHITECTURE.md`
- YAML run config: `docs/RUN_CONFIG.md`

## Architecture

- `roic_builder.interfaces`: contracts for providers and engines
- `roic_builder.services`: orchestration and domain services
- `roic_builder.adapters`: concrete integration stubs (provider, scraping, PPT, LLM)
- `roic_builder.pipeline`: end-to-end run composition
- `roic_builder.cli`: command line entrypoint
