# Exceptions Reference

## Exception Hierarchy

```
AppleSearchAdsError
├── AuthenticationError
├── ConfigurationError
├── NotFoundError
├── RateLimitError
└── ValidationError
```

## AppleSearchAdsError

Base exception for all API errors.

```python
from search_ads_api import AppleSearchAdsError

try:
    client.campaigns.list()
except AppleSearchAdsError as e:
    print(f"API error: {e}")
```

## AuthenticationError

Raised when authentication fails.

```python
from search_ads_api import AuthenticationError

try:
    client.campaigns.list()
except AuthenticationError:
    print("Invalid credentials or expired token")
```

## ConfigurationError

Raised when client configuration is invalid.

```python
from search_ads_api import ConfigurationError

try:
    client = AppleSearchAdsClient(...)
except ConfigurationError as e:
    print(f"Configuration error: {e}")
```

## NotFoundError

Raised when a resource is not found.

```python
from search_ads_api import NotFoundError

try:
    campaign = client.campaigns.get(123)
except NotFoundError:
    print("Campaign not found")
```

## RateLimitError

Raised when API rate limit is exceeded.

```python
from search_ads_api import RateLimitError

try:
    client.campaigns.list()
except RateLimitError as e:
    print(f"Rate limited, retry after: {e.retry_after}")
```

## ValidationError

Raised when request validation fails.

```python
from search_ads_api import ValidationError

try:
    client.campaigns.create(invalid_data)
except ValidationError as e:
    print(f"Validation error: {e}")
```
