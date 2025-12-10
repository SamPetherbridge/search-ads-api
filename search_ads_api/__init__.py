"""Apple Search Ads API client library.

A modern, fully-typed Python client for the Apple Search Ads API
with async support, Pydantic models, and comprehensive logging.

Example:
    Basic usage with the client::

        from search_ads_api import AppleSearchAdsClient

        client = AppleSearchAdsClient(
            client_id="your-client-id",
            team_id="your-team-id",
            key_id="your-key-id",
            org_id=123456,
            private_key_path="path/to/private-key.pem",
        )

        # List all campaigns
        campaigns = client.campaigns.list()

        # Async usage
        campaigns = await client.campaigns.list_async()
"""

from search_ads_api.client import AppleSearchAdsClient
from search_ads_api.exceptions import (
    AppleSearchAdsError,
    AuthenticationError,
    ConfigurationError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)
from search_ads_api.logging import configure_logging
from search_ads_api.settings import Settings

__all__ = [
    "AppleSearchAdsClient",
    "AppleSearchAdsError",
    "AuthenticationError",
    "ConfigurationError",
    "NotFoundError",
    "RateLimitError",
    "ValidationError",
    "Settings",
    "configure_logging",
]

__version__ = "0.1.0"
