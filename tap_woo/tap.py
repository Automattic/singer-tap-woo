"""woo tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_woo import streams


class Tapwoo(Tap):
    """woo tap class."""

    name = "tap-woo"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "consumer_key",
            th.StringType,
            required=True,
            description="Consumer Key",
        ),
        th.Property(
            "consumer_secret",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="Consumer Secret",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.mysample.com",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.wooStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ProductsStream(tap=self),
            streams.OrdersStream(tap=self),
            streams.RefundsStream(tap=self),
            streams.SubscriptionsStream(tap=self),
            streams.SubscriptionOrdersStream(tap=self),
            # streams.CouponsStream(tap=self),
            # streams.CustomersStream(tap=self),
            # streams.ProductVariationsStream(tap=self),
            # streams.RefundsStream(tap=self),
            # streams.ShippingZonesStream(tap=self),
            # streams.ShippingMethodsStream(tap=self),
            # streams.WebhooksStream(tap=self),
            # streams.TaxRatesStream(tap=self),
            # streams.TaxClassesStream(tap=self),
            # streams.CategoriesStream(tap=self),
            # streams.TagsStream(tap=self),
            # streams.AttributesStream(tap=self),
            # streams.AttributeTermsStream(tap=self),
            # streams.AttributeSetsStream(tap=self),
        ]


if __name__ == "__main__":
    Tapwoo.cli()
