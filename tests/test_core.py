"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_woo.tap import Tapwoo

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
}


# Run standard built-in tap tests from the SDK:
TestTapwoo = get_tap_test_class(
    tap_class=Tapwoo,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
