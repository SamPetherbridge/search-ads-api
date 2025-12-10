"""Pydantic models for the Apple Search Ads API.

This module exports all the data models used to interact with the
Apple Search Ads API. All models are Pydantic BaseModels with full
type hints and validation.
"""

from search_ads_api.models.base import (
    Condition,
    ConditionOperator,
    Money,
    PageDetail,
    PaginatedResponse,
    Pagination,
    Selector,
    Sorting,
    SortOrder,
)
from search_ads_api.models.campaigns import (
    AdChannelType,
    BillingEvent,
    Campaign,
    CampaignCountryOrRegionServingStateReason,
    CampaignCreate,
    CampaignDisplayStatus,
    CampaignServingStateReason,
    CampaignServingStatus,
    CampaignStatus,
    CampaignSupplySource,
    CampaignUpdate,
)
from search_ads_api.models.ad_groups import (
    AdGroup,
    AdGroupCreate,
    AdGroupDisplayStatus,
    AdGroupServingStateReason,
    AdGroupServingStatus,
    AdGroupStatus,
    AdGroupUpdate,
    AutomatedKeywordsOptInStatus,
    CpaGoal,
    TargetingDimensions,
)
from search_ads_api.models.keywords import (
    Keyword,
    KeywordCreate,
    KeywordMatchType,
    KeywordStatus,
    KeywordUpdate,
    NegativeKeyword,
    NegativeKeywordCreate,
)
from search_ads_api.models.reports import (
    GranularityType,
    ReportingRequest,
    ReportingResponse,
    ReportMetadata,
    ReportRow,
    SpendRow,
)

__all__ = [
    # Base
    "Condition",
    "ConditionOperator",
    "Money",
    "PageDetail",
    "PaginatedResponse",
    "Pagination",
    "Selector",
    "Sorting",
    "SortOrder",
    # Campaigns
    "AdChannelType",
    "BillingEvent",
    "Campaign",
    "CampaignCountryOrRegionServingStateReason",
    "CampaignCreate",
    "CampaignDisplayStatus",
    "CampaignServingStateReason",
    "CampaignServingStatus",
    "CampaignStatus",
    "CampaignSupplySource",
    "CampaignUpdate",
    # Ad Groups
    "AdGroup",
    "AdGroupCreate",
    "AdGroupDisplayStatus",
    "AdGroupServingStateReason",
    "AdGroupServingStatus",
    "AdGroupStatus",
    "AdGroupUpdate",
    "AutomatedKeywordsOptInStatus",
    "CpaGoal",
    "TargetingDimensions",
    # Keywords
    "Keyword",
    "KeywordCreate",
    "KeywordMatchType",
    "KeywordStatus",
    "KeywordUpdate",
    "NegativeKeyword",
    "NegativeKeywordCreate",
    # Reports
    "GranularityType",
    "ReportingRequest",
    "ReportingResponse",
    "ReportMetadata",
    "ReportRow",
    "SpendRow",
]
