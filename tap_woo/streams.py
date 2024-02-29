"""Stream type classes for tap-woo."""

from __future__ import annotations

import sys
import typing as t
from typing import Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_woo.client import wooStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class OrdersStream(wooStream):
    """Orders Stream."""

    name = "orders"
    path = "/orders"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "date_modified_gmt"
    is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("parent_id", th.IntegerType),
        th.Property("number", th.StringType),
        th.Property("order_key", th.StringType),
        th.Property("created_via", th.StringType),
        th.Property("version", th.StringType),
        th.Property("status", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("currency_symbol", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("discount_total", th.StringType),
        th.Property("discount_tax", th.StringType),
        th.Property("shipping_total", th.StringType),
        th.Property("shipping_tax", th.StringType),
        th.Property("cart_tax", th.StringType),
        th.Property("total", th.StringType),
        th.Property("total_tax", th.StringType),
        th.Property("prices_include_tax", th.BooleanType),
        th.Property("customer_id", th.IntegerType),
        th.Property("customer_ip_address", th.StringType),
        th.Property("customer_user_agent", th.StringType),
        th.Property("customer_note", th.StringType),
        th.Property(
            "billing",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("address_1", th.StringType),
                th.Property("address_2", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state", th.StringType),
                th.Property("postcode", th.StringType),
                th.Property("country", th.StringType),
                th.Property("email", th.StringType),
                th.Property("phone", th.StringType),
            ),
        ),
        th.Property(
            "shipping",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("address_1", th.StringType),
                th.Property("address_2", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state", th.StringType),
                th.Property("postcode", th.StringType),
                th.Property("country", th.StringType),
            ),
        ),
        th.Property("payment_method", th.StringType),
        th.Property("payment_method_title", th.StringType),
        th.Property("transaction_id", th.StringType),
        th.Property("date_paid", th.DateTimeType),
        th.Property("date_paid_gmt", th.DateTimeType),
        th.Property("date_completed", th.DateTimeType),
        th.Property("date_completed_gmt", th.DateTimeType),
        th.Property("cart_hash", th.StringType),
        th.Property(
            "line_items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("product_id", th.IntegerType),
                    th.Property("variation_id", th.IntegerType),
                    th.Property("quantity", th.NumberType),
                    th.Property("tax_class", th.StringType),
                    th.Property("subtotal", th.StringType),
                    th.Property("subtotal_tax", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property(
                                    "id", th.CustomType({"type": ["integer", "string"]})
                                ),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                    th.Property("sku", th.CustomType({"type": ["boolean", "string"]})),
                    th.Property("price", th.NumberType),
                ),
            ),
        ),
        th.Property(
            "tax_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("rate_code", th.StringType),
                    th.Property("rate_id", th.IntegerType),
                    th.Property("label", th.StringType),
                    th.Property("compound", th.BooleanType),
                    th.Property("tax_total", th.StringType),
                    th.Property("shipping_tax_total", th.StringType),
                )
            ),
        ),
        th.Property(
            "shipping_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("method_title", th.StringType),
                    th.Property("method_id", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "fee_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("tax_class", th.StringType),
                    th.Property("tax_status", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property(
                                    "id", th.CustomType({"type": ["integer", "string"]})
                                ),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "coupon_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property(
                        "discount", th.CustomType({"type": ["string", "number"]})
                    ),
                    th.Property("discount_tax", th.StringType),
                ),
            ),
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "order_id": record["id"],
        }


class RefundsStream(wooStream):
    name = "refunds"
    path = "/orders/{order_id}/refunds"
    primary_keys = ["id"]
    parent_stream_type = OrdersStream

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("original_order_id", th.IntegerType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("amount", th.StringType),
        th.Property("reason", th.StringType),
        th.Property("refunded_by", th.IntegerType),
        th.Property("refunded_payment", th.BooleanType),
        th.Property(
            "meta_data",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("key", th.StringType),
                    th.Property(
                        "value",
                        th.CustomType({"type": ["string", "null", "array", "object"]}),
                    ),
                )
            ),
        ),
        th.Property(
            "line_items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("product_id", th.IntegerType),
                    th.Property("variation_id", th.IntegerType),
                    th.Property("quantity", th.NumberType),
                    th.Property("tax_class", th.StringType),
                    th.Property("subtotal", th.StringType),
                    th.Property("subtotal_tax", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property(
                                    "id", th.CustomType({"type": ["integer", "string"]})
                                ),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                    th.Property(
                        "meta_data",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.IntegerType),
                                th.Property("key", th.StringType),
                                th.Property(
                                    "value",
                                    th.CustomType(
                                        {"type": ["string", "null", "array", "object"]}
                                    ),
                                ),
                            )
                        ),
                    ),
                    th.Property("sku", th.CustomType({"type": ["boolean", "string"]})),
                    th.Property("price", th.NumberType),
                )
            ),
        ),
    ).to_dict()

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        # Add in the original order id
        row["original_order_id"] = (context or {}).get("order_id")
        return super().post_process(row, context)


class ProductsStream(wooStream):
    """Products Stream."""

    name = "products"
    path = "/products"
    primary_keys: t.ClassVar[list[str]]
    replication_key = "date_modified_gmt"
    is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("permalink", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("date_on_sale_from_gmt", th.DateTimeType),
        th.Property("date_on_sale_to_gmt", th.DateTimeType),
        th.Property("low_stock_amount", th.CustomType({"type": ["string", "number"]})),
        th.Property("type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("featured", th.BooleanType),
        th.Property("catalog_visibility", th.StringType),
        th.Property("description", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("sku", th.StringType),
        th.Property("brands", th.CustomType({"type": ["array", "string"]})),
        th.Property("price", th.CustomType({"type": ["string", "number"]})),
        th.Property("regular_price", th.CustomType({"type": ["string", "number"]})),
        th.Property("sale_price", th.CustomType({"type": ["string", "number"]})),
        th.Property("date_on_sale_from", th.DateTimeType),
        th.Property("date_on_sale_to", th.DateTimeType),
        th.Property("price_html", th.StringType),
        th.Property("on_sale", th.BooleanType),
        th.Property("purchasable", th.BooleanType),
        th.Property("total_sales", th.CustomType({"type": ["string", "number"]})),
        th.Property("virtual", th.BooleanType),
        th.Property("downloadable", th.BooleanType),
        th.Property("downloads", th.CustomType({"type": ["object", "array"]})),
        th.Property("download_limit", th.IntegerType),
        th.Property("download_expiry", th.IntegerType),
        th.Property("external_url", th.StringType),
        th.Property("button_text", th.StringType),
        th.Property("tax_status", th.StringType),
        th.Property("tax_class", th.StringType),
        th.Property("manage_stock", th.BooleanType),
        th.Property("stock_quantity", th.NumberType),
        th.Property("stock_status", th.StringType),
        th.Property("backorders", th.StringType),
        th.Property("backorders_allowed", th.BooleanType),
        th.Property("backordered", th.BooleanType),
        th.Property("sold_individually", th.BooleanType),
        th.Property("weight", th.StringType),
        th.Property(
            "dimensions",
            th.ObjectType(
                th.Property("length", th.StringType),
                th.Property("width", th.StringType),
                th.Property("height", th.StringType),
            ),
        ),
        th.Property("shipping_required", th.BooleanType),
        th.Property("shipping_taxable", th.BooleanType),
        th.Property("shipping_class", th.StringType),
        th.Property("shipping_class_id", th.IntegerType),
        th.Property("reviews_allowed", th.BooleanType),
        th.Property("average_rating", th.StringType),
        th.Property("rating_count", th.IntegerType),
        th.Property("related_ids", th.ArrayType(th.IntegerType)),
        th.Property("upsell_ids", th.ArrayType(th.IntegerType)),
        th.Property("cross_sell_ids", th.CustomType({"type": ["object", "array"]})),
        th.Property("parent_id", th.IntegerType),
        th.Property("purchase_note", th.StringType),
        th.Property(
            "categories",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("slug", th.StringType),
                )
            ),
        ),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("slug", th.StringType),
                )
            ),
        ),
        th.Property(
            "images",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("date_created", th.DateTimeType),
                    th.Property("date_modified", th.DateTimeType),
                    th.Property("src", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("alt", th.StringType),
                )
            ),
        ),
        th.Property(
            "attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("position", th.IntegerType),
                    th.Property("visible", th.BooleanType),
                    th.Property("variation", th.BooleanType),
                    th.Property("options", th.ArrayType(th.StringType)),
                )
            ),
        ),
        th.Property(
            "default_attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("option", th.StringType),
                )
            ),
        ),
        th.Property("variations", th.ArrayType(th.IntegerType)),
        th.Property("grouped_products", th.ArrayType(th.IntegerType)),
        th.Property("menu_order", th.IntegerType),
        th.Property(
            "meta_data",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("key", th.StringType),
                    th.Property(
                        "value",
                        th.CustomType({"type": ["string", "null", "array", "object"]}),
                    ),
                )
            ),
        ),
    ).to_dict()


class SubscriptionsStream(wooStream):
    name = "subscriptions"
    path = "/subscriptions"
    primary_keys = ["id"]
    replication_key = "date_modified_gmt"
    is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("parent_id", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("version", th.StringType),
        th.Property("prices_include_tax", th.BooleanType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("discount_total", th.StringType),
        th.Property("discount_tax", th.StringType),
        th.Property("shipping_total", th.StringType),
        th.Property("shipping_tax", th.StringType),
        th.Property("cart_tax", th.StringType),
        th.Property("total", th.StringType),
        th.Property("total_tax", th.StringType),
        th.Property("customer_id", th.IntegerType),
        th.Property("order_key", th.StringType),
        th.Property(
            "billing",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("address_1", th.StringType),
                th.Property("address_2", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state", th.StringType),
                th.Property("postcode", th.StringType),
                th.Property("country", th.StringType),
                th.Property("email", th.StringType),
                th.Property("phone", th.StringType),
            ),
        ),
        th.Property(
            "shipping",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("address_1", th.StringType),
                th.Property("address_2", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state", th.StringType),
                th.Property("postcode", th.StringType),
                th.Property("country", th.StringType),
            ),
        ),
        th.Property("payment_method", th.StringType),
        th.Property("payment_method_title", th.StringType),
        th.Property("customer_ip_address", th.StringType),
        th.Property("customer_user_agent", th.StringType),
        th.Property("created_via", th.StringType),
        th.Property("customer_note", th.StringType),
        th.Property("date_completed", th.DateTimeType),
        th.Property("date_paid", th.DateTimeType),
        th.Property("number", th.StringType),
        th.Property(
            "meta_data",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("key", th.StringType),
                    th.Property(
                        "value",
                        th.CustomType({"type": ["string", "null", "array", "object"]}),
                    ),
                )
            ),
        ),
        th.Property(
            "line_items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("product_id", th.IntegerType),
                    th.Property("variation_id", th.IntegerType),
                    th.Property("quantity", th.NumberType),
                    th.Property("tax_class", th.StringType),
                    th.Property("subtotal", th.StringType),
                    th.Property("subtotal_tax", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property(
                                    "id", th.CustomType({"type": ["integer", "string"]})
                                ),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                    th.Property(
                        "meta_data",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.IntegerType),
                                th.Property("key", th.StringType),
                                th.Property(
                                    "value",
                                    th.CustomType(
                                        {"type": ["string", "null", "array", "object"]}
                                    ),
                                ),
                            )
                        ),
                    ),
                    th.Property("sku", th.CustomType({"type": ["boolean", "string"]})),
                    th.Property("price", th.NumberType),
                )
            ),
        ),
        th.Property(
            "tax_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("rate_code", th.StringType),
                    th.Property("rate_id", th.IntegerType),
                    th.Property("label", th.StringType),
                    th.Property("compound", th.BooleanType),
                    th.Property("tax_total", th.StringType),
                    th.Property("shipping_tax_total", th.StringType),
                )
            ),
        ),
        th.Property(
            "shipping_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("method_title", th.StringType),
                    th.Property("method_id", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "fee_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("tax_class", th.StringType),
                    th.Property("tax_status", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property(
                                    "id", th.CustomType({"type": ["integer", "string"]})
                                ),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "coupon_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property(
                        "discount", th.CustomType({"type": ["string", "number"]})
                    ),
                    th.Property("discount_tax", th.StringType),
                ),
            ),
        ),
        th.Property("date_completed_gmt", th.DateTimeType),
        th.Property("date_paid_gmt", th.DateTimeType),
        th.Property("billing_period", th.StringType),
        th.Property("billing_interval", th.StringType),
        th.Property("start_date_gmt", th.DateTimeType),
        th.Property("trial_end_date_gmt", th.DateTimeType),
        th.Property("next_payment_date_gmt", th.DateTimeType),
        th.Property("last_payment_date_gmt", th.DateTimeType),
        th.Property("cancelled_date_gmt", th.DateTimeType),
        th.Property("end_date_gmt", th.DateTimeType),
        th.Property("resubscribed_from", th.StringType),
        th.Property("resubscribed_subscription", th.StringType),
        th.Property("removed_line_items", th.ArrayType(th.IntegerType)),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "subscription_id": record["id"],
        }


class SubscriptionOrdersStream(wooStream):
    name = "subscription_orders"
    path = "/subscriptions/{subscription_id}/orders"
    primary_keys = ["subscription_id"]
    parent_stream_type = SubscriptionsStream

    schema = th.PropertiesList(
        th.Property(
            "subscription_id", th.IntegerType
        ),  # This seems to come from the parent stream, although I dont understand how
        th.Property("order_id", th.IntegerType),
    ).to_dict()

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        # Rename the id field to order_id
        row["order_id"] = row["id"]
        del row["id"]
        return super().post_process(row, context)
