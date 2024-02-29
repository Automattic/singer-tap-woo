"""REST client handling, including wooStream base class."""

from __future__ import annotations

from typing import Callable
from urllib.parse import urljoin, parse_qsl

import pendulum
import requests
from requests.utils import parse_header_links
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.pagination import (
    BaseAPIPaginator, BaseHATEOASPaginator,
)  # noqa: TCH002
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]


DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class WooPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response):
        links = {link.get('rel'): link.get('url') for link in parse_header_links(response.headers.get('Link', ''))}
        return links.get('next')


class wooStream(RESTStream):
    """woo stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return urljoin(self.config["api_url"], 'wp-json/wc/v3')

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
            "per_page": 10,
            "order": "asc"
        }
        starting_date = self.get_starting_timestamp(context)
        if starting_date:
            params["modified_after"] = starting_date.strftime(DATETIME_FORMAT)

        end_date = self.config.get("end_date")
        if end_date:
            params["modified_before"] = pendulum.parse(end_date).strftime(DATETIME_FORMAT)

        if next_page_token is not None:
            params["page"] = dict(parse_qsl(next_page_token.query)).get('page')

        self.logger.info(f"URL params: {params}")
        return params

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Get a fresh paginator for this API endpoint.

        Returns:
            A paginator instance.
        """
        return WooPaginator()

