"""REST client handling, including wooStream base class."""

from __future__ import annotations

from typing import Callable

import requests
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.pagination import SimpleHeaderPaginator, BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]


class wooStream(RESTStream):
    """woo stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config.get("api_url", "") + 'wp-json/wc/v3'

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config.get("consumer_key", ""),
            password=self.config.get("consumer_secret", ""),
        )
    
    def get_url_params(self, context, next_page_token):
        self.logger.debug(f"Next page token: {next_page_token}")
        params = {
            "per_page": 100,
            "order": "asc",
            }

        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["modified_after"] = starting_date

        if next_page_token is not None:
            params["page"] = next_page_token

        self.logger.info(f"URL params: {params}")
        return params

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Get a fresh paginator for this API endpoint.

        Returns:
            A paginator instance.
        """
        # https://woocommerce.github.io/woocommerce-rest-api-docs/#parameters
        return SimpleHeaderPaginator("next")
