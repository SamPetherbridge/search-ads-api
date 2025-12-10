# Installation

## Using uv (Recommended)

[uv](https://docs.astral.sh/uv/) is a fast Python package manager:

```bash
uv add search-ads-api
```

With pandas support for DataFrame exports:

```bash
uv add "search-ads-api[pandas]"
```

## Using pip

```bash
pip install search-ads-api
```

With pandas support:

```bash
pip install "search-ads-api[pandas]"
```

## Requirements

- Python 3.13+
- Valid Apple Search Ads API credentials

## Dependencies

The package has minimal dependencies:

- `httpx` - HTTP client with async support
- `pydantic` - Data validation
- `pydantic-settings` - Settings management
- `pyjwt[crypto]` - JWT authentication

Optional:

- `pandas` - DataFrame export support
