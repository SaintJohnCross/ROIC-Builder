# Run Configuration (YAML)

## Why YAML
YAML lets each run be configured without changing code or command flags.

## Schema
Required keys:
- `ticker`
- `period`
- `template_path`
- `output_path`

Example:

```yaml
ticker: MSFT
period: 2025Q4
template_path: templates/base.pptx
output_path: out/MSFT.txt
```

## Run commands

Using YAML:

```bash
python -m roic_builder.cli --config configs/run.example.yaml
```

Using CLI flags:

```bash
python -m roic_builder.cli --ticker MSFT --period 2025Q4 --template templates/base.pptx --output out/MSFT.txt
```

## Validation behavior
- If `--config` is provided, YAML is used.
- If `--config` is omitted, all four CLI flags are required.
- Missing fields raise a clear `ValueError`.
