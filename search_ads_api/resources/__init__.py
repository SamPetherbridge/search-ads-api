"""Resource classes for the Apple Search Ads API.

Resources provide a structured interface for interacting with
different API endpoints. Each resource handles a specific entity
type (campaigns, ad groups, keywords, etc.).
"""

from search_ads_api.resources.campaigns import CampaignResource
from search_ads_api.resources.ad_groups import AdGroupResource
from search_ads_api.resources.keywords import KeywordResource, NegativeKeywordResource
from search_ads_api.resources.reports import ReportResource

__all__ = [
    "CampaignResource",
    "AdGroupResource",
    "KeywordResource",
    "NegativeKeywordResource",
    "ReportResource",
]
