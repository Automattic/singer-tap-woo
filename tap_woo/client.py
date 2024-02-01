"""REST client handling, including wooStream base class."""

from __future__ import annotations

import sys
from typing import Any, Callable, Iterable

import requests
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"


class wooStream(RESTStream):
    """woo stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config.get("api_url", "") + 'wp-json/wc/v3'

    records_jsonpath = "$[*]"  # Or override `parse_response`.

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

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        return headers

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return super().get_new_paginator()

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
    
    def get_url_params(self, context, next_page_token):
        self.logger.info(f"Next page token: {next_page_token}")
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

    def get_url(self, context):
        url = super().get_url(context)
        self.logger.info(f"URL: {url}")
        return url

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # Get the total pages header
        total_pages = response.headers.get("X-WP-TotalPages")
        # If the response is an error, we want to retry the request
        if response.status_code >= 400:
            previous_token = previous_token or 1
            total_pages = previous_token + 1

        if total_pages is None or int(total_pages) <= 1:
            return None

        if previous_token is None:
            return 2

        if int(total_pages) > previous_token:
            return previous_token + 1

        return None
